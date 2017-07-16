## This is the text editor interface. 
## Anything you type or change here will be seen by the other person in real time.

#
# 123 -> one hundred twenty three
# 87 624 -> eighty seven thousand six hundred twenty four
# 1 784 930

import math

def stringReader(num):
    num = str(num)[::-1]
    
    ones = {0: "", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:'seven', 8:'eight', 9:'nine'}
    tenth = {2:"twenty", 3:"thirty", 4:"fourty", 5:"fifty", 6:"sixty", 7:'seventy', 8:'eighty', 9:'ninety'}
    tens = {11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 
            17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
    hundrethposn = {0:"", 1: "thousand" , 2: "million" }
    ans = []
    
    for pos in xrange(int(math.ceil(len(num)/3))):
        hundreth = hundrethposn[pos]
        ans.append(hundreth)
        
        for i in xrange(3):
            if (3*pos+i < len(num)):
                print(num[3*pos+i])
                
                if (i==0):
                    ans.append(ones[int(num[3*pos+i])])
                if (i==1):
                    if (num[3*pos+i] == 1):
                        ans.pop()
                        ans.append(tens[int(num[3*pos+i])])
                    else:
                        ans.append(tenth[int(num[3*pos+i])])
                if (i==2):
                    ans.append("hundred")
                    ans.append(ones[int(num[3*pos+i])])
        
    ans = ans[::-1]
    for word in ans:
        print word
    
    
#if __name__ == "__main__":
stringReader(123456789)