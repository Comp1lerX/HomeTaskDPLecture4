def remove_spaces(str_with_spaces:str)->str:
    WL = list(str_with_spaces.split())
    str_without_spaces = ' '.join(WL)
    return str_without_spaces

with open('1.2.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('1.2.txt', 'w', encoding='utf-8') as f:
    for i_string in lines:
        string = remove_spaces(i_string)
        f.write(string + '\n')

with open('1.2.txt', 'r', encoding='utf-8') as f:
    speakers_lines_new = f.readlines()
    print(*speakers_lines_new)

