import meetup.api, sys, random, re

api_key = 'ENTER API KEY'
client = meetup.api.Client(api_key)

# assuming all meetups are in NY, USA
looked_at = []
group_info = client.GetFindGroups({'state': 'NY'})

# test case in a small sample
#group_info = client.GetFindGroups({'state': 'NY', 'page': 5})

# Remove html tags from @param 'txt'
def cleanText(txt):
	clean = re.compile('<.*?>')
	cleantxt = re.sub(clean,'',txt)
	return cleantxt

choice = int(input("Look for random Meetup groups, enter '1' for YES or '0' for NO: "))
while choice not in (0,1):
	print("Incorrect input")
	choice = int(input("Look for random Meetup groups, enter '1' for YES or '0' for NO: "))

while choice != 0:
	# generates random number
	rand = random.randrange(0,len(group_info))
	if choice == 1:
		if len(looked_at) != len(group_info):		
			if group_info[rand] not in looked_at:
				print("\nName:", group_info[rand].name,"\n")
				
				# remove group from list and add to looked_at
				looked_at.append(group_info[rand])
				#print("looked_at length:", len(looked_at), "\ngroup_info length:",len(group_info))

				# ask for more info, new group or exit
				choice = int(input("Look for random Meetup groups, enter '1' for YES or '0' for NO\nFor more information on the group, enter '2': "))
				if choice == 2:
					des = cleanText(group_info[rand].description)
					print("\nDescription:", des, "\nNumber of members: ", group_info[rand].members, "\nLink:", group_info[rand].link,"\n")
					choice = int(input("Look for random Meetup groups, enter '1' for YES or '0' for NO: "))
		# all groups looked up
		else:
			print("\nLooked at all Meetup groups in NY already")
			break
	# incorrect input
	else:
		print("\nIncorrect input")
		choice = int(input("Look for random Meetup groups, enter '1' for YES or '0' for NO\nFor more information on the group, enter '2': "))

print("Bye!")
sys.exit()

