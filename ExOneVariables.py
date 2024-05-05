desired_age = 25
real_age = 31
name = 'Jake'

print(name + " wants to be " + str(desired_age) + " years old.")

#simple if statement
if desired_age < real_age:
    print(name + " is " + str(real_age) + ". He wishes he was younger so he could learn Python earlier.")
elif desired_age > real_age:
    print(name + " is " + str(real_age) + ". He wishes he was older. He wants those cheaper cinema tickets.")
else:
    print(name + " is " + str(real_age) + ". He is exactly the age he wants to be. Go him!")

#index a string
print('What is the second letter in the name?')
print(name[1])
print('What is the last letter in the name?')
print(name[-1])
print('What are the middle two letters in the name?')
print(name[1:3])