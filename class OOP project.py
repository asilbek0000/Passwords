#print("class project in a big scale OOP-topic")

class Credential():
    
    def __init__(self, App, User, Pass):
        self.App = App
        self.Username = User
        self.Password = Pass
     
#function
    def getInfo(self):
       output = f"\nApp:{self.App} \nUsername: {self.Username} \nPassword: {self.Password}"
       return output

#result
cered = Credential("Insta", "Asilbek", "asilbek2008")
cered1= Credential("Telegram", "Asadov", "Asadov7000")
#list
my_list=[]
my_list.append(cered)
my_list.append(cered1)

#loop
ghost = input("Enter the app")
for cered in my_list:
    if cered.App==ghost:
      print(cered.getInfo())

