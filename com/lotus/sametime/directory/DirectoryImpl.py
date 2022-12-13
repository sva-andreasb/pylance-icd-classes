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
def DirectoryImpl():
'''public DirectoryImpl(final STSession stSession)
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
def processSTEvent():
'''public void processSTEvent(final STEvent stEvent)
'''
pass
def channelOpened():
'''public void channelOpened(final ChannelEvent channelEvent)
'''
pass
def channelOpenFailed():
'''public void channelOpenFailed(final ChannelEvent channelEvent)
'''
pass
def channelClosed():
'''public void channelClosed(final ChannelEvent channelEvent)
'''
pass
def channelMsgReceived():
'''public void channelMsgReceived(final ChannelEvent channelEvent)
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
def loggedOut():
'''public void loggedOut(final LoginEvent loginEvent)
'''
pass
