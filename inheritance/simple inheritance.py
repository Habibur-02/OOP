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
