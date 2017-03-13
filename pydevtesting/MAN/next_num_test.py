import unittest
from next_num import next_num, error_msg_from_code

class next_num_test(unittest.TestCase):

    def test_next_num(self):
        self.assertRaises(ValueError, next_num, [1, -1], [0.4, 0.9])
        self.assertRaises(ValueError, next_num, [1, -1], [0.4, -0.9])
        self.assertRaises(ValueError, next_num, [1, -1], [0.4, '-0.9'])
        self.assertRaises(ValueError, next_num, [1, -1], [0.4])
        nnum = next_num([1, 1], [0.2, 0.8])
        self.assertTrue(nnum==1, "Next Num matches 1")
        
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
        self.assertEqual("Input probabilities has a negative value", errmsg, "")
        errmsg = error_msg_from_code(3)
        self.assertEqual("Probabilities do not sum up to 1", errmsg, "")
        
        
if __name__ == "__main__":
    next_num_test.main()