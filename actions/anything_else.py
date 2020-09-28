from .__init__ import *

class ActionAnythingElse(Action):
    def name(self) -> Text:
       return "action_anything_else"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        mensagem = "Algo mais em que posso te ajudar brother?"
        dispatcher.utter_message(text=mensagem,buttons=[{"title": "Sim", "payload": "/affirmation"},
                                                        {"title": "Não", "payload": "/denial"}])
        return []