# Powered by Kl1nge5
# 2021/11/25
# 夜好深了

import core
import ScreenShot
import tkinter

APP_ID = ''
APP_KEY = ''
core.Config.setAppInfo(core.Config, APP_ID, APP_KEY)
requestSender = core.RequestSender()

shot = ScreenShot.Shot()
shot.setScale(1.5)
shot.start()
img = shot.getImage()
if img is not None:
    img.save('__temp.png')
    print(requestSender.getResult('__temp.png'))
