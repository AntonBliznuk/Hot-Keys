import sqlite3 as sq

from app.support import copy_current_link
from app.Browser import open_my_url


def create_db_and_tabl():
    db = sq.connect('Hot-Keys.db')
    cur = db.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS urls (slot INTEGER PRIMARY KEY, url TEXT)")

    return db, cur


def insert_url(slot):
    start = create_db_and_tabl()

    db = start[0]
    cur = start[1]

    url = copy_current_link()

    if cur.execute(f"SELECT url FROM urls WHERE slot = {slot}").fetchone() is None:

        cur.execute(f"INSERT INTO urls (slot, url) VALUES ({slot}, '{url}')")

    else:

        cur.execute(f"UPDATE urls SET url = '{url}' WHERE slot = {slot}")

    print(f"Now number {slot} is now the link ---> {url}")

    db.commit()
    db.close

    return


def select_url(slot):
    start = create_db_and_tabl()

    db = start[0]
    cur = start[1]

    if (url := cur.execute(f"SELECT url FROM urls WHERE slot = {slot}").fetchone()) is None:

        print(f"No recorded references numbered - {slot}")

    else:
        try:
            open_my_url(str(url[0]))

        except Exception as ex:
            print(f"Having trouble opening the link under the number - {slot}")

    db.commit()
    db.close

    return


def show_urls():
    start = create_db_and_tabl()

    db = start[0]
    cur = start[1]

    result = ''

    for i in cur.execute('SELECT * FROM urls').fetchall():
        result += f'{i[0]} ---> {i[1]}\n'

    print(result)

    db.commit()
    db.close

    return


if __name__ == '__main__':
    show_urls()
