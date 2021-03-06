# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

<<<<<<< HEAD
=======
# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

>>>>>>> 97291e0ab336883791da52e084cf13790b119bfc
from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from excel_data_store_read import DataStore, FetchData


class ActionSaveData(Action):

    def name(self) -> Text:
        return "action_save_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        DataStore(tracker.get_slot("name"),
            tracker.get_slot("number"),
            tracker.get_slot("addres"),
            tracker.get_slot("animal_name"),
            tracker.get_slot("animal_symptoms"))
        dispatcher.utter_message(text="Data Stored Successfully.")

        return []

class ActionFetchData(Action):

    def name(self) -> Text:
        return "action_fetch_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        output=FetchData(tracker.latest_message['entities'][0]['value'],
                         tracker.latest_message['entities'][1]['value'])
        dispatcher.utter_message(text="This is the data that you asked for, \n{}".format(",".join(output)))

        return []

class FormDataCollect(FormAction):
    def name(self) -> Text:
        return "Form_Info"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["name","number","addres","animal_name","animal_symptoms"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
        return {
            "name":[self.from_text()],
            "number":[self.from_entity(entity="number")],
            "addres":[self.from_text()],
            "animal_name":[self.from_text()],
            "animal_symptoms":[self.from_text()]
        }

    def submit(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        dispatcher.utter_message("Here are the information that you provided. Do you want to save it?\nName: {0},\nMobile Number: {1},\naddres: {2},\nanimal_name: {3},\nanimal_symptoms: {4}".format(
            tracker.get_slot("name"),
            tracker.get_slot("number"),
            tracker.get_slot("addres"),
            tracker.get_slot("animal_name"),
            tracker.get_slot("animal_symptoms"),

        ))
        return []
