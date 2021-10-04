
import os

class validate_inputs:

    def __init__(self, user_inputs):
        self.user_inputs = user_inputs

    def validate_paths(self, path):
        if os.path.isdir(path):
            return True
        return False

    def validate_inputs(self):
        #validate first if path exists
        if !self.validate_paths(user_inputs['input_path']):
            return False

        #if output path doesnt exist return False
        if !self.validate_paths(user_inputs['output_path']):
            return False

        return True













if __name__ == "__main__":
    v = validate_inputs(dict())
    print(v.validate_paths('/home/hon'))
