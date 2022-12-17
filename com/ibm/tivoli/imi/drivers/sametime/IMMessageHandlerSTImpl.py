def ():
    '''returns IMMessageHandlerSTImpl\n\n
    (final IMSessionSTImpl session, final InstantMessagingService imService, final IMUser imPartner, final STUser stPartner)\n
    '''
def addListener():
    '''returns None\n\n
    addListener(final IMMessageListener imMessageListener)\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener(final IMMessageListener imMessageListener)\n
    '''
def removeAllListeners():
    '''returns None\n\n
    removeAllListeners()\n
    '''
def imReceived():
    '''returns None\n\n
    imReceived(final ImEvent imEvent)\n
    '''
def sendMessage():
    '''returns String\n\n
    sendMessage(final String s)\n
    '''
def imOpened():
    '''returns None\n\n
    imOpened(final ImEvent imEvent)\n
    '''
def openImFailed():
    '''returns None\n\n
    openImFailed(final ImEvent imEvent)\n
    '''
def textReceived():
    '''returns None\n\n
    textReceived(final ImEvent imEvent)\n
    '''
def dataReceived():
    '''returns None\n\n
    dataReceived(final ImEvent imEvent)\n
    '''
def closeConversation():
    '''returns None\n\n
    closeConversation()\n
    '''
def imClosed():
    '''returns None\n\n
    imClosed(final ImEvent imEvent)\n
    '''
def isOpened():
    '''returns boolean\n\n
    isOpened()\n
    '''
