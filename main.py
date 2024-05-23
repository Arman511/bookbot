def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters = {alphabet[i]: 0 for i in range(len(alphabet))}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words_list = file_contents.split()
    for word in words_list:
        for letter in word.lower():
            if letter.lower().isalpha():
                letters[letter] += 1
    sorted_letters = sorted(letters.items(), key=lambda x: x[1], reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words_list)} words found in the document\n")

    for letter, count in sorted_letters:
        print(f"The '{letter}' character was found {count} times")
    
    print("--- End report ---")

main()