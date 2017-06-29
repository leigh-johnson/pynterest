import requests
import os

API_BASE = 'https://api.pinterest.com/v1'
BOARDS_ENDPOINT = API_BASE + '/boards/'

# The interfaces below are intended for use with a higher-order auth system
# which selects a candidate from a pool of accounts
# e.g.
# @authenticate(pool='name_of_account_pool')
# For now, supply some defaults while we use one account for all operations
DEFAULT_ACCESS_TOKEN = os.environ.get('PINTEREST_ACCESS_TOKEN')
DEFAULT_USERNAME = os.environ.get('PINTEREST_USERNAME')


# The following functionality requires using a private Pinterest API
# Private APIs are more prone to change, and we would want to obfuscate our usage patterns
def invite_board_user(email):
    ''' Sends callaborative / group board editing invitation to specified email '''
    raise NotImplementedError

def remove_board_user(email):
    ''' Removes account from collaborative / group board editing '''
    raise NotImplementedError

# A 1-1 method map for API @ https://developers.pinterest.com/docs/api/boards/


def get_one(name, username=DEFAULT_USERNAME, access_token=DEFAULT_ACCESS_TOKEN):
    ''' Returns one board by name '''
    if not isinstance(name, str):
        raise TypeError('Expected name string but received {}'.format((name)))
    path = {'name': name, 'username': username}
    params = {'access_token': access_token}
    return requests.get(BOARDS_ENDPOINT + '{username}/{name}/'.format(**path), params)

def get_boards_by_user(access_token=DEFAULT_ACCESS_TOKEN):
    ''' Returns all boards belonging to owner of bearer token'''
    params = {'access_token': access_token}
    return requests.get(API_BASE + '/me/boards/', params)

def get_pins(name, username=DEFAULT_USERNAME, access_token=DEFAULT_ACCESS_TOKEN):
    ''' Returns all pins associated with board '''
    if not isinstance(name, str):
        raise TypeError('Expected name string but received {}'.format((name)))
    path = {'name': name, 'username': username}
    params = {'access_token': access_token} 
    return requests.get(BOARDS_ENDPOINT + '{username}/{name}'.format(**path) + '/pins/', params)

def create(name, description, access_token=DEFAULT_ACCESS_TOKEN):
    ''' Creates a board beloning to owner of bearer token'''
    if not (isinstance(name, str) and isinstance(description, str)):
        raise TypeError('Expected name and description strings but received {}'.format((name , description)))
    params = {'name': name, 'description': description, 'access_token': access_token}
    return requests.post(BOARDS_ENDPOINT, params)

def update(name, description, username=DEFAULT_USERNAME, access_token=DEFAULT_ACCESS_TOKEN):
    ''' Updates the name or description of the specified board'''
    if not isinstance(name, str):
        raise TypeError('Expected name string but received {}'.format((name)))      
    params = { k:v for k,v in {'name': name, 'description': description, 'access_token': DEFAULT_ACCESS_TOKEN} if v is not None}
    path = {'name': name, 'username': username}
    return requests.patch(BOARDS_ENDPOINT + '{username}/{name}/'.format(**path), params)

def delete(name, username=DEFAULT_USERNAME):
    path = {'board_name': name, 'username': username}
    return requests.delete(BOARDS_ENDPOINT + '{username}/{board_name}/'.format(**path)) 