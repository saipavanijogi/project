import json

user=input("enter login or signup :")
if user=="signup":
    user_name=input("enter the user_name :")
    password=input("enter the password here : ")
    print("enter your conformation password")
    conformation_password=input("enter the conformation password :")
    if len(password)>=1 and len(password)<=17:
        if "A" or "Z" in password:
            if "@" in password or "#"in password or "$" in password:
                if "a" or "z" in password:
                    if "0" or "9" in password:
                        print("strong password")
                    else:
                        print("week password")
                else:
                    print("lower case is not there")
            
            else:
                print("special character is not there")
        else:
            print("upper  case is not there")
    else:    
        print("wrong password")
    if password==conformation_password:
        pass
        with open ('Signup.json'):
            b=open('Signup.json',"r")
            data=json.load(b)
            for i in data["user"]:
                if i["username"]==user_name:
                    print("it's already exists")
                else:
                    dict={}
                    d={}
                    dict["user name"]=user_name
                    dict["password"]=password
                    d["description"]=input("enter the description here:")
                    d["date of birth"]=input('enter the date of birth:')
                    d["gender"]=input("enter the gender here:")
                    d["Hobbies"]=input("enter your hobbies :")
                    dict["profile"]=d
                    b=data["user"]
                    b.append(dict)
                    f=open("signup.json","w")
                    json.dump(data,f,indent=4)
                    f.close()
                    print("sigup succesfully")
                    break
    else:
        print("does not match")
elif user=="login":  
    b=open("signup.json","r")
    f=json.load(b)
    c=input("enter the user name for login:")
    d=input("enter the password for login:")
    for i in f["user"]:
        if c==i["username"]:
            if d==i["password"]:  
                print("login sucessfully")
                print(i)
            else:
                print("check your password")
        else:
            print("check your username")
            break
else:
    print("check your pin number")