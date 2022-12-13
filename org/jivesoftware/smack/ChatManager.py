def accept():
'''public boolean accept(final Packet packet)
'''
pass
def processPacket():
'''public void processPacket(final Packet packet)
'''
pass
def createChat():
'''public Chat createChat(final String userJID, final MessageListener listener)
public Chat createChat(final String userJID, String thread, final MessageListener listener)
'''
pass
def getThreadChat():
'''public Chat getThreadChat(final String thread)
'''
pass
def addChatListener():
'''public void addChatListener(final ChatManagerListener listener)
'''
pass
def removeChatListener():
'''public void removeChatListener(final ChatManagerListener listener)
'''
pass
def getChatListeners():
'''public Collection<ChatManagerListener> getChatListeners()
'''
pass
def addOutgoingMessageInterceptor():
'''public void addOutgoingMessageInterceptor(final PacketInterceptor packetInterceptor)
public void addOutgoingMessageInterceptor(final PacketInterceptor packetInterceptor, final PacketFilter filter)
'''
pass
