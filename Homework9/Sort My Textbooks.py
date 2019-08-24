def sorter(textbooks):
    textbooks.sort(key=lambda val: val.lower())
    return textbooks