class UserAccount:
    def __init__(self,username,email,passw):
        self._password=passw
        self._email=email
        self._username=username
        self._logged_in=False
    def login(self, passw):
        if self._password==passw:
            self._logged_in=True
        else:
            print("wrong password")
    def logout(self):
        if self._logged_in==True:
            self._logged_in=False
            print("logged out")
        else:
            print("already logged out")

    def changePassword(self, oldpass, newpass):
        if self._logged_in and self._password==oldpass:
            self._password=newpass
        else:
            print("Wrong pass or log in first")

    def getmaskingemail(self):
        if self._logged_in:
            name, domain= self._email.split('@')
            return name[0]+"****"+name[-1]+"@"+domain
    def getProfile(self):
        if self._logged_in:
            name, domain= self._email.split('@')
            mail=name[0]+"****"+name[-1]+"@"+domain
            return {"username": self._username, "email":mail}
        else:
            print("Login first")


account1=UserAccount("Habibur", "hraasif@gmail.com", "1234")
account1.login("1234")
account1.getProfile()
account1.getmaskingemail()
account1.logout()
account1.getProfile()




class Admin(UserAccount):
    def __init__(self, username, email, passw):
        # Initialize the parent class (UserAccount)
        super().__init__(username, email, passw)
        # Set the specific attribute for this subclass
        self.role = 'ADMIN'
      
    def getProfile(self):
        if not self._logged_in:
            print("Login First")
            return None
            
        # Call the parent's getProfile method to get the base data
        profile = super().getProfile()
        
        # Optionally, you could add admin-specific info here
        profile['role'] = self.role
        
        return profile

admin1=Admin("Habibur", "hraasif@gmail.com", "1234")
admin1.login("1234")
admin1.getProfile()
