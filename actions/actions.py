# actions/actions.py
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import csv
from datetime import datetime

class ActionSaveBooking(Action):
    def name(self) -> Text:
        return "action_save_booking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        room_type = tracker.get_slot('room_type')
        date = tracker.get_slot('date')
        time = tracker.get_slot('time')
        
        # Save the booking information to a CSV file
        with open('bookings.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([room_type, date, time, datetime.now()])
        
        return []