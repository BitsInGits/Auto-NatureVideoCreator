import os
import psutil
import ctypes
import time
# Function to delete all files in the specified directory

print("delete process")
time.sleep(5)

def find_and_kill_process(file_path):
    """Find and terminate the process locking the file."""
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            for item in proc.open_files():
                if file_path == item.path:
                    print(f"Found process '{proc.info['name']}' (PID: {proc.info['pid']}) locking the file.")
                    proc.terminate()  # Terminate the process
                    proc.wait()  # Wait for process to terminate
                    print(f"Terminated process {proc.info['name']} (PID: {proc.info['pid']}).")
                    return True
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue
    print("No process found locking the file.")
    return False

def force_delete_file(file_path):
    """Force delete the file."""
    try:
        os.remove(file_path)
        print(f"Deleted file: {file_path}")
    except PermissionError:
        print(f"Failed to delete {file_path}. Attempting to adjust permissions.")
        # Change file permissions to allow deletion
        ctypes.windll.kernel32.SetFileAttributesW(file_path, 0o200)  # Normal attribute
        os.remove(file_path)
        print(f"Force-deleted file: {file_path}")
    except Exception as e:
        print(f"Error deleting file {file_path}: {e}")

def delete_all_temp_files():
    directories = [
        r"src\video", 
        r"src\video_output", 
        r"src\image"
    ]

    ###########
    folder_path = 'src/video'

    # Get the first file in the folder
    files = os.listdir('src/video')
    if not files:
        print(f"No files found in folder '{folder_path}'.")
    else:
        first_file = files[0]
        file_to_delete = os.path.join(folder_path, first_file)
    ###########

    # Step 1: Attempt to kill the process locking the file
    if find_and_kill_process(file_to_delete):
        print("Process terminated. Proceeding to delete the file.")

        # Step 2: Attempt to delete the file
        force_delete_file(file_to_delete)

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
                        os.rmdir(file_path)  # This removes empty directories only
                        print(f"Deleted directory: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
        else:
            print(f"Directory {directory} does not exist")