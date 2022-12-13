def getInstanceFor():
'''public static synchronized ChatManager getInstanceFor(final XMPPConnection connection)
'''
pass
def processStanza():
'''public void processStanza(final Stanza packet)
'''
pass
def isNormalIncluded():
'''public boolean isNormalIncluded()
'''
pass
def setNormalIncluded():
'''public void setNormalIncluded(final boolean normalIncluded)
'''
pass
def getMatchMode():
'''public MatchMode getMatchMode()
'''
pass
def setMatchMode():
'''public void setMatchMode(final MatchMode matchMode)
'''
pass
def createChat():
'''public Chat createChat(final EntityJid userJID)
public Chat createChat(final EntityJid userJID, final ChatMessageListener listener)
public Chat createChat(final EntityJid userJID, String thread, final ChatMessageListener listener)
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
'''public Set<ChatManagerListener> getChatListeners()
'''
pass
def addOutgoingMessageInterceptor():
'''public void addOutgoingMessageInterceptor(final MessageListener messageInterceptor)
public void addOutgoingMessageInterceptor(final MessageListener messageInterceptor, final StanzaFilter filter)
'''
pass
def setDefaultMatchMode():
'''public static void setDefaultMatchMode(final MatchMode mode)
'''
pass
def setDefaultIsNormalIncluded():
'''public static void setDefaultIsNormalIncluded(final boolean allowNormal)
'''
pass
