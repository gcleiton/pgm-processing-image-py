import npyscreen
from view.home import InitialScreen
from view.process import ProcessScreen

class CreateInterface(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", InitialScreen, name="PGM Image Processing Program")
        self.addForm("PROCESSING", ProcessScreen, name="Processing Image...")