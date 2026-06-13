# write a program to print the content of the directory using the os module
import os


content = os.listdir('/ai_engineering/python')


for item in content:
    print(item);


