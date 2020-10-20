import requests
token = input("\n\n > Token?\n > ")
token = token.replace('"','')
user = input(" > ID to block/unblock?\n > ")
blockorwhat = input(" > 1 > Block\n > 2 > Unblock\n > ")
headers = {'Authorization': token}

if "1" in blockorwhat:
	print(f" > Blocking {user}")
	abc = requests.put(f"https://discord.com/api/v8/users/@me/relationships/{user}", json={'type': "2"}, headers=headers)
	#print(abc.text)
	input(" > Done!\n > ")
if "2" in blockorwhat:
	print(f" > Unblocking {user}")
	abc = requests.delete(f"https://discord.com/api/v8/users/@me/relationships/{user}", headers=headers)
	#print(abc.text)
	input(" > Done!\n > ")
