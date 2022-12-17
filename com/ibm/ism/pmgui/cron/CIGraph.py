COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
def ():
    '''returns CIGraph\n\n
    ()\n
    '''
def pushVisibleNodeStack():
    '''returns None\n\n
    pushVisibleNodeStack(final CINode node)\n
    '''
def popVisibleNodeStack():
    '''returns None\n\n
    popVisibleNodeStack()\n
    '''
def getLastVisibleNode():
    '''returns CINode\n\n
    getLastVisibleNode()\n
    '''
def getVisibleNodeStackDepth():
    '''returns int\n\n
    getVisibleNodeStackDepth()\n
    '''
def notVisited():
    '''returns boolean\n\n
    notVisited(final String cinum)\n
    '''
def pushNodeStack():
    '''returns None\n\n
    pushNodeStack(final String ciNum, final CINode node)\n
    '''
def popNodeStack():
    '''returns None\n\n
    popNodeStack()\n
    '''
def getNodeStackDepth():
    '''returns int\n\n
    getNodeStackDepth()\n
    '''
def getLastNode():
    '''returns CINode\n\n
    getLastNode()\n
    '''
def addNode():
    '''returns None\n\n
    addNode(final CINode n)\n
    '''
def getNode():
    '''returns CINode\n\n
    getNode(final String ciNum)\n
    '''
def addLInk():
    '''returns None\n\n
    addLInk(final CILink l)\n
    '''
def getNodesSkipped():
    '''returns String\n\n
    getNodesSkipped(final CINode from, final CINode to)\n
    '''
def printLinks():
    '''returns None\n\n
    printLinks(final String cinum)\n
    '''
def log():
    '''returns None\n\n
    log(final String method, final String str)\n
    '''
def getLinks():
    '''returns ArrayList<CILink>\n\n
    getLinks()\n
    '''
def setLinks():
    '''returns None\n\n
    setLinks(final ArrayList<CILink> links)\n
    '''
