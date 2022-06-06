import PySimpleGUI as sg
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib.image as mpim
import shutil

s = HTMLSession()

sg.theme('Topanga')

MenuLayout = [
             [sg.Text('This is a simple weather gui')],
             [sg.Button('Search')],
             [sg.Button('Quit')]             
]

window = sg.Window('Weather', MenuLayout, size=(400,200))

while True:             
    event, values = window.read()
    if event == 'Search':
        city= sg.popup_get_text('Enter a city: ')
        url = f'https://www.google.com/search?q=weather+{city}'
        r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.27'})
        temp = r.html.find('span#wob_tm',first=True).text   #if first = true it doesnt return in list form
        unit = r.html.find('div.vk_bk.wob-unit span.wob_t',first=True).text # the first string returns a list c c f f but when we specify span.wob_t it returns what we want
        description = r.html.find('div.VQF4g', first=True).find('span#wob_dc',first= True).text

        # the code above gets weather
        
        sg.popup(city + ": " + temp + " " + unit + " " + description)
    elif event in (sg.WIN_CLOSED, 'Quit'):
        break

window.close()