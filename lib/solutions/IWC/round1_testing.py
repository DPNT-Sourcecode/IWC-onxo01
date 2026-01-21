import unittest

from solutions.IWC.queue_solution_entrypoint import QueueSolutionEntrypoint

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q= QueueSolutionEntrypoint()
        self.q.purge()
 
    def test_rule_of_three(self):
        self.q.enqueue({"user_id":1, "provider":"companies_house",   "timestamp":"2025-10-20 12:00:00 "}) 
        self.q.enqueue({"user_id":2, "provider":"bank_statements",   "timestamp":"2025-10-20 12:00:00"})
        self.q.enqueue({"user_id":1, "provider":"id_verification",   "timestamp":"2025-10-20 12:00:00" })
        self.q.enqueue({"user_id":1, "provider":"bank_statements",   "timestamp":"2025-10-20 12:00:00" })
        
        #Checking the first one belongs to user 1 
        self.assertEqual(self.q.dequeue()["user_id"],1)
    
    def test_timestamp_ordering(self):
        self.q.enqueue({"user_id":1, "provider":"bank_statements",   "timestamp":"2025-10-20 12:05:00" })
        self.q.enqueue({"user_id":2, "provider":"bank_statements",   "timestamp":"2025-10-20 12:00:00" })
        # Checking order when removing from queue, older one first then second one
        self.assertEqual(self.q.dequeue()["timestamp"], "2025-10-20 12:00:00")
        self.assertEqual(self.q.dequeue()["timestamp"], "2025-10-20 12:05:00")
    
    def test_dependency_resolution(self):
        self.q.enqueue({"user_id":1, "provider":"credit_check",   "timestamp":"2025-10-20 12:00:00 "}) 

        self.assertEqual(self.q.dequeue()["provider"], "companies_house")
        self.assertEqual(self.q.dequeue()["provider"], "credit_check")

if __name__=="__main__":
    unittest.main()
