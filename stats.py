
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


def word_occurrence(book):
  book_ascii = filter_text(book)
  words = book_ascii.split()
  results = {}
  for word in words:
    if word not in results:
      results[word] = 0
    results[word] += 1

  return results


# Control codes, hyphens, and lower-case letters ONLY
def filter_text(text):
  text_no_emdashes = text.lower().replace("—"," ")
  return ''.join(i for i in text_no_emdashes if ord(i) < 33 or ord(i) == 45 or 96 < ord(i) < 123)


# Intended for use as the key function used in sort()
def sort_on(items):
  return items["num"]


# Second argument takes the name of the first key
def sort_counts(counts, key):
  ct_list = []
  for ct in counts:
    pretty_ct = {}
    pretty_ct[key] = ct
    pretty_ct["num"]  = counts[ct]

    if isinstance(ct, str):
      if len(ct) == 1 and not ct.isalpha():
        continue
      ct_list.append(pretty_ct)

  ct_list.sort(reverse=True, key=sort_on)

  return ct_list

