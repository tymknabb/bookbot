#!/usr/bin/env python3

import sys
from stats import word_count
from stats import char_count
from stats import sorted_char_count


def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()


def main():

	book_path = sys.argv[1]
	book_content = get_book_text(book_path)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")

	word_count_result = word_count(book_content)
	char_count_result = char_count(book_content)

	print("----------- Word Count ----------")
	print(f"Found {word_count_result} total words")

	print("----------- Character Count ----------")
	sorted_char_list = sorted_char_count(char_count_result)
	for char_ct in sorted_char_list:
		print(f"{char_ct["char"]}: {char_ct["num"]}")


if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

main()







