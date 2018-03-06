from functools import partial

from ocflib.infra import db

get_connection = partial(db.get_connection, user='anonymous', password=None, db='ocfinventory')


def get_devices():
    with get_connection() as c:
        return c.execute('SELECT `hostname`, `vendor`, `type`, `name` FROM `lab_inventory`')


def get_missing_devices():
    with get_connection() as c:
        return c.execute('SELECT `hostname`, `vendor`, `type`, `name` FROM `lab_inventory`'
                         'WHERE TIMESTAMPDIFF(DAY, `last_seen`, NOW()) > 1')
