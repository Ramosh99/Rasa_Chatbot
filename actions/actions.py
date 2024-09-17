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
        if username == "admin" and password == "password123":
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

        csv_file_path = "bookings.csv"  

        try:
            with open(csv_file_path, 'r') as file:
                csv_reader = csv.reader(file)
                headers = next(csv_reader)  # Read the header row
                
                # Create a formatted string for the headers
                header_str = " | ".join(headers)
                dispatcher.utter_message(text=f"CSV Headers: {header_str}")
                
                # Read and display each row
                for row in csv_reader:
                    row_str = " | ".join(row)
                    dispatcher.utter_message(text=f"Row: {row_str}")
                
            dispatcher.utter_message(text="All CSV data has been displayed.")
        except FileNotFoundError:
            dispatcher.utter_message(text=f"Error: CSV file not found at {csv_file_path}")
        except Exception as e:
            dispatcher.utter_message(text=f"An error occurred: {str(e)}")

        return []

class ActionDisplayCSVData(Action):
    def name(self) -> Text:
        return "action_display_csv_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        csv_file_path = "bookings.csv"  

        try:
            with open(csv_file_path, 'r') as file:
                csv_reader = csv.reader(file)
                headers = next(csv_reader)  # Read the header row
                
                # Create a formatted string for the headers
                header_str = " | ".join(headers)
                dispatcher.utter_message(text=f"CSV Headers: {header_str}")
                
                # Read and display each row
                for row in csv_reader:
                    row_str = " | ".join(row)
                    dispatcher.utter_message(text=f"Row: {row_str}")
                
            dispatcher.utter_message(text="All CSV data has been displayed.")
        except FileNotFoundError:
            dispatcher.utter_message(text=f"Error: CSV file not found at {csv_file_path}")
        except Exception as e:
            dispatcher.utter_message(text=f"An error occurred: {str(e)}")

        return []