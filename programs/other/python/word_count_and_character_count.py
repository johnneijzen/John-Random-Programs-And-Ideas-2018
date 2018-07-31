def main():
    userinput = input("Enter a sentence:")
    wordcount = len(userinput.split())
    charactercount = len(userinput)
    charactercountnospacechars = len(userinput.replace(' ', ''))

    print("The total word count is: " + str(wordcount))
    print("The total character count: " + str(charactercount))
    print("The total character count without space : " +
          str(charactercountnospacechars))


main()
