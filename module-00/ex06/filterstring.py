import sys

def parse_arg(args):
	if (len(args) != 3):
		return (print("tuto : \"python filterstring [string] [number]\""), 1)
	if (not args[1].replace(' ', '').isalpha()):
		return (print("first argument must be a string"), 1)
	if (not args[2].isdigit()):
		return (print("second argument must be a number"), 1)
	return (0)

def filter_string(string, n):
	get_len = lambda str : len(str) < n
	return [word for word in string.split() if get_len(word)]

def main():
	if (parse_arg(sys.argv) == 1):
		return (1)
	print(filter_string(str(sys.argv[1]), int(sys.argv[2])))
	return (0)


if __name__ == "__main__":
    main()