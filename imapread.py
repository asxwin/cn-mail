import imaplib
import pprint

imap_host = 'imap.gmail.com'
imap_user = '20z208@psgtech.ac.in'
imap_pass = 'ASHWIN12345'

imap = imaplib.IMAP4_SSL(imap_host)

imap.login(imap_user, imap_pass)

imap.select('Inbox')

tmp, data = imap.search(None, 'SINCE "27-OCT-2022"')
# to get all mails
# status, messages = imap.search(None, "ALL")
# to get mails by subject
# status, messages = imap.search(None, 'SUBJECT "Thanks for Subscribing to our Newsletter !"')
# to get mails after a specific date
# status, messages = imap.search(None, 'SINCE "01-JAN-2020"')
# to get mails before a specific date
# status, messages = imap.search(None, 'BEFORE "01-JAN-2020"')

print(data[0])
for num in data[0].split():
	tmp, data = imap.fetch(num, '(RFC822)')
	print('Message: {0}\n'.format(num))
	pprint.pprint(data[0][1].decode('utf-8'))
imap.close()