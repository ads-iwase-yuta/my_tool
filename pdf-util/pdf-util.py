import sys
from pathlib import Path

import PyPDF2

def main():
    args = sys.argv[1:]

    merger = PyPDF2.PdfFileMerger(strict=False)

    try:
        order_counter = 0
        print('order:')
        for arg in args:
            (path, page_ranges) = solve_arg(arg)
            abs_path = str(path.resolve())

            if page_ranges:
                for page_range in page_ranges:
                    is_single_page = (len(page_range.split(':')) == 1)
                    if is_single_page:
                        corrected_page_range = page_range
                    else:
                        start_page = int(page_range.split(':')[0])
                        end_page   = int(page_range.split(':')[1])+1
                        corrected_page_range = f'{start_page}:{end_page}'

                    merger.append(
                        abs_path, pages=PyPDF2.pagerange.PageRange(corrected_page_range)
                    )
                    print(f' {order_counter}: {abs_path}?{page_range}')
                    order_counter += 1
            else:
                merger.append(abs_path)
                print(f' {order_counter}: {abs_path}')
                order_counter += 1

        output_path = Path('./merged.pdf')
        output_abs_path = str(output_path.resolve())

        merger.write(output_abs_path)
        merger.close()
        
        total_pages = PyPDF2.PdfFileReader(open(output_abs_path, mode='rb')).getNumPages()
        print(f'\nMerge process complete! See {output_abs_path}')
        print(f'{output_path.name} has {total_pages} pages.')
    except Exception as e:
        print(str(e))
        print('\nMerge process failed!')

def solve_arg(arg: str):
    has_range = (len(arg.split('?')) >= 2)

    if has_range:
        path        = Path(arg.split('?')[0])
        page_ranges =      arg.split('?')[1].split(',')
    else:
        path        = Path(arg)
        page_ranges = None

    return (path, page_ranges)

if __name__=='__main__':
    main()