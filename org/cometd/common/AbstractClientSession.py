def addExtension():
'''public void addExtension(final ClientSession.Extension extension)
'''
pass
def removeExtension():
'''public void removeExtension(final ClientSession.Extension extension)
'''
pass
def getChannel():
'''public ClientSessionChannel getChannel(final String channelId)
'''
pass
def startBatch():
'''public void startBatch()
'''
pass
def endBatch():
'''public boolean endBatch()
'''
pass
def batch():
'''public void batch(final Runnable batch)
'''
pass
def getAttribute():
'''public Object getAttribute(final String name)
public Object getAttribute(final String name)
'''
pass
def getAttributeNames():
'''public Set<String> getAttributeNames()
public Set<String> getAttributeNames()
'''
pass
def removeAttribute():
'''public Object removeAttribute(final String name)
public Object removeAttribute(final String name)
'''
pass
def setAttribute():
'''public void setAttribute(final String name, final Object value)
public void setAttribute(final String name, final Object value)
'''
pass
def receive():
'''public void receive(final Message.Mutable message)
'''
pass
def dump():
'''public void dump(final StringBuilder b, final String indent)
'''
pass
def getChannelId():
'''public ChannelId getChannelId()
'''
pass
def addListener():
'''public void addListener(final ClientSessionChannel.ClientSessionChannelListener listener)
'''
pass
def removeListener():
'''public void removeListener(final ClientSessionChannel.ClientSessionChannelListener listener)
'''
pass
def subscribe():
'''public void subscribe(final ClientSessionChannel.MessageListener listener)
'''
pass
def unsubscribe():
'''public void unsubscribe(final ClientSessionChannel.MessageListener listener)
public void unsubscribe()
'''
pass
def release():
'''public boolean release()
'''
pass
def isReleased():
'''public boolean isReleased()
'''
pass
def getId():
'''public String getId()
'''
pass
def isDeepWild():
'''public boolean isDeepWild()
'''
pass
def isMeta():
'''public boolean isMeta()
'''
pass
def isService():
'''public boolean isService()
'''
pass
def isBroadcast():
'''public boolean isBroadcast()
'''
pass
def isWild():
'''public boolean isWild()
'''
pass
def toString():
'''public String toString()
'''
pass
def getReference():
'''public T getReference()
'''
pass
def isMarked():
'''public boolean isMarked()
'''
pass
