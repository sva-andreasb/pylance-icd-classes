def processStanza():
    '''returns None\n\n
    processStanza(final Stanza packet)\n
    '''
def isNormalIncluded():
    '''returns boolean\n\n
    isNormalIncluded()\n
    '''
def setNormalIncluded():
    '''returns None\n\n
    setNormalIncluded(final boolean normalIncluded)\n
    '''
def getMatchMode():
    '''returns MatchMode\n\n
    getMatchMode()\n
    '''
def setMatchMode():
    '''returns None\n\n
    setMatchMode(final MatchMode matchMode)\n
    '''
def createChat():
    '''returns Chat\n\n
    createChat(final EntityJid userJID)\n
    createChat(final EntityJid userJID, final ChatMessageListener listener)\n
    createChat(final EntityJid userJID, String thread, final ChatMessageListener listener)\n
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
    '''returns Set<ChatManagerListener>\n\n
    getChatListeners()\n
    '''
def addOutgoingMessageInterceptor():
    '''returns None\n\n
    addOutgoingMessageInterceptor(final MessageListener messageInterceptor)\n
    addOutgoingMessageInterceptor(final MessageListener messageInterceptor, final StanzaFilter filter)\n
    '''
