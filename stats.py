import os
class Stats:

    def __init__(self, path, out_path):
        self.path = path
        self.out_path = out_path
        


    def calculate_size(self):
        return float(os.path.getsize(self.out_path) * 100 / os.path.getsize(self.path))
        

    def calculate_percentage(self):
        print('Original file size: ' + str(os.path.getsize(self.path)) +' kB')
        print('Compressed file size: ' + str(os.path.getsize(self.out_path))+' kB')
        print('Compressed total:', end=' ')
        print(round(self.calculate_size()), end='% \n')
        
        
    def clean_screen(self, lines):
        count = 0
        while count < lines:
            print()
            count = count + 1



    

