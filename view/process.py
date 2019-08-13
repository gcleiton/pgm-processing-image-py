import npyscreen
from model.model import init

class ProcessScreen(npyscreen.ActionForm):
    def activate(self):
        self.edit()

    def create(self):
        self.getDirFile = self.add(npyscreen.TitleFixedText, name="Selected Directory: ")
        self.getOption = self.add(npyscreen.TitleFixedText, name="Selected Transformation: ")
        self.add(npyscreen.FixedText, value=" ")
        self.add(npyscreen.FixedText, value="Press OK to start processing, or Cancel to back.")

    def getAbrevOption(self):
        option = self.getOption.value
        if option == "Rotate 90° Degrees to Right":
            return "r90r"
        elif option == "Rotate 90° Degrees to Left":
            return "r90l"
        elif option == "Rotate 180° Degrees":
            return "r180"
        elif option == "Flip Vertically":
            return "fv"
        elif option == "Flip Horizontally":
            return "fh"
        elif option == "Apply Mean Filter":
            return "af"
        elif option == "Apply Median Filter":
            return "mf"

    def on_ok(self):
        textProcImg = ( "The process is fast, wait a little longer.\n"
                        "Processing image...")

        npyscreen.notify_wait(textProcImg, title = "PGM Image Processing")
        init(self.getDirFile.value, self.getAbrevOption())
        self.parentApp.switchForm(None)
    
    def on_cancel(self):
        self.parentApp.switchForm("MAIN")