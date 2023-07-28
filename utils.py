import requests
# SOAP request URL
url = "https://test-admissions-griffith.studylink.com/webservices/CreateapplicationAPI.cfc?wsdl"

# structured XML
payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
			    
<SOAP-ENV:Envelope
	xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
	xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:xsd="http://www.w3.org/2001/XMLSchema">
	<SOAP-ENV:Body>
		<m:login
			xmlns:m="http://webservices" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
			<authusername xsi:type="xsd:string">IDP_GRIFFITH</authusername>
			<authpassword xsi:type="xsd:string">Wc6rmHWtb5Hq$l.</authpassword>
			<providerCode xsi:type="xsd:string">GRIFFITHDIRECT</providerCode>
		</m:login>
	</SOAP-ENV:Body>
</SOAP-ENV:Envelope>"""
# headers
headers = {
	'Content-Type': 'text/xml; charset=utf-8',
    'SOAPAction': ''
}
# POST request
response = requests.request("POST", url, headers=headers, data=payload, timeout=180)

# prints the response
print(response.text)
