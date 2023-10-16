import json
import os
import ast
PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)
from logic import Person

class PersonController(object):

    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'storage.json')

    def add(self, new_person: Person = Person()) -> str:
        with open(self.file, 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data.append(new_person.__str__())
            f.seek(0)
            json.dump(data, f)
        f.close()
        return new_person

    def show(self):
        # Opening JSON file
        with open(self.file, 'r') as openfile:
            # Reading from json file
            data = json.load(openfile)
            # Convert the dictionary to a string
            data_str = json.dumps(data)
            # Print the string
            print(ast.literal_eval(data_str))
        return data_str