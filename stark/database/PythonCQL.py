# -*- coding: utf-8 -*-
from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy
from random import randint
import uuid
from pandas import DataFrame






class CassandraDB():
    class DEFINE(object):
        DatabaseName = 'iot2'
        KeyspaceName = 'cassandra_io_t'
        HostIP       = '127.0.0.1'
        Port         = 9042

    def clear_dict(self):
        d = {'IoT Cihaz 1': {
            'example_id': [],
            'name': [],
            'voltaj': [],
            'akim': [],
            'aktif': [],
            'reaktif': [],
            'faz_acisi': [],
            'sicaklik': [],
            'sinyal': [],
        },

            'IoT Cihaz 2': {
                'example_id': [],
                'name': [],
                'voltaj': [],
                'akim': [],
                'aktif': [],
                'reaktif': [],
                'faz_acisi': [],
                'sicaklik': [],
                'sinyal': [],
            },

            'IoT Cihaz 3': {
                'example_id': [],
                'name': [],
                'voltaj': [],
                'akim': [],
                'aktif': [],
                'reaktif': [],
                'faz_acisi': [],
                'sicaklik': [],
                'sinyal': [],
            },

            'IoT Cihaz 4': {
                'example_id': [],
                'name': [],
                'voltaj': [],
                'akim': [],
                'aktif': [],
                'reaktif': [],
                'faz_acisi': [],
                'sicaklik': [],
                'sinyal': [],
            },

            'IoT Cihaz 5': {
                'example_id': [],
                'name': [],
                'voltaj': [],
                'akim': [],
                'aktif': [],
                'reaktif': [],
                'faz_acisi': [],
                'sicaklik': [],
                'sinyal': [],
            },

            'IoT Cihaz 6': {
                'example_id': [],
                'name': [],
                'voltaj': [],
                'akim': [],
                'aktif': [],
                'reaktif': [],
                'faz_acisi': [],
                'sicaklik': [],
                'sinyal': [],
            },

        }


    def connect(self):
        try:
            self.cluster = Cluster(['%s'% CassandraDB.DEFINE.HostIP], port=CassandraDB.DEFINE.Port)
            self.session = self.cluster.connect()
            self.session.execute('USE %s' % CassandraDB.DEFINE.DatabaseName)
            print "Database bağlantısı kuruldu!"
        except:
            print "Bağlantı başarısız!"

    def select(self):
        rows = self.session.execute('SELECT * FROM %s'% CassandraDB.DEFINE.KeyspaceName)
        d = {'IoT Cihaz 1': {
            'example_id': [],
            'name': [],
            'voltaj': [],
            'akim': [],
            'aktif': [],
            'reaktif': [],
            'faz_acisi': [],
            'sicaklik': [],
            'sinyal': [],
        },

            'IoT Cihaz 2': {
                'example_id': [],
                'name': [],
                'voltaj': [],
                'akim': [],
                'aktif': [],
                'reaktif': [],
                'faz_acisi': [],
                'sicaklik': [],
                'sinyal': [],
            },

            'IoT Cihaz 3': {
                'example_id': [],
                'name': [],
                'voltaj': [],
                'akim': [],
                'aktif': [],
                'reaktif': [],
                'faz_acisi': [],
                'sicaklik': [],
                'sinyal': [],
            },

            'IoT Cihaz 4': {
                'example_id': [],
                'name': [],
                'voltaj': [],
                'akim': [],
                'aktif': [],
                'reaktif': [],
                'faz_acisi': [],
                'sicaklik': [],
                'sinyal': [],
            },

            'IoT Cihaz 5': {
                'example_id': [],
                'name': [],
                'voltaj': [],
                'akim': [],
                'aktif': [],
                'reaktif': [],
                'faz_acisi': [],
                'sicaklik': [],
                'sinyal': [],
            },

            'IoT Cihaz 6': {
                'example_id': [],
                'name': [],
                'voltaj': [],
                'akim': [],
                'aktif': [],
                'reaktif': [],
                'faz_acisi': [],
                'sicaklik': [],
                'sinyal': [],
            },

        }

        df = DataFrame(rows.current_rows )
        df.columns = rows.column_names
        for i in df.columns:
            d['IoT Cihaz 1']['%s'%i].append(df.loc[df['name'].isin(['IoT Cihaz 1'])]['%s'%i])


        return d







    def insert(self):
        self.session.execute(
            """
            INSERT INTO cassandra_io_t (example_id,name, voltaj,akim,aktif,reaktif,faz_acisi,sicaklik,sinyal)
            VALUES (  %s, %s, %s,%s, %s, %s,%s,%s,%s)
            """,
            (
            uuid.uuid1(),
             'IoT Cihaz 6',
             randint(215,225),
             randint(5,20),
             randint(1000,4000),
             randint(0,900),
             randint(70,135),
             randint(30,65),
             'Yuksek' )
        )


