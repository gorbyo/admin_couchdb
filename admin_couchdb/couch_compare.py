#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  couch_migrate.py
#  
#  Copyright 2017 Oleh Horbachov <gorbyo@gmail.com>
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
The script help you to enable pull replication between 2 servers

Usage:
python couch_migrate.py --source/-s source_host:port  --target/-t target_host:port

Example:
python couch_migrate.py  -s couch-src.example.com:5984 -t couch-trg.example.com:5984
"""

import json, urllib
import couchdb
import argparse
from argparse import RawTextHelpFormatter


def arguments():
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter,
                                     description="This script create pull replication for all databases")
    parser.add_argument('-t', '--target', help='Target COUCHDB Server')
    parser.add_argument('-s', '--source', help='Source COUCHDB Server')

    return parser


def get_db_info(url):
    response = urllib.urlopen(url)
    db_info = json.loads(response.read())
    return db_info



def main(dbsource, dbtarget):
    couchdbserver = couchdb.Server('http://'+dbsource+'/')

    for id in couchdbserver:
        if id != '_replicator' and id != '_users':
            source = get_db_info("http://" + dbsource + "/" + id)
            target = get_db_info("http://" + dbtarget + "/" + id)
            if source['doc_count'] !=  target['doc_count']:
                print source['db_name'] + "::","\t", source['doc_count'] - target['doc_count']



    return 0


if __name__ == '__main__':
    try:
        dbsource = arguments().parse_args().source
        dbtarget = arguments().parse_args().target
        main(dbsource, dbtarget, )
    except:
        arguments().print_help()
