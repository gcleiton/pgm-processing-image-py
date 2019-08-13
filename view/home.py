import npyscreen
import sys

class InitialScreen(npyscreen.ActionForm):
    def activate(self):
        self.edit()

    def create(self):
        
        textIntro = ["Welcome to the user interface.",
                    "If you have any questions about using the program, see the documentation in https://github.com/gcleiton/pgm-processing-image-py",
                    "We hope your experience is the best you can!"]

        textAboutUs = ( "Initially developed for academic purposes, the program" 
                    "offers a range of operations over any PGM (Portable "
                    "Gray Map) format image, provited its header is in "
                    "P2(ASCII). We hope you enjoy the service!\n"
                    "Press OK to start program, or Cancel to exit." )
        
        availableOptions = ["Rotate 90° Degrees to Right", 
                            "Rotate 90° Degrees to Left",
                            "Rotate 180° Degrees",
                            "Flip Vertically",
                            "Flip Horizontally",
                            "Apply Mean Filter",
                            "Apply Median Filter"]

        quitOrContinue = npyscreen.notify_ok_cancel(textAboutUs, title="About Us")
        if quitOrContinue == True:
            npyscreen.notify_wait("Loading...", title = "PGM Image Processing Program")
            for i in range(len(textIntro)):
                self.intro = self.add(npyscreen.FixedText, value=textIntro[i])

            self.add(npyscreen.FixedText, value=" ")
            self.fileName = self.add(npyscreen.TitleFilenameCombo, name = "Filename:", )
            self.add(npyscreen.FixedText, value=" ")
            self.options = self.add(npyscreen.TitleSelectOne, 
                                  values=availableOptions, name="What transformation do you want to do?")

        else:
            npyscreen.notify_wait("Exiting...", title = "About Us")
            exit()

    def on_ok(self):
        toProcess = self.parentApp.getForm("PROCESSING")
        try:
            toProcess.getOption.value = self.options.values[self.options.value[0]]
        except IndexError:
            print("No options select. Program closed!")
            exit()

        toProcess.getDirFile.value = self.fileName.value   
        self.parentApp.switchForm("PROCESSING")
    
    def on_cancel(self):    
        self.parentApp.switchFormPrevious()