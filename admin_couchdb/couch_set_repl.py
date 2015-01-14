#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  couch_set_repl.py
#  
#  Copyright 2013 Oleh Horbachov <gorbyo@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

"""
The script help you to enable replication between 2 servers

Usage:
python couch_set_repl.py source_url target_url

Example:
python couch_set_repl.py  http://couch-src.example.com:5984/ http://couch-trg.example.com:5984/
"""

import sys
import couchquery
import couchdb


def main(dbsource, dbtarget):
    couchdbserver = couchdb.Server(dbsource)
    dbrep = couchquery.Database(dbsource + '_replicator')

    for id in couchdbserver:
        print id
        if id != '_replicator' and id != '_users':
            dbrep.create({'source': id, 'target': dbtarget + id, 'create_target': True, 'continuous': True})
    return 0

if __name__ == '__main__':
    try:
        dbsource = sys.argv[1]
        dbtarget = sys.argv[2]
        main(dbsource,dbtarget)
    except IndexError:
        print(__doc__)