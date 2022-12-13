def IlvGrapher():
'''public IlvGrapher()
public IlvGrapher(final int n)
public IlvGrapher(final int n, final int n2)
public IlvGrapher(final IlvInputStream ilvInputStream)
public IlvGrapher(final IlvGrapher ilvGrapher)
'''
pass
def copy():
'''public IlvGraphic copy()
'''
pass
def write():
'''public void write(final IlvOutputStream ilvOutputStream)
'''
pass
def writePrefix():
'''public void writePrefix(final IlvOutputStream ilvOutputStream, final boolean b)
'''
pass
def writeSuffix():
'''public void writeSuffix(final IlvOutputStream ilvOutputStream, final boolean b)
'''
pass
def readPrefix():
'''public void readPrefix(final IlvInputStream ilvInputStream, final boolean b)
'''
pass
def readSuffix():
'''public void readSuffix(final IlvInputStream ilvInputStream, final boolean b)
'''
pass
def addObject():
'''public void addObject(final IlvGraphic obj, final int n, final boolean b)
'''
pass
def addNode():
'''public void addNode(final IlvGraphic ilvGraphic, final boolean b)
public void addNode(final IlvGraphic ilvGraphic, final int n, final boolean b)
'''
pass
def addLink():
'''public void addLink(final IlvLinkImage ilvLinkImage, final boolean b)
public void addLink(final IlvLinkImage ilvLinkImage, final int n, final boolean b)
'''
pass
def getExternalInterGraphLinks():
'''public final IlvGraphicEnumeration getExternalInterGraphLinks()
'''
pass
def getExternalInterGraphLinksCount():
'''public final int getExternalInterGraphLinksCount()
'''
pass
def getTreeExternalInterGraphLinks():
'''public final IlvGraphicEnumeration getTreeExternalInterGraphLinks()
'''
pass
def hasMoreElements():
'''public boolean hasMoreElements()
public boolean hasMoreElements()
public boolean hasMoreElements()
public final boolean hasMoreElements()
'''
pass
def nextElement():
'''public IlvGraphic nextElement()
public IlvGraphic nextElement()
public IlvGraphic nextElement()
public final IlvGraphic nextElement()
'''
pass
def getTreeExternalInterGraphLinksCount():
'''public final int getTreeExternalInterGraphLinksCount()
'''
pass
def getInterGraphLinks():
'''public final IlvGraphicEnumeration getInterGraphLinks()
'''
pass
def getInterGraphLinksCount():
'''public final int getInterGraphLinksCount()
'''
pass
def addInterGraphLink():
'''public static void addInterGraphLink(final IlvLinkImage ilvLinkImage, final boolean b)
'''
pass
def getLowestCommonGrapher():
'''public static IlvGrapher getLowestCommonGrapher(final IlvGraphic ilvGraphic, final IlvGraphic ilvGraphic2)
'''
pass
def removeObject():
'''public void removeObject(final IlvGraphic ilvGraphic, final boolean b)
'''
pass
def removeLink():
'''public void removeLink(final IlvLinkImage obj, final boolean b)
'''
pass
def removeNode():
'''public void removeNode(final IlvGraphic obj, final boolean b)
'''
pass
def getLinksInsertionLayer():
'''public final int getLinksInsertionLayer()
'''
pass
def setLinksInsertionLayer():
'''public final void setLinksInsertionLayer(final int e)
'''
pass
def setLayer():
'''public void setLayer(final IlvGraphic ilvGraphic, final int n, final boolean b)
'''
pass
def replaceObject():
'''public void replaceObject(final IlvGraphic obj, final IlvGraphic ilvGraphic, final boolean b)
'''
pass
def getLinksFrom():
'''public final IlvGraphicEnumeration getLinksFrom(final IlvGraphic obj)
'''
pass
def getLinksFromCount():
'''public final int getLinksFromCount(final IlvGraphic obj)
'''
pass
def getLinksTo():
'''public final IlvGraphicEnumeration getLinksTo(final IlvGraphic obj)
'''
pass
def getLinksToCount():
'''public final int getLinksToCount(final IlvGraphic obj)
'''
pass
def getLinks():
'''public final IlvGraphicEnumeration getLinks(final IlvGraphic obj)
'''
pass
def getLinksCount():
'''public final int getLinksCount(final IlvGraphic obj)
'''
pass
def getNeighbors():
'''public final IlvGraphicEnumeration getNeighbors(final IlvGraphic obj)
'''
pass
def getFromNeighbors():
'''public final IlvGraphicEnumeration getFromNeighbors(final IlvGraphic obj)
'''
pass
def getToNeighbors():
'''public final IlvGraphicEnumeration getToNeighbors(final IlvGraphic obj)
'''
pass
def getLinksVisibleFrom():
'''public final IlvGraphicEnumeration getLinksVisibleFrom(final IlvGraphic ilvGraphic)
'''
pass
def getLinksVisibleFromCount():
'''public final int getLinksVisibleFromCount(final IlvGraphic ilvGraphic)
'''
pass
def getLinksVisibleTo():
'''public final IlvGraphicEnumeration getLinksVisibleTo(final IlvGraphic ilvGraphic)
'''
pass
def getLinksVisibleToCount():
'''public final int getLinksVisibleToCount(final IlvGraphic ilvGraphic)
'''
pass
def isNode():
'''public final boolean isNode(final IlvGraphic ilvGraphic)
'''
pass
def isLink():
'''public final boolean isLink(final IlvGraphic ilvGraphic)
'''
pass
def isNodeOrLink():
'''public final boolean isNodeOrLink(final IlvGraphic ilvGraphic)
'''
pass
def isInterGraphLink():
'''public final boolean isInterGraphLink(final IlvGraphic ilvGraphic)
'''
pass
def setMarked():
'''public final void setMarked(final IlvGraphic ilvGraphic, final boolean b)
'''
pass
def isMarked():
'''public final boolean isMarked(final IlvGraphic ilvGraphic)
'''
pass
def nodeHasSons():
'''public final boolean nodeHasSons(final IlvGraphic ilvGraphic)
'''
pass
def isLinkBetween():
'''public final boolean isLinkBetween(final IlvGraphic ilvGraphic, final IlvGraphic ilvGraphic2)
'''
pass
def makeNode():
'''public void makeNode(final IlvGraphic ilvGraphic)
'''
pass
def unmakeNode():
'''public void unmakeNode(final IlvGraphic obj)
'''
pass
def getSelectedMovingObjects():
'''public IlvGraphicEnumeration getSelectedMovingObjects(final boolean[] array)
'''
pass
def setCrossingAwareLinksFrozen():
'''public void setCrossingAwareLinksFrozen(final boolean f)
'''
pass
def isCrossingAwareLinksFrozen():
'''public boolean isCrossingAwareLinksFrozen()
'''
pass
def setVisibleBranch():
'''public void setVisibleBranch(final IlvGraphic ilvGraphic, final boolean b, final boolean b2)
public void setVisibleBranch(final IlvGraphic ilvGraphic, final int n, final boolean b, final boolean b2)
public void setVisibleBranch(final IlvGraphic ilvGraphic, final int n, final int n2, final boolean b, final boolean b2, final boolean b3, final boolean b4)
'''
pass
