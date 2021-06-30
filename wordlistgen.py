import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

while 1: 
    password_len = int(input("what length should it be : "))
    password_count = int(input("how much : "))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password      = password + password_char
        print("Here is your password : ", password)
        appendFile = open("file.txt","a")
        appendFile.write("\n")
        appendFile.write(password)
        appendFile.close    
    quit()

