import os, sys

def read_file(filepath):
    f = open(filepath, "r") 
    content = f.read()
    return content

def word_count(text):
    words = text.split(" ")
    return len(words)

def main():
    filename = "data.txt"
    if not os.path.exists(filename):
        print("File not found:", filename)
        sys.exit(1)

    text = read_file(filename)
    print("Word count:", word_count(text))

if __name__ == "__main__":
    main()
