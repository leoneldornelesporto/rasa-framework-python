from .__init__ import *

class ActionFarewell(Action):
    def name(self) -> Text:
        return "action_farewell"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Obrigado por utilizar o PredictTimeBot, tenha um bom dia :)"
                                 "\nCasos queria saber a previsão do tempo para outra cidade é só conversar comigo."
                                 "Até mais.")
        return []
