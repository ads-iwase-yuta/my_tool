import os
import re
import glob

import PyPDF2

merger = PyPDF2.PdfFileMerger(strict=False)

file_list = glob.glob('input/*.pdf')

for f in file_list:
    merger.append(f)

# merger.append('input/01.pdf')
# merger.append('input/02.pdf')

merger.write('output/sample_merge.pdf')
merger.close()