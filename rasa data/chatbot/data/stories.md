## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## help path
* help
  - utter_help

* send_name
  - utter_send_name

* send_number
  - utter_send_number

* send_address
  - utter_send_address

* send_animal_name
  - utter_send_animal_name

* send_animal_symptoms
  - utter_send_animal_symptoms

* out_of_scope
  - utter_out_of_scope