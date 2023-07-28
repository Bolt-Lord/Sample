"""GENERATE GU TOKEN"""
from zeep import Client

URL = 'https://preprod-admissions-griffith.studylink.com/webservices/createapplicationAPI.cfc?wsdl'
USER_NAME = 'GRIFFITH_IDP'
PASSWORD = '5*XDdxB5Jlwx.dH'
PROVIDER_CODE = 'GRIFFITHDIRECT'

client = Client(URL)
print("Sending request to studylink")
token = client.service.login(
    authusername=USER_NAME, authpassword=PASSWORD, providerCode=PROVIDER_CODE)
if token:
    print(token)
    print("SUCESS")
