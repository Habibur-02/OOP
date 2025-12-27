class UserAccount:
    def __init__(self,username,email,passw):
        self.__password=passw
        self.__email=email
        self.__username=username
        self.__logged_in=False
    def login(self, passw):
        if self.__password==passw:
            self.__logged_in=True
        else:
            print("wrong password")
    def logout(self):
        if self.__logged_in==True:
            self.__logged_in=False
            print("logged out")
        else:
            print("already logged out")

    def changePassword(self, oldpass, newpass):
        if self.__logged_in and self.__password==oldpass:
            self.___password=newpass
        else:
            print("Wrong pass or log in first")

    def getmaskingemail(self):
        if self.__logged_in:
            name, domain= self.__email.split('@')
            return name[0]+"****"+name[-1]+"@"+domain
    def getProfile(self):
        if self.__logged_in:
            name, domain= self.__email.split('@')
            mail=name[0]+"****"+name[-1]+"@"+domain
            return {"username": self.__username, "email":mail}
        else:
            print("Login first")


account1=UserAccount("Habibur", "hraasif@gmail.com", "1234")
account1.login("1234")
account1.getProfile()
account1.getmaskingemail()
account1.logout()
account1.getProfile()
