# pyperclip will allow us to automatically copy the formatted text in clipboard
from pyperclip import copy

while True:
    # Must be inside the loop because of the re-initialization
    copyable_text = ""

    text = str(input('Please input text you wish to be embaded in spoiler tags:\n--> '))

    # Close the console if the client's input is either 'close' or 'exit'
    if text == "close" or text == 'exit':
        exit()
    # If the input text is empty, do not format the string, but repeat the loop
    elif not text:
        print('Acting smart, huh?? Try again.')
        continue
    
    # Loop through the given text, and embade it in spoilers
    for index in range(0, len(text)):
        copyable_text += "||" + text[index] + "||"
    
    print(f'{text} was successfully copied to the clipboard (embaded in spoiler tags).')

    # Copy the embaded string to clipboard
    copy(copyable_text)
