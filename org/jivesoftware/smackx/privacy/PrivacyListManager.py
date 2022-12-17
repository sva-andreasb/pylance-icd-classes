NAMESPACE = "String  \"jabber:iq:privacy\""
def handleIQRequest():
    '''returns IQ\n\n
    handleIQRequest(final IQ iqRequest)\n
    '''
def processStanza():
    '''returns None\n\n
    processStanza(final Stanza packet)\n
    processStanza(final Stanza packet)\n
    processStanza(final Stanza packet)\n
    processStanza(final Stanza packet)\n
    processStanza(final Stanza packet)\n
    '''
def authenticated():
    '''returns None\n\n
    authenticated(final XMPPConnection connection, final boolean resumed)\n
    '''
def getActiveList():
    '''returns PrivacyList\n\n
    getActiveList()\n
    '''
def getActiveListName():
    '''returns String\n\n
    getActiveListName()\n
    '''
def getDefaultList():
    '''returns PrivacyList\n\n
    getDefaultList()\n
    '''
def getDefaultListName():
    '''returns String\n\n
    getDefaultListName()\n
    '''
def getEffectiveListName():
    '''returns String\n\n
    getEffectiveListName()\n
    '''
def getPrivacyList():
    '''returns PrivacyList\n\n
    getPrivacyList(String listName)\n
    '''
def getPrivacyLists():
    '''returns List<PrivacyList>\n\n
    getPrivacyLists()\n
    '''
def setActiveListName():
    '''returns None\n\n
    setActiveListName(final String listName)\n
    '''
def declineActiveList():
    '''returns None\n\n
    declineActiveList()\n
    '''
def setDefaultListName():
    '''returns None\n\n
    setDefaultListName(final String listName)\n
    '''
def declineDefaultList():
    '''returns None\n\n
    declineDefaultList()\n
    '''
def createPrivacyList():
    '''returns None\n\n
    createPrivacyList(final String listName, final List<PrivacyItem> privacyItems)\n
    '''
def updatePrivacyList():
    '''returns None\n\n
    updatePrivacyList(final String listName, final List<PrivacyItem> privacyItems)\n
    '''
def deletePrivacyList():
    '''returns None\n\n
    deletePrivacyList(final String listName)\n
    '''
def addListener():
    '''returns boolean\n\n
    addListener(final PrivacyListListener listener)\n
    '''
def removeListener():
    '''returns boolean\n\n
    removeListener(final PrivacyListListener listener)\n
    '''
def isSupported():
    '''returns boolean\n\n
    isSupported()\n
    '''
def connectionCreated():
    '''returns None\n\n
    connectionCreated(final XMPPConnection connection)\n
    '''
