GET_DIRECTORIES = "short  0"
OPEN_DIRECTORY = "short  1"
CLOSE_DIRECTORY = "short  2"
GET_ENTRIES = "short  3"
NEXT_CHUNK = "int  0"
PREVIOUS_CHUNK = "int  1"
START_WITH_STRING = "int  8"
AT_FIRST_CHUNK = "int  2"
AT_LAST_CHUNK = "int  4"
ENTRY_TYPE_USER = "int  0"
ENTRY_TYPE_GROUP = "int  1"
def ():
    '''returns DirectoryImpl\n\n
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
def processSTEvent():
    '''returns None\n\n
    processSTEvent(final STEvent stEvent)\n
    '''
def channelOpened():
    '''returns None\n\n
    channelOpened(final ChannelEvent channelEvent)\n
    '''
def channelOpenFailed():
    '''returns None\n\n
    channelOpenFailed(final ChannelEvent channelEvent)\n
    '''
def channelClosed():
    '''returns None\n\n
    channelClosed(final ChannelEvent channelEvent)\n
    '''
def channelMsgReceived():
    '''returns None\n\n
    channelMsgReceived(final ChannelEvent channelEvent)\n
    '''
def serviceAvailable():
    '''returns None\n\n
    serviceAvailable(final ServiceEvent serviceEvent)\n
    '''
def loggedIn():
    '''returns None\n\n
    loggedIn(final LoginEvent loginEvent)\n
    '''
def loggedOut():
    '''returns None\n\n
    loggedOut(final LoginEvent loginEvent)\n
    '''
