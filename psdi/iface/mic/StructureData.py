def ():
    '''returns StructureData\n\n
    ()\n
    (final String operaton, final String osName, final String lang, final int size, final boolean isEvent, final boolean isResponse)\n
    (final Document input)\n
    (final byte[] data)\n
    (final String data)\n
    '''
def isIR():
    '''returns boolean\n\n
    isIR()\n
    '''
def isBroken():
    '''returns boolean\n\n
    isBroken()\n
    '''
def addIntObject():
    '''returns None\n\n
    addIntObject()\n
    '''
def addObjectStructure():
    '''returns None\n\n
    addObjectStructure()\n
    '''
def moveToNextIntObject():
    '''returns boolean\n\n
    moveToNextIntObject()\n
    '''
def moveToNextObjectStructure():
    '''returns boolean\n\n
    moveToNextObjectStructure()\n
    '''
def moveToPrevIntObject():
    '''returns boolean\n\n
    moveToPrevIntObject()\n
    '''
def moveToPrevObjectStructure():
    '''returns boolean\n\n
    moveToPrevObjectStructure()\n
    '''
def moveToFirstIntObject():
    '''returns None\n\n
    moveToFirstIntObject()\n
    '''
def moveToFirstObjectStruture():
    '''returns None\n\n
    moveToFirstObjectStruture()\n
    '''
def removeCurrentIntObject():
    '''returns None\n\n
    removeCurrentIntObject()\n
    '''
def removeCurrentObjectStructure():
    '''returns None\n\n
    removeCurrentObjectStructure()\n
    '''
def removeChildrenFromPrimaryObject():
    '''returns None\n\n
    removeChildrenFromPrimaryObject()\n
    '''
def removeChildren():
    '''returns None\n\n
    removeChildren()\n
    '''
def getData():
    '''returns Document\n\n
    getData()\n
    '''
def hasDocument():
    '''returns boolean\n\n
    hasDocument()\n
    '''
def getDataAsBytes():
    '''returns byte[]\n\n
    getDataAsBytes()\n
    '''
def getDataAsString():
    '''returns String\n\n
    getDataAsString()\n
    '''
def getOriginalByteData():
    '''returns byte[]\n\n
    getOriginalByteData()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def breakData():
    '''returns None\n\n
    breakData()\n
    '''
def breakIntObject():
    '''returns None\n\n
    breakIntObject()\n
    '''
def breakObjectStructure():
    '''returns None\n\n
    breakObjectStructure()\n
    '''
def setMicData():
    '''returns StructureObject\n\n
    setMicData(final Element data)\n
    '''
def createChildrenData():
    '''returns None\n\n
    createChildrenData(final String name, final boolean setAsCurrent)\n
    '''
def setParentAsCurrent():
    '''returns boolean\n\n
    setParentAsCurrent()\n
    '''
def getChildrenData():
    '''returns List\n\n
    getChildrenData()\n
    '''
def getIntObjectList():
    '''returns List\n\n
    getIntObjectList()\n
    '''
def getPrimaryObjectList():
    '''returns List\n\n
    getPrimaryObjectList()\n
    '''
def getHierarchyObjectList():
    '''returns List\n\n
    getHierarchyObjectList()\n
    '''
def getSize():
    '''returns int\n\n
    getSize()\n
    '''
def isMultiIntObject():
    '''returns boolean\n\n
    isMultiIntObject()\n
    '''
def isMultiObjectStructure():
    '''returns boolean\n\n
    isMultiObjectStructure()\n
    '''
def getPrimaryObjectName():
    '''returns String\n\n
    getPrimaryObjectName()\n
    '''
def getLanguage():
    '''returns String\n\n
    getLanguage()\n
    '''
def getTransLanguage():
    '''returns String\n\n
    getTransLanguage()\n
    '''
def getPrimaryObject():
    '''returns Element\n\n
    getPrimaryObject()\n
    '''
def getPrimaryObjectAsObject():
    '''returns Object\n\n
    getPrimaryObjectAsObject()\n
    '''
def getStructureObject():
    '''returns StructureObject\n\n
    getStructureObject(final int pos)\n
    getStructureObject(final String xPathExpression)\n
    '''
def getAction():
    '''returns String\n\n
    getAction()\n
    '''
def isActionNull():
    '''returns boolean\n\n
    isActionNull()\n
    '''
def isPatch():
    '''returns boolean\n\n
    isPatch()\n
    '''
def setIsPatch():
    '''returns None\n\n
    setIsPatch(final boolean isPatch)\n
    '''
def getMessageID():
    '''returns String\n\n
    getMessageID()\n
    '''
def removeCurrentData():
    '''returns None\n\n
    removeCurrentData()\n
    '''
def setPrimaryObject():
    '''returns None\n\n
    setPrimaryObject(final Element h)\n
    setPrimaryObject(final String name)\n
    '''
def setCurrentPosition():
    '''returns None\n\n
    setCurrentPosition(final int pos)\n
    '''
def getCurrentPosition():
    '''returns int\n\n
    getCurrentPosition()\n
    '''
def getRootName():
    '''returns String\n\n
    getRootName()\n
    '''
def setAction():
    '''returns None\n\n
    setAction(final String action)\n
    '''
def setActionNull():
    '''returns None\n\n
    setActionNull()\n
    '''
def setChildrenData():
    '''returns None\n\n
    setChildrenData(final List<Element> l)\n
    '''
def setAsCurrent():
    '''returns StructureObject\n\n
    setAsCurrent(final Element data)\n
    setAsCurrent(final Object data)\n
    setAsCurrent(final List data, final int i)\n
    setAsCurrent()\n
    setAsCurrent(final String xPathExpression)\n
    '''
def getXPathData():
    '''returns String\n\n
    getXPathData(final String xPathExpression)\n
    '''
def getStructureObjectList():
    '''returns List\n\n
    getStructureObjectList(final String xPathExpression)\n
    '''
def setMessageID():
    '''returns None\n\n
    setMessageID(final String id)\n
    '''
def setMboArray():
    '''returns None\n\n
    setMboArray(final ArrayList<MboRemote> in)\n
    '''
def setCurrentMbo():
    '''returns None\n\n
    setCurrentMbo(final MboRemote mbo)\n
    '''
def getCurrentMbo():
    '''returns MboRemote\n\n
    getCurrentMbo()\n
    '''
def getMboArray():
    '''returns ArrayList<MboRemote>\n\n
    getMboArray()\n
    '''
def getRealMbo():
    '''returns MboRemote\n\n
    getRealMbo(final String objectName)\n
    '''
def setRealMbo():
    '''returns None\n\n
    setRealMbo(final MboRemote rm)\n
    '''
def getCurrentObject():
    '''returns StructureObject\n\n
    getCurrentObject()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def getBuild():
    '''returns String\n\n
    getBuild()\n
    '''
def getMajorVersion():
    '''returns String\n\n
    getMajorVersion()\n
    '''
def getMinorVersion():
    '''returns String\n\n
    getMinorVersion()\n
    '''
def getDbBuild():
    '''returns String\n\n
    getDbBuild()\n
    '''
def getJsonRequest():
    '''returns OslcRequest\n\n
    getJsonRequest()\n
    '''
def getMboFromMemory():
    '''returns MboRemote\n\n
    getMboFromMemory()\n
    '''
def setJsonRequest():
    '''returns None\n\n
    setJsonRequest(final OslcRequest jsonRequest)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
