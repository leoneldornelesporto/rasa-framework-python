from .__init__ import *

class ActionFallBack(Action):
    def name(self) -> Text:
       return "action_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        mensagem = random.choice(["Desculpe, mas não entendi sua frase.",
                                  "Opa, não entendi o que você falou.",
                                  "Repete para mim novamente?\nNão entendi :(",
                                  "Desculpe, não consegue compreender  você :/" ])
        dispatcher.utter_message(text=mensagem)
        return []