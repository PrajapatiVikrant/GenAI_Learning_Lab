str = '''
     Dear <|Name|>
     You are selected!
     <|Date|>
'''

str = str.replace("<|Name|>", "John").replace("<|Date|>", "2024-06-30")


print(str)