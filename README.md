# auto-generate-emails-python
This code contains a method which when provided parameters in the way specified can send emails to the quoted emails with the self designed template.

send_email(path_csv,n,path_temp,subject,mail_id,password,smtp_host,p)

path_csv:
the path of the csv file which contains the names, emails and other details 
that needed to be sent in a format such that(the fields should be in the same order).
(name,email,var_1,..var_i)

n:
the number of fields other than name and email must be counted

path_temp:
this is path to the sample template. It should be a text file, where the replacable variables must be specified as 
$NAME for replacing it whith name
$VAR_i for replacing it with respevctive variables mentioned in the csv file
example $VAR_1 or $VAR_5 

*note* The above paths must be given as a string preceded by r to eleminate special characters
       example: r'C:\Users\anjan\OneDrive\mail.csv'

subject:
the subject for the emails is given in the form of a string

mail_id:
the from mail address should be passed in the form of a string

password:
the password should be given in the form a string

smtp_host:
host name of smpt the sender is using should be given in the form of a string
the common servers with there host names and port numbers are given in the site mentioned below
https://www.arclab.com/en/kb/email/list-of-smtp-and-imap-servers-mailserver-list.html

p:
port number should be given here
