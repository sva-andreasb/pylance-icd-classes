def connectionClosed():
    '''public void connectionClosed()
    '''
def connectionClosedOnError():
    '''public void connectionClosedOnError(final Exception e)
    '''
def reconnectionFailed():
    '''public void reconnectionFailed(final Exception e)
    '''
def reconnectingIn():
    '''public void reconnectingIn(final int seconds)
    '''
def reconnectionSuccessful():
    '''public void reconnectionSuccessful()
    '''
def processPacket():
    '''public void processPacket(final Packet packet)
    '''
def getChildElementXML():
    '''public String getChildElementXML()
    '''
def getInstanceFor():
    '''public static PrivacyListManager getInstanceFor(final Connection connection)
    '''
def getActiveList():
    '''public PrivacyList getActiveList()
    '''
def getDefaultList():
    '''public PrivacyList getDefaultList()
    '''
def getPrivacyList():
    '''public PrivacyList getPrivacyList(final String listName)
    '''
def getPrivacyLists():
    '''public PrivacyList[] getPrivacyLists()
    '''
def setActiveListName():
    '''public void setActiveListName(final String listName)
    '''
def declineActiveList():
    '''public void declineActiveList()
    '''
def setDefaultListName():
    '''public void setDefaultListName(final String listName)
    '''
def declineDefaultList():
    '''public void declineDefaultList()
    '''
def createPrivacyList():
    '''public void createPrivacyList(final String listName, final List<PrivacyItem> privacyItems)
    '''
def updatePrivacyList():
    '''public void updatePrivacyList(final String listName, final List<PrivacyItem> privacyItems)
    '''
def deletePrivacyList():
    '''public void deletePrivacyList(final String listName)
    '''
def addListener():
    '''public void addListener(final PrivacyListListener listener)
    '''
def connectionCreated():
    '''public void connectionCreated(final Connection connection)
    '''
