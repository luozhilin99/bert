import os

for file in os.listdir('./'):
    if file.endswith('.py') and file != 'test.py':
        f = open(file)
        lines = f.readlines()
        f.close()
        f = open(file, 'w')
        f.writelines(lines[1:])
        f.close()