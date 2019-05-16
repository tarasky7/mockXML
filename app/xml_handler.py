import os
import re

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

def set_idle_time(id, key, req, step, idle_time):
   reply = common_handler(id, key, req, step)
   begin = r'<idle-timeout>'
   end = r'</idle-timeout>'
   reply = sub_pattern_xml(reply, begin, end, idle_time)
   if __name__ == '__main__':
      print reply
   return reply
   
def sub_pattern_xml(reply, begin, end, sub_str):
   pattern = re.compile(begin + r'(.+)' + end)
   sub_str = begin + sub_str + end
   return re.sub(pattern, lambda m: sub_str, reply)

if __name__ == '__main__':
   set_idle_time('', 'do-submit-authentication', '', '', '10')
