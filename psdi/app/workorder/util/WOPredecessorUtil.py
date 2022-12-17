def ():
    '''returns WOPredecessorUtil\n\n
    ()\n
    '''
def getExcludedList():
    '''returns List<String>\n\n
    getExcludedList()\n
    '''
def setExcludedList():
    '''returns None\n\n
    setExcludedList(final List<String> excludedList)\n
    '''
def getChildList():
    '''returns List<String>\n\n
    getChildList()\n
    '''
def setChildList():
    '''returns None\n\n
    setChildList(final List<String> childList)\n
    '''
def getLinkList():
    '''returns List<String>\n\n
    getLinkList()\n
    '''
def setLinkList():
    '''returns None\n\n
    setLinkList(final List<String> linkList)\n
    '''
def validateLink():
    '''returns boolean\n\n
    validateLink(final MboRemote workorder, final String wonum, final String target)\n
    '''
def getRelationshipsUp():
    '''returns None\n\n
    getRelationshipsUp(final UserInfo userInfo, final String wonum)\n
    '''
def getRelationshipsDown():
    '''returns None\n\n
    getRelationshipsDown(final UserInfo userInfo, final String predwonum)\n
    '''
def checkDirectRelationship():
    '''returns boolean\n\n
    checkDirectRelationship(final MboRemote workorder, final String wonum, final String target)\n
    '''
def getParent():
    '''returns String\n\n
    getParent(final MboRemote workorder, final String wonum)\n
    '''
def getAllChildrenToExclude():
    '''returns None\n\n
    getAllChildrenToExclude(final MboRemote workorder, final String wonum)\n
    '''
def getAllChildren():
    '''returns None\n\n
    getAllChildren(final MboRemote workorder, final String wonum)\n
    '''
def getWOMboFromWonum():
    '''returns MboRemote\n\n
    getWOMboFromWonum(final String wonum, final UserInfo userinfo)\n
    '''
def isALinked():
    '''returns boolean\n\n
    isALinked(final MboRemote workorder, final String wonum)\n
    '''
def hasALink():
    '''returns boolean\n\n
    hasALink(final MboRemote workorder, final String wonum)\n
    '''
