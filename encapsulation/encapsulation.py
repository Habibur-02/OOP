class UserAccount:
    def __init__(self,username,email,passw):
        self.__password=passw
        self.__email=email
        self.__username=username
        self._logged_in=False
    def login(self, passw):
        if self.__password==passw:
            self._logged_in=True
        else:
            print("wrong password")
    def logout(self):
        self._logged_in=False
    def changePassword(self, oldpass, newpass):
        if self._logged_in and self.__password==oldpass:
            self.__password=newpass
        else:
            print("Wrong pass or log in first")

    def getmaskingemail(self):
        if self._logged_in:
            name, domain= self.__email.split('@')
            return name[0]+"****"+name[-1]+"@"+domain
    def getProfile(self):
        if self._logged_in:
            return {"username": self.__username, "email":self.__email}
        else:
            print("Login first")


account1=UserAccount("Habibur", "hraasif@gmail.com", "1234")
account1.login("1234")
account1.getProfile()
account1.getmaskingemail()
account1.logout()
account1.getProfile()

