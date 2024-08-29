import sqlite3 as sq
from app.support import copy_current_link
from app.Browser import open_my_url


def create_db_and_tabl():
    """
    Creates a SQLite database and a table for storing URLs if they do not already exist.

    Returns:
    db -- the database connection object
    cur -- the database cursor object
    """
    db = sq.connect('Hot-Keys.db')
    cur = db.cursor()

    # Create a table for storing URLs with a slot as the primary key
    cur.execute(
        "CREATE TABLE IF NOT EXISTS urls (slot INTEGER PRIMARY KEY, url TEXT)")

    return db, cur


def insert_url(slot):
    """
    Inserts or updates a URL in the database at the specified slot.

    Arguments:
    slot -- the slot number where the URL will be stored
    """
    db, cur = create_db_and_tabl()
    url = copy_current_link()

    # Check if the slot already contains a URL
    if cur.execute(f"SELECT url FROM urls WHERE slot = {slot}").fetchone() is None:
        # Insert the URL into the database
        cur.execute(f"INSERT INTO urls (slot, url) VALUES ({slot}, '{url}')")
    else:
        # Update the existing URL in the database
        cur.execute(f"UPDATE urls SET url = '{url}' WHERE slot = {slot}")

    print(f"Now number {slot} is now the link ---> {url}")

    db.commit()
    db.close()


def select_url(slot):
    """
    Retrieves and opens a URL from the database based on the specified slot.

    Arguments:
    slot -- the slot number of the URL to be retrieved
    """
    db, cur = create_db_and_tabl()

    # Fetch the URL from the database
    if (url := cur.execute(f"SELECT url FROM urls WHERE slot = {slot}").fetchone()) is None:
        print(f"No recorded references numbered - {slot}")
    else:
        try:
            open_my_url(str(url[0]))
        except Exception as ex:
            print(f"Having trouble opening the link under the number - {slot}")

    db.commit()
    db.close()


def show_urls():
    """
    Displays all the URLs stored in the database along with their slot numbers.
    """
    db, cur = create_db_and_tabl()

    result = ''

    # Retrieve and format all URLs from the database
    for i in cur.execute('SELECT * FROM urls').fetchall():
        result += f'{i[0]} ---> {i[1]}\n'

    print(result)

    db.commit()
    db.close()


if __name__ == '__main__':
    # Show all stored URLs when the script is executed directly
    show_urls()
