import os
from app import app, xml_handler
from flask import Flask, request, Response, send_from_directory
import xmltodict

@app.route('/broker/xml', methods = ['POST'])
def xml_message_handler():
   test_case = ''
   test_step = ''
   if not request.is_xhr:
      print "mockxml only accept XHR request"
   xml_message = request.get_data()
   if 'TestCase' in request.cookies.keys():
      test_case = request.cookies['TestCase']
      print test_case

   if 'TestStep' in request.cookies.keys():
      test_step = request.cookies['TestStep']
      print test_step

   response = xml_handler.header()
   xml_dict = xmltodict.parse(xml_message)['broker']
   for key in xml_dict:
      if key == '@version':
         continue
      print 'receive ' + key + ' message from client'
      response += xml_handler.common_handler(test_case, key, xml_dict[key], test_step)
      #TODO: if needed
      #response += getattr(xml_handler, key.replace('-', '_'))(test_case, key, xml_dict[key], test_step)
   response += xml_handler.tail()
   return Response(response, status=200, mimetype='text/xml;charset=UTF-8')

@app.route('/broker/resources/icon/<string:icon_name>', methods=['GET'])
def icon_message_handler(icon_name):
   static_dir = os.path.dirname(os.path.realpath('__file__')) + '/data/icons'
   return send_from_directory(static_dir, icon_name)
