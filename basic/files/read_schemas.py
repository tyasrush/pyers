import os
import glob

# Open file with specific file type on any specific folder.
for fname in glob.glob(os.path.join(os.getcwd(), 'basic/files/schemas/*.sql')):
    with open(fname, 'r') as fre:
        print(fre.read())

# Open all files in folder.
for fname in os.listdir(os.getcwd() + '/basic/files/schemas'):
    with open(f'{os.getcwd()}/basic/files/schemas/{fname}', 'r') as fre:
        print(fre.read())

strTestQueries = ''
for fname in os.listdir(os.getcwd() + '/basic/files/schemas'):
    with open(f'{os.getcwd()}/basic/files/schemas/{fname}', 'r') as fre:
        strTestQueries += fre.read()

print('--------------------\n')
print(strTestQueries)
