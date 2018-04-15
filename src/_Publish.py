import zipfile
import os

rt = './SVGPathExporter/'

def src(z, file):
    path = rt + file
    print('add src : ' + path)
    z.write(rt + file)

# install target
def defFiles(z):
    src(z, '__init__.py')
    src(z, 'blut.py')
    src(z, 'ut.py')
    src(z, 'opSVGExport.py')

z = zipfile.ZipFile('Installer/SVGPathExporter.zip', 'w', zipfile.ZIP_STORED)
defFiles(z)
z.close()
