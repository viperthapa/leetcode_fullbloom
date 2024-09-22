import time
import unittest
import logging
from fullbloom import earliestFullBloom

logger = logging.getLogger()


class TestEarliestFullBloom(unittest.TestCase):

    def test_earliestFullBloom1(self):
        # Case 1
        plantTime = [1,4,3]
        growTime = [2,3,1]
        expected = 9
        
        start_time = time.time()
        result = earliestFullBloom(plantTime,growTime)
        elapsed = time.time() - start_time
        
        print(f"Execution time: {elapsed:.6f} seconds")          
        self.assertEqual(result, expected, f"For plantTime {plantTime} and growTime {growTime}, expected {expected} but got {result}")
    
    def test_earliestFullBloom2(self):
        # Case 2
        plantTime = [1,2,3,2]
        growTime = [2,1,2,1]
        expected = 9
        
        start_time = time.time()
        result = earliestFullBloom(plantTime,growTime)
        elapsed = time.time() - start_time
        
        print(f"Execution time: {elapsed:.6f} seconds")          
        self.assertEqual(result, expected, f"For plantTime {plantTime} and growTime {growTime}, expected {expected} but got {result}")
    
    
    def test_earliestFullBloom3(self):
        # Case 3
        plantTime = [1]
        growTime = [1]
        expected = 2
        
        start_time = time.time()
        result = earliestFullBloom(plantTime,growTime)
        elapsed = time.time() - start_time
        
        print(f"Execution time: {elapsed:.6f} seconds")          
        self.assertEqual(result, expected, f"For plantTime {plantTime} and growTime {growTime}, expected {expected} but got {result}")

        
if __name__ == '__main__':
    unittest.main()