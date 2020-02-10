#################################################################################################### If you know plaintext , e , n and want to find ciphertext, this script is for you ;)

###################################################################################################
print("\n\n\n\033[95m######### Calculating plaintext^e #########\033[0m\n")                    ######## plaintext^e calculation
                                                                                               ####
# Python program to compute                                                                    ####
# factorial of big numbers 

# Maximum number of digits in 
# output 
MAX=10000000 # FOr your RAM's good, just do not put insane number XD

# This function multiplies x 
# with the number represented by res[]. 
# res_size is size of res[] or 
# number of digits in the number 
# represented by res[]. This function 
# uses simple school mathematics 
# for multiplication. 
# This function may value of res_size 
# and returns the new value of res_size 
def multiply(x, res, res_size): 

    # Initialize carry 
    carry = 0

    # One by one multiply n with 
    # individual digits of res[] 
    for i in range(res_size): 
        prod = res[i] * x + carry 

        # Store last digit of 
        # 'prod' in res[] 
        res[i] = prod % 10

        # Put rest in carry 
        carry = prod // 10

    # Put carry in res and 
    # increase result size 
    while (carry): 
        res[res_size] = carry % 10
        carry = carry // 10
        res_size+=1

    return res_size 


# This function finds 
# power of a number x 
def power(x,n): 
    
    # printing value "1" for power = 0 
    if (n == 0) : 
        print("1") 
        return
    
    res=[0 for i in range(MAX)] 
    res_size = 0
    temp = x 

    # Initialize result 
    while (temp != 0): 
        res[res_size] = temp % 10; 
        res_size+=1
        temp = temp // 10


    # Multiply x n times 
    # (x^n = x*x*x....n times) 
    for i in range(2, n + 1): 
        res_size = multiply(x, res, res_size) 
    print("\033[94m")
    print(x , "\033[0m^\033[91m" , n , "\033[0m = ",end="\n\033[93m") 
    for i in range(res_size - 1, -1, -1): 
        print(res[i], end="") 

print('\033[0m')
# Driver program 
plaintext = int(input("plaintext="))
print("\n")
e_variable = int(input("e="))
exponent = e_variable
base = plaintext

power(base, exponent,) 

# This code is contributed 
# by Anant Agarwal. 

############################ Source for the code ############################                  ####
# https://www.geeksforgeeks.org/writing-power-function-for-large-numbers/                      ####
                                                                                               ####
###################################################################################################
                      ### ||
                      ### || Copy and paste the plaintext^e result
                      ### \/
###################################################################################################
print("\n\n\n\033[95m######### Calculating (plaintext^e) mod n #########\033[0m\n\n\n")        ######## ciphertext = (plaintext^e) mod n calculation
                                                                                               ####
                                                                                               ####
# Python 3 program of finding 
# modulo multiplication 
  
# Returns (a * b) % mod 
def moduloMultiplication(a, b, mod): 
  
    res = 0; # Initialize result 
  
    # Update a if it is more than 
    # or equal to mod 
    a = a % mod; 
  
    while (b): 
      
        # If b is odd, add a with result 
        if (b & 1): 
            res = (res + a) % mod; 
              
        # Here we assume that doing 2*a 
        # doesn't cause overflow 
        a = (2 * a) % mod; 
  
        b >>= 1; # b = b / 2 
      
    return res; 
  
# Driver Code 

plaintext_e = int(input("plaintext^e="))
print("\n")
n_variable = int(input("n="))
print("\n")

#######################
a = plaintext_e;     #### (a*b) mod n
b = 1;               ##
n = n_variable;      ##
#######################

print("ciphertext = \033[94m(plaintext ^ e)\033[0m mod \033[91mn\033[0m =\033[93m") 
print(moduloMultiplication(a, b, n)); 
      
# This code is contributed 
# by Shivi_Aggarwal 

############################ Source for the code ############################
# https://www.geeksforgeeks.org/multiply-large-integers-under-large-modulo/
                                                                                               ####
                                                                                               ####
                                                                                               ####
###################################################################################################
