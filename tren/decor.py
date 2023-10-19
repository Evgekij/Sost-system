import json


def caller(file_name):
    def arhivar(func):
        data = func()
        with open(file_name, "w") as f:
            json.dump(data, f, indent = 4)
        return func
    return arhivar