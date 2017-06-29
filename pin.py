import requests
import re
from . import board as Board

API_BASE = 'https://api.pinterest.com/v1'
PINS_ENDPOINT = API_BASE + '/pins/'

# The interfaces below are intended for use with a higher-order auth system
# which selects a candidate from a pool of accounts
# e.g.
# @authenticate(pool='name_of_account_pool')
# For now, supply some defaults while we use one account for all operations
DEFAULT_ACCESS_TOKEN = os.environ.get('PINTEREST_ACCESS_TOKEN')
DEFAULT_USERNAME = os.environ.get('PINTEREST_USERNAME')


# A 1-1 method map for API @ https://developers.pinterest.com/docs/api/pins/

def create(board_name, description, link, image_url, username=DEFAULT_USERNAME, access_token=DEFAULT_ACCESS_TOKEN):
    ''' Creates a board with board_name, description, link, and image_url '''
    if not ((isinstance(board_name, str) and isinstance(description, str) 
        and isinstance(link, str) and isinstance(image_url, str))):
        raise TypeError('Expected board_name, description, link, image or image_url strings but received {}'.format((name)))
    board = {'username': username, 'board_name': board_name}
    params = {'board': '{username}/{board_name}'.format(**board), 'note': description, 'link': link, 'image_url': image_url, 'access_token': access_token}
    print(params)
    return requests.post(PINS_ENDPOINT, params)

def get_one(pin_id, access_token=DEFAULT_ACCESS_TOKEN):
    ''' Gets one pin by unique identifier '''
    if not isinstance(pin_id, str):
        raise TypeError('Expected pin_id string but received {}'.format((name)))
    params = {'access_token': access_token}
    return requests.get(PINS_ENDPOINT + '{}/'.format(pin_id), params)

def get_pins_by_user(access_token=DEFAULT_ACCESS_TOKEN):
    ''' Gets all pins by user who owns bearer token'''
    params = {'access_token': access_token}
    return requests.get(API_BASE + '/me/pins/', params)

def get_pins_by_board(board_name, username=DEFAULT_USERNAME, access_token=DEFAULT_ACCESS_TOKEN):
    ''' Gets all pins associated with board_name '''
    if not isinstance(board_name, str):
        raise TypeError('Expected board_name string but received {}'.format((name)))
    params = {'access_token': access_token}
    path = {'username': username, 'board_name': board_name}     
    return requests.get(API_BASE + '/boards/{username}/{board_name}/pins/'.format(**path), params)

def update(pin_id, description, link, board_name, username=DEFAULT_USERNAME, access_token=DEFAULT_ACCESS_TOKEN):
    ''' update the description / link of a pin, and optionally move it to a different board'''
    if not isinstance(pin_id, str):
        raise TypeError('Expected pin_id string but received {}'.format((name)))
    
    params = { k:v for k,v in {'link': link, 'description': description, 'access_token': DEFAULT_ACCESS_TOKEN} if v is not None}

    if board_name:
        board = {'board_name': board_name, 'username': username}
        params['board'] = '{username}/{board_name}'.format(**board)
    
    return requests.patch(PINS_ENDPOINT + '{}/'.format(pin_id), params) 

def delete(pin_id, access_token):
    ''' Deletes a pin by unique identifier '''
    return requests.delete(PINS_ENDPOINT + '{}/'.format(pin_id), {'access_token': access_token})
