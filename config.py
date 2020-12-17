import os

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'QEyEDmME/jr9D3YJfvJlORnkF4Jtko6ItxH8kMmZ6CQ='

    MONGODB_SETTINGS = { 'db': 'UTA_Enrollment' }





# import os

# class Config(object):
#     SECRET_KEY = os.environ.get('SECRET_KEY') or b'6\xe9\xda\xead\x81\xf7\x8d\xbbH\x87\xe8m\xdd3%'

#     MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment' }


    