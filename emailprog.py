import smtplib,random,sys,pickle
from email.mime.text import MIMEText
def send_mail(to_email,name,phone,address,time,canName,canCapacity,Mode,amount):
    data = pickle.load(open("emailData.pkl","rb"))
    email = data['email']
    passw = data['password']
    #text = '''<h1>Bill</h1><br>Name: %s<br>Phone: %s<br>Address: %s<br>Date: %s<br>Can Name: %s<br>Can capacity: %s<br>Mode: %s<br>Amount: %s'''%(name,phone,address,time,canName,canCapacity,Mode,amount)
    text = '''<h1>Watercan order bill</h1><br>UserName: %s<br>Phone: %s<br>Address: %s<br><br><br>
    
    <table>
    <tr> 
    
    <th>Date</th>
    <th>Can Name</th>
    <th>Can Capacity</th>
    <th>Mode</th>
    <th>Amount</th>
  </tr>
  <tr>

    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
  </tr>
</table>
'''%(name,phone,address,time,canName,canCapacity,Mode,amount)
    email_message = MIMEText(text,_subtype = 'html')
    email_message['subject'] = 'Waterman analysis project'
    email_message['from'] = email
    email_message['to'] = to_email

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email,passw)
    server.sendmail(email,to_email,email_message.as_string())
    server.close()


send_mail(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8],sys.argv[9])
    


    
 
