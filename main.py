import random

char=int(input("How many characters do you want in password?"))
num=int(input("How many numbers do you want in password?"))
sym=int(input("How many symbols do you wants in password?"))

characters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','&','*','(',')','{','}','=','+','-','_']

passwd=[]
for i in range(char):
    passwd.append(random.choice(characters))
for i in range(num):
    passwd.append(random.choice(numbers))
for i in range(sym):
    passwd.append(random.choice(symbols))

print(passwd)

random.shuffle(passwd)
print(passwd)

x=''
for i in passwd:
    x+=i

print(x)
print(len(x))