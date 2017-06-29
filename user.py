import requests

API_BASE = 'https://api.pinterest.com/v1'
BOARDS_ENDPOINT = API_BASE + '/me/'

# The interfaces below are intended for use with a higher-order auth system
# which selects a candidate from a pool of accounts
# e.g. 
# @authenticate(pool='name_of_account_pool')
# For now, supply some defaults while we use one account for all operations
DEFAULT_ACCESS_TOKEN = os.environ.get('PINTEREST_ACCESS_TOKEN')
DEFAULT_USERNAME = os.environ.get('PINTEREST_USERNAME')


# A 1-1 method map for API @ https://developers.pinterest.com/docs/api/users/

raise NotImplementedError