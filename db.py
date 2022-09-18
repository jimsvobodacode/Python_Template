import pyodbc, csv

class db:
    
    def __init__(self):
        self.connstring = "DRIVER={SQL Server};SERVER=192.168.1.122;DATABASE=AdventureWorks2019;UID=bstruebing;PWD=training"

    def Process(self):
        sql = "select top 100 * from person.person"
        conn = pyodbc.connect(self.connstring)
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        mylist = []
        for row in results:
            print(row[6])
            columns = []
            columns.append(row[4])
            columns.append(row[6])
            
            mylist.append(columns)
        
        self.writecsv(mylist)

    def writecsv(self, items):
        with open("output.csv", "w") as file:
            writer = csv.writer(file)
            for item in items:
                writer.writerow(item)