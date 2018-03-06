import sqlite3
import datetime

start_time = datetime.datetime.now()

# console log
def clog(msg):
  error_format = '({}ms from exec): {}'
  current_time = datetime.datetime.now()
  diff = current_time - start_time

  print(error_format.format(diff.microseconds/1000, msg))

def main():
  clog('entered main')
  conn = sqlite3.connect('test.db')
  clog('connected to db')

  c = conn.cursor()
  cmd = """SELECT * FROM users"""
  c.execute(cmd)
  print(c.fetchone())

  clog('saving db changes')
  conn.commit()
  clog('saved db changes')

  clog('closing db')
  conn.close()
  clog('closed db')

if __name__ == '__main__':
  main()