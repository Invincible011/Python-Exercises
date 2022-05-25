"""
        All about RegEx
        pattern = REgEx metacharacters
        [].^$*+?{}()\|

        [] = Specifies a set of characters you wish to match.
        . = Matches any single character except a newline. {.. - a: No Match, - abh: Match}
        ^ Caret = If a string starts with a certain character. {^abc - abc: No match, - abcnbd: Match}
        $ = If a string ends with a certain character
        * = Matches Zero or more occurrence of the pattern left to it.
        + = Matches One or more occurrence of the pattern left to it.
        ? =  Matches Zero or One occurrence of the pattern left to it.
        {} = Matches at least n, and at most m repetitions of the pattern left to it. (a{2,4}).
        () = Grouping sub patterns - (a|b|c)xz match any string that matches either a or b or c followed by xz
        \ = To escape various characters including all metacharacters.
        | = Alternative (or operator) a|b - a or b in a string character.
        \Athe = Matches if the specified characters (the) are at the start of a string.
        \bthe = Matches if the specified characters are at the beginning or end of a word.
        \Bthe = Matches if the specified characters are not at the beginning or end of a word.
        \d = if matches any decimal digit. Equivalent to [0-9].
        \D = if matches any non-decimal digit. Equivalent to [^0-9].
        \s = matches if contain any Whitespace. Equivalent to [\t\n\r\f\v].
        \S = matches if contain any non-whitespace. Equivalent to [^\t\n\r\f\v].
        \w = matches if contain any alphanumeric character (digigts and alphabets). Equivalent to [a-zA-Z0-9_].
        \W = matches if contain any non-alphanumeric character (digigts and alphabets). Equivalent to [^a-zA-Z0-9_].
        \W = Matches if the specified characters are not at the End of a string.


        ^a...s$ = 5 letter string starting with a and ending with s

        re.match() - Find matches if they occur at the start of the string being searched for,
                    if a string starts with a number instead of an alphabet, the match function return null even
                    if there are alphabets after the number in the string.
        re.search() - It is similar to match(), but search() doesn't restrict us to only finding matches at the beginning of the string but the whole string
                    It will return the first instance where it find the matches.
        re.findall() -

        re.match(pattern, test_string)
        re.search(pattern, test_string)
        re.findall(pattern, test_string)
"""

import re
'''pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)
if result:
    print(result)
    print('Search successful.')
else:
    print(result)
'''

pattern = r'[abc]'
test_string = 'all the Movie are interesting but Terror.'
result = re.findall( pattern, test_string)
if result:
    print(result)
    print('Search successful.')
else:
    print('Search unsuccessful.')

