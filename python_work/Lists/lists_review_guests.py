print("We are happy to announce that we are organizing our Bday party this March!")

# Guest list
guest_list = ['Badger', 'George the Chicken', 'Sneaky Rat', 'Squizel', 'Rob the Robin']

# Send an invite message
invite = f"Dear {guest_list[0]}, we would like to invite you to our Bday party that will be taking place on March the 17th in our Secret Quarter. Please respond to confirm your attendence. Gnocchi & Capo"
print(invite)

# Guest who can't attend
print(guest_list[2])

# Replace guests
print(f"We would like to inform you that regretabbly {guest_list[2]} can't attend our Bday party. He didn't give a reason as to why but we think it's because the parents would be mad if they saw him...")
del guest_list[2]
print(guest_list)
guest_list.insert(4, 'Pidgeon Lady')
print(guest_list)

# Add more quests
print("Hooray! We found a bigger table at the scrapyard. We would love to extend our Bday party invitation to more guests! Please ask around if anyone would like to pop in.")
guest_list.insert(0, 'Rocky the Rabbit')
guest_list.insert(2, 'Lucy the Cow')
guest_list.append('Reggie')
print(guest_list)

# Remove guests
print("We are sorry to inform that apparently the parents threw away our table (probably because it only had three legs - it was a fine table!!! :(. And so now we can only invite two guests. Our sincere aplogies. Gnocchi and Capo")
guest_list.pop()
print("Sorry Reggie, but we can't invite you to the party because there's not enough space... :(")
print(guest_list)

guest_list.pop()
print("Pidgeon Lady, but we can't invite you to the party because there's not enough space... :(")
print(guest_list)

guest_list.pop()
print("Sorry Rob the Robin, but we can't invite you to the party because there's not enough space... :(")
print(guest_list)

guest_list.pop()
print("Sorry Squizel, but we can't invite you to the party because there's not enough space... :(")
print(guest_list)

guest_list.pop()
print("Sorry George the Chicken, but we can't invite you to the party because there's not enough space... :(")
print(guest_list)

guest_list.pop()
print("Sorry Lucy the Cow, but we can't invite you to the party because there's not enough space... :(")
print(guest_list)

print(f"Dear {guest_list[0]}, we are still happy to have you at our Bday party. We hope you can make it. Treats and card games in the program.")
print(f"Dear {guest_list[1]}, we are still happy to have you at our Bday party. We hope you can make it. Treats and card games in the program.")

# Remove all guests
guest_list.remove('Badger')
guest_list.remove('Rocky the Rabbit')
print(guest_list)
print('The party is over so we erased our guest list. We hope next year we will have the whole crew at our Bday party. This time we will not let the parents spoil the fun!')