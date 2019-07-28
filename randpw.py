import random
import pyperclip
str="qwertyuiopasdfghjklzxcvbnm1234567890*#"
def randstr (length_pw,prestr):

	return ''.join(random.choice(str) for x in range(length_pw))

n=int(input ("Enter the length of the password: "))
newstr=randstr(n,str)
print ("Your Password is: "+newstr)
pyperclip.copy(newstr) #copy to clipboard

