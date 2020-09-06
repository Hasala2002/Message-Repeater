import time

for i in range(100):
            if i<=10:
                 print(i)
            elif i>10 and i<=30:
                 time.sleep(1)
                 print(i)
            elif i>30 and i<=40:
                 time.sleep(1.5)
                 print(i)
            elif i>40:
                 time.sleep(2.5)
                 print(i) 