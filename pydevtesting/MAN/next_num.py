import numpy as np 
import sys

ST_SENTINEL= None
SUCCESS_CODE = 100

def generate_next_num(nums, nums_prob):
    res = ST_SENTINEL
    try: 
        err_code, err_msg = error_msg_from_code(-1)
        if (len(nums) != len(nums_prob)):
            err_code, err_msg = error_msg_from_code(0)
        elif (len(nums) == 0 or len(nums_prob)==0):
            err_code, err_msg = error_msg_from_code(4)
        elif not all(isinstance(k, (int, float)) for k in nums_prob):
            err_code, err_msg = error_msg_from_code(1)
        elif (any(k <= 0 for k in nums_prob)) or (any(k > 1 for k in nums_prob)):
            err_code, err_msg = error_msg_from_code(2)
        elif abs(sum(nums_prob)-1.0) > 1.0e-5:
            err_code, err_msg = error_msg_from_code(3)
        else:  
            res = num_choice(nums, nums_prob)
            err_code, err_msg = error_msg_from_code(SUCCESS_CODE)
    except Exception as e: 
        err_code, err_msg = -1, e
    return res, err_code, err_msg     
  
def next_num(nums, nums_prob):
    num, errcode, errmsg = generate_next_num(nums, nums_prob)
    if errcode == SUCCESS_CODE: 
        return num
    else: # handle error reporting 
        raise ValueError("ERR_CODE {}: {}".format(str(errcode), errmsg))
        
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
        raise ValueError("No message set for code:{}. Allowed Error codes: {}".format(code, str(code_to_msg.keys())))

def num_choice(nums, prob):
    x = np.random.random()
    cpr = 0.0
    try:
        for n, npr in zip(nums, prob):
            cpr += npr
            if x < cpr: 
                break
        return n  
    except Exception as e:
        raise Exception("Issue Handling nums and prob lists in num_choice: {}".format(sys.exc_info()[0]))    
    
if __name__ == "__main__":
    #print ( generate_num_choice([1,2,3],[0.36, 0.63, 0.01]))
    j,i,u = 0, 0, 0
    for k in range(100):
        nnum = next_num([1, 2 ,3], [0.3, 0.6, 0.1])
        if nnum == 1:
            j+=1
        elif nnum ==2: 
            i+=1
        else: 
            u+=1
            
    print("Occurrence Count for [1, 2 ,3] with prob: [0.3, 0.6, 0.1] :", j,i,u)
        