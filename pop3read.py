import poplib
pop3server = 'pop.gmail.com'
username = 'your_email_address'
password = '********'
pop3server = poplib.POP3_SSL(pop3server) # open connection
print (pop3server.getwelcome()) #show welcome message
pop3server.user(username)
pop3server.pass_(password)
pop3info = pop3server.stat() 
mailcount = pop3info[0] 
print("Total no. of Email : " , mailcount)
print ("\n\nStart Reading Messages\n\n")

for i in range(mailcount-1,mailcount,1):
    for message in pop3server.retr(i+1)[1]:
        print (message)
