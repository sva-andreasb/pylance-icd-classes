def subscribe():
    '''public boolean subscribe(final ServerSession session)
    '''
def unsubscribe():
    '''public boolean unsubscribe(final ServerSession session)
    '''
def getSubscribers():
    '''public Set<ServerSession> getSubscribers()
    '''
def isBroadcast():
    '''public boolean isBroadcast()
    '''
def isDeepWild():
    '''public boolean isDeepWild()
    '''
def isLazy():
    '''public boolean isLazy()
    '''
def isPersistent():
    '''public boolean isPersistent()
    '''
def isWild():
    '''public boolean isWild()
    '''
def setLazy():
    '''public void setLazy(final boolean lazy)
    '''
def setPersistent():
    '''public void setPersistent(final boolean persistent)
    '''
def addListener():
    '''public void addListener(final ServerChannel.ServerChannelListener listener)
    '''
def removeListener():
    '''public void removeListener(final ServerChannel.ServerChannelListener listener)
    '''
def getChannelId():
    '''public ChannelId getChannelId()
    '''
def getId():
    '''public String getId()
    '''
def isMeta():
    '''public boolean isMeta()
    '''
def isService():
    '''public boolean isService()
    '''
def publish():
    '''public void publish(final Session from, final ServerMessage.Mutable mutable)
    public void publish(final Session from, final Object data, final String id)
    '''
def remove():
    '''public void remove()
    '''
def setAttribute():
    '''public void setAttribute(final String name, final Object value)
    '''
def getAttribute():
    '''public Object getAttribute(final String name)
    '''
def getAttributeNames():
    '''public Set<String> getAttributeNames()
    '''
def removeAttribute():
    '''public Object removeAttribute(final String name)
    '''
def addAuthorizer():
    '''public void addAuthorizer(final Authorizer authorizer)
    '''
def removeAuthorizer():
    '''public void removeAuthorizer(final Authorizer authorizer)
    '''
def getAuthorizers():
    '''public List<Authorizer> getAuthorizers()
    '''
def toString():
    '''public String toString()
    '''
