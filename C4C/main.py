from CustomExceptions import EntityNotFound, SearchWithNotFound
from c4c_class import C4C

entity_list = ["ic", "lead", "document", "oppurtunity"]

search_with_list = ["object_id", "crm_id", "email_id", "lead_with_id_url", "lead_with_crm_id", "object_id", "opp_id"]

DOMAIN = "dev"

ENTITY = "ic"

SEARCH_WITH = "email_id"

SEARCH_VALUE = "zafarhdsadik@gmail.com"

if ENTITY not in entity_list:
    raise EntityNotFound(f"{ENTITY} not in the entity_list")

if SEARCH_WITH not in search_with_list:
    raise SearchWithNotFound(f"{SEARCH_WITH} not in the search_with_list")
# create an object of class C4C with domain and search parameters as parameters.
c4c_session = C4C(DOMAIN, ENTITY, SEARCH_WITH, SEARCH_VALUE)

response = c4c_session.get_result()

c4c_session.write_output_to_file(response)
