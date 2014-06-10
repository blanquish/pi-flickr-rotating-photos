
# Create your views here.
from django.shortcuts import render
from models import Photo
from raw_api_calls import get_photos_for_vivid_festival, get_photo_url_large


def index(request):
    # return HttpResponse("Hello, world. You're at the photoslideshow app.")

    #latest_photos = Photo.objects.all()[:5]
    #output = ', '.join([p.url for p in latest_photos])
    #output = ''

    xmlphotoset = get_photos_for_vivid_festival()

    photoset = xmlphotoset.find('photoset')
    #print(photoset.attrib)

    latest_photos = []
    for photo in photoset.findall('photo'):
        photo_id = photo.attrib['id']

        photo_title = photo.attrib['title']
        photo_url = get_photo_url_large(photo_id)
        #photo_created_date = ''
        p = Photo(title=photo_title, url=photo_url, created_date='')
        latest_photos.append(p)

    #for p in latest_photos:
        #new_image = '<img src="' + p.url + '" + alt="' + p.title + '" > <br/>'
        #output += new_image
    #return HttpResponse(output)
    return render(request, 'display_photo.html', {'photos': latest_photos, 'firstphoto' : latest_photos[0]})