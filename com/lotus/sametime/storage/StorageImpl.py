VPCONFIG_STORAGE_GET = "short  4"
VPCONFIG_STORAGE_ONGET = "short  5"
VPCONFIG_STORAGE_SET = "short  6"
VPCONFIG_STORAGE_ONSET = "short  7"
ST_OTM_STORAGE_SUBSCRIBE = "short  -32767"
ST_OTM_STORAGE_UNSUBSCRIBE = "short  -32766"
ST_OTM_STORAGE_CHANGED = "short  -32765"
def ():
    '''returns StorageImpl\n\n
    (final STSession stSession)\n
    '''
def start():
    '''returns None\n\n
    start()\n
    '''
def stop():
    '''returns None\n\n
    stop()\n
    '''
def componentLoaded():
    '''returns None\n\n
    componentLoaded(final STCompApi stCompApi)\n
    '''
def channelOpened():
    '''returns None\n\n
    channelOpened(final ChannelEvent channelEvent)\n
    '''
def channelMsgReceived():
    '''returns None\n\n
    channelMsgReceived(final ChannelEvent channelEvent)\n
    '''
def channelClosed():
    '''returns None\n\n
    channelClosed(final ChannelEvent channelEvent)\n
    '''
def channelOpenFailed():
    '''returns None\n\n
    channelOpenFailed(final ChannelEvent channelEvent)\n
    '''
def loggedOut():
    '''returns None\n\n
    loggedOut(final LoginEvent loginEvent)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def checkTimeout():
    '''returns None\n\n
    checkTimeout(final int n)\n
    '''
def set():
    '''returns None\n\n
    set(final Integer n, final Vector vector, final STUser stUser)\n
    '''
def get():
    '''returns None\n\n
    get(final Integer n, final Vector vector, final STUser stUser)\n
    '''
def processSTEvent():
    '''returns None\n\n
    processSTEvent(final STEvent stEvent)\n
    '''
def serviceAvailable():
    '''returns None\n\n
    serviceAvailable(final ServiceEvent serviceEvent)\n
    '''
def loggedIn():
    '''returns None\n\n
    loggedIn(final LoginEvent loginEvent)\n
    '''
def otmRecieved():
    '''returns None\n\n
    otmRecieved(final OTMEvent otmEvent)\n
    '''
def sendOTMDenied():
    '''returns None\n\n
    sendOTMDenied(final OTMEvent otmEvent)\n
    '''
