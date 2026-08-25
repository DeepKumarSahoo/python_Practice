class num:
    def __init__(self, numlist):
        self.numlist = numlist
    def num2(self):
        num1=str(self.numlist)
        reverse_num=num1[::-1]
        if num1 == reverse_num:
            print("It is a palindrome number!!")
        else:
            print("Not palindrome!!")    
    
s1=num(121)    
s1.num2()