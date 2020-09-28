from .__init__ import *


class ActionPredictTimeToday(Action):
    def name(self) -> Text:
        return "action_predict_time_week"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slot_city = tracker.get_slot('slot_city')
        print(slot_city)
        city = slot_city.replace(' ', '%20')
        city = normalize('NFKD', city).encode('ASCII', 'ignore').decode('ASCII')
        states_slots = tracker.get_slot('states_slots')

        lista = util.previsao_tempo_7_dias(city, states_slots)
        if(lista!=0):
            text = "Tempo para semana na cidade de {} - {} é:\n".format(slot_city, states_slots)

            for l in lista:
                text += "\n* Data   - {}\n* Tempo  - {}\n* Máxima - {}\n* Mínima - {}\n\n######".format(
                    util.format_date(l['dia']), l['tempo'], l['maxima'],
                    l['minima'])
            text += "\nEssas são as informações atuais, Lembrando que nossos dados atualizam sempre entre as 16 e 17 horas.\nObrigado por utilizar o PredictTimeBot :)"
            dispatcher.utter_message(text)

            return [SlotSet("slot_city", ""),SlotSet("states_slots", "")]
        else:
            dispatcher.utter_message("Por favor informe a Cidade e o Estado\n(Cidade - UF)")
            return [SlotSet("slot_city", ""), SlotSet("states_slots", "")]