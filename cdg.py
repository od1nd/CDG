import argparse

def output(filename: str, word: str) -> None:
    with open(filename, 'a') as file:
        file.write(word + "\n")
    file.close()

def generate(size_list_words: int, list_words: list[str], filename: str) -> None:
    temp_list: list[int] = []

    for index in range(0, size_list_words):
        temp_list.append(0)

    word: str = "".join(word for word in list_words)
    output(filename=filename, word=word)

    index: int = 0
    while index < size_list_words:
        if temp_list[index] < index:
            if index % 2 == 0:
                list_words[0], list_words[index] = list_words[index], list_words[0]
            else:
                list_words[temp_list[index]], list_words[index] = list_words[index], list_words[temp_list[index]]

            word: str = "".join(word for word in list_words)
            output(filename=filename, word=word)

            temp_list[index] += 1
            index = 0
        else:
            temp_list[index] = 0
            index += 1        

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--add", dest="add", action="extend", nargs='+', help="Add words to the dictionary")
    parser.add_argument("-o", "--output", dest="output", help="Output file name")

    args = parser.parse_args()

    if(args.add and args.output):
        generate(size_list_words=len(args.add), list_words=args.add, filename=args.output)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()