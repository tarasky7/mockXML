from app import app, xml_handler
from flask import Flask, request, Response
import xmltodict

@app.route("/broker/xml", methods = ['POST'])
def front_handler():
   test_case = '0'
   if not request.is_xhr:
      print "mockxml only accept XHR request"
   xml_message = request.get_data()
   if 'TestCase' in request.cookies.keys():
      test_case = request.cookies['TestCase']
   response = xml_handler.header()
   xml_dict = xmltodict.parse(xml_message)['broker']
   for key in xml_dict:
      if key == '@version':
         continue
      response += getattr(xml_handler, key.replace('-', '_'))(test_case, key, xml_dict[key])
   response += xml_handler.tail()

   return Response(response, 'text/xml;charset=UTF-8')