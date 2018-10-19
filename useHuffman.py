from huffman import HuffmanCoding
import sys
import os

if len(sys.argv) == 1:

    path = "sample.txt"

else:
    path = sys.argv[1]

h = HuffmanCoding(path)

output_path = h.compress()
print("Compressed file path: " + output_path)

decom_path = h.decompress(output_path)
print("Decompressed file path: " + decom_path)

percent_reduce = os.path.getsize(output_path) * 100 / os.path.getsize(path)
print('Original file -> ' + str(os.path.getsize(path)))
print('Compressed file -> ' + str(os.path.getsize(output_path)))
print(percent_reduce)

