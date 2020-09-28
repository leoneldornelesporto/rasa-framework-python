## start
* start
   - action_greet
   - utter_menu

## Saudação
* greet
    - action_greet
    - utter_menu

## Menu
* menu
    - utter_menu

## Despedida
* goodbye
    - action_farewell

## agradecimento

* obrigado
    - utter_obrigado

## None

* none
    - action_fallback

## story_321_day

* busca{"today":"hoje","states":"RS"}
    - action_find_city
    - slot{"slot_city":"Pelotas"}
    - slot{"states_slots":"RS"}
    - action_predict_time_today
    - slot{"slot_city":""}
    - slot{"states_slots":""}

## story_321_week

* busca{"week":"Semana","states":"RS"}
    - action_find_city
    - slot{"slot_city":"Pelotas"}
    - slot{"states_slots":"RS"}
    - action_predict_time_week
    - slot{"slot_city":""}
    - slot{"states_slots":""}

## story_31-2_day

* busca{"today":"hoje"}
    - action_find_city
* busca{"states":"RS"}
    - action_find_city
    - slot{"slot_city":"Pelotas"}
    - slot{"states_slots":"RS"}
    - action_predict_time_today
    - slot{"slot_city":""}
    - slot{"states_slots":""}

## story_31-2_week

* busca{"week":"Semana"}
    - action_find_city
* busca{"states":"RS"}
    - action_find_city
    - slot{"slot_city":"Pelotas"}
    - slot{"states_slots":"RS"}
    - action_predict_time_week
    - slot{"slot_city":""}

## story_32-1_day
* busca{"today":"hoje","states":"RS"}
    - action_find_city
* busca{"states":"RS"}
    - action_find_city
    - slot{"slot_city":"Pelotas"}
    - slot{"states_slots":"RS"}
    - slot{"states_slots":"RS"}
    - action_predict_time_today
    - slot{"slot_city":""}
    - slot{"states_slots":""}

## story_32-1_week
* busca{"week": "semana", "states": "RS"}
    - action_find_city
* busca{"states": "RS"}
    - action_find_city
    - slot{"slot_city": "Pelotas"}
    - slot{"states_slots": "RS"}
    - action_predict_time_week
    - slot{"slot_city": ""}
    - slot{"states_slots": ""}

## story_12-3_day
* busca{"states": "RS"}
    - action_find_city
    - slot{"slot_city": "Pelotas"}
    - slot{"states_slots": "RS"}
    - utter_week_or_day
* busca{"today": "Dia de Hoje"}
    - action_predict_time_today
    - slot{"slot_city": ""}
    - slot{"states_slots": ""}

## story_12-3_week
* busca{"states": "RS"}
    - action_find_city
    - slot{"slot_city": "Pelotas"}
    - slot{"states_slots": "RS"}
    - utter_week_or_day
* busca{"week": "semana"}
    - action_predict_time_week
    - slot{"slot_city": ""}
    - slot{"states_slots": ""}

## story_3-2-1_day
* busca{"today": "Hoje"}
    - action_find_city
* busca{"states": "RS"}
    - action_find_city
* busca{"states": "RS"}
    - action_find_city
    - slot{"slot_city": "Pelotas"}
    - slot{"states_slots": "RS"}
    - action_predict_time_today
    - slot{"slot_city": ""}
    - slot{"states_slots": ""}

## story_3-2-1_week
* busca{"week": "semana"}
    - action_find_city
* busca{"states": "RS"}
    - action_find_city
* busca{"states": "RS"}
    - action_find_city
    - slot{"slot_city": "Pelotas"}
    - slot{"states_slots": "RS"}
    - action_predict_time_week
    - slot{"slot_city": ""}
    - slot{"states_slots": ""}

## story_3-1-2_day
* busca{"today": "Hoje"}
    - action_find_city
* busca
    - action_find_city
* busca{"states": "RS"}
    - action_find_city
    - slot{"slot_city": "Pelotas"}
    - slot{"states_slots": "RS"}
    - action_predict_time_today
    - slot{"slot_city": ""}
    - slot{"states_slots": ""}

## story_3-1-2_week
* busca{"week": "semana"}
    - action_find_city
* busca
    - action_find_city
* busca{"states": "RS"}
    - action_find_city
    - slot{"slot_city": "Pelotas"}
    - slot{"states_slots": "RS"}
    - action_predict_time_week
    - slot{"slot_city": ""}
    - slot{"states_slots": ""}

