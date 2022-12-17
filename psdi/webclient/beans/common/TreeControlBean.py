def ():
    '''returns TreeControlBean\n\n
    ()\n
    '''
def selectrecord():
    '''returns int\n\n
    selectrecord()\n
    '''
def selectnode():
    '''returns int\n\n
    selectnode()\n
    '''
def setcurrentnode():
    '''returns None\n\n
    setcurrentnode(final String newobjectname, final String newuniqueidname, final String newuniqueidvalue)\n
    '''
def getTop():
    '''returns Object[][]\n\n
    getTop(final String[] dataattributes, final int maxchildren)\n
    '''
def getChildren():
    '''returns Object[][]\n\n
    getChildren(final String objectname, final String uniqueid, final String[] dataattributes, final int maxchildren)\n
    '''
def getPathToTop():
    '''returns Object[][]\n\n
    getPathToTop(final String objectname, final String uniqueid, final String[] dataattributes, final int maxchildren)\n
    '''
def getMboValueData():
    '''returns Object[]\n\n
    getMboValueData(final String[] dataattributes)\n
    '''
def setHierarchy():
    '''returns None\n\n
    setHierarchy(final String objectname, final String uniqueid, final String hierarchy)\n
    '''
def getobjectname():
    '''returns String\n\n
    getobjectname()\n
    '''
def setobjectname():
    '''returns None\n\n
    setobjectname(final String newobjectname)\n
    '''
def getuniqueidname():
    '''returns String\n\n
    getuniqueidname()\n
    '''
def setuniqueidname():
    '''returns None\n\n
    setuniqueidname(final String newuniqueidname)\n
    '''
def getuniqueidvalue():
    '''returns String\n\n
    getuniqueidvalue()\n
    '''
def setuniqueidvalue():
    '''returns None\n\n
    setuniqueidvalue(final String newuniqueidvalue)\n
    '''
def setRefreshTree():
    '''returns None\n\n
    setRefreshTree(final boolean flag)\n
    '''
def getRefreshTree():
    '''returns boolean\n\n
    getRefreshTree()\n
    '''
def getSourceAttributeValue():
    '''returns String\n\n
    getSourceAttributeValue()\n
    '''
def setSourceAttributeValue():
    '''returns None\n\n
    setSourceAttributeValue(final String sourceAttributevalue)\n
    '''
def getSourceDataAttribute():
    '''returns String\n\n
    getSourceDataAttribute()\n
    '''
def setSourceDataAttribute():
    '''returns None\n\n
    setSourceDataAttribute(final String sourceDataattribute)\n
    '''
def getBreadcrumbs():
    '''returns ArrayList\n\n
    getBreadcrumbs()\n
    '''
def clearbreadcrumbs():
    '''returns int\n\n
    clearbreadcrumbs()\n
    '''
def getBoundTree():
    '''returns Tree\n\n
    getBoundTree()\n
    '''
def markTreesForRefresh():
    '''returns None\n\n
    markTreesForRefresh(final String dontRefreshMe)\n
    '''
def setIgnoreTreeRefresh():
    '''returns None\n\n
    setIgnoreTreeRefresh(final boolean ignoreTreeRefresh)\n
    '''
def dataChangedEvent():
    '''returns None\n\n
    dataChangedEvent(final DataBean speaker)\n
    '''
