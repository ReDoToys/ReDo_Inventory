import os
import shutil

def clear_files():
    # Read the txt file to get the mapping of files to folders
    with open('file_mapping.txt', 'r') as f:
        fullpaths = [line.strip() for line in f.readlines()]

    # Remove .stl, .json, and .png files from the destination folders
    for fullpath in fullpaths:
        destination_folder = os.path.dirname(fullpath)
        # Check if the destination folder exists
        if os.path.exists(destination_folder):
            for file_name in os.listdir(destination_folder):
                if file_name.endswith(('.stl', '.json', '.png')):
                    file_path = os.path.join(destination_folder, file_name)
                    try:
                        os.remove(file_path)
                    except FileNotFoundError:
                        pass  # Ignore if the file doesn't exist

def copy_files():
    # Clear existing .stl, .json, and .png files from the destination folders
    clear_files()

    # Read the txt file to get the mapping of files to folders
    with open('file_mapping.txt', 'r') as f:
        fullpaths = [line.strip() for line in f.readlines()]

    # Move files to proper folders
    current_directory = os.path.dirname(os.path.abspath(__file__))
    source_directory = os.path.join(current_directory, 'source')
    for fullpath in fullpaths:
        # Extract the folder name without extension from the destination folder path
        filename = os.path.splitext(os.path.basename(fullpath))[0]
        # Construct the source file paths
        source_files = [os.path.join(source_directory, filename + ext) for ext in ['.stl', '.json', '.png']]
        # Ensure the destination folder exists, create it if necessary
        destination_folder = os.path.dirname(fullpath)  
        folders = destination_folder.split('/')
        # Join the remaining folders starting from the second element
        destination_folder = os.path.join(folders[0], *folders[1:]) # destination_folder = os.path.join(*folders[1:])

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        # Move each source file to the destination folder
        for source_file in source_files:
            if os.path.exists(source_file):
                # Copy the source file to the destination folder
                shutil.copy(source_file, destination_folder)

if __name__ == "__main__":
    copy_files()
