import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class UserInfo:
    def __init__(self, name, phone):
    #def set_info(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("--------------------------")
        print("Name : " + self.name)
        print("Phone : " + self.phone)
        print("--------------------------")

    def __del__(self):
        print("delete!")

user1 = UserInfo("kim","010-1234-1234")
user2 = UserInfo("park","010-5678-5678")
#user1 = UserInfo()
#user2 = UserInfo()

print(id(user1))
print(id(user2))

#user1.set_info("kim","010-1234-1234")
#user2.set_info("park","010-5678-5678")

user1.print_info()
user2.print_info()

print(user1.__dict__)
print(user2.__dict__)

print(user1.name,user1.phone)
