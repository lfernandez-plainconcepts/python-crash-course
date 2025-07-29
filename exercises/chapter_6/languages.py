language_favs = {
    'alice': 'c#',
    'bob': 'python',
    'carmen': 'typescript',
    'dave': 'java',
    'eve': 'javascript',
    'frank': 'go',
    'grace': 'python',
    'heidi': 'java',
    'ivan': 'kotlin',
}

print("List of favorite languages:")
for language in language_favs.values():
    print(f"- {language}")

print("\nList of favorite languages (remove duplicates):")
for language in set(language_favs.values()):
    print(f"- {language}")
