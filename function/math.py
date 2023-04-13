def add(d,c):
    answer=d+c
    return answer

    def subtraction(a,b):
     answer=a-b
    return answer

def sum_multiplication(sum,multiplication):
   return (f"the sum of 6 and 2 is{sum} amd their product is {multiplication}")
          
        #   positional ,arguments
print(sum_multiplication(6+2,6*2,))
        # keyword arguments
 
#  default arguments
def names(firstname="a",secondname="b"):
   return (f"my name is {firstname} {secondname}")
print (names())
print(names("joyce"))
print(names("mumbi","wanjiku"))
print(names(secondname="wanjiku",))