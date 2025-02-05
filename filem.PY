import os
import shutil

# Define the file types and their corresponding folders
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.pptx', '.xls', '.xlsx'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.m4a'],
    'Video': ['.mp4', '.mkv', '.avi', '.mov'],
    'Archives': ['.zip', '.tar', '.gz', '.rar', '.7z'],
    'Scripts': ['.py', '.js', '.html', '.css'],
    'Others': []  # For any other files that don't fit into the categories
}

def get_category(extension):
    """
    Get the category of a file based on its extension.
    """
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return 'Others'  # If no category matches, classify as 'Others'

def organize_downloads(download_dir):
    # Check if the provided path is a directory
    if not os.path.isdir(download_dir):
        print(f"Error: {download_dir} is not a valid directory.")
        return
    
    # List all files in the Downloads directory
    files = [f for f in os.listdir(download_dir) if os.path.isfile(os.path.join(download_dir, f))]
    
    # Sort files alphabetically
    files.sort()

    # Loop through each file and move it to the appropriate folder
    for file in files:
        file_path = os.path.join(download_dir, file)
        
        # Get the file extension
        _, file_extension = os.path.splitext(file)
        
        # Get the appropriate category (folder) for the file
        category = get_category(file_extension)
        
        # Create a category folder if it doesn't exist
        category_folder = os.path.join(download_dir, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        # Define the destination path
        destination = os.path.join(category_folder, file)
        
        # Move the file to the corresponding category folder
        if file_path != destination:
            shutil.move(file_path, destination)
            print(f"Moved: {file} -> {category}")

# Main execution block
if __name__ == "__main__":  # Ensure this line is indented properly
    download_folder = os.path.expanduser(r'C:\Users\context01\Downloads')  # Updated to fix path
    organize_downloads(download_folder)
