from direct.showbase.ShowBase import ShowBase
from panda3d.core import Camera

class tt_webview(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        base.oobe()
        camera.hide()
        self.loadModel()
    
    def loadModel(self):
        model = loader.loadModel('phase_4/models/minigames/apple.bam')
        model.reparentTo(render)

tt_webview()

base.run()