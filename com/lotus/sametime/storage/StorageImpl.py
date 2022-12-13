VPCONFIG_STORAGE_GET = "short  4"
VPCONFIG_STORAGE_ONGET = "short  5"
VPCONFIG_STORAGE_SET = "short  6"
VPCONFIG_STORAGE_ONSET = "short  7"
ST_OTM_STORAGE_SUBSCRIBE = "short  -32767"
ST_OTM_STORAGE_UNSUBSCRIBE = "short  -32766"
ST_OTM_STORAGE_CHANGED = "short  -32765"
def StorageImpl():
    '''    public StorageImpl(final STSession stSession)
    '''
def start():
    '''    public void start()
    '''
def stop():
    '''    public void stop()
    '''
def componentLoaded():
    '''    public void componentLoaded(final STCompApi stCompApi)
    '''
def channelOpened():
    '''    public void channelOpened(final ChannelEvent channelEvent)
    '''
def channelMsgReceived():
    '''    public void channelMsgReceived(final ChannelEvent channelEvent)
    '''
def channelClosed():
    '''    public void channelClosed(final ChannelEvent channelEvent)
    '''
def channelOpenFailed():
    '''    public void channelOpenFailed(final ChannelEvent channelEvent)
    '''
def loggedOut():
    '''    public void loggedOut(final LoginEvent loginEvent)
    '''
def toString():
    '''    public String toString()
    '''
def checkTimeout():
    '''    public void checkTimeout(final int n)
    '''
def set():
    '''    public void set(final Integer n, final Vector vector, final STUser stUser)
    '''
def get():
    '''    public void get(final Integer n, final Vector vector, final STUser stUser)
    '''
def processSTEvent():
    '''    public void processSTEvent(final STEvent stEvent)
    '''
def serviceAvailable():
    '''    public void serviceAvailable(final ServiceEvent serviceEvent)
    '''
def loggedIn():
    '''    public void loggedIn(final LoginEvent loginEvent)
    '''
def otmRecieved():
    '''    public void otmRecieved(final OTMEvent otmEvent)
    '''
def sendOTMDenied():
    '''    public void sendOTMDenied(final OTMEvent otmEvent)
    '''
