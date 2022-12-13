def TelnetClient():
'''public TelnetClient()
public TelnetClient(final String termtype)
'''
pass
def disconnect():
'''public void disconnect()
'''
pass
def getOutputStream():
'''public OutputStream getOutputStream()
'''
pass
def getInputStream():
'''public InputStream getInputStream()
'''
pass
def getLocalOptionState():
'''public boolean getLocalOptionState(final int option)
'''
pass
def getRemoteOptionState():
'''public boolean getRemoteOptionState(final int option)
'''
pass
def sendAYT():
'''public boolean sendAYT(final long timeout)
'''
pass
def addOptionHandler():
'''public void addOptionHandler(final TelnetOptionHandler opthand)
'''
pass
def deleteOptionHandler():
'''public void deleteOptionHandler(final int optcode)
'''
pass
def registerSpyStream():
'''public void registerSpyStream(final OutputStream spystream)
'''
pass
def stopSpyStream():
'''public void stopSpyStream()
'''
pass
def registerNotifHandler():
'''public void registerNotifHandler(final TelnetNotificationHandler notifhand)
'''
pass
def unregisterNotifHandler():
'''public void unregisterNotifHandler()
'''
pass
def setReaderThread():
'''public void setReaderThread(final boolean flag)
'''
pass
def getReaderThread():
'''public boolean getReaderThread()
'''
pass
