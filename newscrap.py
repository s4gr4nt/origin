import json  # You can use other serialization formats like pickle, XML, etc.

class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_data(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file)

    def read_data(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON in file '{self.file_path}'.")
            return None

# Example usage:
file_manager = FileManager("data.json")

# Writing data to the file
data_to_write = {"name": "John", "age": 30, "city": "Example City"}
file_manager.write_data(data_to_write)

# Reading data from the file
read_data = file_manager.read_data()

if read_data is not None:
    print("Read data:", read_data)


