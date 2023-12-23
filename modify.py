import json

string = {'d': {'results': [{'__metadata': {'uri': "https://my333889.crm.ondemand.com/sap/c4c/odata/cust/v1/individualcustomer_pubsub_v1/CustomerCollection('00163E2BE7F01EE880B5BB0B62470EF0')", 'type': 'cust.Customer', 'etag': 'W/"datetimeoffset\'2022-04-27T11%3A36%3A47.9720200Z\'"'}, 'ObjectID': '00163E2BE7F01EE880B5BB0B62470EF0', 'ETag': '/Date(1651059407972)/', 'RecordNumber': '', 'ExternalKey': '', 'InternalID': '50076002', 'UUID': '00163E2B-E7F0-1EE8-80B5-BB0B62470EF0', 'OscarLegacyID_KUT': '', 'BusinessPartnerFormattedName': 'Chalermkwan Eurlaphan', 'CategoryCode': '1', 'CategoryCodeText': 'Person', 'CustomerABCClassificationCode': '', 'CustomerABCClassificationCodeText': '', 'ZKUT_HowDidYouHear_KUT': '', 'ZKUT_HowDidYouHear_KUTText': '', 'ZKUT_WalkIn_KUT': False, 'ZKUT_CustomerCreatedon_KUT': '/Date(1516838400000)/', 'ZKUT_EBSSyncDate_KUT': None, 'ZKUT_EBSAccountSiteID_KUT': '', 'KUT_PreferredStudyCountryCode_KUT': 'NZ', 'RegisteredOnlineIndicator_SDK': False, 'KUT_PreferredStudyLanguageCode_KUT': '', 'KUT_PreferredStudyLanguageCode_KUTText': '', 'KUT_PrimaryLanguageCode_KUT': 'TH', 'KUT_PrimaryLanguageCode_KUTText': 'Thai', 'TCAcceptance_KUT': True, 'KUT_STUDENT_ContactMethodMVCode_KUT': 'IDP010,IDP020', 'ZKUT_PrimFinSource_KUT': '', 'ZKUT_PrimFinSource_KUTText': '', 'CreationIdentityUUID': '00163E2B-E81A-1EE7-A5E9-9A9DB2921E9C', 'LastChangeDateTime': '/Date(1586497117875)/', 'LastChangeIdentityUUID': '00163E66-CD7F-1ED9-9190-74E3EEDFF5D0', 'LifeCycleStatusCode': '2', 'LifeCycleStatusCodeText': 'Active', 'ZKUT_HighestEdu_KUT': '', 'ZKUT_HighestEdu_KUTText': '', 'RoleCode': 'ZIDP03', 'RoleCodeText': 'Student', 'AcademicTitleCode': '', 'AcademicTitleCodeText': '', 'MiddleName': '', 'GivenName': 'Chalermkwan', 'NationalityCountryCode': '', 'NationalityCountryCodeText': '', 'MaritalStatusCode': '', 'MaritalStatusCodeText': '', 'GenderCode': '1', 'GenderCodeText': 'Male', 'BirthDate': None, 'BusinessPartnerUUID': '00163E2B-E7F0-1EE8-80B5-BB0B62470EF0', 'PrimaryEmailAddresscontent_SDK': 'Eur.kwan.4@gmail.com', 'SecondaryEmailAddresscontent1_SDK': '', 'BirthCountryCode1_SDK': '', 'BirthCountryCode1_SDKText': '', 'AlumniIndicator1_SDK': False, 'SiteID1_SDK': 'thailand', 'MarketingAcceptanceIndicator1_SDK': True, 'ZSDK_ReferredBy1_SDK': '', 'ZSDK_ReferredByName_SDK': '', 'ZSDK_ReferralCounsellorName_SDK': '', 'NonEnglishName1_SDK': 'เฉลิมขวัญ เอื้อละพันธ์', 'ZSDK_ReferralCounsellor     rUUIDcontent1_SDK': None, 'ZSDK_ReferralCounsellorcontent_SDK': '', 'FamilyName': 'Eurlaphan', 'FormOfAddressCode': '0002', 'FormOfAddressCodeText': 'Mr.', 'ResidencyCountryCode1_SDK': '', 'ResidencyCountryCode1_SDKText': '', 'CreatedByName': '', 'LastChangedByName': 'Data Migration23', 'LastChangedByBPID': '8000006360', 'CreatedByBPID': '', 'CounsellorName': 'Wanapa Sumanus', 'CounsellorEmpID': '440000061', 'ZSDKIsReferral': False, 'CounsellorUUID': '00163E42-24F7-1EE7-B5BD-2CFB11B24313', 'MainAddressUUID': '00163E2B-E7F0-1EE8-80B5-BB0B62480EF0', 'TypeCode1_SDK': '01', 'TypeCode1_SDKText': 'Home', 'CounsellorBPID': '000000000000000000000000000000000000000000000000000440000061', 'LastChangedByUUID': '00163E66-CD7F-1ED9-9190-70C58A0DF5CB', 'CreatedByUUID': None, 'CreationDateTime': '/Date(1516870681850)/', 'TechUserCreatedByID': '_YCOM', 'TechUserChangedByID': 'DATA.MIGRATION23.INVALID', 'SiteIDCodecontent_SDK': 'TH', 'SiteIDCodecontent_SDKText': 'thailand', 'ZKUT_CounsellingMode_KUT': '', 'ZKUT_CounsellingMode_KUTText': '', 'ZKUT_SPAppIndicator_KUT': '', 'ZKUT_SPAppIndicator_KUTText': '', 'ZKUT_SPAppLastLogin_KUT': None, 'refCounsSalesOfficeID_SDK': '', 'ZKUT_YMrktReferalFlag_KUT': False, 'ZKUT_MigratedSystem_KUT': '', 'ZKUT_MigratedSystem_KUTText': '', 'ZKUT_MigratedSystemCreatedOn_KUT': None, 'ZKUT_MigratedSystemID_KUT': '', 'CustomerCurrentEmployeeResponsible': {'__deferred': {'uri': "https://my333889.crm.ondemand.com/sap/c4c/odata/cust/v1/individualcustomer_pubsub_v1/CustomerCollection('00163E2BE7F01EE880B5BB0B62470EF0')/CustomerCurrentEmployeeResponsible"}}, 'MarketingPermissionChannelPermission': {'__deferred': {'uri': "https://my333889.crm.ondemand.com/sap/c4c/odata/cust/v1/individualcustomer_pubsub_v1/CustomerCollection('00163E2BE7F01EE880B5BB0B62470EF0')/MarketingPermissionChannelPermission"}}, 'CustomerAddressInformation': {'__deferred': {'uri': "https://my333889.crm.ondemand.com/sap/c4c/odata/cust/v1/individualcustomer_pubsub_v1/CustomerCollection('00163E2BE7F01EE880B5BB0B62470EF0')/CustomerAddressInformation"}}, 'MarketingPermission': {'__deferred': {'uri': "https://my333889.crm.ondemand.com/sap/c4c/odata/cust/v1/individualcustomer_pubsub_v1/CustomerCollection('00163E2BE7F01EE880B5BB0B62470EF0')/MarketingPermission"}}, 'AddressSnapshot': {'__deferred': {'uri': "https://my333889.crm.ondemand.com/sap/c4c/odata/cust/v1/individualcustomer_pubsub_v1/CustomerCollection('00163E2BE7F01EE880B5BB0B62470EF0')/AddressSnapshot"}}}]}}

a = json.dumps(string, indent=4)
print(a)

# with open(r'C:\Users\balasubramaniam.cs\OneDrive - IDP Education Ltd\Desktop\Sample\modify.json', 'w') as output:
#     output.write(a)