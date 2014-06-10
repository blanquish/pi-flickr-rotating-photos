import flickrapi

# flickr api https://www.flickr.com/services/apps/by/bgarciagil
# flickr key 4ec3c57159771996d1e238bdf3ecd7f4
# flickr secret 275626a0863c66b6

api_key = '4ec3c57159771996d1e238bdf3ecd7f4'
api_secret = '275626a0863c66b6'
bgarciagil_userId = '9097953@N03'
photos_per_page = '10'

# use ElementTree as the parser
myFlickr = flickrapi.FlickrAPI(api_key, api_secret, bgarciagil_userId, format='etree')
#photos = myFlickr.photos_search(api_key, 'food', per_page=photos_per_page)
#print(photos)
# for photo in photos:
#     title = photo.find('title').text
#     print('[' + title + ']')

# sets = myFlickr.photosets_getList(user_id=bgarciagil_userId)

# for set in sets.find('photosets'):
#     title = set.find('title').text
#     description = set.find('description').text
#     count = set.attrib['photos']
#
#     if description is None:
#         print('[' + title + '] has ' + count + ' photos')
#     else:
#         print('[' + title + '] has ' + count + ' photos')
#         #print('[' + title + '] : [' + description + ']')

favourites = myFlickr.favorites_getList()
#print(sets.find('photosets').findall('photoset')[0].find('title').text)

# get favourites titles
#favourites = flickrapi.flickrClient.favorites_getPublicList(user_id=bgarciagil_userid)
for photo in favourites.photos[0].photo:
    print photo['title']

#<rsp stat='ok'>
#    <photosets cancreate="1">
#        <photoset id="5" primary="2483" secret="abcdef"
#                server="8" photos="4">
#            <title>Test</title>
#            <description>foo</description>
#        </photoset>
#        <photoset id="4" primary="1234" secret="832659"
#                server="3" photos="12">
#            <title>My Set</title>
#            <description>bar</description>
#        </photoset>
#    </photosets>
#</rsp>

