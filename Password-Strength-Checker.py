
'''
Author : Jitendra Kumar Mohapatra
Description : This python script checks the strength/complexity of your password
'''
# special character - [!@#$%^&*]
specialCharacter = [] 

# numerics - [0123456789]
numerics = []

# alphabetsChars - [a-z]
alphabetsChars = []

while True:
    password = input('Enter your password: \n').strip()
    
    if (len(password)==0):
        print("Null!")
        continue
    else:
        break
for i in range(len(password)):
                
# for special chars
    if(not password[i].isalnum()):
        specialCharacter.append(password[i])
            
        
#for numerics
    if(password[i].isnumeric()):
        numerics.append(password[i])
           

#for alphabets
    if(password[i].isalnum() and ( not password[i].isnumeric())):
        alphabetsChars.append(password[i])
            
                        
if(len(password)<8):
    print("Your password should be a minimum of 8 characters inlength")
    
#for strong password... [example:*Jit@2023]
elif((len(specialCharacter) != 0) and (len(numerics) != 0) and (len(alphabetsChars)!=0)):
    print("Great! Your password is strong.")
# [example:*@2023]
elif((len(specialCharacter) != 0) and (len(numerics) != 0) and (len(alphabetsChars)==0)):
    print("Your password is only contains special character & number, Add some alphabet")
# # [example:*Jit@]
elif((len(specialCharacter) != 0) and (len(numerics) == 0) and (len(alphabetsChars)!=0)):
    print("Your password is only contains special character & alphabet, Add some number")
# [example:*@]
elif((len(specialCharacter) != 0) and (len(numerics) == 0) and (len(alphabetsChars)==0)):
    print("Your password is only contains special character, Add some number & alphabet")
# [example:Jit2023]
elif((len(specialCharacter) == 0) and (len(numerics) != 0) and (len(alphabetsChars)!=0)):
    print("Your password is only contains alphabet & number, Add some special character")
# [example:2023]
elif((len(specialCharacter) == 0) and (len(numerics) != 0) and (len(alphabetsChars)==0)):
    print("Your password is only contains number, Add some special character & alphabet")
# [example:Jit]
elif((len(specialCharacter) == 0) and (len(numerics) == 0) and (len(alphabetsChars)!=0)):
    print("Your password is only contains alphabet, Add some special character & Number")
