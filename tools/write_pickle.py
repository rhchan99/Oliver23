import pickle
import sys

# Read the string from command line arguments
full_file_path = sys.argv[1]
string_to_write = sys.argv[2]

# Specify the path and filename for the pickle file
pickle_file = full_file_path

# Write the string into the pickle file
with open(pickle_file, 'wb') as file:
    pickle.dump(string_to_write, file)
