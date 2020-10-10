import random, string

def getcaptchaans():
    valid_input=False
    return valid_input
        
def showNewCaptcha():
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) 
                for _ in range(4))
    print(x)
    return x
    

def input_check(valid_input):
    while not valid_input:
        validAnswer=showNewCaptcha()
        answer=input("take the input")
        #answer=answer.lower()
        #validAnswer= validAnswer.lower()
        if answer == validAnswer:
            valid_input = True
        else:
            print('please try again')
    return answer


input_check(getcaptchaans())

