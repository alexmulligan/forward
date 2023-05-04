from typing import List
import requests
from urllib import parse

import config

url = f'https://api.telegram.org/bot{config.TOKEN}/sendMessage?chat_id={config.CHAT_ID}&text='


class Notif:
    def __init__(self, app_name, title, lines: List[str]):
        self.app_name = app_name
        self.title = title
        body = ''
        for line in lines:
            body += line + '\n'
        self.body = body

    def output_console(self):
        print("---------------------\n\n[{}]\n\n\n\t{}\n\n{}".format(
            self.app_name, self.title, self.body))

    def output_telegram(self):
        message = parse.quote(f"{self.app_name} - {self.title}\n\n{self.body}")
        res = requests.get(url+message).json()
        if config.DEBUG:
            print(f"DEBUG: res: {res}\n")

    def output_email(self):
        pass # TODO
