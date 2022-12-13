def accept():
    '''    public boolean accept(final Packet packet)
    '''
def processPacket():
    '''    public void processPacket(final Packet packet)
    '''
def createChat():
    '''    public Chat createChat(final String userJID, final MessageListener listener)
    public Chat createChat(final String userJID, String thread, final MessageListener listener)
    '''
def getThreadChat():
    '''    public Chat getThreadChat(final String thread)
    '''
def addChatListener():
    '''    public void addChatListener(final ChatManagerListener listener)
    '''
def removeChatListener():
    '''    public void removeChatListener(final ChatManagerListener listener)
    '''
def getChatListeners():
    '''    public Collection<ChatManagerListener> getChatListeners()
    '''
def addOutgoingMessageInterceptor():
    '''    public void addOutgoingMessageInterceptor(final PacketInterceptor packetInterceptor)
    public void addOutgoingMessageInterceptor(final PacketInterceptor packetInterceptor, final PacketFilter filter)
    '''
