import sqlite3

class RealtimeDatabase:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        query = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns})'
        self.cursor.execute(query)

    def insert_data(self, table_name, data):
        query = f'INSERT INTO {table_name} VALUES ({data})'
        self.cursor.execute(query)
        self.conn.commit()

    def select_data(self, table_name, columns):
        query = f'SELECT {columns} FROM {table_name}'
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

# Example usage:
db_file = 'ealtime.db'
realtime_db = RealtimeDatabase(db_file)
realtime_db.create_table('sensors', 'temperature REAL, humidity REAL')
data = (25, 60)
realtime_db.insert_data('sensors', data)
results = realtime_db.select_data('sensors', 'temperature, humidity')
print(results)
realtime_db.close()
