# actions/actions.py
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import csv

class ActionStoreData(Action):

    def name(self) -> Text:
        return "action_store_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the current slot values
        name = tracker.get_slot('name')

        # Check if both name and email are provided
        if name :
            # Store both name and email in CSV
            with open('user_data.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([name])
            
            dispatcher.utter_message(text=f"Data stored: Name - {name}")

        else:
            # If neither name nor email is provided
            dispatcher.utter_message(text="I need either your name or email to store your data.")

        return []
