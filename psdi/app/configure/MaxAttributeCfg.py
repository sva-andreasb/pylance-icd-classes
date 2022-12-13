def MaxAttributeCfg():
    '''public MaxAttributeCfg(final MboSet ms)
    '''
def init():
    '''public void init()
    '''
def add():
    '''public void add()
    '''
def canDelete():
    '''public void canDelete()
    '''
def delete():
    '''public void delete(final long accessModifier)
    '''
def deleteIndexesForAttribute():
    '''public void deleteIndexesForAttribute()
    '''
def canUndelete():
    '''public void canUndelete()
    '''
def undelete():
    '''public void undelete()
    '''
def appValidate():
    '''public void appValidate()
    '''
def getAuditColumnSet():
    '''public MboSetRemote getAuditColumnSet(final boolean anyStatus)
    '''
def getLangColumnSet():
    '''public MboSetRemote getLangColumnSet(final boolean anyStatus)
    '''
def getAuditColumn():
    '''public MboRemote getAuditColumn(final boolean anyStatus)
    '''
def getLangColumn():
    '''public MboRemote getLangColumn(final boolean anyStatus)
    '''
def langAndAuditMetadata():
    '''public void langAndAuditMetadata(final MboRemote baseCol)
    '''
def getSameAsParent():
    '''public MboRemote getSameAsParent()
    '''
def checkSameAsChild():
    '''public void checkSameAsChild()
    '''
def setValuesForSameAs():
    '''public void setValuesForSameAs(final MboRemote sameasMbo, final boolean changeMustBe, final boolean mustBeValue)
    '''
def preventInternalChanges():
    '''public boolean preventInternalChanges()
    '''
def sameAsMiscChecks():
    '''public void sameAsMiscChecks(final MboRemote sameasMbo, final boolean adjustYORN)
    '''
def setChanged():
    '''public void setChanged()
    '''
def getValidateOrder():
    '''public String[] getValidateOrder()
    '''
def isLocAllowed():
    '''public boolean isLocAllowed()
    '''
def getLocDefault():
    '''public boolean getLocDefault()
    '''
def nativeColumnExists():
    '''public boolean nativeColumnExists()
    '''
def setLengthAndScaleReadonlyState():
    '''public void setLengthAndScaleReadonlyState()
    '''
def validateDomain():
    '''public void validateDomain(final String domainid)
    public void validateDomain(final String domainid, final String errorTitle, final String attrmaxtype, final int attrlength, final int attrscale, final int whatToValidate)
    '''
def validateDefaultValue():
    '''public void validateDefaultValue()
    '''
def indexInvolvement():
    '''public boolean indexInvolvement()
    '''
def getCurrentNativeDatatype():
    '''public String getCurrentNativeDatatype()
    '''
def getNewNativeDatatype():
    '''public String getNewNativeDatatype()
    '''
def columnIsEmpty():
    '''public boolean columnIsEmpty()
    '''
def nullValueExists():
    '''public boolean nullValueExists()
    '''
def getCurrentAttribute():
    '''public MboRemote getCurrentAttribute()
    '''
def getNativeDateDefault():
    '''public String getNativeDateDefault()
    '''
def getDefaultString():
    '''public String getDefaultString()
    '''
def getSequenceInfo():
    '''public String[] getSequenceInfo()
    '''
def getSequenceMbo():
    '''public MboRemote getSequenceMbo()
    '''
def sequenceExists():
    '''public boolean sequenceExists(final String sequenceName, final boolean differentColumn)
    '''
def validateSearchType():
    '''public void validateSearchType()
    '''
def setSearchTypeValue():
    '''public void setSearchTypeValue()
    '''
def setSearchTypeReadonlyFlag():
    '''public void setSearchTypeReadonlyFlag()
    '''
def createAutokeyMbos():
    '''public void createAutokeyMbos(final String autokeyname)
    '''
def getMboValueData():
    '''public MboValueData getMboValueData(final String attribute)
    '''
def smartFill():
    '''public MboSetRemote smartFill(final String attribute, final String value, final boolean exact)
    '''
def clearNonEssentialRelatedSets():
    '''public void clearNonEssentialRelatedSets()
    '''
