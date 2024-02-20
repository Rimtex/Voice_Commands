import os
import time


def printt(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.015)

with open('gpt_code.py', 'r', encoding='utf-8') as file:
    data = file.read()


try:
    print(data)
    import gpt_code    
    input()
except Exception as e:
    error = str(e)
    printt(error)
    if "No module named" in error:
        import_error = error.split("'")[1]    
        printt("\nПопытка установить необходимый модуль\n")
        os.system(f'pip install --upgrade {import_error}')        
        os.startfile("gpt_code_tester.py")
    else:
        input()            

"""



"""
