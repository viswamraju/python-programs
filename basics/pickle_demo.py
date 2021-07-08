import pickle

name = "viswam"

def pickle_str():
    with open('mypicke', 'wb') as f:
        pickle.dump(name, f)

def unpickle():
    with open('mypicke', 'rb') as f:
        print(pickle.load(f))

# unpickle()

