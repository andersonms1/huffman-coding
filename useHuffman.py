from huffman import HuffmanCoding
from stats import Stats
import sys
import os

if len(sys.argv) == 1:

    print('Incorrect use!')
    print('Put the the files on the files folder')
    print('Especify the file in the args')
    print('Example: python useHuffman.py file1 file2 file3')

    sys.exit

else:
    path = []
    for file in range(1, len(sys.argv)):
        print('----- '+sys.argv[file]+' -----')
        
        h = HuffmanCoding('./files/'+sys.argv[file]+'.txt')
        output_path = h.compress()
        decom_path = h.decompress(output_path)

        s = Stats('./files/'+sys.argv[file]+'.txt', output_path)
        s.calculate_percentage()
        
        print('---------------------')
        print()


    











