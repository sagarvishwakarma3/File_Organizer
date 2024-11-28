import os

def organize_files(directory):

    os.chdir(directory)
    files = os.listdir()
    
    for file in files:
        if os.path.isdir(file):
            continue
        
        _, extension = os.path.splitext(file)
        extension = extension[1:]
        
        if extension:
            if not os.path.exists(extension):
                os.makedirs(extension)
            os.rename(file, os.path.join(extension, file))
            print(f'Moved: {file} -> {extension}/{file}')

if __name__ == "__main__":
    
    directory_to_organize = input("Enter the directory : ")
    organize_files(directory_to_organize)