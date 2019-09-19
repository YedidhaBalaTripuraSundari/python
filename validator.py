# phone number validator
import re
def phone(number):
    p='[6-9][0-9]{9}|[+][9][1][6-9][0-9]{9}'
    if re.match(p,str(number)):
        return True
    else:
        return False
    
import re
def emailid(email):
    g='^[a-z][0-9a-z.]{5,15}[@][0-9a-z]{3,8}.[a-z]{2,4}|[a-z][0-9a-z.]{5,15}[@][0-9a-z]{3,8}.[a-z]{2,4}|.[a-z]{2,3}$'
    if re.match(g,str(email)):
        return True
    else:
        return False
