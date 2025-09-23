def count_words(filename):
    with open(filename, 'r') as f:
        contents = f.read()
    words = contents.split()
    return len(words)
