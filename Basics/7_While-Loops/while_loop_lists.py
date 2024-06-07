# Verify users using lists and a while loop
unconfirmed_users = ['harmony', 'sylvie', 'afra', 'ilana', 'Žemyna', 'ceres', 'dagda', 'enki', 'bryn' ]
confirmed_users = []

# while loop runs as long as the list unconfirmed_users is not empty 2
while unconfirmed_users:
    #  pop() removes unverified users one at a time from the end of unconfirmed_users
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Print confirmed users
print("\nConfirmed the following users:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())