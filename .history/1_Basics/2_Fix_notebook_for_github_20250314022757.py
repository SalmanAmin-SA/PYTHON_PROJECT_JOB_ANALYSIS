import nbformat
import os

# Change this to your project’s root folder (use '.' if you run from the project directory)
root_folder = 'PYTHON_PROJECT_YOUTUBE'

# Walk through all folders and files
for dirpath, dirnames, filenames in os.walk(root_folder):
    for filename in filenames:
        if filename.endswith('.ipynb'):
            file_path = os.path.join(dirpath, filename)
            try:
                # Read the notebook using nbformat (this loads it as nbformat version 4)
                nb = nbformat.read(file_path, as_version=4)
                # Write it back to the same file, ensuring proper JSON formatting
                nbformat.write(nb, file_path)
                print(f"Fixed: {file_path}")
            except Exception as e:
                print(f"Error fixing {file_path}: {e}")
