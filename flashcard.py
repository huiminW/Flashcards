from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

import json
import time
from random import shuffle


class FlashCards(BoxLayout):
    def show_card(self):
        if self.cardlist == []:
            self.show_result()
            return
        self.card = self.cardlist.pop()


        label1 = self.ids['label1']
        label1.text = str(self.card['acronym'])

        label2 = self.ids['label2']
        label2.text = ''

    def show_image(self):
        label2 = self.ids['label2']
        term_position = self.card['term'].find('.')
        label2.text = '[i][b]' + self.card['term'][:term_position] + '[/b][/i] \n' + self.card['term'][term_position+2:]

    def show_card1(self):
        self.know_list.append(self.card)
        self.show_card()

    def show_card2(self):
        self.dontknow_list.append(self.card)
        self.show_card()

    def show_result(self):
        print('Need to study:')
        print(self.dontknow_list)
        t = time.localtime(time.time())
        timestamp = str(t.tm_mon)+str(t.tm_mday)+str(t.tm_hour)+str(t.tm_min)
        with open('%s.json'%timestamp, 'w') as recycle_card_pool:
            json.dump(self.dontknow_list, recycle_card_pool)
        exit()

class FlashCardApp(App):
    def build(self):
        f = FlashCards()
        with open('cards.json', 'r') as card_pool:
            f.cardlist = json.load(card_pool)
        shuffle(f.cardlist)
        print(len(f.cardlist))
        f.show_card()
        f.know_list = []
        f.dontknow_list = []
        return f

if __name__ == '__main__':
    FlashCardApp().run()