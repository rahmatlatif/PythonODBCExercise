#!c:\Python27\python.exe

import cgi,cgitb
import MySQLdb

cgitb.enable()

db = MySQLdb.connect("127.0.0.1","rahmatbin","g7#^VaE(","rahmatbin")

formData = cgi.FieldStorage()
student_firstname = formData.getvalue('FirstName')
student_lastname = formData.getvalue('LastName')
residential_address = formData.getvalue('ResidentialAddress')
phoneno = formData.getvalue('PhoneNo')
gender = formData.getvalue('gender')
course_id = formData.getvalue('course_id')

cursor = db.cursor()

cursor.execute("""INSERT INTO studentmaster (student_firstname, student_lastname, residential_address, phoneno, gender, course_id) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')""" .format(student_firstname, student_lastname, residential_address, phoneno, gender, course_id))
db.commit()

print "content-type:text/html\r\n\r\n"
print "<html><head>"
print "<title>Thank you!</title>"
print "</head><body>"
print "<h1>Thank you for registering!</h1>"
print "</body></html>"
