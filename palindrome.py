def palindrome(word):
    aux = word[::-1]
    if aux == word:
        return True
    else:
        return False

def run():
    word = str(input("Digite la palabra: "))
    if palindrome(word) == True:
        print("this word is palindrome")
    else:
        print("This word isn´t palindrome")





if __name__ == '__main__':
    run()