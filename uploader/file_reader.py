"""Read Files."""

import os


class FileReader:
    """
    class for reading files from a directory and its subdirectories.
    
    Attributes:
        root_dir (str): The root directory to search for files.
    """

    def __init__(self, root_dir):
        """
        Initializes FileReader with the given root directory.
        
        Args:
            root_dir (str): The root directory to search for files.
        """
        self.root_dir = root_dir

    def get_files(self):
        """
        Retrieves all files from the directory and its subdirectories.
        
        Returns:
            list: A list of file paths.
        """
        files = []
        for subdir, _, file_list in os.walk(self.root_dir):
            for file_name in file_list:
                files.append(os.path.join(subdir, file_name))
        return files