## story_2-1-3_day

* busca{"states": "RS"}
    - action_find_city
* busca{"states": "RS"}
    - action_find_city
    - slot{"slot_city": "Pelotas"}
    - slot{"states_slots": "RS"}
    - utter_week_or_day
* busca{"today": "Hoje"}
    - action_predict_time_today
    - slot{"slot_city": ""}
    - slot{"states_slots": ""}

## story_2-1-3_week

* busca{"states": "RS"}
    - action_find_city
* busca{"states": "RS"}
    - action_find_city
    - slot{"slot_city": "Pelotas"}
    - slot{"states_slots": "RS"}
    - utter_week_or_day
* busca{"week": "semana"}
    - action_predict_time_today
    - slot{"slot_city": ""}
    - slot{"states_slots": ""}

## story_1-2-3_day
* busca
    - action_find_city
* busca{"states": "RS"}
    - action_find_city
    - slot{"slot_city": "Pelotas"}
    - slot{"states_slots": "RS"}
    - utter_week_or_day
* busca{"today": "Hoje"}
    - action_predict_time_today
    - slot{"slot_city": ""}
    - slot{"states_slots": ""}

## story_1-2-3_week
* busca
    - action_find_city
* busca{"states": "RS"}
    - action_find_city
    - slot{"slot_city": "Pelotas"}
    - slot{"states_slots": "RS"}
    - utter_week_or_day
* busca{"week": "semana"}
    - action_predict_time_today
    - slot{"slot_city": ""}
    - slot{"states_slots": ""}

## story_quest_123_day
* busca
    - action_find_city
* busca{"states": "RS", "today": "Hoje"}
    - action_find_city
    - slot{"slot_city": "Pelotas"}
    - slot{"states_slots": "RS"}
    - action_predict_time_today
    - slot{"slot_city": ""}
    - slot{"states_slots": ""}

## story_quest_123_week
* busca
    - action_find_city
* busca{"week": "semana", "states": "RS"}
    - action_find_city
    - slot{"slot_city": "Pelotas"}
    - slot{"states_slots": "RS"}
    - action_predict_time_week
    - slot{"slot_city": ""}
    - slot{"states_slots": ""}

## story_exeption_123_day
* busca{"today": "hoje", "states": "RJ"}
    - action_find_city
    - slot{"slot_city": "Rio de Janeiro"}
    - slot{"states_slots": "RJ"}
    - action_predict_time_today
    - slot{"slot_city": ""}
    - slot{"states_slots": ""}

## story_exeption_123_week
* busca{"week": "semana", "states": "RJ"}
    - action_find_city
    - slot{"slot_city": "Rio de Janeiro"}
    - slot{"states_slots": "RJ"}
    - action_predict_time_week
    - slot{"slot_city": ""}
    - slot{"states_slots": ""}

## New Story

* goodbye
    - action_farewell
* obrigado
    - utter_obrigado

## New Story

* busca{"today":"hoje","states":"BA"}
    - action_find_city
    - slot{"slot_city":"Salvador"}
    - action_predict_time_today
    - slot{"slot_city":""}
* busca{"states":"BA"}
    - action_find_city
    - slot{"slot_city":"Salvador"}
    - utter_week_or_day
* busca{"week":"semana"}
    - action_predict_time_week
    - slot{"slot_city":""}
* goodbye
    - action_farewell
* none
    - action_fallback
* obrigado
    - utter_obrigado

## New Story

* none
    - utter_obrigado

## New Story

* greet
    - action_greet
    - utter_menu
* goodbye
    - action_farewell

## New Story

* greet
    - action_greet
    - utter_menu
* busca{"today":"hoje"}
    - action_find_city
* none
    - utter_sair

## New Story

* busca{"today":"hoje","states":"AM"}
    - action_find_city
    - slot{"slot_city":"Humaitá"}
    - action_predict_time_today
    - slot{"slot_city":""}

## New Story

* busca{"today":"hoje","states":"AM"}
    - action_find_city
    - slot{"slot_city":"Maués"}
    - action_predict_time_today
    - slot{"slot_city":""}

## New Story

* busca{"week":"semana","states":"AM"}
    - action_find_city
    - slot{"slot_city":"Maués"}
    - action_predict_time_week
    - slot{"slot_city":""}

## New Story

