# нахождение палиндрома в готовом списке
list_words = ['heleh', 'hello', 'itrrti']


def palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return palindrome(string[1:-1])


for words in list_words:
    print(palindrome(words))


# нахождение палиндрома с вводом строк
def is_palindrome(word):
    reversed_list = list(reversed(word))
    palindrome = ""
    for letter in reversed_list:
        palindrome += letter
    if word == palindrome:
        print("This is a palindrome!")
    else:
        print("This is not a palindrome :( ")
    return 0


first_word = input("Please, input the first word: ").lower()
second_word = input("Please, input the second word: ").lower()
third_word = input("Please, input the third word: ").lower()
is_palindrome(first_word)
is_palindrome(second_word)
is_palindrome(third_word)
