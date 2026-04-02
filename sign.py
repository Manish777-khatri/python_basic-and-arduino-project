print("Regester ")
username=input("username: ")
password=input("password: ")
if(username=="" or password==""):
     print("please Fill the username and password!")
else:
     print("Login Now:")
     username1=input("username: ")
     password1=input("password:")
     if(username1==username and password1==password):
          print("Login Successfull !!!")
     else:
          print("Enter correct username and password!!")



