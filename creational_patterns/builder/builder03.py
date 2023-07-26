'''
Create a simple User class which holds such data as: 
First_name – required, last_name – required, age – optional, phone_number – optional address 
– optional, email_adress – required. Make all these elements immutable in your User class, 
provide only getters. 
Create a UserBuilder class that can build a user with above elements and which then can be 
used to initialize the User class.

'''


class User:

    def __init__(self, first_name, last_name, email_address, age=None, phone_number=None, address=None):
        self._first_name = first_name
        self._last_name = last_name
        self._email_address = email_address
        self._age = age
        self._phone_number = phone_number
        self._address = address

    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @property
    def age(self):
        return self._age
    
    @property
    def phone_number(self):
        return self._phone_number
    
    @property
    def address(self):
        return self._address
    
    @property
    def email_address(self):
        return self._email_address


class UserBuilder:

    def __init__(self):
        self._first_name = None
        self._last_name = None
        self._email_address = None
        self._age = None
        self._phone_number = None
        self._address = None

    def set_first_name(self, name):
        self._first_name = name
        return self

    def set_last_name(self, last_name):
        self._last_name = last_name
        return self

    def set_email_address(self, email_address):
        self._email_address = email_address
        return self

    def set_age(self, age):
        self._age = age
        return self

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number
        return self

    def set_address(self, address):
        self._address = address
        return self

    def build(self):
        if not self._first_name or not self._last_name or not self._email_address:
            raise ValueError('First name, last name and email address are mandatory.')
        return User(self._first_name, self._last_name, self._email_address, self._age, self._phone_number, self._address)

# Example of use:
builder = UserBuilder()
user = (builder.set_first_name('Luki')
              .set_last_name('Zbyszowski')
              .set_email_address('luki.zbyszowski@gmail.com')
              .set_age(30)
              .set_address('sliska 14')
              .build())

        
print(user.first_name) 
print(user.last_name) 
print(user.email_address) 
print(user.age) 
print(user.address) 
print(user.phone_number)  