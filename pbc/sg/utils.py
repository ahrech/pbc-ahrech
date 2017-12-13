def find_occurrences(text, search_string):
    # type: (str, str) -> [int]
    result = []
    k = 0
    while k < len(text):
        k = text.find(search_string, k)
        if k == -1:
            break
        else:
            result.append(k)
            k += len(search_string)
    return result