* busca
    - action_fallback

## New Story

* busca{"today":"hoje"}
    - action_find_city
* busca{"states":"RS"}
    - action_find_city
    - slot{"slot_city":"Pelotas"}
    - action_predict_time_today
    - slot{"slot_city":""}

## New Story

* none{"today":"hj"}
    - action_fallback
* busca{"week":"semana"}
    - action_find_city
* busca{"states":"RS"}
    - action_find_city
    - slot{"slot_city":"Pelotas"}
    - action_predict_time_week
    - slot{"slot_city":""}
* obrigado
    - utter_obrigado

## New Story

* none
    - action_fallback

## New Story

* none
    - action_fallback

## New Story

* busca{"states":"RS"}
    - action_find_city
    - utter_week_or_day
* busca{"week":"semana"}
    - action_predict_time_week
    - slot{"slot_city":""}

## New Story

* greet
    - action_greet
    - utter_menu

## New Story

* greet
    - action_greet
    - utter_menu
* busca{"week":"semana"}
    - action_find_city
* states{"states":"RJ"}
    - action_find_city
    - slot{"slot_city":"Rio de Janeiro"}
    - action_predict_time_week
    - slot{"slot_city":""}

## New Story

* busca{"today":"hoje","states":"RJ"}
    - action_find_city
    - slot{"slot_city":"Rio de Janeiro"}
    - action_predict_time_today
    - slot{"slot_city":""}

## New Story

* obrigado
    - utter_obrigado
* none
    - action_fallback

## New Story

* busca{"states":"SP"}
    - action_find_city
    - slot{"slot_city":"São Paulo"}
    - utter_week_or_day
* busca{"today":"hoje"}
    - action_predict_time_today
    - slot{"slot_city":""}

## New Story

* busca{"states":"RJ"}
    - action_find_city
    - slot{"slot_city":"Rio de Janeiro"}
    - utter_week_or_day
* busca{"week":"semana"}
    - action_predict_time_week
    - slot{"slot_city":""}

## New Story

* greet
    - action_greet
    - utter_menu
* busca{"states":"RJ"}
    - action_find_city
    - slot{"slot_city":"Rio de Janeiro"}
    - utter_week_or_day
* busca{"week":"semana"}
    - action_predict_time_week
    - slot{"slot_city":""}

## New Story

* greet
    - action_greet
    - utter_menu
* busca{"week":"semana"}
    - action_find_city
* busca{"states":"SP"}
    - action_find_city
    - slot{"slot_city":"Bauru"}
    - action_predict_time_week
    - slot{"slot_city":""}
* obrigado
    - utter_obrigado
* goodbye
    - action_farewell

## New Story

* busca{"states":"MS"}
    - action_find_city
    - slot{"slot_city":"Coxim"}
    - utter_week_or_day
* busca{"today":"hoje"}
    - action_predict_time_today
    - slot{"slot_city":""}
* obrigado
    - utter_obrigado
* goodbye
    - action_farewell

## New Story

* busca{"week":"semana","states":"MS"}
    - action_find_city
    - slot{"slot_city":"Coxim"}
    - action_predict_time_week
    - slot{"slot_city":""}
* obrigado
    - utter_obrigado
* goodbye
    - action_farewell

## New Story

* busca{"states":"MS"}
    - action_find_city
    - slot{"slot_city":"Coxim"}
    - utter_week_or_day
* busca{"week":"semana"}
    - action_predict_time_week
    - slot{"slot_city":""}

## New Story

* busca{"states":"RO"}
    - action_find_city
    - slot{"slot_city":"Ariquemes"}
    - slot{"states_slots":"RO"}
    - utter_week_or_day
* busca{"today":"hoje"}
    - action_predict_time_today
    - slot{"slot_city":""}
* obrigado
    - utter_obrigado
* goodbye
    - action_farewell

## New Story

* busca{"states":"RO"}
    - action_find_city
    - slot{"slot_city":"Cacoal"}
    - utter_week_or_day
* busca{"week":"semana"}
    - action_predict_time_week
    - slot{"slot_city":""}
* obrigado
    - utter_obrigado
* goodbye
    - action_farewell

## New Story

* busca{"states":"PR"}
    - action_find_city
    - slot{"slot_city":"Altamira"}
    - utter_week_or_day
* busca{"week":"semana"}
    - action_predict_time_week
    - slot{"slot_city":""}
