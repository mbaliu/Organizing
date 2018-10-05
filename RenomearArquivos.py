#encoding: utf-8
# RENOMEIA lista de arquivo em uma pasta, internamente ao QGIS.
#não faz distinção entre os formatos ou cojunto do mesmo nome.

import os, shutil


dir = 'C:\\..\\Q_Temp\\__LIXOOO\\CMD\\'
    
files = os.listdir(r'C:\..\Q_Temp\__LIXOOO\CMD')
for i in files:
    filedir_from = [dir, i]
    filedir_from = ''.join(filedir_from)
    
    filedir_to = [dir, 'PNU_'+i[4:]]
    filedir_to = ''.join(filedir_to)
    
    
    shutil.move(filedir_from, filedir_to)
