#!/usr/bin/python3
"""
A script that takes in the name of a state as an
argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cu = db.cursor()
    cu.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    print(", ".join([ct[2] for ct in cu.fetchall() if ct[4] == sys.argv[4]]))
