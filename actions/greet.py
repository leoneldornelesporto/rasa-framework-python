from .__init__ import *
from datetime import datetime

class ActionGreet(Action):
    def name(self) -> Text:
       return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        hora_atuail= datetime.now()
        hora_em_texto = hora_atuail.strftime('%H:%M')

        tempo = ''

        if hora_em_texto >= '06:00' and hora_em_texto <= '12:00':
            tempo = 'Bom dia,'
        elif hora_em_texto > '12:00' and hora_em_texto <= '18:00':
            tempo = 'Boa tarde,'
        else:
            tempo = 'Boa noite,'

        text = "{} eu sou o Carlos estou aqui para  te enviar a previsão do tempo da semana e para o dia de hoje, para as cidades do Brasil." \
               "Lembrando que nosso dados são atualizados entre as quatorze e\ou quinze horas.".format(tempo)

        dispatcher.utter_message(text)
        return []
