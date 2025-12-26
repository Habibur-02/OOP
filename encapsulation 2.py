class User:
    def __init__(self, username, password, email):
        self.username = username          # public
        self.__password = password        # private
        self.__email = email              # private

def setPassword(self, new_password):
        self.__password = new_password

def checkPassword(self, input_password):
        return self.__password == input_password

def getMaskedEmail(self):
        name, domain = self.__email.split("@")
        masked_name = name[0] + "****" + name[-1]
        return masked_name + "@" + domain

user1 = User("habibur", "1234", "habibur@gmail.com")

print(user1.username)                 # allowed
print(user1.checkPassword("1234"))    # True
print(user1.checkPassword("0000"))    # False
print(user1.getMaskedEmail())