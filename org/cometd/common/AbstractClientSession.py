def addExtension():
    '''    public void addExtension(final ClientSession.Extension extension)
    '''
def removeExtension():
    '''    public void removeExtension(final ClientSession.Extension extension)
    '''
def getChannel():
    '''    public ClientSessionChannel getChannel(final String channelId)
    '''
def startBatch():
    '''    public void startBatch()
    '''
def endBatch():
    '''    public boolean endBatch()
    '''
def batch():
    '''    public void batch(final Runnable batch)
    '''
def getAttribute():
    '''    public Object getAttribute(final String name)
    public Object getAttribute(final String name)
    '''
def getAttributeNames():
    '''    public Set<String> getAttributeNames()
    public Set<String> getAttributeNames()
    '''
def removeAttribute():
    '''    public Object removeAttribute(final String name)
    public Object removeAttribute(final String name)
    '''
def setAttribute():
    '''    public void setAttribute(final String name, final Object value)
    public void setAttribute(final String name, final Object value)
    '''
def receive():
    '''    public void receive(final Message.Mutable message)
    '''
def dump():
    '''    public void dump(final StringBuilder b, final String indent)
    '''
def getChannelId():
    '''    public ChannelId getChannelId()
    '''
def addListener():
    '''    public void addListener(final ClientSessionChannel.ClientSessionChannelListener listener)
    '''
def removeListener():
    '''    public void removeListener(final ClientSessionChannel.ClientSessionChannelListener listener)
    '''
def subscribe():
    '''    public void subscribe(final ClientSessionChannel.MessageListener listener)
    '''
def unsubscribe():
    '''    public void unsubscribe(final ClientSessionChannel.MessageListener listener)
    public void unsubscribe()
    '''
def release():
    '''    public boolean release()
    '''
def isReleased():
    '''    public boolean isReleased()
    '''
def getId():
    '''    public String getId()
    '''
def isDeepWild():
    '''    public boolean isDeepWild()
    '''
def isMeta():
    '''    public boolean isMeta()
    '''
def isService():
    '''    public boolean isService()
    '''
def isBroadcast():
    '''    public boolean isBroadcast()
    '''
def isWild():
    '''    public boolean isWild()
    '''
def toString():
    '''    public String toString()
    '''
def getReference():
    '''    public T getReference()
    '''
def isMarked():
    '''    public boolean isMarked()
    '''
