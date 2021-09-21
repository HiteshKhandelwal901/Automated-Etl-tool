
import pickle

class write_to_file:

    def __init__(self, user_inputs):
        self.user_inputs = user_inputs

    def dump(self):
        with open('user_inputs.pickle', 'wb') as f:
            pickle.dump(self.user_inputs, f)


    def load(self, pickle_file):
        with open(pickle_file, 'rb') as f:
            loaded_obj = pickle.load(f)
        return loaded_obj

    def write_pickle_file(self):
        self.dump(user_inputs)


if __name__ == "__main__":
    d = dict()
    d['x'] = 20
    d['y'] = 30
    d['z'] = 40
    wr = write_to_file(d)
    wr.dump()
    dic = wr.load('user_inputs.pickle')
    print("dic = ", dic)
