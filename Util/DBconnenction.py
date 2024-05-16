import pyodbc
server_name = "ABISHEK\\SQLEXPRESS"
database_name = "TicketBookingSystem"
 
 
conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)

print(conn_str)
conn = pyodbc.connect(conn_str)


class DBConnection:
    def __init__(self) -> None:
        self.conn=pyodbc.connect(conn_str)
        self.cursor=self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()