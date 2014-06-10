import urllib2
import xml.etree.ElementTree as ET


API_KEY = '4ec3c57159771996d1e238bdf3ecd7f4'
SHARED_SECRET = '275626a0863c66b6'
USER_ID = '9097953@N03'
NUM_PHOTOS = '10'

#### Will only get public photosets
def get_photosets():
    url_photo_list = "https://api.flickr.com/services/rest/?method=flickr.photosets.getList"
    url_photo_list += "&api_key=" + API_KEY
    url_photo_list += "&user_id=" + USER_ID

    # get the result
    response = urllib2.urlopen(url_photo_list)
    elementtree = ET.fromstring(response.read())
    print(elementtree.attrib)

    return elementtree


def print_photosets_title_and_count(xmlroot):
    photosets = xmlroot.find('photosets')
    print(photosets.attrib)

    for pset in photosets.findall('photoset'):
        title = pset.find('title').text
        count = pset.attrib['count_views']

        print('[' + title + '] has ' + count + ' photos')


def get_photos_for_vivid_festival():
    url_photo_list = "https://api.flickr.com/services/rest/?method=flickr.photosets.getPhotos"
    url_photo_list += "&api_key=" + API_KEY
    url_photo_list += "&photoset_id=" + '72157635003975675'
    url_photo_list += "&user_id=" + USER_ID

    response = urllib2.urlopen(url_photo_list)
    elementtree = ET.fromstring(response.read())
    return elementtree


def print_photoset_photos(xmlphotoset):

    photoset = xmlphotoset.find('photoset')
    #print(photoset.attrib)

    for photo in photoset.findall('photo'):
        photo_id = photo.attrib['id']

        print(get_photo_url_large(photo_id))

def get_photo_url_large(photo_id):

    url_photo_large  = "https://api.flickr.com/services/rest/?method=flickr.photos.getSizes"
    url_photo_large += "&api_key=" + API_KEY
    url_photo_large += "&photo_id=" + photo_id
    response = urllib2.urlopen(url_photo_large)
    elementtree = ET.fromstring(response.read())

    sizes = elementtree.find('sizes')
    for s in sizes.findall('size'):
        if s.attrib['label'] == 'Large':
            return s.attrib['source']



######## Main Application ##########
if __name__ == '__main__':
    #mysets = get_photosets()
    #print_photosets_title_and_count(mysets)

    vividfestival = get_photos_for_vivid_festival()

    print_photoset_photos(vividfestival)

    print(get_photo_url_large('9478683550'))

    # requires authentication
    url_favourites_list = "https://api.flickr.com/services/rest/?method=flickr.favorites.getList"


