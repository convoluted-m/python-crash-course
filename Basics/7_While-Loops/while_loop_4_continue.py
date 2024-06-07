# use continue to return to the beginning of the loop
prompt = "\nDo you wish to continue? Y/N:"

while True:
    answer = input(prompt)
    if answer == 'N':
        print("Ok bye!")
        break
    else:
        print("Yay!")
        continue