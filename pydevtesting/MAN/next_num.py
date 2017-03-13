import numpy as np 

ST_SENTINEL= None
SUCCESS_CODE = 100

def _generate_next_num(nums, nums_prob):
    res = ST_SENTINEL
    if (len(nums) != len(nums_prob)):
        return res, 0
    elif not all(isinstance(k, (int, float)) for k in nums_prob):
        return res, 1
    elif any(k < 0 for k in nums_prob):
        return res, 2
    elif sum(nums_prob) != 1:
        return res, 3
    else:  
        try:
            res = np.random.choice(a=nums, p=nums_prob)
            return res, SUCCESS_CODE
        except ValueError as e: 
            return res, e

def next_num(nums, nums_prob):
    num, errcode = _generate_next_num(nums, nums_prob)
    if errcode == SUCCESS_CODE: 
        return num
    else: # handle error reporting 
        if isinstance(errcode, int): 
            raise ValueError(error_msg_from_code(errcode))
        else:
            raise ValueError(str(errcode))
        
def error_msg_from_code(code):
    code_to_msg = {-1: "Unknown",
                   0: "Length of nums and num of probs does not match",
                   1: "Input probabilities need to be [int, float]",
                   2: "Input probabilities has a negative value",
                   3: "Probabilities do not sum up to 1",
                   100: ""
                }
      
    if code in code_to_msg.keys():
        return code_to_msg.get(code)
    else: 
        raise ValueError("No message set for code:{}. Allowed Error codes: {}".format(code, str(code_to_msg.keys())))
    

if __name__ == "__main__":
    for k in range(10):
        nnum = next_num(['a', 2], [0.36, 0.63])
        print (nnum)
        