import json
import httplib2

def getGeocodeLocation(inputString):
    google_api_key = "AIzaSyDPJjZpmZN5f7fguXAOaHRGRzGVmSILPjQ"
    locationString = inputString.replace(" ", "+")
    url =('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'%(locationString,google_api_key))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    latitude = result['results'][0]['geometry']['location']['lat']
    longtude = result['results'][0]['geometry']['location']['lng']
    #print "response header: %s \n \n" % response
    return (latitude,longtude)
