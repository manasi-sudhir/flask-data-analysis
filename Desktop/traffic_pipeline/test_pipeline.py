#unit testing 
import unittest
import pandas as pd 
import sqlite3

class TestPipeline(unittest.TestCase):
    def test_timestamp_conversion(self):
        conn=sqlite3.connect('traffic_data.db')
        self.assertIsNotNone(conn)
        conn.close()
    
    def test_table_exist(self):
        conn=sqlite3.connect('traffic_data.db')
        query= "SELECT name FROM sqlite_master WHERE type='table';"
        tables=pd.read_sql(query,conn)\
        
        self.assertIn('Traffic_features',tables['name'].values)
        conn.close()

    def test_data_not_empty(self):
        conn=sqlite3.connect('traffic_data.db')
        df= pd.read_sql("SELECT * FROM Traffic_features",conn)

        self.assertTrue(len(df)>0)
        conn.close()

if __name__=='__main__':
    unittest.main()

