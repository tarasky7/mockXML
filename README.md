This is a xml mock up application for [htmlaccess](https://gitlab.eng.vmware.com/core-build/htmlaccess). It is used to help run all the P0 test cases for HTML5 client automatically. 
Details can be found [here](https://confluence.eng.vmware.com/pages/viewpage.action?spaceKey=~jinxingh&title=Mockxml).
## How it works
- The Nginx server will forward the request for broker XML message to the mockXML server. To be specific, the nginx will redirect the AJAX request for "/broker/xml" to the mockup Server.
- MockXML will check the cookie and load the related XML messages from the corresponding folder and files.(It will use the default ones if the files in the cookie folder is not existed)

## Cookies
- TestCase: denotes which test case to run.
- TestStep: if one case has several steps, this cookie will decide which step to run.
- EditXML: if one case need to modify xml file, this cookie will specify which file to change.
- TestFunc: if one case need to modify the xml files(for example, set the idle time in do-submit-authentication.xml), this cookie will tell the application which function to run.
- TestValue: corresponds with TestFunc, determines the value we want to set in a specific function.

## Resources
- [ProtractorTemp](https://gitlab.eng.vmware.com/horizonweb/protractortemp)
- [Mockxml](https://confluence.eng.vmware.com/display/~jinxingh/Mockxml)
- [Internal XML API Documentation](https://confluence.eng.vmware.com/pages/viewpage.action?spaceKey=HorizonArchitecture&title=Internal+XML+API+Documentation)
- [HTML5 client automation](https://confluence.eng.vmware.com/display/CNVDES/HTML5+client+automation)
