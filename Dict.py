user = {
"name" : str(input()),
"family" : str(input()),
"age " : int(input()),
}
for key,value in user.items():
    print(key,value)
print(type(user)) 
