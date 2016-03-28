import facebook
token = "CAACEdEose0cBANEy9XDV2iuHrAvzm4SsnVQJ1hQMsE3sgF5WGWdEQkNveBmcTv2iVUKCyM2TijNyZCbM0gMSwqk6TXxVFWJxZAhDHvUducWJ24rPPNy5FZARmNkeQ5FEnPIcpfwEUIQTPnwnAwe5QiPZACZAI9Wb0wIGIiBAhKTEvHTviZBoZAov6qNQ8bIRNlewSR3tkLpCgZDZD"
graph = facebook.GraphAPI(token)
profile = graph.get_object("3ST Technologies")
posts=graph.get_connections(profile['id'],"posts")

for post in posts['data']:
	try:
		graph.put_object(post['id'],"likes")
		print "Liking the topic: "+post['message']
	except:
		continue
