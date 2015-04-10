__author__ = 'rakesh'


import urllib2
import json, time

'''
class NYCGeoclient is the NYC API gecoder.
'''

class NYGeoclient():
    '''
    the documentation for NYC geocoder is here https://developer.cityofnewyork.us/api/geoclient-api
    '''

    def __init__(self, api_key, api_id):
        '''
        api_key and api_id are mandatory field here
        API Authentication is required for the NYC geoclient
        '''

        self.api_key = '&app_key=' + api_key
        self.domain_name = 'https://api.cityofnewyork.us/geoclient/v1/search.json?input='
        self.api_id = '&app_id=' + api_id



    def geocode(self, address):
        '''
        geolocator = NYGeoclient('bb80a97381a0fa916bb860768fa71b8f', 'e7df1765')

        address, latitude, longitude = geolocator.geocode('175 5th Avenue NYC')

        print address, latitude, longitude
        '''
        address = address.split()

        urlAddress = "%20".join(address)

        urlAddress = "%20" + urlAddress

        full_address = self.domain_name + str(urlAddress) + self.api_id + self.api_key

        a = urllib2.urlopen(full_address)

        location = json.load(a)['results'][0]['response']

        normalizedAddress = location['houseNumberIn'] + " " + location['boePreferredStreetName'] + " " + location['firstBoroughName'] + " " + location['zipCode']

        latitude = location['latitude']

        longitude = location['longitude']

        return normalizedAddress, latitude, longitude


    def parameters(self, address, *args):
        '''
        if you need particular information then you should call this function with those parameters

        geolocator = NYGeoclient('bb80a97381a0fa916bb860768fa71b8f', 'e7df1765')

        print geolocator.parameters('175 5th Avenue NYC', 'houseNumberIn', 'boePreferredStreetName')
        '''
        address = address.split()

        urlAddress = "%20".join(address)

        urlAddress = "%20" + urlAddress

        full_address = self.domain_name + str(urlAddress) + self.api_id + self.api_key

        a = urllib2.urlopen(full_address)

        location = json.load(a)['results'][0]['response']

        information = {}
        if args:
            for i in range(len(args)):
                information[args[i]] = location[args[i]]

        return information  #it will return a dictionary of information




