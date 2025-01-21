class File:
    def __init__(self, name, size, owner, permissions):
        self.name = name
        self.size = size
        self.owner = owner
        self.permissions = permissions  # Example: {'read': True, 'write': True, 'execute': False}

class Directory:
    def __init__(self, name, owner, permissions):
        self.name = name
        self.owner = owner
        self.permissions = permissions
        self.files = {}  # Stores files as name: File
        self.subdirectories = {}  # Stores subdirectories as name: Directory

    def has_permission(self, requester, action):
        if requester == self.owner:
            return True
        return self.permissions.get(action, False)

    def add_file(self, name, size, owner, permissions):
        if name in self.files:
            raise ValueError(f"File '{name}' already exists.")
        self.files[name] = File(name, size, owner, permissions)

    def add_subdirectory(self, name, owner, permissions):
        if name in self.subdirectories:
            raise ValueError(f"Subdirectory '{name}' already exists.")
        self.subdirectories[name] = Directory(name, owner, permissions)

    def delete_file(self, name, requester):
        if not self.has_permission(requester, 'write'):
            raise PermissionError(f"Requester '{requester}' does not have permission to delete files.")
        if name not in self.files:
            raise ValueError(f"File '{name}' does not exist.")
        del self.files[name]

    def delete_subdirectory(self, name, requester):
        if not self.has_permission(requester, 'write'):
            raise PermissionError(f"Requester '{requester}' does not have permission to delete subdirectories.")
        if name not in self.subdirectories:
            raise ValueError(f"Subdirectory '{name}' does not exist.")
        del self.subdirectories[name]

    def display_contents(self, level=0):
        indent = "  " * level
        print(f"{indent}Directory: {self.name}")
        for file_name, file in self.files.items():
            print(f"{indent}  File: {file.name} (Size: {file.size}, Owner: {file.owner})")
        for dir_name, subdir in self.subdirectories.items():
            subdir.display_contents(level + 1)
if __name__ == "__main__":
    # Create a root directory
    root = Directory("root", "admin", {"read": True, "write": True, "execute": True})

    # Add files and subdirectories
    root.add_file("file1.txt", 100, "user1", {"read": True, "write": False, "execute": False})
    root.add_subdirectory("subdir1", "user2", {"read": True, "write": True, "execute": False})

    # Add file to subdirectory
    subdir1 = root.subdirectories["subdir1"]
    subdir1.add_file("file2.txt", 200, "user3", {"read": True, "write": True, "execute": False})

    # Display contents
    print("Contents before deletion:")
    root.display_contents()

    # Try deleting a file with insufficient permissions
    try:
        root.delete_file("file1.txt", "user2")  # Should raise PermissionError
    except PermissionError as e:
        print(e)

    # Delete file with sufficient permissions
    root.delete_file("file1.txt", "admin")

    # Display contents after deletion
    print("\nContents after file deletion:")
    root.display_contents()

    # Delete subdirectory
    root.delete_subdirectory("subdir1", "admin")

    # Display contents after subdirectory deletion
    print("\nContents after subdirectory deletion:")
    root.display_contents()
