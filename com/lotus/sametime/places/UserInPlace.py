USER_VERSION_UNKNOWN = "int  0"
USER_VERSION_EXTERNAL = "int  1"
USER_VERSION_15 = "int  2"
USER_VERSION_WATSON = "int  4"
def addUserInPlaceListener():
    '''public void addUserInPlaceListener(final UserInPlaceListener obj)
    '''
def removeUserInPlaceListener():
    '''public synchronized void removeUserInPlaceListener(final UserInPlaceListener obj)
    '''
def sendText():
    '''public void sendText(final String s)
    '''
def sendData():
    '''public void sendData(final int n, final byte[] array)
    '''
def queryAttrContent():
    '''public void queryAttrContent(final int n)
    '''
def changeAttribute():
    '''public void changeAttribute(final STExtendedAttribute stExtendedAttribute)
    '''
def removeAttribute():
    '''public void removeAttribute(final int n)
    '''
def getUserVersion():
    '''public int getUserVersion()
    '''
def getSection():
    '''public Section getSection()
    '''
def getMemberId():
    '''public Integer getMemberId()
    '''
def getPlace():
    '''public Place getPlace()
    '''
def getAttributes():
    '''public Enumeration getAttributes()
    '''
def processPlacesEvent():
    '''public void processPlacesEvent(final PlacesEvent placesEvent)
    '''
def sendFailed():
    '''public void sendFailed(final PlaceMemberEvent placeMemberEvent)
    '''
def attributeChanged():
    '''public void attributeChanged(final PlaceMemberEvent placeMemberEvent)
    '''
def attributeRemoved():
    '''public void attributeRemoved(final PlaceMemberEvent placeMemberEvent)
    '''
def changeAttributeFailed():
    '''public void changeAttributeFailed(final PlaceMemberEvent placeMemberEvent)
    '''
def removeAttributeFailed():
    '''public void removeAttributeFailed(final PlaceMemberEvent placeMemberEvent)
    '''
def queryAttrContentFailed():
    '''public void queryAttrContentFailed(final PlaceMemberEvent placeMemberEvent)
    '''
