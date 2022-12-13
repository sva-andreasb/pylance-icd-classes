def SimpleMessageBus():
    '''public SimpleMessageBus()
    '''
def getInstance():
    '''public static SimpleMessageBus getInstance()
    '''
def registerListener():
    '''public void registerListener(final String id, final MessageHandler handler, final boolean single)
    '''
def postMessage():
    '''public void postMessage(final String msgId, final Object... args)
    '''
def removeListener():
    '''public void removeListener(final String msgId, final MessageHandler handler)
    '''
def reset():
    '''public void reset()
    '''
def getHandlers():
    '''public List<MessageHandler> getHandlers(final String id)
    '''
