import random

characters = ["+","-","/","*","!","&","$","#","?","=","@","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]
length = int(input("Enter the length of the desired password: "))
password = ""

for i in range(length):
    password = password + random.choice(characters)

print("Generated password is: ", password)
