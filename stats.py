
def word_count(book):
  words = book.split()
  word_ct = len(words)

  return word_ct


def char_count(book):
  words = book.lower()
  results = {}
  for char in words:
    if char not in results:
      if not char.isascii():
        continue
      results[char] = 0
    results[char] += 1

  return results


def sort_on(items):
  return items["num"]


def sorted_char_count(char_cts):
  char_ct_list = []
  for char_ct in char_cts:
    pretty_char_ct = {}
    pretty_char_ct["char"] = char_ct
    pretty_char_ct["num"]  = char_cts[char_ct]

    if char_ct.isalpha():
      char_ct_list.append(pretty_char_ct)

  char_ct_list.sort(reverse=True, key=sort_on)

  return char_ct_list

