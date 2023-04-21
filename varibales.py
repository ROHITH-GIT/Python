import zipfile

with zipfile.ZipFile('files.zip', 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
   zf.write('results.csv')
   