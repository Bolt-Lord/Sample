import json

import requests


class C4C:
    entity = ""
    search_with = ""
    spec_url = ""

    def __init__(self, domain, entity, search_with, search_value) -> None:
        self.domain = domain
        if domain == "dev":
            self.base_url = "https://my332876.crm.ondemand.com"
        if domain == "stage":
            self.base_url = "https://my330697.crm.ondemand.com"
        if domain == "uat":
            self.base_url = "https://my334392.crm.ondemand.com"
        if domain == "prod":
            self.base_url = "https://my333889.crm.ondemand.com"
        self.entity = entity
        self.search_with = search_with
        self.search_value = search_value
        entity_set = {
            "student": {
                "object_id": "/sap/c4c/odata/cust/v1/individualcustomer_pubsub_v1/CustomerCollection?$format=json&$filter=InternalID eq '{}'&$expand=CustomerAddressInformation/CustomerAddress",
                "crm_id": "/sap/c4c/odata/cust/v1/individualcustomer_pubsub_v1/CustomerCollection?$format=json&$filter=InternalID eq '{}'",
                "email_id": "/sap/c4c/odata/cust/v1/individualcustomer_pubsub_v1/CustomerCollection?$format=json&$filter=PrimaryEmailAddresscontent_SDK eq '{}'"
            },
            "lead": {
                "lead_with_id_url": "/sap/c4c/odata/cust/v1/lead_pubsub_v1/LeadCollection?$format=json&$filter=ID eq '{}'",
                "lead_with_crm_id": "/sap/c4c/odata/cust/v1/lead_pubsub_v1/LeadCollection?$format=json&$filter=PartyID eq '{}'"
            },
            "document": {
                "object_id": "sap/c4c/odata/v1/c4codataapi/IndividualCustomerAttachmentFolderCollection?$format=json&$filter=ObjectID eq '{}'"
            },
            "oppurtunity": {
                "crm_id": "/sap/c4c/odata/cust/v1/idpd_student_details_v1/StudentDetailsBORootCollection?$format=json&$filter=InternalID eq '{}'&$expand=StudentExtensionIdentificationDocument",
                "opp_id": "/sap/c4c/odata/cust/v1/idpdirect/IDPDirectRootCollection?$format=json&$filter=OpportunityID eq '{}'"
            },
            "nps": {
                "ticket": "/sap/c4c/odata/v1/c4codataapi/ServiceRequestCollection"
            },
            "employer": {
                "id": "/sap/c4c/odata/v1/c4codataapi/EmployeeCollection?$filter=EmployeeID eq '{}'&$expand=EmployeeOrganisationalUnitAssignment,BusinessUser",
                "object_id": "/sap/c4c/odata/v1/c4codataapi/EmployeeCollection?$filter=ObjectID eq '{}'&$expand=EmployeeOrganisationalUnitAssignment,BusinessUser"
            }
        }
        self.auth_path = r"C:\Users\balasubramaniam.cs\OneDrive - IDP Education Ltd\Desktop\Sample\C4C\certificates\c4c_auth "

        if entity in entity_set:
            self.spec_url = entity_set[entity][search_with]

        self.cert_loc = self.auth_path + self.domain + ".crt"
        self.key_loc = self.auth_path + self.domain + ".key"

    def get_full_url(self):
        url = self.base_url + self.spec_url
        formatted_url = url.format(self.search_value)
        return formatted_url

    def get_result(self):
        c4c_response = requests.get(self.get_full_url(), params={"$top": "1"}, headers={'Content-type': 'application/json'}, cert=(
            self.cert_loc, self.key_loc), timeout=60)
        result = c4c_response.json()
        json.dumps(result["d"]["results"], indent=4)
        return json.dumps(result, indent=4)

    def write_output_to_file(self, response):
        with open(r'C:\Users\balasubramaniam.cs\OneDrive - IDP Education Ltd\Desktop\Sample\C4C\result.json', 'w') as output:
            output.write(response)
