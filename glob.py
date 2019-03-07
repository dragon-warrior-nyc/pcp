import glob

# grab files matching the re
files = glob.glob('./files/*.txt')

for file in files:
    print(f'{file}')
