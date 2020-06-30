import glob
import os

import PyPDF2

merger = PyPDF2.PdfFileMerger(strict=False)

file_list = glob.glob('input/*.pdf')

print('order:')
for i, f in enumerate(file_list):
    basename = os.path.basename(f)
    print(' {}: {}'.format(i, basename))
    merger.append(f)

output_path = 'output/merged.pdf'
merger.write(output_path)
merger.close()

print('\nMerge process complete! See {}\n'.format(output_path))