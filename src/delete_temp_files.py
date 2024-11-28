import os

# Function to delete all files in the specified directory
def delete_all_temp_files():
    directories = [
        r"src\video", 
        r"src\video_output", 
        r"src\image"
    ]

    for directory in directories:
        if os.path.exists(directory):
            # Loop through all the files in the directory
            for filename in os.listdir(directory):
                file_path = os.path.join(directory, filename)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)  # Delete the file
                        print(f"Deleted file: {file_path}")
                    elif os.path.isdir(file_path):
                        # If it's a directory, remove it and its contents
                        os.rmdir(file_path)  # This removes empty directories only
                        print(f"Deleted directory: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
        else:
            print(f"Directory {directory} does not exist")