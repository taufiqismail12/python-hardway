formaatter = "{} {} {} {}"

print(formaatter.format(1, 2, 3, 4))
print(formaatter.format("one", "two", "three", "four"))
print(formaatter.format(True, False, False, True))
print(formaatter.format(formaatter, formaatter, formaatter, formaatter))
print(formaatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
