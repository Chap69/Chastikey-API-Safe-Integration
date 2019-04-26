import urllib.request
#The above library automatically performs SSL certificate authentication. I'm pretty sure at least...

username = 'type_your_username_here'
lock_id = 'type_your_lock_id_here'

#sends lock_id and username to API. Returns API output as string
response = urllib.request.urlopen('https://api.chastikey.com/v0.3/checklock.php?username=' + username + '&lockid=' + lock_id)
bytes_string = response.read()
result = str(bytes_string, 'utf-8')

#Searches result for 'UnlockedReal'. -1 means 'UnlockedReal was not returned and safe stays locked
#If 'UnlockedReal' is found, a number other than -1 will be returned and safe will be unlocked.
if result.find('UnlockedReal') == -1:
	print('Locked')
	#call to function to notify safe status was checked and remains locked
else:
	print('Open Safe')
	#call to function to notify safe status was checked and is being unlocked
	#call to function to unlock the safe
	



	
