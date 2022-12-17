def connectionClosed():
    '''returns None\n\n
    connectionClosed()\n
    '''
def connectionClosedOnError():
    '''returns None\n\n
    connectionClosedOnError(final Exception e)\n
    '''
def reconnectionFailed():
    '''returns None\n\n
    reconnectionFailed(final Exception e)\n
    '''
def reconnectingIn():
    '''returns None\n\n
    reconnectingIn(final int seconds)\n
    '''
def reconnectionSuccessful():
    '''returns None\n\n
    reconnectionSuccessful()\n
    '''
def processPacket():
    '''returns None\n\n
    processPacket(final Packet packet)\n
    '''
def getChildElementXML():
    '''returns String\n\n
    getChildElementXML()\n
    '''
def getActiveList():
    '''returns PrivacyList\n\n
    getActiveList()\n
    '''
def getDefaultList():
    '''returns PrivacyList\n\n
    getDefaultList()\n
    '''
def getPrivacyList():
    '''returns PrivacyList\n\n
    getPrivacyList(final String listName)\n
    '''
def getPrivacyLists():
    '''returns PrivacyList[]\n\n
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
    '''returns None\n\n
    addListener(final PrivacyListListener listener)\n
    '''
def connectionCreated():
    '''returns None\n\n
    connectionCreated(final Connection connection)\n
    '''
