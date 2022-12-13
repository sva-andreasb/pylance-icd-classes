VPCONFIG_STORAGE_GET = "short  4"
VPCONFIG_STORAGE_ONGET = "short  5"
VPCONFIG_STORAGE_SET = "short  6"
VPCONFIG_STORAGE_ONSET = "short  7"
ST_OTM_STORAGE_SUBSCRIBE = "short  -32767"
ST_OTM_STORAGE_UNSUBSCRIBE = "short  -32766"
ST_OTM_STORAGE_CHANGED = "short  -32765"
def StorageImpl():
'''public StorageImpl(final STSession stSession)
'''
pass
def start():
'''public void start()
'''
pass
def stop():
'''public void stop()
'''
pass
def componentLoaded():
'''public void componentLoaded(final STCompApi stCompApi)
'''
pass
def channelOpened():
'''public void channelOpened(final ChannelEvent channelEvent)
'''
pass
def channelMsgReceived():
'''public void channelMsgReceived(final ChannelEvent channelEvent)
'''
pass
def channelClosed():
'''public void channelClosed(final ChannelEvent channelEvent)
'''
pass
def channelOpenFailed():
'''public void channelOpenFailed(final ChannelEvent channelEvent)
'''
pass
def loggedOut():
'''public void loggedOut(final LoginEvent loginEvent)
'''
pass
def toString():
'''public String toString()
'''
pass
def checkTimeout():
'''public void checkTimeout(final int n)
'''
pass
def set():
'''public void set(final Integer n, final Vector vector, final STUser stUser)
'''
pass
def get():
'''public void get(final Integer n, final Vector vector, final STUser stUser)
'''
pass
def processSTEvent():
'''public void processSTEvent(final STEvent stEvent)
'''
pass
def serviceAvailable():
'''public void serviceAvailable(final ServiceEvent serviceEvent)
'''
pass
def loggedIn():
'''public void loggedIn(final LoginEvent loginEvent)
'''
pass
def otmRecieved():
'''public void otmRecieved(final OTMEvent otmEvent)
'''
pass
def sendOTMDenied():
'''public void sendOTMDenied(final OTMEvent otmEvent)
'''
pass
