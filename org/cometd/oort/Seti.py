def Seti():
    '''    public Seti(final Oort oort)
    '''
def isDebugEnabled():
    '''    public boolean isDebugEnabled()
    '''
def setDebugEnabled():
    '''    public void setDebugEnabled(final boolean debug)
    '''
def getOort():
    '''    public Oort getOort()
    '''
def getId():
    '''    public String getId()
    '''
def configureChannel():
    '''    public void configureChannel(final ConfigurableServerChannel channel)
    public void configureChannel(final ConfigurableServerChannel channel)
    public void configureChannel(final ConfigurableServerChannel channel)
    '''
def onMessage():
    '''    public void onMessage(final ClientSessionChannel channel, final Message message)
    public void onMessage(final ClientSessionChannel channel, final Message message)
    '''
def associate():
    '''    public boolean associate(final String userId, final ServerSession session)
    '''
def isAssociated():
    '''    public boolean isAssociated(final String userId)
    '''
def isPresent():
    '''    public boolean isPresent(final String userId)
    '''
def disassociate():
    '''    public boolean disassociate(final String userId, final ServerSession session)
    '''
def sendMessage():
    '''    public void sendMessage(final String toUserId, final String toChannel, final Object data)
    public void sendMessage(final Collection<String> toUserIds, final String toChannel, final Object data)
    '''
def addPresenceListener():
    '''    public void addPresenceListener(final PresenceListener listener)
    '''
def removePresenceListener():
    '''    public void removePresenceListener(final PresenceListener listener)
    '''
def send():
    '''    public void send(final String toUser, final String toChannel, final Object data)
    public void send(final String toUser, final String toChannel, final Object data)
    '''
def receive():
    '''    public void receive(final String toUser, final String toChannel, final Object data)
    public void receive(final String toUser, final String toChannel, final Object data)
    '''
def removed():
    '''    public void removed(final ServerSession session, final boolean timeout)
    '''
def equals():
    '''    public boolean equals(final Object obj)
    public boolean equals(final Object obj)
    '''
def hashCode():
    '''    public int hashCode()
    public int hashCode()
    '''
def toString():
    '''    public String toString()
    public String toString()
    '''
def Event():
    '''    public Event(final Seti source, final String userId, final String url)
    '''
def getUserId():
    '''    public String getUserId()
    '''
def getURL():
    '''    public String getURL()
    '''
