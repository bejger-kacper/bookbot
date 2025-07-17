from stats import get_num_words
from stats import get_num_times_char
from stats import get_sorted
import sys

def get_book_text(url):
    with open(url) as f:
        file_contents = f.read()
    return file_contents

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_contents = get_book_text(sys.argv[1])
    chars = get_num_times_char(file_contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(file_contents)} total words")
    print("--------- Character Count -------")
    
    new_list = get_sorted(chars)
    for i in range(0, len(new_list)):
        if new_list[i]["char"].isalpha():
            print(f"{new_list[i]["char"]}: {new_list[i]["num"]}")
    
    print("============= END ===============")

main()
