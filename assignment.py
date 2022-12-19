#incomplete
def two_sum (*nums, target):
    nums= list(nums[0])
    for i in range (len(nums)):
        for j in range(len(nums)):
            if target==nums[i]+nums[j]:
                return [i,j]

        
    


def power(x,n):

     return (x**n)

def increment(a):
    a+=1
    return(list (str(a)))
       
def Palindrome (a : str):
    b=list (str(a))
    for i in range(len(b)):
        if b[i] == b[len(b) -1 -i]:
            return True
        else:
            return False

def max_profit (*prices):
    prices=list(prices[0])
    a=min(prices)
    prices = prices[prices.index(a):]
    b= max(prices)
    return b-a
    
prices = [2,7,11,15]
print(two_sum(prices, target=9))
  





    

