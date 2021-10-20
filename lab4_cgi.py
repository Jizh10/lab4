#!/usr/bin/python37all
import cgi
import json
print("Content-type: text/html\n\n")
data = cgi.FieldStorage()
led = data.getvalue('led')
brightness = data.getvalue('slider')
output = {"led":led, "slider":brightness}

with open('lab4.txt', 'w') as f:
  json.dump(output,f)

print('Content-type: text/html\n\n')
print('<html>')
print(' <head>')
print('   <title>Lab 4 - CGI</title>')
print(' </head>')
print(' <body>')
print('   <div style="width:600px;background:#ADD8E6;border:2px;text-align:center">')
print('   <br>')
print('   <font size="3" color="black" face="helvetica">')
print('   <b>')
print('     <h4>Select an LED to change its brightness</h4>')
print('   </b>')
print('   <form action ="/cgi-bin/lab4_cgi.py" method="POST">')
for i in range(3):
  check = ""
  if i+1 == output['led']:
    check = "checked"
  print('     <input type="radio" name="led" value="1"'+check+'> LED ' + str(i+1) + ' <br>')
print('     <b>')
print('       <h4>Use the slider to adjust the brightness level</h4>')
print('     </b')
print('     <input type="range" name="slider" min="0" max="100" value="'+str(output['slider'])+'"/>')
print('     <br>')
print('     <br>')
print('     <input type="submit" value="Change LED Brightness">')
print('   </form>')
print('   <br>')
print('   Brightness = %s' % output['slider'])
print('   <br>')
print(' </body>')
print('</html>')


  
  






