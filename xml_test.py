"""GENERATE GU TOKEN"""
from zeep import Client

URL = 'https://test-admissions-griffith.studylink.com/webservices/CreateapplicationAPI.cfc?wsdl'
USER_NAME = 'IDP_GRIFFITH'
PASSWORD = 'Wc6rmHWtb5Hq$l.'
PROVIDER_CODE = 'GRIFFITHDIRECT'

client = Client(URL)
print("Sending request to studylink")
token = client.service.login(
    authusername=USER_NAME, authpassword=PASSWORD, providerCode=PROVIDER_CODE)

if token != 'Authentication Failed':
    print(token)
    print("SUCESS")
else:
    print("FAILED")