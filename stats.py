def get_num_words(file_contents):
    count = 0
    words = file_contents.split()
    for word in words:
        count += 1
    return count

def get_num_times_char(string):
    count = 0
    chars = {}
    words = string.split()
    for word in words:
        for char in word.lower():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

def sort_on(sort_list):
    return sort_list["num"]

def get_sorted(chars):
    sort_list = []

    for char in chars:
        sort_list.append({"char": char, "num": chars[char]})

    sort_list.sort(reverse=True, key=sort_on)

    return sort_list
