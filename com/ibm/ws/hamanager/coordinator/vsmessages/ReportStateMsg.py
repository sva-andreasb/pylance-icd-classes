BULLETIN_BOARD_LOCAL = "String  \"BULLETIN_BOARD_LOCAL\""
BULLETIN_BOARD_PROXY = "String  \"BULLETIN_BOARD_PROXY\""
def ():
    '''returns ReportStateMsg\n\n
    ()\n
    '''
def getModes():
    '''returns Map\n\n
    getModes()\n
    '''
def setBulletinBoardLocalMode():
    '''returns None\n\n
    setBulletinBoardLocalMode(final int mode)\n
    '''
def setBulletinBoardProxyMode():
    '''returns None\n\n
    setBulletinBoardProxyMode(final int mode)\n
    '''
def flushProxyState():
    '''returns int\n\n
    flushProxyState()\n
    '''
def addHAGroupData():
    '''returns None\n\n
    addHAGroupData(final GroupName gn, final GroupState gs)\n
    '''
def addBulletinBoardLocalPost():
    '''returns None\n\n
    addBulletinBoardLocalPost(final SubjectInfo subject, final BulletinBoardPost post)\n
    '''
def setBridgeConfigurationData():
    '''returns None\n\n
    setBridgeConfigurationData(final Set bridgeConfigData)\n
    '''
def getBridgeConfigurationData():
    '''returns Set\n\n
    getBridgeConfigurationData()\n
    '''
def addBulletinBoardProxyPost():
    '''returns None\n\n
    addBulletinBoardProxyPost(final SubjectInfo subject, final BulletinBoardPost post)\n
    '''
def addBulletinBoardProxyPostMap():
    '''returns None\n\n
    addBulletinBoardProxyPostMap(final SubjectInfo subject, final Map posts)\n
    '''
def addBulletinBoardLocalSubscriber():
    '''returns None\n\n
    addBulletinBoardLocalSubscriber(final SubjectInfo subject, final Boolean state)\n
    '''
def addBulletinBoardProxySubscriber():
    '''returns None\n\n
    addBulletinBoardProxySubscriber(final SubjectInfo subject, final Boolean state)\n
    '''
def addBridgeOwnedSubjects():
    '''returns None\n\n
    addBridgeOwnedSubjects(final Set ownedSubjects)\n
    '''
def addBridgeOwnedSubject():
    '''returns None\n\n
    addBridgeOwnedSubject(final SubjectInfo ownedSubject)\n
    '''
def getBridgeSubjects():
    '''returns Set\n\n
    getBridgeSubjects()\n
    '''
def getDescription():
    '''returns String\n\n
    getDescription()\n
    '''
def getHAGroupData():
    '''returns Map\n\n
    getHAGroupData()\n
    '''
def getLocalPosts():
    '''returns Map\n\n
    getLocalPosts()\n
    '''
def getProxyPosts():
    '''returns Map\n\n
    getProxyPosts()\n
    '''
def getLocalSubscribers():
    '''returns Map\n\n
    getLocalSubscribers()\n
    '''
def getProxySubscribers():
    '''returns Map\n\n
    getProxySubscribers()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
