def reverse_str(input):
    words = input.split()
    reversed_words = [word[::-1] for word in words]
    reversed_str = ' '.join(reversed_words)
    return reversed_str