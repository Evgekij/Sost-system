import json
from functools import wraps

def caller(file_name):
    def arhivar(func):
        @wraps(func)
        def dopf():
            data = func()
            with open(file_name, "w") as f:
                json.dump(data, f, indent = 4)
            return data
        
        return dopf
    
    return arhivar