# Flashcards
A toy project

This is a toy project for me to play around with scrapy and kivy.

In this project: 

I used scrapy to extract all of the acronyms and their meaning used for Security+ exam. (From http://getcertifiedgetahead.com/index.php/security/security-acronyms/). I then stored the results in a json file.

I took advantage of the kivy language and wrote a python program to immitate flashcards: 
For each card, I first show an acronym, then give user the option to choose 'Show Definition'; 
For each card, user has to choose between 'know' and 'don't know'; 
For each card chosen 'don't know', card will be added to list; 
When finished with all cards, list of 'don't know's will be exported to a json file named after time of completion; 
User can change program to review the exported 'don't know' lists.
