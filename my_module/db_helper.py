'''
#python3 MySQLdb
sudo apt-get install python-dev libmysqlclient-dev
sudo apt-get install python3-dev
pip install mysqlclient
'''

DB_TYPE = 'mysql'  # mysql

import MySQLdb
def get_db_conn_mysql():
    # conn = MySQLdb.connect("10.12.192.135", "dlp", "dlp13502965818", "AI", use_unicode=True, charset='utf8')
    conn = MySQLdb.connect('localhost', "root", "Venvar@123", "majorproject", use_unicode=True, charset='utf8')
    return conn




    db.close()
