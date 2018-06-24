#! python3
#moveRename.py - Modifica o nome dos arquivos.

import shutil, os

'''cwd INPUT'''
cwd = input('cwd: ')
newcwd = r'%s\py' %cwd


'''Cria nova pasta e copia arquivos para nova pasta'''
shutil.copytree (cwd, newcwd)


'''Navega entre as pastas'''
for folderName, subfolders, filenames in os.walk(newcwd):
    numFiles = 0
    for file in filenames:
        nfilename = ' '.join(file.split('+'))
        nfilename = ' '.join(nfilename.split('_'))
        nfilename = ' '.join(nfilename.split('-'))
        #print(nfilename)
        filedir = newcwd+'\\'+file
        nwfiledir = newcwd+'\\'+nfilename
        shutil.move(filedir, nwfiledir)
        numFiles += 1
    print(str(numFiles)+' files renamed!')
