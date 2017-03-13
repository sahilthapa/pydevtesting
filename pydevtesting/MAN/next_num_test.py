import unittest
from next_num import next_num, error_msg_from_code, generate_next_num, num_choice, ST_SENTINEL, SUCCESS_CODE

class next_num_test(unittest.TestCase):

    def test_next_num(self):
        self.assertRaises(ValueError, next_num, [1, -1], [0.4, 0.9])
        self.assertRaises(ValueError, next_num, [1, -1], [0.4, -0.9])
        self.assertRaises(ValueError, next_num, [1, -1], [0.4, '-0.9'])
        self.assertRaises(ValueError, next_num, [1, -1], [0.4])
        nnum = next_num([1, 1], [0.2, 0.8])
        self.assertTrue(nnum==1, "Next Num matches 1")
        j,i,u = 0, 0, 0
        for k in range(100):
            nnum = next_num([1, 2 ,3], [0.3, 0.6, 0.1])
            if nnum == 1:
                j+=1
            elif nnum ==2: 
                i+=1
            else: 
                u+=1
        self.assertTrue(j > u, "Over 100 samples more 1s than 3s")
        self.assertTrue(i > j, "Over 100 samples more 2s than 1s")
        
    def test_error_msg_from_code(self):
        errmsg = error_msg_from_code(-1)
        self.assertEqual("Unknown", errmsg, "-1 is Unknown")
        errmsg = error_msg_from_code(100)
        self.assertEqual("", errmsg, "Success code has empty string as error code")
        errmsg = error_msg_from_code(0)
        self.assertEqual("Length of nums and num of probs does not match", errmsg)
        errmsg = error_msg_from_code(1)
        self.assertEqual("Input probabilities need to be [int, float]", errmsg, "")
        errmsg = error_msg_from_code(2)
        self.assertNotEqual("", errmsg, "Success code has empty string as error code")
        self.assertEqual("Input probabilities cannot be negative or greater than 1 in value", errmsg, "")
        errmsg = error_msg_from_code(3)
        self.assertEqual("Probabilities do not sum up to 1", errmsg, "")
    
    def test_num_choice(self):
        a = num_choice([1, 1], [0.36, 0.64])
        self.assertEqual(1, 1, "Function should return basic boundary data")
    
    def test_generate_next_num(self):
        a, b, c = generate_next_num([1, 1], [0.36, 0.63])  
        self.assertEqual(b, 3, "Errocode 3")
        self.assertEqual(a, ST_SENTINEL, "Sentinel Value")
        a, b, c = generate_next_num([1, 2], [0.36, 0.64])  
        self.assertEqual(b, SUCCESS_CODE, "Success Code")
        self.assertEqual(a in [1, 2], True, "Value returned from nums list")
        
if __name__ == "__main__":
    next_num_test.main()