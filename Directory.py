class File:
    def __init__(self, name):
        self.name = name

class Directory:
    def __init__(self, name):
        self.name = name
        self.contents = {}  # Store files and subdirectories

    def add_file(self, file_name):
        if file_name in self.contents:
            raise Exception(f"File '{file_name}' already exists!")
        self.contents[file_name] = File(file_name)

    def add_subdirectory(self, dir_name):
        if dir_name in self.contents:
            raise Exception(f"Directory '{dir_name}' already exists!")
        self.contents[dir_name] = Directory(dir_name)

    def list_contents(self):
        return list(self.contents.keys())

    def search_file(self, file_name):
        result = []
        self._search_recursive(file_name, self, result)
        return result

    def _search_recursive(self, file_name, directory, result, path=""):
        for name, obj in directory.contents.items():
            current_path = f"{path}/{directory.name}".strip("/")
            if isinstance(obj, File) and obj.name == file_name:
                result.append(f"{current_path}/{obj.name}")
            elif isinstance(obj, Directory):
                self._search_recursive(file_name, obj, result, current_path)

# Test Cases
root = Directory("root")
root.add_file("file1.txt")
root.add_file("file2.txt")

subdir1 = Directory("subdir1")
subdir1.add_file("file3.txt")
root.contents["subdir1"] = subdir1

subdir2 = Directory("subdir2")
subdir2.add_file("file4.txt")
subdir1.contents["subdir2"] = subdir2

# Operations
print("Contents of root:", root.list_contents())  # Should list 'file1.txt', 'file2.txt', 'subdir1'
print("Recursive search for 'file3.txt':", root.search_file("file3.txt"))  # Path to 'file3.txt'
print("Recursive search for 'file4.txt':", root.search_file("file4.txt"))  # Path to 'file4.txt'
