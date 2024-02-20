import os
import time

def printt(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.015)

try:
    import gpt_code
except Exception as e:
    error = str(e)
    printt(error)
    import_error = error.split("'")[1]
    printt("\nПопытка установить необходимый модуль")
    os.system(f'pip install --upgrade {import_error}')
    if "No module named" in str(error):
        os.startfile("tester.py")
"""


```
import os

try:
    import gpt_code
except Exception as e:
    if "No module named 'gpt_code'" in str(e):
        print("Trying to install the required module")
        os.system('pip install --upgrade "gpt_code"')
        input(error)
```


```python
import os

try:
    import gpt_code
except Exception as e:
    error = e
    if "No module named 'gpt_code'" in str(error):
        print(error)
        import_error = str(error).split("'")[1]
        print("Попытка установить необходимый модуль")
        os.system(f'pip install --upgrade {import_error}')
```






"""   

