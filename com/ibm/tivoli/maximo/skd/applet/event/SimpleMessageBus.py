def ():
    '''returns SimpleMessageBus\n\n
    ()\n
    '''
def registerListener():
    '''returns None\n\n
    registerListener(final String id, final MessageHandler handler, final boolean single)\n
    '''
def postMessage():
    '''returns None\n\n
    postMessage(final String msgId, final Object... args)\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener(final String msgId, final MessageHandler handler)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def getHandlers():
    '''returns List<MessageHandler>\n\n
    getHandlers(final String id)\n
    '''
