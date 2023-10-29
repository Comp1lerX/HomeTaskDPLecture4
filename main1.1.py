def remove_spaces(str_with_spaces:str)->str:
    WL = list(str_with_spaces.split())
    str_without_spaces = ' '.join(WL)
    return str_without_spaces

a="Hello                    word"
print(a)
a = remove_spaces(a)
print(a)