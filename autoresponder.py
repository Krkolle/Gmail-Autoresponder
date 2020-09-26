#Author : Karthik Kolle
import ezgmail
unreadThreads = ezgmail.unread()
a = len(unreadThreads)
for i in range(0,a-1):
    msg = unreadThreads[i].messages[i]    
    ezgmail.send(msg.sender, 'Enter the Subject here', 'Enter the email Body here', ['attachment1.jpg', 'attachment2.mp3'])
