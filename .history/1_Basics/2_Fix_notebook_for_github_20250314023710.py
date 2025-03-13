import nbformat
import os

root_folder = "D:/Python_Project_Youtube"  # Set the correct path

found_files = False  # Track if any .ipynb files are found

for dirpath, dirnames, filenames in os.walk(root_folder):  # Recursively search
    for filename in filenames:
        if filename.endswith('.ipynb'):
            found_files = True
            file_path = os.path.join(dirpath, filename)
            print(f"🔄 Processing: {file_path}")  # Debugging line
            try:
                nb = nbformat.read(file_path, as_version=4)
                nbformat.write(nb, file_path)
                print(f"✅ Fixed: {file_path}")
            except Exception as e:
                print(f"❌ Error fixing {file_path}: {e}")

if not found_files:
    print("⚠️ No .ipynb files found. Check your folder path.")

