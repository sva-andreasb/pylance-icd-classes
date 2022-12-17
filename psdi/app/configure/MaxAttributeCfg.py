def ():
    '''returns MaxAttributeCfg\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def deleteIndexesForAttribute():
    '''returns None\n\n
    deleteIndexesForAttribute()\n
    '''
def canUndelete():
    '''returns None\n\n
    canUndelete()\n
    '''
def undelete():
    '''returns None\n\n
    undelete()\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def getAuditColumnSet():
    '''returns MboSetRemote\n\n
    getAuditColumnSet(final boolean anyStatus)\n
    '''
def getLangColumnSet():
    '''returns MboSetRemote\n\n
    getLangColumnSet(final boolean anyStatus)\n
    '''
def getAuditColumn():
    '''returns MboRemote\n\n
    getAuditColumn(final boolean anyStatus)\n
    '''
def getLangColumn():
    '''returns MboRemote\n\n
    getLangColumn(final boolean anyStatus)\n
    '''
def langAndAuditMetadata():
    '''returns None\n\n
    langAndAuditMetadata(final MboRemote baseCol)\n
    '''
def getSameAsParent():
    '''returns MboRemote\n\n
    getSameAsParent()\n
    '''
def checkSameAsChild():
    '''returns None\n\n
    checkSameAsChild()\n
    '''
def setValuesForSameAs():
    '''returns None\n\n
    setValuesForSameAs(final MboRemote sameasMbo, final boolean changeMustBe, final boolean mustBeValue)\n
    '''
def preventInternalChanges():
    '''returns boolean\n\n
    preventInternalChanges()\n
    '''
def sameAsMiscChecks():
    '''returns None\n\n
    sameAsMiscChecks(final MboRemote sameasMbo, final boolean adjustYORN)\n
    '''
def setChanged():
    '''returns None\n\n
    setChanged()\n
    '''
def getValidateOrder():
    '''returns String[]\n\n
    getValidateOrder()\n
    '''
def isLocAllowed():
    '''returns boolean\n\n
    isLocAllowed()\n
    '''
def getLocDefault():
    '''returns boolean\n\n
    getLocDefault()\n
    '''
def nativeColumnExists():
    '''returns boolean\n\n
    nativeColumnExists()\n
    '''
def setLengthAndScaleReadonlyState():
    '''returns None\n\n
    setLengthAndScaleReadonlyState()\n
    '''
def validateDomain():
    '''returns None\n\n
    validateDomain(final String domainid)\n
    validateDomain(final String domainid, final String errorTitle, final String attrmaxtype, final int attrlength, final int attrscale, final int whatToValidate)\n
    '''
def validateDefaultValue():
    '''returns None\n\n
    validateDefaultValue()\n
    '''
def indexInvolvement():
    '''returns boolean\n\n
    indexInvolvement()\n
    '''
def getCurrentNativeDatatype():
    '''returns String\n\n
    getCurrentNativeDatatype()\n
    '''
def getNewNativeDatatype():
    '''returns String\n\n
    getNewNativeDatatype()\n
    '''
def columnIsEmpty():
    '''returns boolean\n\n
    columnIsEmpty()\n
    '''
def nullValueExists():
    '''returns boolean\n\n
    nullValueExists()\n
    '''
def getCurrentAttribute():
    '''returns MboRemote\n\n
    getCurrentAttribute()\n
    '''
def getNativeDateDefault():
    '''returns String\n\n
    getNativeDateDefault()\n
    '''
def getDefaultString():
    '''returns String\n\n
    getDefaultString()\n
    '''
def getSequenceInfo():
    '''returns String[]\n\n
    getSequenceInfo()\n
    '''
def getSequenceMbo():
    '''returns MboRemote\n\n
    getSequenceMbo()\n
    '''
def sequenceExists():
    '''returns boolean\n\n
    sequenceExists(final String sequenceName, final boolean differentColumn)\n
    '''
def validateSearchType():
    '''returns None\n\n
    validateSearchType()\n
    '''
def setSearchTypeValue():
    '''returns None\n\n
    setSearchTypeValue()\n
    '''
def setSearchTypeReadonlyFlag():
    '''returns None\n\n
    setSearchTypeReadonlyFlag()\n
    '''
def createAutokeyMbos():
    '''returns None\n\n
    createAutokeyMbos(final String autokeyname)\n
    '''
def getMboValueData():
    '''returns MboValueData\n\n
    getMboValueData(final String attribute)\n
    '''
def smartFill():
    '''returns MboSetRemote\n\n
    smartFill(final String attribute, final String value, final boolean exact)\n
    '''
def clearNonEssentialRelatedSets():
    '''returns None\n\n
    clearNonEssentialRelatedSets()\n
    '''
