def subscribe():
'''public boolean subscribe(final ServerSession session)
'''
pass
def unsubscribe():
'''public boolean unsubscribe(final ServerSession session)
'''
pass
def getSubscribers():
'''public Set<ServerSession> getSubscribers()
'''
pass
def isBroadcast():
'''public boolean isBroadcast()
'''
pass
def isDeepWild():
'''public boolean isDeepWild()
'''
pass
def isLazy():
'''public boolean isLazy()
'''
pass
def isPersistent():
'''public boolean isPersistent()
'''
pass
def isWild():
'''public boolean isWild()
'''
pass
def setLazy():
'''public void setLazy(final boolean lazy)
'''
pass
def setPersistent():
'''public void setPersistent(final boolean persistent)
'''
pass
def addListener():
'''public void addListener(final ServerChannel.ServerChannelListener listener)
'''
pass
def removeListener():
'''public void removeListener(final ServerChannel.ServerChannelListener listener)
'''
pass
def getChannelId():
'''public ChannelId getChannelId()
'''
pass
def getId():
'''public String getId()
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
def publish():
'''public void publish(final Session from, final ServerMessage.Mutable mutable)
public void publish(final Session from, final Object data, final String id)
'''
pass
def remove():
'''public void remove()
'''
pass
def setAttribute():
'''public void setAttribute(final String name, final Object value)
'''
pass
def getAttribute():
'''public Object getAttribute(final String name)
'''
pass
def getAttributeNames():
'''public Set<String> getAttributeNames()
'''
pass
def removeAttribute():
'''public Object removeAttribute(final String name)
'''
pass
def addAuthorizer():
'''public void addAuthorizer(final Authorizer authorizer)
'''
pass
def removeAuthorizer():
'''public void removeAuthorizer(final Authorizer authorizer)
'''
pass
def getAuthorizers():
'''public List<Authorizer> getAuthorizers()
'''
pass
def toString():
'''public String toString()
'''
pass
