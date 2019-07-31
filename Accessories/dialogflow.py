'''
<iframe
    allow="microphone;"
    width="350"
    height="430"
    src="https://console.dialogflow.com/api-client/demo/embedded/335c0e76-c71d-46b7-9600-f258b2049ef7">
</iframe>


<p src="https://console.dialogflow.com/api-client/demo/embedded/335c0e76-c71d-46b7-9600-f258b2049ef7"></p>
'''

import dialogflow_v2 as dialogflow
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=<your google credential json path>

def detect_intent_texts(project_id, session_id, text, language_code):
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(project_id, session_id)

        if text:
            text_input = dialogflow.types.TextInput(
                text=text, language_code=language_code)
            query_input = dialogflow.types.QueryInput(text=text_input)
            response = session_client.detect_intent(
                session=session, query_input=query_input)

            return response.query_result.fulfillment_text


print(detect_intent_texts('lustrous-jet-246503','unique','i am sad?','en'))
