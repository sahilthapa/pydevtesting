import numpy as np

class RandomGen():
    ST_SENTINEL = None
    SUCCESS_CODE = 100
    random_nums = []
    probabilties = []
    def __init__(self, nums, nums_prob):
        self.random_nums = nums
        self.probabilities = nums_prob
        
            
    def next_num(self, showError=False):
        res = RandomGen.ST_SENTINEL
        try: 
            err_code, err_msg = self.error_msg_from_code(-1)
            if (len(self.random_nums) != len(self.probabilities)):
                err_code, err_msg = self.error_msg_from_code(0)
            elif (len(self.random_nums) == 0 or len(self.probabilities)==0):
                err_code, err_msg = self.error_msg_from_code(4)
            elif not all(isinstance(k, (int, float)) for k in self.probabilities):
                err_code, err_msg = self.error_msg_from_code(1)
            elif (any(k <= 0 for k in self.probabilities)) or (any(k > 1 for k in self.probabilities)):
                err_code, err_msg = self.error_msg_from_code(2)
            elif abs(sum(self.probabilities)-1.0) > 1.0e-5:
                err_code, err_msg = self.error_msg_from_code(3)
            else:  
                res = self._num_choice()
                err_code, err_msg = self.error_msg_from_code(RandomGen.SUCCESS_CODE)
        except ValueError as e: 
            err_code, err_msg = -1, e
        if showError:
            return res, err_code, err_msg
        else: 
            return res
   
    @staticmethod
    def error_msg_from_code(code):
        code_to_msg = {
                   -1: "Unknown",
                   0: "Length of nums and num of probs does not match",
                   1: "Input probabilities need to be [int, float]",
                   2: "Input probabilities cannot be negative or greater than 1 in value",
                   3: "Probabilities do not sum up to 1",
                   4: "Length 0 of nums and prob of nums lists",
                   100: ""
                }
      
        if code in code_to_msg.keys():
            return code, code_to_msg.get(code)
        else: 
            raise ValueError("No message set for code:{}. Allowed" +
            "Error codes: {}".format(code, str(code_to_msg.keys())))

    def _num_choice(self):
        x = np.random.random()
        cpr = 0.0
        try:
            for n, npr in zip(self.random_nums, self.probabilities):
                cpr += npr
                if x < cpr: 
                    break
            return n  
        except Exception:
            raise Exception("Issue Handling nums and prob lists in num_choice: {}".format(sys.exc_info()[0]))    
        

if __name__ == "__main__":
    a = RandomGen([1, 2], [0.2, 0.8])
    for k in range(100):
        print (a.next_num())