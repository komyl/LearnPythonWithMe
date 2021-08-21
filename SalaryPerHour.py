def salaryperhours (H , P):
    salary = H * P
    if H > 8 :
        print("You Work :",H ,"Hours,This Too Much And It's HarmFul To Your Health,Please Rest")
        print("However Your Salary Per Hours :", salary)
    else :
        print("Your Salary Per Hour : " , salary)
        
                       
        
print("Hello sir , Please enter the required values :")        
H  = int(input("How Many Hours Do You Work ?"))
P = int(input("You Earn a Few Dollars an Hour ?"))
salaryperhours(H, P)
print("Good Luck")    
  
    