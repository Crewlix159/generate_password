import random
all_simbols = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!?/.@#$%^&*><"
length_password = int(input("ВВедите длину пароля: "))
password = ""
for i in range(length_password):
    password += random.choice(all_simbols)
print(password)