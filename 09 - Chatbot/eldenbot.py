import os
from google.cloud import dialogflow_v2 as dialogflow


def get_response(project_id, session_id, text):
    """
    Gets the API response from dialogflow and returns it
    as a dictionary
    """
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=text, language_code='en-US')
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(session=session, query_input=query_input)

    response_dict = {
        'query_text': response.query_result.query_text,
        'speech_recognition_confidence': response.query_result.speech_recognition_confidence,
        'action': response.query_result.action,
        'all_required_params_present': response.query_result.all_required_params_present,
        'fulfillment_text': response.query_result.fulfillment_text,
        'fulfillment_messages': response.query_result.fulfillment_messages,
        'output_contexts': response.query_result.output_contexts,
        'intent': response.query_result.intent,
        'intent_detection_confidence': response.query_result.intent_detection_confidence,
        'diagnostic_info': response.query_result.diagnostic_info,
        'sentiment_analysis_result': response.query_result.sentiment_analysis_result
    }

    return response_dict


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './eldenbot-tbwr-f1e3e126e016.json'
project_id = 'eldenbot-tbwr'
session_id = '123456'

print('EldenBot: Hi! How can I help you today?')
while True:
    text = input('You: ')
    if text.upper() == 'STOP':
        print('EldenBot: Goodbye!')
        break

    response_dict = get_response(project_id, session_id, text)
    response_text = response_dict['fulfillment_text']
    print('EldenBot: ' + response_text)
