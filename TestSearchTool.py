import os
from crewai_tools import DirectorySearchTool


class SafeDirectorySearchTool(DirectorySearchTool):

    def add(self, directory, ignore_dirs=None, ignore_files=None):
        ignore_dirs = ignore_dirs if ignore_dirs else [
            '.git', 'target', '.idea', 'META-INF']
        ignore_files = ignore_files if ignore_files else ['.gitignore']

        # Traverse the directory and add files using the safe_load_data function
        for root, dirs, files in os.walk(directory):
            # Remove directories to ignore from the traversal
            dirs[:] = [d for d in dirs if d not in ignore_dirs]

            for file in files:
                if file not in ignore_files:
                    file_path = os.path.join(root, file)
                    data = self.safe_load_data(file_path)
                    if data:
                        self.adapter.add(data)

    def safe_load_data(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                print(f"Archivo leído: {file_path}")
                return f.read()
        except UnicodeDecodeError:
            print(f"Skipping non-UTF-8 file: {file_path}")
            return None
