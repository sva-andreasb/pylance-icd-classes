def StructureData():
'''public StructureData()
public StructureData(final String operaton, final String osName, final String lang, final int size, final boolean isEvent, final boolean isResponse)
public StructureData(final Document input)
public StructureData(final byte[] data)
public StructureData(final String data)
'''
pass
def isIR():
'''public boolean isIR()
'''
pass
def isBroken():
'''public boolean isBroken()
'''
pass
def addIntObject():
'''public void addIntObject()
'''
pass
def addObjectStructure():
'''public void addObjectStructure()
'''
pass
def moveToNextIntObject():
'''public boolean moveToNextIntObject()
'''
pass
def moveToNextObjectStructure():
'''public boolean moveToNextObjectStructure()
'''
pass
def moveToPrevIntObject():
'''public boolean moveToPrevIntObject()
'''
pass
def moveToPrevObjectStructure():
'''public boolean moveToPrevObjectStructure()
'''
pass
def moveToFirstIntObject():
'''public void moveToFirstIntObject()
'''
pass
def moveToFirstObjectStruture():
'''public void moveToFirstObjectStruture()
'''
pass
def removeCurrentIntObject():
'''public void removeCurrentIntObject()
'''
pass
def removeCurrentObjectStructure():
'''public void removeCurrentObjectStructure()
'''
pass
def removeChildrenFromPrimaryObject():
'''public void removeChildrenFromPrimaryObject()
'''
pass
def removeChildren():
'''public void removeChildren()
'''
pass
def getData():
'''public Document getData()
'''
pass
def hasDocument():
'''public boolean hasDocument()
'''
pass
def getDataAsBytes():
'''public byte[] getDataAsBytes()
'''
pass
def getDataAsString():
'''public String getDataAsString()
'''
pass
def getOriginalByteData():
'''public byte[] getOriginalByteData()
'''
pass
def clone():
'''public Object clone()
'''
pass
def breakData():
'''public void breakData()
'''
pass
def breakIntObject():
'''public void breakIntObject()
'''
pass
def breakObjectStructure():
'''public void breakObjectStructure()
'''
pass
def setMicData():
'''public StructureObject setMicData(final Element data)
'''
pass
def createChildrenData():
'''public void createChildrenData(final String name, final boolean setAsCurrent)
'''
pass
def setParentAsCurrent():
'''public boolean setParentAsCurrent()
'''
pass
def getChildrenData():
'''public List getChildrenData()
'''
pass
def getIntObjectList():
'''public List getIntObjectList()
'''
pass
def getPrimaryObjectList():
'''public List getPrimaryObjectList()
'''
pass
def getHierarchyObjectList():
'''public List getHierarchyObjectList()
'''
pass
def getSize():
'''public int getSize()
'''
pass
def isMultiIntObject():
'''public boolean isMultiIntObject()
'''
pass
def isMultiObjectStructure():
'''public boolean isMultiObjectStructure()
'''
pass
def getPrimaryObjectName():
'''public String getPrimaryObjectName()
'''
pass
def getLanguage():
'''public String getLanguage()
'''
pass
def getTransLanguage():
'''public String getTransLanguage()
'''
pass
def getPrimaryObject():
'''public Element getPrimaryObject()
'''
pass
def getPrimaryObjectAsObject():
'''public Object getPrimaryObjectAsObject()
'''
pass
def getStructureObject():
'''public StructureObject getStructureObject(final int pos)
public StructureObject getStructureObject(final String xPathExpression)
'''
pass
def getAction():
'''public String getAction()
'''
pass
def isActionNull():
'''public boolean isActionNull()
'''
pass
def isPatch():
'''public boolean isPatch()
'''
pass
def setIsPatch():
'''public void setIsPatch(final boolean isPatch)
'''
pass
def getMessageID():
'''public String getMessageID()
'''
pass
def removeCurrentData():
'''public void removeCurrentData()
'''
pass
def setPrimaryObject():
'''public void setPrimaryObject(final Element h)
public void setPrimaryObject(final String name)
'''
pass
def setCurrentPosition():
'''public void setCurrentPosition(final int pos)
'''
pass
def getCurrentPosition():
'''public int getCurrentPosition()
'''
pass
def getRootName():
'''public String getRootName()
'''
pass
def setAction():
'''public void setAction(final String action)
'''
pass
def setActionNull():
'''public void setActionNull()
'''
pass
def setChildrenData():
'''public void setChildrenData(final List<Element> l)
'''
pass
def setAsCurrent():
'''public StructureObject setAsCurrent(final Element data)
public StructureObject setAsCurrent(final Object data)
public void setAsCurrent(final List data, final int i)
public StructureObject setAsCurrent()
public StructureObject setAsCurrent(final String xPathExpression)
'''
pass
def getXPathData():
'''public String getXPathData(final String xPathExpression)
'''
pass
def getStructureObjectList():
'''public List getStructureObjectList(final String xPathExpression)
'''
pass
def setMessageID():
'''public void setMessageID(final String id)
'''
pass
def setMboArray():
'''public void setMboArray(final ArrayList<MboRemote> in)
'''
pass
def setCurrentMbo():
'''public void setCurrentMbo(final MboRemote mbo)
'''
pass
def getCurrentMbo():
'''public MboRemote getCurrentMbo()
'''
pass
def getMboArray():
'''public ArrayList<MboRemote> getMboArray()
'''
pass
def getRealMbo():
'''public MboRemote getRealMbo(final String objectName)
'''
pass
def setRealMbo():
'''public void setRealMbo(final MboRemote rm)
'''
pass
def getCurrentObject():
'''public StructureObject getCurrentObject()
'''
pass
def clear():
'''public void clear()
'''
pass
def getBuild():
'''public String getBuild()
'''
pass
def getMajorVersion():
'''public String getMajorVersion()
'''
pass
def getMinorVersion():
'''public String getMinorVersion()
'''
pass
def getDbBuild():
'''public String getDbBuild()
'''
pass
def getJsonRequest():
'''public OslcRequest getJsonRequest()
'''
pass
def getMboFromMemory():
'''public MboRemote getMboFromMemory()
'''
pass
def setJsonRequest():
'''public void setJsonRequest(final OslcRequest jsonRequest)
'''
pass
def toString():
'''public String toString()
'''
pass
