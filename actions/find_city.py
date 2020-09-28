from .__init__ import *


class ActionFindCity(Action):
    def name(self) -> Text:
        return "action_find_city"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = '0'
        cityReturn = []
        slot_city = ''

        prediction = tracker.latest_message
        states_slots = util.filterEntities(prediction, 'states', 2)

        entrada = prediction.get("text")
        inputUser = entrada.lower()
        inputUser = normalize('NFKD', inputUser).encode('ASCII', 'ignore').decode('ASCII')

        for y in util.cidades:
            x = normalize('NFKD', y).encode('ASCII', 'ignore').decode('ASCII')

            if inputUser.find(x.lower()) != -1:
                cityReturn.append(y)
                print(inputUser.find(y.lower()))
        if len(cityReturn) == 1:
            city = cityReturn[0]
        if len(cityReturn) > 1:
            for y in cityReturn:
                if len(y) > len(city):
                    city = y

        if city != '0':
            slot_city = city
        else:
            if states_slots == "RJ":
                slot_city = "Rio de Janeiro"
            if states_slots == "SP":
                slot_city = "São Paulo"
            if states_slots == "TO":
                slot_city = "Tocantins"
            if states_slots == "ES":
                slot_city = "Espírito Santo"
            if states_slots == "PR":
                slot_city = "Paraná"
            if states_slots == "MT":
                slot_city = "Mato Grosso"
            if states_slots == "GO":
                slot_city = "Goiás"

        if city == '0' and states_slots != 0:
            dispatcher.utter_message("Por favor informe a Cidade e o Estado\n(Cidade - UF)")
            return []
        if city != '0' and states_slots == 0:
            dispatcher.utter_message("Por favor informe a Cidade e o Estado\n(Cidade - UF)")
            return []
        if city == '0' and states_slots == 0:
            dispatcher.utter_message(" Qual cidade você gostaria de receber as informações, porfavor envie no seguinte formato (cidade - uf)")
            return []

        print("Cidade")
        print(slot_city)

        print("\nEstado")
        print(states_slots)

        return [SlotSet("slot_city", slot_city), SlotSet("states_slots", states_slots)]
