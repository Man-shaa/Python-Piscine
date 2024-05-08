import sys
from time import sleep
from tqdm import tqdm

def ft_tqdm(lst: range) -> None:
	total = len(lst)
	length = 64
	for i, item in enumerate(lst):
		percent = (i + 1) / total
		progress_bar = int(length * percent)
		bar = '█' * progress_bar + ' ' * \
    (length - progress_bar)
		sys.stdout.write(f'\r{int(percent * 100)}%|{bar}| {i + 1}/{total}')
		sleep(0.005)
	sys.stdout.write('\n')
	return lst

def main():
	for elem in tqdm(range(333)):
		sleep(0.005)
	for elem in ft_tqdm(range(333)):
		sleep(0.005)
	print()

if __name__ == "__main__":
	main()