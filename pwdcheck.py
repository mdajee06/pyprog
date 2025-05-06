inp = open("users.csv" , "r")
data = inp.readlines()
inp.close()
print(data)

users = {}
for line in data:
    user = line.strip().split (",")
    users.update({user[0]:user[1]})

print(users['username 1'])

name=input("username? ")
pwd=input("password? ")
if[name,pwd] in users:
    print("correct!")
else:
    print("wrong!")    
