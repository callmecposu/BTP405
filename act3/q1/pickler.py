# this program pickles the python objects

# change the 'obj' in the source code to pickle various data

# also specify the correct file name for the output

import pickle

# change this to store different data
obj = {
    "name": "Bob",
    "age": 20,
    "social_credit": -20.87
}

# change this to a respective filename
out_name = 'bob'

file = open(out_name, 'wb')
pickle.dump(obj, file)
file.close()
