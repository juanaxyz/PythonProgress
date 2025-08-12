'''
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("this is decorating your func")
        print(f"{args}, {kwargs}")
        func(*args,**kwargs)
    return wrapper

@my_decorator
def hello_world(name , pesan ="hallow"):
    print(f"hello {name}!, pesan = {pesan}")
    
# my_decorator(hello_world)
hello_world(name="juana", pesan="hai sayang")
output {'name': 'juana', 'pesan': 'hai sayang'}

'''

import time 

def log_file(function):
    def wrapper(*args,**kwargs):
        t = time.gmtime()
        user = kwargs.get("name","Guest")
        return_value = function(*args,**kwargs)
        log_text = f"user : {user} running function : {function.__name__} at {time.asctime(t)} UTC TimeZone. \n" 
        with open("logFile.txt","+a") as f:
            f.write(log_text)
        return return_value
    return wrapper


@log_file            
def sum(a,b,name ="guest"):
    return a + b

# sum(20,b=50)
sum(a=10,b=20, name="juana")
sum(a=5,b=50, name="aku")
            