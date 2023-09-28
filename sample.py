import json
import logging
from uuid import uuid4

# from common import common_utils
# from common.Constants import CORRELATION_ID

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class LOGS:
    correlation_id = ''

    def __init__(self, event, context):
        self.event = event['Records'][0]
        self.context = context

    def log_info(self, message):
        logger.info(message)

    def log_error(self, message):
        logger.error(message)

    def get_log_values(self, event, context, log_type, message_type, payload, publish_message, response_details, error_type=None, exc_line_no=None):
        try:
            common_response = {
                'message_type': log_type,
                'processing_stage': message_type,
                'error_type': error_type,
                'exception_line_no': exc_line_no,
                'original_source_app': 'CP',
                'request_payload': payload,
                'publish_message': publish_message,
                'response_details': response_details,
                'target_idp_application': 'CP',
                'correlation_id': str(CORRELATION_ID),
                'aws_request_id': context.aws_request_id,
                'invoker_agent': event['eventSourceARN'],
                'retry_attempt': event['attributes']['ApproximateReceiveCount'],
                'invoked_component': context.function_name,
                'response_timestamp': common_utils.get_external_timestamp(),
                'Log Stream': context.log_stream_name,
                'Log Group': context.log_group_name
            }
            return common_response
        except Exception as err:
            self.log_error('Error while getting common values for log ' + str(err))
            raise

    def logging_error(self, message_type, error_type, exc_line_no):
        try:
            final_log = self.get_log_values(self.event, self.context, 'ERROR', message_type, None, None, None, error_type, exc_line_no)
            self.log_error(json.dumps(final_log))
        except Exception as err:
            self.log_error('Error while logging final error ' + str(err))
            raise

    def logging_info(self, message_type, payload=None, publish_message=None, response_details=None):
        try:
            final_log = self.get_log_values(self.event, self.context, 'INFO', message_type, payload, publish_message, response_details)
            self.log_info(json.dumps(final_log))
        except Exception as err:
            self.log_error('Error while logging final info ' + str(err))
            raise

    def get_correlation_id(self):

        if self.check_correlation_in_header():
            return self.event['params']['header']['X-Correlation-ID']

        if "correlationId" in self.event:
            self.correlation_id = self.event["correlationId"]
            return self.correlation_id

        body_inpayload = json.loads(self.event['body'])
        if 'Message' in body_inpayload:
            message_inpayload = json.loads(body_inpayload['Message'])
            if "meta-data" in message_inpayload and "event-id" in message_inpayload["meta-data"]:
                return message_inpayload["meta-data"]['event-id']

        if "messageAttributes" in self.event and "correlation_id" in self.event['messageAttributes']:
            correlation_id = self.event['messageAttributes']['correlation_id']
            return correlation_id['stringValue']

        if "requestContext" in self.event and "requestId" in self.event['requestContext']:
            self.correlation_id = self.event['requestContext']["requestId"]
            return self.correlation_id

        self.correlation_id = uuid4()
        return str(self.correlation_id)


    def check_correlation_in_header(self):
        if 'params' in self.event and 'header' in self.event['params'] and 'X-Correlation-ID' in self.event['params']['header']:
            return True
        return False
