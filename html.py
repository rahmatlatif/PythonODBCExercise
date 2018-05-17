#!C:\Python27\python.exe

import cgi,cgitb,MySQLdb

def db_dropdown():
    db = MySQLdb.connect(user='rahmatbin', db='rahmatbin', passwd='g7#^VaE(', host='127.0.0.1')
    cursor = db.cursor()

    sql = '''SELECT course_id FROM coursemaster''' 
    cursor.execute(sql)
    list_tested = cursor.fetchall()
    list_tested = [i for sub in list_tested for i in sub]

    return list_tested

def print_dropdown(data):
    print '<div>'
    print '<select name="course_id">'
    for i in data:
        print '<option value="%s"selected>%s</option>' % (i, i)
    print '</select>'
    print '</div>'

cgitb.enable()

print "content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<link rel="stylesheet" href="style.css">'
print '<title> Student Registration Form </title>'
print "</head>"

print "<body>"
print '<div class="main">'
print "<h1>Student Registration Form</h1>"
print '<form action="FormProcess.py" method="POST">'
print '<p>First Name:</p> <input type="text" name="FirstName" required/>'
print "<br>"
print '<p>Last Name:</p> <input type="text" name="LastName" required/>'
print "<br>"
print '<p>Residential Address:</p> <input type="text" name="ResidentialAddress"/>'
print "<br>"
print '<p>Phone No:</p> <div class="number"><input type="number" pattern="^[0-9]" min="0" max="100000000000" title="Only numerical value of length not more than 11" /></div>'
print "<br>"
print "<p>Gender:</p>"
print '<input type="radio" name="gender" value="male"> <p>Male</p>'
print '<input type="radio" name="gender" value="female"> <p>Female</p>'
print "<br>"
print "<p>Course:</p>"
print_dropdown(db_dropdown())
print "<br>"
print '<div class="buttons">'
print '<button type="submit" value="Submit">Save</button>'
print '<button type="reset" value="Reset">Clear</button>'
print "</div>"
print "</form>"
print "</div>"

print "</body>"
print "</html>"

