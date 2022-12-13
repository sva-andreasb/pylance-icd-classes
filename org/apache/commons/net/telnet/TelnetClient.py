def TelnetClient():
    '''public TelnetClient()
    public TelnetClient(final String termtype)
    '''
def disconnect():
    '''public void disconnect()
    '''
def getOutputStream():
    '''public OutputStream getOutputStream()
    '''
def getInputStream():
    '''public InputStream getInputStream()
    '''
def getLocalOptionState():
    '''public boolean getLocalOptionState(final int option)
    '''
def getRemoteOptionState():
    '''public boolean getRemoteOptionState(final int option)
    '''
def sendAYT():
    '''public boolean sendAYT(final long timeout)
    '''
def addOptionHandler():
    '''public void addOptionHandler(final TelnetOptionHandler opthand)
    '''
def deleteOptionHandler():
    '''public void deleteOptionHandler(final int optcode)
    '''
def registerSpyStream():
    '''public void registerSpyStream(final OutputStream spystream)
    '''
def stopSpyStream():
    '''public void stopSpyStream()
    '''
def registerNotifHandler():
    '''public void registerNotifHandler(final TelnetNotificationHandler notifhand)
    '''
def unregisterNotifHandler():
    '''public void unregisterNotifHandler()
    '''
def setReaderThread():
    '''public void setReaderThread(final boolean flag)
    '''
def getReaderThread():
    '''public boolean getReaderThread()
    '''
