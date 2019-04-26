import urllib.request #automatically performs SSL certificate authentication. I'm pretty sure at least...
import smtplib #library used for sending notification emails from gmail

#Replace with your info. Don't delete the ' ' marks! 
username = 'Chastikey_Username'
lock_id = 'Chastikey_lockid_here'
safe_gmail_address = 'gmail_for_safe_you_created@gmail.com'  
safe_gmail_password = 'password_for_safe_gmail_account'
kh_email = 'kh_email@kholder.com'
lockee_email = 'lockee@lockedup.com'
lockee_name = 'Lockee_name'

def kh_notify(message):
	
	sent_from = safe_gmail_address  
	to = [kh_email]  
	subject = 'Chastikey Safe Status Update'  
	body = message

	email_text = """  
	From: %s  
	To: %s  
	Subject: %s

	%s
	""" % (sent_from, ", ".join(to), subject, body)

	try:  
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(safe_gmail_address, safe_gmail_password)
		server.sendmail(sent_from, to, email_text)
		server.close()

		print('success')
	except:  
		print('Something went wrong')
def lockee_notify(message):
	
	sent_from = safe_gmail_address  
	to = [lockee_email]  
	subject = 'Chastikey Safe Status Update'  
	body = message

	email_text = """  
	From: %s  
	To: %s  
	Subject: %s

	%s
	""" % (sent_from, ", ".join(to), subject, body)

	try:  
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(safe_gmail_address, safe_gmail_password)
		server.sendmail(sent_from, to, email_text)
		server.close()

		print('success')
	except:  
		print('Something went wrong')


#sends lock_id and username to API. Returns API output as string
response = urllib.request.urlopen('https://api.chastikey.com/v0.3/checklock.php?username=' + username + '&lockid=' + lock_id)
bytes_string = response.read()
result = str(bytes_string, 'utf-8')

#Searches result for 'UnlockedReal'. -1 means 'UnlockedReal was not returned and safe stays locked
#If 'UnlockedReal' is found, a number other than -1 will be returned and safe will be unlocked.
if result.find('UnlockedReal') == -1:
	kh_notify('Lock status checked: lock_active. '+lockee_name+' will remain locked a bit longer.')
	lockee_notify("Lock status checked: lock_active. You'll remain locked a bit longer.")
else:
	kh_notify(lockee_name+"'s lock has been completed. Unlocking safe.")
	#call to function to unlock the safe
	



	
