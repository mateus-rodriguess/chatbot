# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions.pln_request import request_pln


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_feed_back"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data_message = {}
        message = tracker.latest_message['text']

        data_message["message"] = message
        data_message["save"] = True
        data_message["translate"] = True
        data_message["user"] = "whatsapp"
        request_pln(data_message)
        dispatcher.utter_message(text="Obrigado pelo Feedback")
        return []
