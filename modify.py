import random

REPOS = [
"aws-global-student-english-proficieny-test-publication",
"aws-lead-publication",
"aws-lead-subscription",
"aws-global-lead-publications",
"aws-bcleads-c4c-publication",
"aws-student-publication",
"aws-student-subscription",
"aws-global-student-publication",
"aws-student-english-proficieny-test-publication",
"aws-student-english-proficieny-test-subscription",
"aws-c4c-student-education-history-publication",
"aws-student-education-history-subscription",
"aws-global-student-education-history-publication",
"aws-c4c-student-social-media-account-publication",
"aws-student-social-media-account-subscription",
"aws-global-student-social-media-account-publication",
"aws-c4c-student-employment-history-publication",
"aws-c4c-student-employment-history-subscription",
"aws-global-student-employement-history-publication",
"aws-global-student-entities-publication",
"aws-c4c-student-id-publication",
"aws-c4c-student-id-subscription",
"aws-global-student-id-publication",
"aws-c4c-student-mp-publication",
"aws-c4c-student-mp-subscription",
"aws-global-student-marketingpermission-publication",
"aws-c4c-appointment-publication",
"aws-c4c-appointment-subscription",
"nps-qualtrics-publication",
"nps-satisfaction-survey-publish",
"nps-qualtrics-subscription",
"nps-c4c-healthcheck-publisher",
"aws-employee-subscription",
"aws-c4c-employee-publication",
"aws-sf-employee-subscriptions",
"aws-c4c-servicetickets-publication",
"aws-c4c-servicetickets-subscription",
"aws-contracts-publication",
"aws-contracts-subscription",
"global-course-data-subscription",
"recomendation_engine_subscribe",
"idp-heart-beat-monitoring-microservice",
"collectnow-publication",
"aws-c4c-stdnotes-publication",
"aws-course-oip-publisher",
"aws-c4c-cap-reports-publish",
"aws-c4c-export-task-data",
"aws-idp-direct-publications",
"aws-ipd-direct-uoa-subscription",
"aws-idpd-gu-subscription",
"aws-idpd-InsearchUTS-subscription",
"aws-idpd-publication",
"aws-idpd-uts-subscription",
"aws-idpd-mock-response-api",
"aws-c4c-monash-eventcode-api",
"aws-mp-dms-bff",
"aws-mp-dms",
"ai-service-dms-subscribe",
"c4c_dms_subscribtion"
]

random.shuffle(REPOS)

BALA = []
ZAFAR = []

# print(REPOS)

for i in range(1, len(REPOS)+1):
    if i % 2 == 0:
        BALA.append(REPOS[i-1])
    else:
        ZAFAR.append(REPOS[i-1])

Z = ['aws-global-student-id-publication', 'aws-c4c-cap-reports-publish', 'aws-c4c-student-education-history-publication', 'collectnow-publication', 'aws-idpd-mock-response-api', 'aws-c4c-student-social-media-account-publication', 'aws-student-english-proficieny-test-subscription', 'global-course-data-subscription', 'recomendation_engine_subscribe', 'aws-c4c-appointment-publication', 'aws-contracts-subscription', 'nps-qualtrics-subscription', 'ai-service-dms-subscribe', 'aws-student-english-proficieny-test-publication', 'aws-student-education-history-subscription', 'aws-c4c-servicetickets-subscription', 'aws-idpd-gu-subscription', 'aws-idp-direct-publications', 'nps-qualtrics-publication', 'aws-c4c-student-employment-history-subscription', 'aws-lead-publication', 'c4c_dms_subscribtion', 'aws-c4c-servicetickets-publication', 'aws-student-publication', 'aws-global-student-entities-publication', 'nps-c4c-healthcheck-publisher', 'aws-global-student-english-proficieny-test-publication', 'aws-contracts-publication', 'aws-lead-subscription', 'idp-heart-beat-monitoring-microservice']
B = ['aws-global-student-social-media-account-publication', 'aws-bcleads-c4c-publication', 'aws-c4c-employee-publication', 'aws-c4c-student-mp-subscription', 'aws-idpd-InsearchUTS-subscription', 'aws-global-lead-publications', 'aws-employee-subscription', 'aws-c4c-monash-eventcode-api', 'aws-c4c-student-id-subscription', 'aws-idpd-uts-subscription', 'aws-global-student-publication', 'aws-global-student-education-history-publication', 'aws-c4c-export-task-data', 'aws-c4c-student-mp-publication', 'aws-c4c-student-id-publication', 'aws-c4c-student-employment-history-publication', 'aws-global-student-employement-history-publication', 'nps-satisfaction-survey-publish', 'aws-mp-dms-bff', 'aws-student-subscription', 'aws-student-social-media-account-subscription', 'aws-c4c-stdnotes-publication', 'aws-course-oip-publisher', 'aws-c4c-appointment-subscription', 'aws-mp-dms', 'aws-global-student-marketingpermission-publication', 'aws-idpd-publication', 'aws-ipd-direct-uoa-subscription', 'aws-sf-employee-subscriptions']

for i in Z:
    print(i)
