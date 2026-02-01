# name=Play/Stop Controller

import transport


def OnMidiMsg(event):
    if event.data2 > 0:  # кнопка нажата
        if transport.isPlaying():
            transport.stop()
        else:
            transport.start()
        event.handled = True
