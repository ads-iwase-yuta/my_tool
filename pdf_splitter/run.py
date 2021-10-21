import glob
import os
from argparse import ArgumentParser

import PyPDF2

merger = PyPDF2.PdfFileMerger(strict=False)

argparser = ArgumentParser()
argparser.add_argument('-f', '--filepath', type=str,
                        default='',
                        help='The file path is "input/[]". Please enter the file name in [].')
argparser.add_argument('-s', '--start', type=int,
                        default=1,
                        help='Start page. This value is greater than or equal to 1')
argparser.add_argument('-e', '--end', type=int,
                        default=-1,
                        help='End page. This value is greater than or equal to 1')
args = argparser.parse_args()

if args.filepath:
    pdf_file_path = 'input/{}'.format(args.filepath)
else:
    pdf_file_path = glob.glob('input/*.pdf')[0]
start_page = args.start-1
if args.end>=1:
    end_page = args.end
else:
    end_page = PyPDF2.PdfFileReader(open(pdf_file_path, mode='rb')).getNumPages()

merger.append(pdf_file_path, pages=PyPDF2.pagerange.PageRange(
    '{}:{}'.format(start_page, end_page))
    )

basename = os.path.basename(pdf_file_path)
basename_without_ext = os.path.splitext(basename)[0]
output_path = 'output/{}_{}to{}.pdf'.format(basename_without_ext, start_page+1, end_page)
merger.write(output_path)
merger.close()

print('\nSplit process complete! See {}\n'.format(output_path))