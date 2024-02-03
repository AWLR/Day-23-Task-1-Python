email = input("Enter your email: ")
name = input("Enter your name: ")
k,j,d = 0,0,0 # k = space, j = upper, d = digit
if len(email) >=6: # length of email should be greater than 6
    if email[0].isalpha(): # first letter should be alphabet
        if "@" in email and email.count("@") == 1: # @ should be present once
            if(email[-4] == "." or email[-3] == "."): # . should be present at the end
                for i in email:
                    if i.isspace(): 
                        k = 1
                    elif i.isalpha(): 
                        if i.isupper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i in ["_",".","@"]:
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("Wrong email format")
                else:
                    print("Right email format")

            else:
                print("Wrong email format: Missing or misplaced dot in the domain")

        else:
            print("Wrong email format: Incorrect number of @ symbols")

    else:
        print("Wrong email format: Email must start with a letter")

else:
    print("Wrong email format: Length of email should be greater than 6")

# 3 conditions for name validate
if len(name) < 2:
    print("name lenght should be more than 2")
elif name.isdigit() == 1:
    print("name should not include numbers or digits")
elif name.isalpha() == 0: #check symbols in string
    print("name must be in alphabelts only")
else:
    print("valid name")
            