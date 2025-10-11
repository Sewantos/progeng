spaces = lambda s: " " in s
aIsFirst = lambda s: s[0] == 'a'
tooShort = lambda s: len(s) < 5

def filter_strings(filter_them, strings):
    return [s for s in strings if not filter_them(s)]

testStrings = ['hey', 'hey you', 'aloha']

print(filter_strings(spaces, testStrings))
print(filter_strings(aIsFirst, testStrings))
print(filter_strings(tooShort, testStrings))