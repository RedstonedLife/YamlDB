import yaml


def yaml_loader(filepath):
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
        return data
    print("Succesfully loaded the data from file!")

def yaml_dump(filepath,data):
    with open(filepath, "w") as file_descriptor:
        yaml.safe_dump(data,file_descriptor)
    print("Succesfully dumped the given data!")

    




