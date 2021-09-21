
import os

class validate_inputs:

    def __init__(self, user_inputs):
        self.user_inputs = user_inputs

    def validate_paths(self, path):
        if os.path.isdir(path):
            return True
        return False

if __name__ == "__main__":
    v = validate_inputs(dict())
    print(v.validate_paths('/home/hon'))
