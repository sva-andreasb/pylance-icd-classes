def WOPredecessorUtil():
    '''public WOPredecessorUtil()
    '''
def getExcludedList():
    '''public List<String> getExcludedList()
    '''
def setExcludedList():
    '''public void setExcludedList(final List<String> excludedList)
    '''
def getChildList():
    '''public List<String> getChildList()
    '''
def setChildList():
    '''public void setChildList(final List<String> childList)
    '''
def getLinkList():
    '''public List<String> getLinkList()
    '''
def setLinkList():
    '''public void setLinkList(final List<String> linkList)
    '''
def validateLink():
    '''public boolean validateLink(final MboRemote workorder, final String wonum, final String target)
    '''
def getRelationshipsUp():
    '''public void getRelationshipsUp(final UserInfo userInfo, final String wonum)
    '''
def getRelationshipsDown():
    '''public void getRelationshipsDown(final UserInfo userInfo, final String predwonum)
    '''
def checkDirectRelationship():
    '''public boolean checkDirectRelationship(final MboRemote workorder, final String wonum, final String target)
    '''
def getParent():
    '''public String getParent(final MboRemote workorder, final String wonum)
    '''
def getAllChildrenToExclude():
    '''public void getAllChildrenToExclude(final MboRemote workorder, final String wonum)
    '''
def getAllChildren():
    '''public void getAllChildren(final MboRemote workorder, final String wonum)
    '''
def getWOMboFromWonum():
    '''public MboRemote getWOMboFromWonum(final String wonum, final UserInfo userinfo)
    '''
def isALinked():
    '''public boolean isALinked(final MboRemote workorder, final String wonum)
    '''
def hasALink():
    '''public boolean hasALink(final MboRemote workorder, final String wonum)
    '''
