class FileProcessor:
    def __init__(self,filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename,'r') as file:
            return file.read()

    def write_file(self,outputfile,content):
        with open(outputfile,'w') as file:
            file.write(content)

def main():
    processor = FileProcessor(r'C:\Users\Lenovo\Desktop\AI_Data_engineer\ai-data-engineer-journey\week_01\input.txt')
    data = processor.read_file()
    print('File Content:')
    print(data)

    processor.write_file(r'C:\Users\Lenovo\Desktop\AI_Data_engineer\ai-data-engineer-journey\week_01\output.txt',data.upper())

if __name__ == '__main__':
    main()
