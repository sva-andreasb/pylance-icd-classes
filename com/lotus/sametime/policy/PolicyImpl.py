def ():
    '''returns PolicyImpl\n\n
    (final STSession stSession)\n
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
def processSTEvent():
    '''returns None\n\n
    processSTEvent(final STEvent stEvent)\n
    '''
def loggedIn():
    '''returns None\n\n
    loggedIn(final LoginEvent loginEvent)\n
    '''
def loggedOut():
    '''returns None\n\n
    loggedOut(final LoginEvent loginEvent)\n
    '''
def serviceAvailable():
    '''returns None\n\n
    serviceAvailable(final ServiceEvent serviceEvent)\n
    '''
def start():
    '''returns None\n\n
    start()\n
    '''
def stop():
    '''returns None\n\n
    stop()\n
    '''
