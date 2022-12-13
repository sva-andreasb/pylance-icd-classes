def getInstanceFor():
    '''    public static synchronized ChatManager getInstanceFor(final XMPPConnection connection)
    '''
def processStanza():
    '''    public void processStanza(final Stanza packet)
    '''
def isNormalIncluded():
    '''    public boolean isNormalIncluded()
    '''
def setNormalIncluded():
    '''    public void setNormalIncluded(final boolean normalIncluded)
    '''
def getMatchMode():
    '''    public MatchMode getMatchMode()
    '''
def setMatchMode():
    '''    public void setMatchMode(final MatchMode matchMode)
    '''
def createChat():
    '''    public Chat createChat(final EntityJid userJID)
    public Chat createChat(final EntityJid userJID, final ChatMessageListener listener)
    public Chat createChat(final EntityJid userJID, String thread, final ChatMessageListener listener)
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
    '''    public Set<ChatManagerListener> getChatListeners()
    '''
def addOutgoingMessageInterceptor():
    '''    public void addOutgoingMessageInterceptor(final MessageListener messageInterceptor)
    public void addOutgoingMessageInterceptor(final MessageListener messageInterceptor, final StanzaFilter filter)
    '''
def setDefaultMatchMode():
    '''    public static void setDefaultMatchMode(final MatchMode mode)
    '''
def setDefaultIsNormalIncluded():
    '''    public static void setDefaultIsNormalIncluded(final boolean allowNormal)
    '''
