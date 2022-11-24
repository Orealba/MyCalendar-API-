import sqlite3

conn = sqlite3.connect('myCalendar_api.db') 
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS events
          ([id] INTEGER PRIMARY KEY, [title] TEXT, [description] TEXT, [start_date] DATETIME, [end_date] DATETIME  )
          ''')