import re


def normalize(input_string):
    normalized_string = ' '.join(input_string.strip().lower().split())
    return normalized_string


def no_vowels(input_string):
    no_vowel_string = re.sub('[aeiou]', '', input_string)
    return no_vowel_string
