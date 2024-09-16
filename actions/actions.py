# actions/actions.py
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
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

class ActionAdminLogin(Action):
    def name(self) -> Text:
        return "action_admin_login"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        username = tracker.get_slot('username')
        password = tracker.get_slot('password')
        
        # In a real application, you would check these credentials against a secure database
        if username == "admin" and password == "123":
            dispatcher.utter_message(response="utter_login_successful")
            return [SlotSet("is_admin", True)]
        else:
            dispatcher.utter_message(response="utter_login_failed")
            return [SlotSet("is_admin", False)]

class ActionViewBookings(Action):
    def name(self) -> Text:
        return "action_view_bookings"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("ActionViewBookings is being executed")  # Debug print
        
        if tracker.get_slot('is_admin'):
            print("User is admin")  # Debug print
            if os.path.exists('bookings.csv'):
                print("bookings.csv exists")  # Debug print
                # Read and display all bookings from the CSV file
                with open('bookings.csv', 'r') as file:
                    reader = csv.reader(file)
                    bookings = list(reader)
                
                if bookings:
                    message = "Here are all the bookings:\n"
                    for booking in bookings:
                        message += f"Room: {booking[0]}, Date: {booking[1]}, Time: {booking[2]}, Booked on: {booking[3]}\n"
                else:
                    message = "There are no bookings yet."
            else:
                print("bookings.csv does not exist")  # Debug print
                message = "There are no bookings yet."
            
            dispatcher.utter_message(text=message)
        else:
            print("User is not admin")  # Debug print
            dispatcher.utter_message(response="utter_not_admin")
        
        return []