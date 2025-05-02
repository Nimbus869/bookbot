import sys
from stats import get_num_words
from stats import char_count
from stats import sort_dict_lists

def main():

    if(len(sys.argv) == 2):
        f_path = sys.argv[1]
        text = get_books_text(f_path)
        chars = char_count(text)
        char_list = sort_dict_lists(chars)

        print_block(f_path,text,char_list)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
  


def print_block(f_path,text,char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {f_path}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    for i in char_list:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
    
def get_books_text(filepath):
    with open(filepath) as f:
        return f.read()
    


main()