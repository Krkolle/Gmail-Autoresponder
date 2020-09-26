# Gmail-Autoresponder
Python Script to automatically sends a mail to every unread mail in your Gmail Inbox.

Steps to implement Auto Replying in your Gmail Inbox with the help of the Python Script.

1. Install ezgmail module on Python3 - pip install EZGmail
2. Follow the instructions provided at https://developers.google.com/gmail/api/quickstart/python to enable the GMAIL API option for your Google Account and to download the credentials.json file. Copy the credentials.json file to the location where your script is located. 
3. For first time setup, you will need to Allow the permission for accessing your GMAIL Account. For doing this, you will need to follow the below steps.
In the Python Shell, run 'import EZGmail' 
This will launch the default web browser and ask you to login to your Google Account.
After this, you will be asked to allow the app to access the data. Give the required access, and return to Python Shell.
4. Now when you run 'import ezgmail', you will be all set to run the script.
5. To verify the account associated, run the command 'ezgmail.EMAIL_ADDRESS'. The output should be of the same Gmail ID.
6. Run autoresponder.py to reply to all the unread mails. 
7. You can make neccessary changes in the code to reply to unread mails in a specific folder.
