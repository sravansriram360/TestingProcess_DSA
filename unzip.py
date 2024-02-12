import os
import zipfile
import shutil

def extract_cpp_files(src_folder):
    for root, dirs, files in os.walk(src_folder):
        if '__MACOSX' in dirs:
            macosx_folder = os.path.join(root, '__MACOSX')
            shutil.rmtree(macosx_folder)
            print(f"Deleted: {macosx_folder}")
    for root, dirs, files in os.walk(src_folder):
        for file_name in files:
            if file_name.lower().endswith('.cpp') or file_name.lower().endswith('.h'):
                file_path = os.path.join(root, file_name)
                if file_path != src_folder + '/' + file_name:
                    shutil.copy2(file_path, src_folder)
                
def unzip_all_files(parent_folder, extract_folder):
    for root, dirs, files in os.walk(parent_folder):
        for file_name in files:
            if file_name.lower().endswith('.zip'):
                zip_path = os.path.join(root, file_name)
                unzip_path = os.path.join(extract_folder, os.path.relpath(zip_path, parent_folder).replace('.zip', ''))
                
                # Create the destination folder if it doesn't exist
                os.makedirs(unzip_path, exist_ok=True)

                # Extract the contents of the zip file
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(unzip_path)
    

# Replace 'your_directory_path' with the path to your folder containing zip folders
directory_path = 'submissions_LE1'
dest_path = 'submissions_LE1/extract'
unzip_all_files(directory_path, dest_path)

all_items = os.listdir(dest_path)
top_level_directories = [item for item in all_items if os.path.isdir(os.path.join(dest_path, item))]

top_level_directories.sort()
for topdir in top_level_directories:
    if not topdir == '__MACOSX':
        extract_cpp_files(dest_path + '/' + topdir)
