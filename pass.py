import secrets
import string
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation 
alphabet = letters + digits + special_chars
pas_length = 12
pas = ""
for i in range(pas_length):
    pas +=''.join(secrets.choice(alphabet))
    print(pas)