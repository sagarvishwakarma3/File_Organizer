# File_Organizer

## **Overview**
This script is a **File Organizer** written in Python. It organizes files within a given directory by grouping them into folders based on their file extensions. This is particularly useful for decluttering directories and making file management easier.

---

## **Features**
1. **Dynamic Organization**:
   - Automatically creates subdirectories for each file type (based on extensions).
   - Moves files into their respective subdirectories.

2. **Handles All File Types**:
   - Organizes files regardless of extension.
   - Ignores directories within the target folder.

3. **Non-Destructive**:
   - Only files are moved; existing directory structures are untouched.
   - Creates new folders only when necessary.

4. **Cross-Platform**:
   - Works seamlessly on Windows, macOS, and Linux using Python's `os` module.

---

## **How It Works**

### **1. Directory Input**
- The script prompts the user to input the path of the directory they want to organize.

### **2. File Processing**
- Lists all items in the directory.
- Identifies files by checking their extensions using the `os.path.splitext()` function.
- Skips directories and files without extensions.

### **3. Folder Creation**
- Creates a subdirectory named after each file extension (e.g., `txt`, `jpg`) if it doesn’t already exist.

### **4. File Movement**
- Moves each file to its corresponding extension-based subdirectory using `os.rename()`.

---

## **Prerequisites**

- **Python Version**: Requires Python 3.6 or higher.
- Ensure the script has appropriate permissions to read, write, and modify the specified directory.

---

## **How to Run**

1. **Save the Script**:
   Save the script as `file_organizer.py` or any name of your choice.

2. **Run the Script**:
   Open a terminal or command prompt and execute:
   ```bash
   python file_organizer.py
   ```

3. **Input the Directory**:
   - Enter the absolute or relative path of the directory you want to organize.
   - Example:
     ```
     Enter the directory: /path/to/your/directory
     ```

4. **View the Results**:
   - Files in the specified directory will be moved to subfolders named after their file extensions.
   - Example structure:
     ```
     /path/to/your/directory/
     ├── txt/
     │   ├── notes.txt
     │   ├── report.txt
     ├── jpg/
     │   ├── photo.jpg
     ├── py/
     │   ├── script.py
     └── (other folders for different extensions)
     ```

---

## **Code Explanation**

### **1. Import Modules**
- **`os`**: Used to navigate the file system, create directories, and move files.

### **2. Define `organize_files` Function**
- Accepts the path of the directory to organize.
- Loops through all items in the directory:
  - Checks if the item is a file (skips directories).
  - Extracts the file extension.
  - Creates a subfolder for the extension if it doesn’t exist.
  - Moves the file to the corresponding subfolder.

### **3. Main Block**
- Prompts the user for the directory to organize.
- Calls the `organize_files()` function with the provided directory path.

---

## **Code**
```python
import os

def organize_files(directory):
    os.chdir(directory)  # Change to the target directory
    files = os.listdir()  # List all files and folders in the directory
    
    for file in files:
        if os.path.isdir(file):  # Skip directories
            continue
        
        _, extension = os.path.splitext(file)  # Extract the file extension
        extension = extension[1:]  # Remove the leading dot (e.g., .txt -> txt)
        
        if extension:  # If the file has an extension
            if not os.path.exists(extension):  # Check if a folder exists for the extension
                os.makedirs(extension)  # Create a folder for the extension
            os.rename(file, os.path.join(extension, file))  # Move the file
            print(f'Moved: {file} -> {extension}/{file}')  # Log the action

if __name__ == "__main__":
    # Prompt the user for the directory to organize
    directory_to_organize = input("Enter the directory: ")
    organize_files(directory_to_organize)
```

---

## **Example**
Suppose you have a directory with the following files:
```
/example_directory/
├── notes.txt
├── photo.jpg
├── script.py
├── report.docx
```

After running the script:
```
/example_directory/
├── txt/
│   ├── notes.txt
├── jpg/
│   ├── photo.jpg
├── py/
│   ├── script.py
├── docx/
│   ├── report.docx
```

---

## **Benefits**
- Simplifies file management by categorizing files.
- Saves time, especially when dealing with large and unorganized directories.
- Works across various file types and directory structures.

---

## **Limitations**
- Doesn’t handle deeply nested directory structures (only organizes files in the specified directory).
- Files without extensions remain in the root directory.

---

## **Future Enhancements**
1. Add support for nested directory organization.
2. Allow custom folder names for specific extensions.
3. Provide an option to undo changes.

---

## **Conclusion**
This script offers a simple and efficient way to organize files in a directory. It is a great tool for maintaining a clean and well-organized workspace.
