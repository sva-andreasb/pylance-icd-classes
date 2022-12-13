def IlvGrapher():
    '''public IlvGrapher()
    public IlvGrapher(final int n)
    public IlvGrapher(final int n, final int n2)
    public IlvGrapher(final IlvInputStream ilvInputStream)
    public IlvGrapher(final IlvGrapher ilvGrapher)
    '''
def copy():
    '''public IlvGraphic copy()
    '''
def write():
    '''public void write(final IlvOutputStream ilvOutputStream)
    '''
def writePrefix():
    '''public void writePrefix(final IlvOutputStream ilvOutputStream, final boolean b)
    '''
def writeSuffix():
    '''public void writeSuffix(final IlvOutputStream ilvOutputStream, final boolean b)
    '''
def readPrefix():
    '''public void readPrefix(final IlvInputStream ilvInputStream, final boolean b)
    '''
def readSuffix():
    '''public void readSuffix(final IlvInputStream ilvInputStream, final boolean b)
    '''
def addObject():
    '''public void addObject(final IlvGraphic obj, final int n, final boolean b)
    '''
def addNode():
    '''public void addNode(final IlvGraphic ilvGraphic, final boolean b)
    public void addNode(final IlvGraphic ilvGraphic, final int n, final boolean b)
    '''
def addLink():
    '''public void addLink(final IlvLinkImage ilvLinkImage, final boolean b)
    public void addLink(final IlvLinkImage ilvLinkImage, final int n, final boolean b)
    '''
def getExternalInterGraphLinks():
    '''public final IlvGraphicEnumeration getExternalInterGraphLinks()
    '''
def getExternalInterGraphLinksCount():
    '''public final int getExternalInterGraphLinksCount()
    '''
def getTreeExternalInterGraphLinks():
    '''public final IlvGraphicEnumeration getTreeExternalInterGraphLinks()
    '''
def hasMoreElements():
    '''public boolean hasMoreElements()
    public boolean hasMoreElements()
    public boolean hasMoreElements()
    public final boolean hasMoreElements()
    '''
def nextElement():
    '''public IlvGraphic nextElement()
    public IlvGraphic nextElement()
    public IlvGraphic nextElement()
    public final IlvGraphic nextElement()
    '''
def getTreeExternalInterGraphLinksCount():
    '''public final int getTreeExternalInterGraphLinksCount()
    '''
def getInterGraphLinks():
    '''public final IlvGraphicEnumeration getInterGraphLinks()
    '''
def getInterGraphLinksCount():
    '''public final int getInterGraphLinksCount()
    '''
def addInterGraphLink():
    '''public static void addInterGraphLink(final IlvLinkImage ilvLinkImage, final boolean b)
    '''
def getLowestCommonGrapher():
    '''public static IlvGrapher getLowestCommonGrapher(final IlvGraphic ilvGraphic, final IlvGraphic ilvGraphic2)
    '''
def removeObject():
    '''public void removeObject(final IlvGraphic ilvGraphic, final boolean b)
    '''
def removeLink():
    '''public void removeLink(final IlvLinkImage obj, final boolean b)
    '''
def removeNode():
    '''public void removeNode(final IlvGraphic obj, final boolean b)
    '''
def getLinksInsertionLayer():
    '''public final int getLinksInsertionLayer()
    '''
def setLinksInsertionLayer():
    '''public final void setLinksInsertionLayer(final int e)
    '''
def setLayer():
    '''public void setLayer(final IlvGraphic ilvGraphic, final int n, final boolean b)
    '''
def replaceObject():
    '''public void replaceObject(final IlvGraphic obj, final IlvGraphic ilvGraphic, final boolean b)
    '''
def getLinksFrom():
    '''public final IlvGraphicEnumeration getLinksFrom(final IlvGraphic obj)
    '''
def getLinksFromCount():
    '''public final int getLinksFromCount(final IlvGraphic obj)
    '''
def getLinksTo():
    '''public final IlvGraphicEnumeration getLinksTo(final IlvGraphic obj)
    '''
def getLinksToCount():
    '''public final int getLinksToCount(final IlvGraphic obj)
    '''
def getLinks():
    '''public final IlvGraphicEnumeration getLinks(final IlvGraphic obj)
    '''
def getLinksCount():
    '''public final int getLinksCount(final IlvGraphic obj)
    '''
def getNeighbors():
    '''public final IlvGraphicEnumeration getNeighbors(final IlvGraphic obj)
    '''
def getFromNeighbors():
    '''public final IlvGraphicEnumeration getFromNeighbors(final IlvGraphic obj)
    '''
def getToNeighbors():
    '''public final IlvGraphicEnumeration getToNeighbors(final IlvGraphic obj)
    '''
def getLinksVisibleFrom():
    '''public final IlvGraphicEnumeration getLinksVisibleFrom(final IlvGraphic ilvGraphic)
    '''
def getLinksVisibleFromCount():
    '''public final int getLinksVisibleFromCount(final IlvGraphic ilvGraphic)
    '''
def getLinksVisibleTo():
    '''public final IlvGraphicEnumeration getLinksVisibleTo(final IlvGraphic ilvGraphic)
    '''
def getLinksVisibleToCount():
    '''public final int getLinksVisibleToCount(final IlvGraphic ilvGraphic)
    '''
def isNode():
    '''public final boolean isNode(final IlvGraphic ilvGraphic)
    '''
def isLink():
    '''public final boolean isLink(final IlvGraphic ilvGraphic)
    '''
def isNodeOrLink():
    '''public final boolean isNodeOrLink(final IlvGraphic ilvGraphic)
    '''
def isInterGraphLink():
    '''public final boolean isInterGraphLink(final IlvGraphic ilvGraphic)
    '''
def setMarked():
    '''public final void setMarked(final IlvGraphic ilvGraphic, final boolean b)
    '''
def isMarked():
    '''public final boolean isMarked(final IlvGraphic ilvGraphic)
    '''
def nodeHasSons():
    '''public final boolean nodeHasSons(final IlvGraphic ilvGraphic)
    '''
def isLinkBetween():
    '''public final boolean isLinkBetween(final IlvGraphic ilvGraphic, final IlvGraphic ilvGraphic2)
    '''
def makeNode():
    '''public void makeNode(final IlvGraphic ilvGraphic)
    '''
def unmakeNode():
    '''public void unmakeNode(final IlvGraphic obj)
    '''
def getSelectedMovingObjects():
    '''public IlvGraphicEnumeration getSelectedMovingObjects(final boolean[] array)
    '''
def setCrossingAwareLinksFrozen():
    '''public void setCrossingAwareLinksFrozen(final boolean f)
    '''
def isCrossingAwareLinksFrozen():
    '''public boolean isCrossingAwareLinksFrozen()
    '''
def setVisibleBranch():
    '''public void setVisibleBranch(final IlvGraphic ilvGraphic, final boolean b, final boolean b2)
    public void setVisibleBranch(final IlvGraphic ilvGraphic, final int n, final boolean b, final boolean b2)
    public void setVisibleBranch(final IlvGraphic ilvGraphic, final int n, final int n2, final boolean b, final boolean b2, final boolean b3, final boolean b4)
    '''
