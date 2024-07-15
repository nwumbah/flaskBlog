from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)


@app.route('/')
def admin():
    return render_template( 'index.html')


#add programing

@app.route('/enternew')
def new_student():
   return render_template('student.html')


@app.route('/addrec', methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['addr']
         city = request.form['city']
         pin = request.form['pin']
         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO Student (nm, addr, city, pin) VALUES (?, ?, ?, ?)", (nm, addr, city, pin) )
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html", msg = msg)
         con.close()



@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from Student")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run('0.0.0.0', debug = True)
