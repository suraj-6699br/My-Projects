import random 
import string 

pass_len= 13
charvalues =string.ascii_letters + string.digits + string.punctuation 

password = ""
for i in range (pass_len):
 password += (random.choice(charvalues))
print("your rndom password is :" , password)

#Another method by list comprihention [fuction for i in range(n)]
# password="".join([random.choice(charvalues) for i in range (pass_len)])
# print("your random password is :" , password)