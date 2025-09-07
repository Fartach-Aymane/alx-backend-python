#!/usr/bin/python3
import seed

def stream_users_in_batches(batch_size):
    """
    Generator to fetch users from database in batches.
    Yields one batch at a time.
    """
    offset = 0
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    
    while True:
        cursor.execute(f"SELECT * FROM user_data LIMIT {batch_size} OFFSET {offset}")
        rows = cursor.fetchall()
        if not rows:
            break
        yield rows
        offset += batch_size
    
    connection.close()


def batch_processing(batch_size):
    """
    Process each batch and print users older than 25.
    Uses the generator from stream_users_in_batches.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)
