def accept():
    '''returns boolean\n\n
    accept(final Packet packet)\n
    '''
def processPacket():
    '''returns None\n\n
    processPacket(final Packet packet)\n
    '''
def createChat():
    '''returns Chat\n\n
    createChat(final String userJID, final MessageListener listener)\n
    createChat(final String userJID, String thread, final MessageListener listener)\n
    '''
def getThreadChat():
    '''returns Chat\n\n
    getThreadChat(final String thread)\n
    '''
def addChatListener():
    '''returns None\n\n
    addChatListener(final ChatManagerListener listener)\n
    '''
def removeChatListener():
    '''returns None\n\n
    removeChatListener(final ChatManagerListener listener)\n
    '''
def getChatListeners():
    '''returns Collection<ChatManagerListener>\n\n
    getChatListeners()\n
    '''
def addOutgoingMessageInterceptor():
    '''returns None\n\n
    addOutgoingMessageInterceptor(final PacketInterceptor packetInterceptor)\n
    addOutgoingMessageInterceptor(final PacketInterceptor packetInterceptor, final PacketFilter filter)\n
    '''
