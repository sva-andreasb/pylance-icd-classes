def ():
    '''returns TelnetClient\n\n
    ()\n
    (final String termtype)\n
    '''
def disconnect():
    '''returns None\n\n
    disconnect()\n
    '''
def getOutputStream():
    '''returns OutputStream\n\n
    getOutputStream()\n
    '''
def getInputStream():
    '''returns InputStream\n\n
    getInputStream()\n
    '''
def getLocalOptionState():
    '''returns boolean\n\n
    getLocalOptionState(final int option)\n
    '''
def getRemoteOptionState():
    '''returns boolean\n\n
    getRemoteOptionState(final int option)\n
    '''
def sendAYT():
    '''returns boolean\n\n
    sendAYT(final long timeout)\n
    '''
def addOptionHandler():
    '''returns None\n\n
    addOptionHandler(final TelnetOptionHandler opthand)\n
    '''
def deleteOptionHandler():
    '''returns None\n\n
    deleteOptionHandler(final int optcode)\n
    '''
def registerSpyStream():
    '''returns None\n\n
    registerSpyStream(final OutputStream spystream)\n
    '''
def stopSpyStream():
    '''returns None\n\n
    stopSpyStream()\n
    '''
def registerNotifHandler():
    '''returns None\n\n
    registerNotifHandler(final TelnetNotificationHandler notifhand)\n
    '''
def unregisterNotifHandler():
    '''returns None\n\n
    unregisterNotifHandler()\n
    '''
def setReaderThread():
    '''returns None\n\n
    setReaderThread(final boolean flag)\n
    '''
def getReaderThread():
    '''returns boolean\n\n
    getReaderThread()\n
    '''
