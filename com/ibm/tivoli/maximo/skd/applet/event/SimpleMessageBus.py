def SimpleMessageBus():
'''public SimpleMessageBus()
'''
pass
def getInstance():
'''public static SimpleMessageBus getInstance()
'''
pass
def registerListener():
'''public void registerListener(final String id, final MessageHandler handler, final boolean single)
'''
pass
def postMessage():
'''public void postMessage(final String msgId, final Object... args)
'''
pass
def removeListener():
'''public void removeListener(final String msgId, final MessageHandler handler)
'''
pass
def reset():
'''public void reset()
'''
pass
def getHandlers():
'''public List<MessageHandler> getHandlers(final String id)
'''
pass
