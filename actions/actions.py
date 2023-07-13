# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionShowBalance(Action):
    def name(self) -> Text:
        return "action_show_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        account_number = tracker.get_slot("account_number")
        name = tracker.get_slot("name")

        balance = 1000 

        response = f"Dear {name}, your account {account_number} has a balance of Rs. {balance}."

        dispatcher.utter_message(text=response)
        return []

class ActionShowTransactionHistory(Action):
    def name(self) -> Text:
        return "action_show_transaction_history"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        account_number = tracker.get_slot("account_number")

        transactions = ["Transaction 1", "Transaction 2", "Transaction 3"] 

        response = f"Here are your recent transactions for account {account_number}: {', '.join(transactions)}."

        dispatcher.utter_message(text=response)
        return []

