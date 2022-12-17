USER_VERSION_UNKNOWN = "int  0"
USER_VERSION_EXTERNAL = "int  1"
USER_VERSION_15 = "int  2"
USER_VERSION_WATSON = "int  4"
def addUserInPlaceListener():
    '''returns None\n\n
    addUserInPlaceListener(final UserInPlaceListener obj)\n
    '''
def sendText():
    '''returns None\n\n
    sendText(final String s)\n
    '''
def sendData():
    '''returns None\n\n
    sendData(final int n, final byte[] array)\n
    '''
def queryAttrContent():
    '''returns None\n\n
    queryAttrContent(final int n)\n
    '''
def changeAttribute():
    '''returns None\n\n
    changeAttribute(final STExtendedAttribute stExtendedAttribute)\n
    '''
def removeAttribute():
    '''returns None\n\n
    removeAttribute(final int n)\n
    '''
def getUserVersion():
    '''returns int\n\n
    getUserVersion()\n
    '''
def getSection():
    '''returns Section\n\n
    getSection()\n
    '''
def getMemberId():
    '''returns Integer\n\n
    getMemberId()\n
    '''
def getPlace():
    '''returns Place\n\n
    getPlace()\n
    '''
def getAttributes():
    '''returns Enumeration\n\n
    getAttributes()\n
    '''
def processPlacesEvent():
    '''returns None\n\n
    processPlacesEvent(final PlacesEvent placesEvent)\n
    '''
def sendFailed():
    '''returns None\n\n
    sendFailed(final PlaceMemberEvent placeMemberEvent)\n
    '''
def attributeChanged():
    '''returns None\n\n
    attributeChanged(final PlaceMemberEvent placeMemberEvent)\n
    '''
def attributeRemoved():
    '''returns None\n\n
    attributeRemoved(final PlaceMemberEvent placeMemberEvent)\n
    '''
def changeAttributeFailed():
    '''returns None\n\n
    changeAttributeFailed(final PlaceMemberEvent placeMemberEvent)\n
    '''
def removeAttributeFailed():
    '''returns None\n\n
    removeAttributeFailed(final PlaceMemberEvent placeMemberEvent)\n
    '''
def queryAttrContentFailed():
    '''returns None\n\n
    queryAttrContentFailed(final PlaceMemberEvent placeMemberEvent)\n
    '''
