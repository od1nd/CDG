import argparse

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--add", dest="add", action="extend", nargs='+', help="Add words to the dictionary")
    parser.add_argument("-o", "--output", dest="output", help="Output file name")

    args = parser.parse_args()

    if(args.add and args.output):
        print("Words: " + str(args.add))
        print("Output: " + args.output)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()