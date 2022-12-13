def Seti():
'''public Seti(final Oort oort)
'''
pass
def isDebugEnabled():
'''public boolean isDebugEnabled()
'''
pass
def setDebugEnabled():
'''public void setDebugEnabled(final boolean debug)
'''
pass
def getOort():
'''public Oort getOort()
'''
pass
def getId():
'''public String getId()
'''
pass
def configureChannel():
'''public void configureChannel(final ConfigurableServerChannel channel)
public void configureChannel(final ConfigurableServerChannel channel)
public void configureChannel(final ConfigurableServerChannel channel)
'''
pass
def onMessage():
'''public void onMessage(final ClientSessionChannel channel, final Message message)
public void onMessage(final ClientSessionChannel channel, final Message message)
'''
pass
def associate():
'''public boolean associate(final String userId, final ServerSession session)
'''
pass
def isAssociated():
'''public boolean isAssociated(final String userId)
'''
pass
def isPresent():
'''public boolean isPresent(final String userId)
'''
pass
def disassociate():
'''public boolean disassociate(final String userId, final ServerSession session)
'''
pass
def sendMessage():
'''public void sendMessage(final String toUserId, final String toChannel, final Object data)
public void sendMessage(final Collection<String> toUserIds, final String toChannel, final Object data)
'''
pass
def addPresenceListener():
'''public void addPresenceListener(final PresenceListener listener)
'''
pass
def removePresenceListener():
'''public void removePresenceListener(final PresenceListener listener)
'''
pass
def send():
'''public void send(final String toUser, final String toChannel, final Object data)
public void send(final String toUser, final String toChannel, final Object data)
'''
pass
def receive():
'''public void receive(final String toUser, final String toChannel, final Object data)
public void receive(final String toUser, final String toChannel, final Object data)
'''
pass
def removed():
'''public void removed(final ServerSession session, final boolean timeout)
'''
pass
def equals():
'''public boolean equals(final Object obj)
public boolean equals(final Object obj)
'''
pass
def hashCode():
'''public int hashCode()
public int hashCode()
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def Event():
'''public Event(final Seti source, final String userId, final String url)
'''
pass
def getUserId():
'''public String getUserId()
'''
pass
def getURL():
'''public String getURL()
'''
pass
