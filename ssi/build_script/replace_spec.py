import re

file_name = 'SSI.spec'
with open(file_name, 'r') as f:
    s = f.read()

with open(file_name, 'w') as f:
    bef = r'(EXE\(.*\n)'
    after = '\\1          Tree(\'../resources\',prefix=\'resources\'),\\n'
    rep = re.sub(bef, after, s)
    print(rep)
    f.write(rep)

