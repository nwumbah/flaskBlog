@app.route("/savedetails",methods = ["POST","GET"])  
     def saveDetails():  
        msg = "msg"  
        if request.method == "POST":  
            try:  
                name = request.form["name"]  
                email = request.form["email"]  
                address = request.form["address"]  
                with sqlite3.connect("employee.db") as con:  
                    cur = con.cursor()  
                    cur.execute("INSERT into Employees (name, email, address) values (?,?,?)",(name,email,address))  
                    con.commit()  
                    msg = "Employee successfully Added"  
            except:  
                con.rollback()  
                msg = "We can not add the employee to the list"  
            finally:  
                return render_template("success.html",msg = msg)  
                con.close()  
