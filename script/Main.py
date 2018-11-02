import yaml
import Storage
import os

class database():

    def __init__(self,file_path):
        self.file_path = file_path

    def devs(self):
        """
            Devs:
            Displays the list of developers that created the project!
        """
        print("The developer(s) of YamlDB is / are:" + "\n" + "RedstonedLife (github.com/RedstonedLife)")

    def dump(self,data):
        """
            Dump:
            Will dump any data given but remove / delete existing data!
            For safe dump to insert data safely without removing past data use safe_dump(data)
        """
        Storage.yaml_dump(self.file_path,data)
            
            
    def safe_dump(self,data):
        """

            Safe Dump:
            Will dump any data given without removing already written data.
            
        """
        # Initialize Data
        Data = Storage.yaml_loader(self.file_path)
        new_dict = dict(data)
        dest = dict(Data)
        dest.update(new_dict)
        Storage.yaml_dump(self.file_path,dest)
        
    def current_file(self):
        print("\n\nCurrent File: " + os.path.basename(self.file_path)+"\nFile Path: " + str(os.path.abspath(self.file_path) + "\nFile Size (In Bytes): " + str(os.path.getsize(self.file_path)) + " Bytes\n\n"))
        
        
        


database = database("data.yml")
test3 = {"Test3":{"Cash":"100"}}
database.dump(test3)
database.current_file()
print("Worked!")

