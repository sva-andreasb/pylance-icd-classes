def StructureData():
    '''public StructureData()
    public StructureData(final String operaton, final String osName, final String lang, final int size, final boolean isEvent, final boolean isResponse)
    public StructureData(final Document input)
    public StructureData(final byte[] data)
    public StructureData(final String data)
    '''
def isIR():
    '''public boolean isIR()
    '''
def isBroken():
    '''public boolean isBroken()
    '''
def addIntObject():
    '''public void addIntObject()
    '''
def addObjectStructure():
    '''public void addObjectStructure()
    '''
def moveToNextIntObject():
    '''public boolean moveToNextIntObject()
    '''
def moveToNextObjectStructure():
    '''public boolean moveToNextObjectStructure()
    '''
def moveToPrevIntObject():
    '''public boolean moveToPrevIntObject()
    '''
def moveToPrevObjectStructure():
    '''public boolean moveToPrevObjectStructure()
    '''
def moveToFirstIntObject():
    '''public void moveToFirstIntObject()
    '''
def moveToFirstObjectStruture():
    '''public void moveToFirstObjectStruture()
    '''
def removeCurrentIntObject():
    '''public void removeCurrentIntObject()
    '''
def removeCurrentObjectStructure():
    '''public void removeCurrentObjectStructure()
    '''
def removeChildrenFromPrimaryObject():
    '''public void removeChildrenFromPrimaryObject()
    '''
def removeChildren():
    '''public void removeChildren()
    '''
def getData():
    '''public Document getData()
    '''
def hasDocument():
    '''public boolean hasDocument()
    '''
def getDataAsBytes():
    '''public byte[] getDataAsBytes()
    '''
def getDataAsString():
    '''public String getDataAsString()
    '''
def getOriginalByteData():
    '''public byte[] getOriginalByteData()
    '''
def clone():
    '''public Object clone()
    '''
def breakData():
    '''public void breakData()
    '''
def breakIntObject():
    '''public void breakIntObject()
    '''
def breakObjectStructure():
    '''public void breakObjectStructure()
    '''
def setMicData():
    '''public StructureObject setMicData(final Element data)
    '''
def createChildrenData():
    '''public void createChildrenData(final String name, final boolean setAsCurrent)
    '''
def setParentAsCurrent():
    '''public boolean setParentAsCurrent()
    '''
def getChildrenData():
    '''public List getChildrenData()
    '''
def getIntObjectList():
    '''public List getIntObjectList()
    '''
def getPrimaryObjectList():
    '''public List getPrimaryObjectList()
    '''
def getHierarchyObjectList():
    '''public List getHierarchyObjectList()
    '''
def getSize():
    '''public int getSize()
    '''
def isMultiIntObject():
    '''public boolean isMultiIntObject()
    '''
def isMultiObjectStructure():
    '''public boolean isMultiObjectStructure()
    '''
def getPrimaryObjectName():
    '''public String getPrimaryObjectName()
    '''
def getLanguage():
    '''public String getLanguage()
    '''
def getTransLanguage():
    '''public String getTransLanguage()
    '''
def getPrimaryObject():
    '''public Element getPrimaryObject()
    '''
def getPrimaryObjectAsObject():
    '''public Object getPrimaryObjectAsObject()
    '''
def getStructureObject():
    '''public StructureObject getStructureObject(final int pos)
    public StructureObject getStructureObject(final String xPathExpression)
    '''
def getAction():
    '''public String getAction()
    '''
def isActionNull():
    '''public boolean isActionNull()
    '''
def isPatch():
    '''public boolean isPatch()
    '''
def setIsPatch():
    '''public void setIsPatch(final boolean isPatch)
    '''
def getMessageID():
    '''public String getMessageID()
    '''
def removeCurrentData():
    '''public void removeCurrentData()
    '''
def setPrimaryObject():
    '''public void setPrimaryObject(final Element h)
    public void setPrimaryObject(final String name)
    '''
def setCurrentPosition():
    '''public void setCurrentPosition(final int pos)
    '''
def getCurrentPosition():
    '''public int getCurrentPosition()
    '''
def getRootName():
    '''public String getRootName()
    '''
def setAction():
    '''public void setAction(final String action)
    '''
def setActionNull():
    '''public void setActionNull()
    '''
def setChildrenData():
    '''public void setChildrenData(final List<Element> l)
    '''
def setAsCurrent():
    '''public StructureObject setAsCurrent(final Element data)
    public StructureObject setAsCurrent(final Object data)
    public void setAsCurrent(final List data, final int i)
    public StructureObject setAsCurrent()
    public StructureObject setAsCurrent(final String xPathExpression)
    '''
def getXPathData():
    '''public String getXPathData(final String xPathExpression)
    '''
def getStructureObjectList():
    '''public List getStructureObjectList(final String xPathExpression)
    '''
def setMessageID():
    '''public void setMessageID(final String id)
    '''
def setMboArray():
    '''public void setMboArray(final ArrayList<MboRemote> in)
    '''
def setCurrentMbo():
    '''public void setCurrentMbo(final MboRemote mbo)
    '''
def getCurrentMbo():
    '''public MboRemote getCurrentMbo()
    '''
def getMboArray():
    '''public ArrayList<MboRemote> getMboArray()
    '''
def getRealMbo():
    '''public MboRemote getRealMbo(final String objectName)
    '''
def setRealMbo():
    '''public void setRealMbo(final MboRemote rm)
    '''
def getCurrentObject():
    '''public StructureObject getCurrentObject()
    '''
def clear():
    '''public void clear()
    '''
def getBuild():
    '''public String getBuild()
    '''
def getMajorVersion():
    '''public String getMajorVersion()
    '''
def getMinorVersion():
    '''public String getMinorVersion()
    '''
def getDbBuild():
    '''public String getDbBuild()
    '''
def getJsonRequest():
    '''public OslcRequest getJsonRequest()
    '''
def getMboFromMemory():
    '''public MboRemote getMboFromMemory()
    '''
def setJsonRequest():
    '''public void setJsonRequest(final OslcRequest jsonRequest)
    '''
def toString():
    '''public String toString()
    '''
