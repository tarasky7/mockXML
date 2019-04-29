import os

def header():
   return '''<?xml version="1.0"?><broker version="15.0">'''

def tail():
   return '</broker>'

def common_handler(id, key, req, step = ''):
   reply = ''
   file_dir = os.path.dirname(os.path.realpath('__file__'))
   default_file = file_dir + '/data/default/' + key + '.xml'
   expected_file = file_dir + '/data/' + id + '/' + key  + '.xml'
   if (step != ''):
      expected_file = file_dir + '/data/' + id + '/' + key  + '.' + step + '.xml'

   exist = os.path.isfile(expected_file)
   if exist:
      with open(expected_file) as f:
         reply = f.read()
   else:
      with open(default_file) as f:
         reply = f.read()
   return reply

# TODO:
# if needed later
# def set_locale(id, key, req, step):
#   return common_handler(id, key, req, step)
