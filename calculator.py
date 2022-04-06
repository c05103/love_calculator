#created and deployed by Collin Chimbwanda 


#these are the inputs of the names of both people

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# makes all inputs lowercase for simpler counting between upper and lower cases


name = name1.lower()
sec_name = name2.lower()

name1 = name 
name2 = sec_name

#adds the count inputs of the true for both names 

t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")
e = name1.count("e") + name2.count("e")

true = t + r + u + e

#adds the count inputs of the love for both names

l = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")
e = name1.count("e") + name2.count("e")

love = l + o + v + e

#score is concatinating love and true, then making then into a int to use in the string for outputs 

score = int(str(true) + str(love))

# if statement to search the criteria of the love calculator 

if score < 10 or score > 90 :
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50 :
    print(f"Your score is {score}, you are alright together.")
else :
    print(f"Your score is {score}.")
    
    
# end of code 
