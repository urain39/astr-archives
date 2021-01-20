from pathlib import Path
from tools.dictionary import parse_dictionary


def main():
	for i in Path('.').glob('**/*.txt'):
		if i.is_file():
			text = i.read_text()

			unmatched_list, _ = parse_dictionary(text)

			if unmatched_list:
				u = unmatched_list[0]
				raise Exception(f'Unmatched list detected at {str(i)}:{u[0]}')


if __name__ == '__main__':
	main()
