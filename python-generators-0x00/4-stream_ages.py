from 0-stream_users import stream_users

def stream_user_ages():
    for user in stream_users():
        yield user['age']

def average_age():
    total = 0
    count = 0
    for age in stream_user_ages():
        total += age
        count += 1
    print(f"Average age of users: {total / count}")

if __name__ == "__main__":
    average_age()

