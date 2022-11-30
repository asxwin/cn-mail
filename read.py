import imaplib
import email
from email.header import decode_header

username = "20z208@psgtech.ac.in"
password = "ASHWIN12345"

imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(username, password)
imap.select("INBOX")
status, messages = imap.search(None, 'SINCE "27-OCT-2022"')

messages = messages[0].split(b' ')
for mail in messages:
    _, msg = imap.fetch(mail, "(RFC822)")
    imap.store(mail, "+FLAGS", "\\Deleted")
# \Seen
# \Answered
# \Flagged
# \Deleted
# \Draft

imap.expunge()
imap.close()
imap.logout()