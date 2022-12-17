def ():
    '''returns MboValue\n\n
    ()\n
    '''
def construct():
    '''returns None\n\n
    construct(final Mbo mbo, final MboValueInfo mvInfo)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def initValue():
    '''returns None\n\n
    initValue()\n
    '''
def getMboValueData():
    '''returns MboValueData\n\n
    getMboValueData()\n
    getMboValueData(final boolean ignoreFieldFlags)\n
    '''
def getMbo():
    '''returns Mbo\n\n
    getMbo()\n
    '''
def getDefault():
    '''returns String\n\n
    getDefault()\n
    '''
def hasLongDescription():
    '''returns boolean\n\n
    hasLongDescription()\n
    '''
def setDefault():
    '''returns None\n\n
    setDefault(final String val)\n
    '''
def setValueNull():
    '''returns None\n\n
    setValueNull(final long accessModifier)\n
    setValueNull()\n
    '''
def _setValueNull():
    '''returns None\n\n
    _setValueNull()\n
    '''
def isNull():
    '''returns boolean\n\n
    isNull()\n
    '''
def getCurrentValue():
    '''returns MaxType\n\n
    getCurrentValue()\n
    '''
def getInitialValue():
    '''returns MaxType\n\n
    getInitialValue()\n
    '''
def getPreviousValue():
    '''returns MaxType\n\n
    getPreviousValue()\n
    '''
def setCurrentFieldAccess():
    '''returns None\n\n
    setCurrentFieldAccess(final long access)\n
    '''
def resetCurrentFieldAccess():
    '''returns None\n\n
    resetCurrentFieldAccess()\n
    '''
def getCurrentFieldAccess():
    '''returns long\n\n
    getCurrentFieldAccess()\n
    '''
def isModified():
    '''returns boolean\n\n
    isModified()\n
    '''
def isReadOnly():
    '''returns boolean\n\n
    isReadOnly()\n
    '''
def setReadOnly():
    '''returns None\n\n
    setReadOnly(final boolean ro)\n
    '''
def isHidden():
    '''returns boolean\n\n
    isHidden()\n
    '''
def setHidden():
    '''returns None\n\n
    setHidden(final boolean val)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getAttributeName():
    '''returns String\n\n
    getAttributeName()\n
    '''
def getMboValueInfo():
    '''returns MboValueInfo\n\n
    getMboValueInfo()\n
    '''
def getLength():
    '''returns int\n\n
    getLength()\n
    '''
def getScale():
    '''returns int\n\n
    getScale()\n
    '''
def getColumnTitle():
    '''returns String\n\n
    getColumnTitle()\n
    '''
def hasList():
    '''returns boolean\n\n
    hasList()\n
    '''
def getList():
    '''returns MboSetRemote\n\n
    getList()\n
    '''
def smartFill():
    '''returns MboSetRemote\n\n
    smartFill(final String value, final boolean exact)\n
    '''
def smartFind():
    '''returns MboSetRemote\n\n
    smartFind(final String value, final boolean exact)\n
    smartFind(final String object, final String value, final boolean exact)\n
    '''
def getMatchingAttr():
    '''returns String\n\n
    getMatchingAttr()\n
    getMatchingAttr(final String sourceObjectName)\n
    '''
def isRequired():
    '''returns boolean\n\n
    isRequired()\n
    '''
def setRequired():
    '''returns None\n\n
    setRequired(final boolean state)\n
    '''
def isPersistent():
    '''returns boolean\n\n
    isPersistent()\n
    '''
def isExtended():
    '''returns boolean\n\n
    isExtended()\n
    '''
def isGuaranteedUnique():
    '''returns boolean\n\n
    isGuaranteedUnique()\n
    '''
def setGuaranteedUnique():
    '''returns None\n\n
    setGuaranteedUnique(final boolean flag)\n
    '''
def autoKey():
    '''returns None\n\n
    autoKey()\n
    '''
def autoKeyByMboSiteOrg():
    '''returns None\n\n
    autoKeyByMboSiteOrg()\n
    '''
def addMboValueListener():
    '''returns None\n\n
    addMboValueListener(final MboValueListener l)\n
    '''
def getListeners():
    '''returns Vector<MboValueListener>\n\n
    getListeners()\n
    '''
def removeMboValueListener():
    '''returns None\n\n
    removeMboValueListener(final MboValueListener l)\n
    '''
def checkFieldAccess():
    '''returns None\n\n
    checkFieldAccess(final long accessModifier)\n
    '''
def hasFieldAccess():
    '''returns boolean\n\n
    hasFieldAccess(final long accessModifier)\n
    '''
def setFlags():
    '''returns None\n\n
    setFlags(final long flags)\n
    setFlags(final long flags, final MXException mxe)\n
    '''
def getFlags():
    '''returns long\n\n
    getFlags()\n
    '''
def setFlag():
    '''returns None\n\n
    setFlag(final long flag, final boolean state)\n
    setFlag(final long flag, final boolean state, final MXException mxe)\n
    '''
def isFlagSet():
    '''returns boolean\n\n
    isFlagSet(final long flag)\n
    '''
def getFieldFlagFromMbo():
    '''returns None\n\n
    getFieldFlagFromMbo(final long flag)\n
    '''
def getMXException():
    '''returns MXException\n\n
    getMXException()\n
    '''
def isToBeValidated():
    '''returns boolean\n\n
    isToBeValidated()\n
    '''
def setToBeValidated():
    '''returns None\n\n
    setToBeValidated(final boolean value)\n
    '''
def getIntegrationService():
    '''returns ServiceRemote\n\n
    getIntegrationService()\n
    '''
def rollbackToCheckpoint():
    '''returns None\n\n
    rollbackToCheckpoint()\n
    '''
def takeCheckpoint():
    '''returns None\n\n
    takeCheckpoint()\n
    '''
def setValueFromLookup():
    '''returns None\n\n
    setValueFromLookup(final MboRemote sourceMbo)\n
    '''
def getAppLink():
    '''returns String[]\n\n
    getAppLink()\n
    '''
def getLookupName():
    '''returns String\n\n
    getLookupName()\n
    '''
def setBypassOperatorCheck():
    '''returns None\n\n
    setBypassOperatorCheck(final boolean val)\n
    '''
def setApplicationError():
    '''returns None\n\n
    setApplicationError(final ApplicationError appError)\n
    '''
def getApplicationError():
    '''returns ApplicationError\n\n
    getApplicationError()\n
    '''
def setCurProcessValue():
    '''returns None\n\n
    setCurProcessValue(final String value)\n
    '''
def getCurProcessValue():
    '''returns String\n\n
    getCurProcessValue()\n
    '''
def setApplicationRequired():
    '''returns None\n\n
    setApplicationRequired(final boolean appRequired)\n
    '''
def isApplicationRequired():
    '''returns boolean\n\n
    isApplicationRequired()\n
    '''
def isRecordHover():
    '''returns boolean\n\n
    isRecordHover()\n
    '''
def setRecordHover():
    '''returns None\n\n
    setRecordHover(final boolean isRecordHover)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
