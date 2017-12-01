# -*- encoding: UTF-8 -*-

import pyautogui

ubicazioni = ["MECTRON", "ICAR", "IAAW0205", "IAARMDR1", "IAAH0105", "IAAH0104",
                "IAAH0103", "IAAH0102", "IAAH0101", ]

collocazioni_mectron = ["01 - R.M.", "02 - M.P.", "03 - M.P.SITE", "04 - W.I.",
                ]

class Setup(object):
    def __init__(self):
        pyautogui.PAUSE = 1
        pyautogui.FAILSAFE = True
        self.screen_width, self.screen_height = pyautogui.size()
        print "ok init setup"


class Estrazione(object):
    def __init__(self, dataset):
        self.calcolo_giacenze_screen_position = (95, 78,)
        self.ubicazione, self.data, self.collocazione = dataset
        print self.ubicazione, self.data, self.collocazione

    def compiler(self):
        pyautogui.typewrite(["tab", "tab"]) # nr documento compilato
        pyautogui.typewrite("AAA")
        pyautogui.typewrite(["tab", "tab", "tab", "tab", "tab",
                            "tab", "tab", "tab", "tab", "tab",
                            "tab"])
        pyautogui.typewrite(self.ubicazione)
        pyautogui.typewrite(["tab", "tab"])
        pyautogui.typewrite(self.data)
        pyautogui.typewrite(["tab", "tab"])
        pyautogui.typewrite(self.collocazione)

    def get_screenshot(self):
        image = pyautogui.screenshot()

    def locate_on_screen(self, path):
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(path)))


dataset = ("MECTRON", "01/01/2016"+chr(46)*2"30/11/2017", "01 - R"+chr(46)"M"+chr(46),)
start = Setup()
go = Estrazione(dataset)
go.locate_on_screen('giac_focus.png')
go.compiler()
