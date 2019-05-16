This is a xml mock up application for [htmlaccess](https://gitlab.eng.vmware.com/core-build/htmlaccess). It is used to help run all the P0 test cases for HTML5 client automatically. 
Details can be found [here](https://confluence.eng.vmware.com/pages/viewpage.action?spaceKey=~jinxingh&title=Mockxml).
## How it works
- The Nginx server will forward the request for broker XML message to the mockXML server. To be specific, the nginx will redirect the AJAX request for "/broker/xml" to the mockup Server.
- MockXML will check the cookie and load the related XML messages from the corresponding folder and files.(It will use the default ones if the files in the cookie folder is not existed)