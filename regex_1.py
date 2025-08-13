import re
nama = "I Wayan Alexandra Sorowwfull Reunion"
email = "uLetHerGoAgain@domain.com"
emailpalsu = "adaw11\adw"
noHP = "088811233"
def cekEmail(email: str):
    return True if re.match(r"^[\w\.\-]+@[\w\.\-]+\.\w+$",email) else False

def cekNo(noHP:str):
    res = re.match(r"[\d]",noHP)
    return True if res else False

if __name__ == "__main__":
    print(cekEmail(emailpalsu))
    print(cekNo(noHP))
    
    