import argparse

def generate(size_list_words: int, list_words: list[str]) -> None:
    temp_list: list[int] = []

    for index in range(0, size_list_words):
        temp_list.append(0)

    print("".join(word for word in list_words))

    index: int = 0
    while index < size_list_words:
        if temp_list[index] < index:
            if index % 2 == 0:
                list_words[0], list_words[index] = list_words[index], list_words[0]
            else:
                list_words[temp_list[index]], list_words[index] = list_words[index], list_words[temp_list[index]]

            print("".join(word for word in list_words))
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
        generate(len(args.add), args.add)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()