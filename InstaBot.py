# -*- coding: utf-8 -*-
"""
Created on Wed Feb 07 01:01:53 2018

@author: HelloWorld
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 06 22:20:16 2018

@author: HelloWorld
"""
#import request to get the api PIL and stringIO to view image
import requests
from PIL import Image
from StringIO import StringIO
#app token
APP_ACCESS_TOKEN = "1056537964.1677ed0.eba5c412df8540069a9bca62389f7ab0"
BASE_URL='https://api.instagram.com/v1/'
#self information
def self_info():
    #url for self info
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    #converting it to json
    user_info = requests.get(request_url).json()
    #code=200 check
    if user_info['meta']['code'] == 200:
        if 'data' in user_info:
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
            response = requests.get(user_info['data']['profile_picture'])
            print "Profile Picture:"
            img = Image.open(StringIO(response.content))
            img.show()
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'
#function call
self_info()

#to get user_id
def get_user_id(insta_username):
    #url
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
    #code=200 check 
    if user_info['meta']['code'] == 200:
        if 'data' in user_info:
            #return user id
            return user_info['data'][0]['id']
        else:
            #return Nono
            return "None"
    else:
        print 'Status code other than 200 received!'
        exit()





def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if 'data' in user_info:
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'There is no data for this user!'
    else:
        print 'Status code other than 200 received!'
        
        
get_user_info("vipsparashar")