MESSAGE_GROUP = "String  \"instantmessaging\""
IM_SERVER_HOST_MX_PROPERTY = "String  \"mxe.imi.serverhostname\""
def userStatusChanged():
    '''returns None\n\n
    userStatusChanged(final IMUserStatusEvent userStatusEvent)\n
    '''
def isUserAvailable():
    '''returns boolean\n\n
    isUserAvailable(final String userId)\n
    '''
def chatClosed():
    '''returns None\n\n
    chatClosed(final String sessionId)\n
    '''
def valueBound():
    '''returns None\n\n
    valueBound(final HttpSessionBindingEvent arg0)\n
    '''
def valueUnbound():
    '''returns None\n\n
    valueUnbound(final HttpSessionBindingEvent arg0)\n
    '''
def serverConnected():
    '''returns None\n\n
    serverConnected(final MXEvent evt)\n
    '''
def serverConnectionError():
    '''returns None\n\n
    serverConnectionError(final MXEvent evt)\n
    '''
def serverDisconnected():
    '''returns None\n\n
    serverDisconnected(final MXEvent evt)\n
    '''
def resetActivityFlag():
    '''returns None\n\n
    resetActivityFlag()\n
    '''
