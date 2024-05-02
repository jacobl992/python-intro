desired_age = 25
real_age = 31
name = 'Jake'

print(name + " wants to be " + str(desired_age) + " years old.")

if desired_age < real_age:
    print(name + " is " + str(real_age) + ". He wishes he was younger so he could learn Python earlier.")
elif desired_age > real_age:
    print(name + " is " + str(real_age) + ". He wishes he was older. He wants those cheaper cinema tickets.")
else:
    print(name + " is " + str(real_age) + ". He is exactly the age he wants to be. Go him!")