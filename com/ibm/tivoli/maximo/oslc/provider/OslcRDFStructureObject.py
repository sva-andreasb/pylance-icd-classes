def OslcRDFStructureObject():
'''public OslcRDFStructureObject(final String operaton, final String osName, final String lang, final int size, final boolean isEvent, final boolean isResponse)
public OslcRDFStructureObject(final Document input)
public OslcRDFStructureObject(final Resource data, final String mosName, final String path, final String messageType, final UserInfo userInfo)
public OslcRDFStructureObject(final Element data)
public OslcRDFStructureObject()
'''
pass
def getName():
'''public String getName()
'''
pass
def getObjectPath():
'''public String getObjectPath()
'''
pass
def getUserInfo():
'''public UserInfo getUserInfo()
'''
pass
def createChildrenData():
'''public void createChildrenData(final String name)
'''
pass
def getChildrenData():
'''public List getChildrenData(final String childPath)
public List getChildrenData()
'''
pass
def hasDetailData():
'''public boolean hasDetailData(final String childPath)
'''
pass
def hasChildren():
'''public boolean hasChildren()
'''
pass
def isCurrentActionNull():
'''public boolean isCurrentActionNull()
'''
pass
def getCurrentData():
'''public Element getCurrentData()
public String getCurrentData(final String col)
'''
pass
def getCurrentObject():
'''public StructureObject getCurrentObject()
'''
pass
def getParentData():
'''public Element getParentData()
public String getParentData(final String col)
'''
pass
def getAttr():
'''public String getAttr(final String col, final String attr)
public String getAttr(final String attr)
'''
pass
def removeFromCurrentData():
'''public void removeFromCurrentData(final String col)
'''
pass
def removeChildData():
'''public void removeChildData(final String childName, final int index)
'''
pass
def removeChildren():
'''public void removeChildren(final String childName)
'''
pass
def getRowStamp():
'''public String getRowStamp()
'''
pass
def getCurrentDataAsBytes():
'''public byte[] getCurrentDataAsBytes(final String col)
'''
pass
def getCurrentDataAsBinaryText():
'''public String getCurrentDataAsBinaryText(final String col)
'''
pass
def isCurrentDataNull():
'''public boolean isCurrentDataNull(final String col)
'''
pass
def isGLDataNull():
'''public boolean isGLDataNull(final String col)
public boolean isGLDataNull(final String col, final String orgId)
'''
pass
def isInCurrentData():
'''public boolean isInCurrentData(final String col)
'''
pass
def isCurrentDataChanged():
'''public boolean isCurrentDataChanged(final String col)
'''
pass
def getCurrentDataAsDouble():
'''public double getCurrentDataAsDouble(final String col)
'''
pass
def getCurrentDataAsInt():
'''public int getCurrentDataAsInt(final String col)
'''
pass
def getCurrentDataAsLong():
'''public long getCurrentDataAsLong(final String col)
'''
pass
def getCurrentDataAsDate():
'''public Date getCurrentDataAsDate(final String col)
'''
pass
def getCurrentDataAsBoolean():
'''public boolean getCurrentDataAsBoolean(final String col)
'''
pass
def getCurrentDataAsElement():
'''public Element getCurrentDataAsElement(final String key)
'''
pass
def getCurrentDataAsList():
'''public List getCurrentDataAsList(final String key)
'''
pass
def getGL():
'''public String getGL(final String col)
public String getGL(final String col, final String orgId)
'''
pass
def getGLComponent():
'''public String getGLComponent(final String col, final int order, final String orgId)
'''
pass
def getCurrentAction():
'''public String getCurrentAction()
'''
pass
def setCurrentData():
'''public void setCurrentData(final String colname, final String data)
public void setCurrentData(final String colname, final Date data)
public void setCurrentData(final String colname, final double data)
public void setCurrentData(final String colname, final long data)
public void setCurrentData(final String colname, final int data)
public void setCurrentData(final String colname, final byte[] data)
'''
pass
def setCurrentAction():
'''public void setCurrentAction(final String action)
'''
pass
def setCurrentDataNull():
'''public void setCurrentDataNull(final String colname)
'''
pass
def setGL():
'''public void setGL(final String colname, final String[] glSegments, final String orgId)
public void setGL(final String colname, final String glString)
'''
pass
def setXPathData():
'''public void setXPathData(final String xPathExpression, final String data)
'''
pass
def getCurrentDataAsString():
'''public String getCurrentDataAsString(final String col)
'''
pass
def getCurrentNamespacePrefix():
'''public String getCurrentNamespacePrefix()
'''
pass
def getCurrentNamespaceURI():
'''public String getCurrentNamespaceURI()
'''
pass
def setCurrentNamespace():
'''public void setCurrentNamespace(final String pref, final String uri)
'''
pass
def getNamespaces():
'''public Map<String, String> getNamespaces()
'''
pass
def setNamespaces():
'''public void setNamespaces(final String key, final String data)
'''
pass
def getOverrideType():
'''public int getOverrideType(final String col, final int currentType)
'''
pass
def toString():
'''public String toString()
'''
pass
