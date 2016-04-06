
import facepy
import facebook

graph = facebook.GraphAPI(access_token="access_token_goes_here", version='2.2')

base_url = 'https://graph.facebook.com/v2.3/'

profile = graph.get_object("page_name")

posts = graph.get_connections(profile['id'],"posts")

for post in posts['data']:
	try:
		graph.put_object(post['id'],"likes")
		print "Liking the topic: " + post['message']
	except:
		continue
