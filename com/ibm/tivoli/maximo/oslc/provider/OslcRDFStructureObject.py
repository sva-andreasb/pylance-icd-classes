def OslcRDFStructureObject():
    '''public OslcRDFStructureObject(final String operaton, final String osName, final String lang, final int size, final boolean isEvent, final boolean isResponse)
    public OslcRDFStructureObject(final Document input)
    public OslcRDFStructureObject(final Resource data, final String mosName, final String path, final String messageType, final UserInfo userInfo)
    public OslcRDFStructureObject(final Element data)
    public OslcRDFStructureObject()
    '''
def getName():
    '''public String getName()
    '''
def getObjectPath():
    '''public String getObjectPath()
    '''
def getUserInfo():
    '''public UserInfo getUserInfo()
    '''
def createChildrenData():
    '''public void createChildrenData(final String name)
    '''
def getChildrenData():
    '''public List getChildrenData(final String childPath)
    public List getChildrenData()
    '''
def hasDetailData():
    '''public boolean hasDetailData(final String childPath)
    '''
def hasChildren():
    '''public boolean hasChildren()
    '''
def isCurrentActionNull():
    '''public boolean isCurrentActionNull()
    '''
def getCurrentData():
    '''public Element getCurrentData()
    public String getCurrentData(final String col)
    '''
def getCurrentObject():
    '''public StructureObject getCurrentObject()
    '''
def getParentData():
    '''public Element getParentData()
    public String getParentData(final String col)
    '''
def getAttr():
    '''public String getAttr(final String col, final String attr)
    public String getAttr(final String attr)
    '''
def removeFromCurrentData():
    '''public void removeFromCurrentData(final String col)
    '''
def removeChildData():
    '''public void removeChildData(final String childName, final int index)
    '''
def removeChildren():
    '''public void removeChildren(final String childName)
    '''
def getRowStamp():
    '''public String getRowStamp()
    '''
def getCurrentDataAsBytes():
    '''public byte[] getCurrentDataAsBytes(final String col)
    '''
def getCurrentDataAsBinaryText():
    '''public String getCurrentDataAsBinaryText(final String col)
    '''
def isCurrentDataNull():
    '''public boolean isCurrentDataNull(final String col)
    '''
def isGLDataNull():
    '''public boolean isGLDataNull(final String col)
    public boolean isGLDataNull(final String col, final String orgId)
    '''
def isInCurrentData():
    '''public boolean isInCurrentData(final String col)
    '''
def isCurrentDataChanged():
    '''public boolean isCurrentDataChanged(final String col)
    '''
def getCurrentDataAsDouble():
    '''public double getCurrentDataAsDouble(final String col)
    '''
def getCurrentDataAsInt():
    '''public int getCurrentDataAsInt(final String col)
    '''
def getCurrentDataAsLong():
    '''public long getCurrentDataAsLong(final String col)
    '''
def getCurrentDataAsDate():
    '''public Date getCurrentDataAsDate(final String col)
    '''
def getCurrentDataAsBoolean():
    '''public boolean getCurrentDataAsBoolean(final String col)
    '''
def getCurrentDataAsElement():
    '''public Element getCurrentDataAsElement(final String key)
    '''
def getCurrentDataAsList():
    '''public List getCurrentDataAsList(final String key)
    '''
def getGL():
    '''public String getGL(final String col)
    public String getGL(final String col, final String orgId)
    '''
def getGLComponent():
    '''public String getGLComponent(final String col, final int order, final String orgId)
    '''
def getCurrentAction():
    '''public String getCurrentAction()
    '''
def setCurrentData():
    '''public void setCurrentData(final String colname, final String data)
    public void setCurrentData(final String colname, final Date data)
    public void setCurrentData(final String colname, final double data)
    public void setCurrentData(final String colname, final long data)
    public void setCurrentData(final String colname, final int data)
    public void setCurrentData(final String colname, final byte[] data)
    '''
def setCurrentAction():
    '''public void setCurrentAction(final String action)
    '''
def setCurrentDataNull():
    '''public void setCurrentDataNull(final String colname)
    '''
def setGL():
    '''public void setGL(final String colname, final String[] glSegments, final String orgId)
    public void setGL(final String colname, final String glString)
    '''
def setXPathData():
    '''public void setXPathData(final String xPathExpression, final String data)
    '''
def getCurrentDataAsString():
    '''public String getCurrentDataAsString(final String col)
    '''
def getCurrentNamespacePrefix():
    '''public String getCurrentNamespacePrefix()
    '''
def getCurrentNamespaceURI():
    '''public String getCurrentNamespaceURI()
    '''
def setCurrentNamespace():
    '''public void setCurrentNamespace(final String pref, final String uri)
    '''
def getNamespaces():
    '''public Map<String, String> getNamespaces()
    '''
def setNamespaces():
    '''public void setNamespaces(final String key, final String data)
    '''
def getOverrideType():
    '''public int getOverrideType(final String col, final int currentType)
    '''
def toString():
    '''public String toString()
    '''
