user_count = 50

def add_user():
    global user_count

    print('number of users is', user_count)
    user_count += 1
    print('number of users is now', user_count)


add_user()
print('number of users is now', user_count)
