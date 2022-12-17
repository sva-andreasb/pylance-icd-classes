def ():
    '''returns MaxAttributeCfgSet\n\n
    (final MboServerInterface ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def setRelationName():
    '''returns None\n\n
    setRelationName(final String relationName)\n
    '''
def setOwner():
    '''returns None\n\n
    setOwner(final MboRemote mbo)\n
    '''
def didSetIsHandleColumn():
    '''returns boolean\n\n
    didSetIsHandleColumn()\n
    '''
def setIsHandleColumn():
    '''returns None\n\n
    setIsHandleColumn()\n
    '''
def canAdd():
    '''returns None\n\n
    canAdd()\n
    '''
def loadCreateTable():
    '''returns None\n\n
    loadCreateTable(final String keycolumn)\n
    '''
def getNativeColumns():
    '''returns None\n\n
    getNativeColumns(final String keycolumn)\n
    '''
def addRowToSet():
    '''returns MboRemote\n\n
    addRowToSet(String name, final String maxtype, final int length, final int scale, final boolean nulls, final String defaultvalue, final boolean isldowner, final int prikeycolseq)\n
    '''
def addLongDescriptionRowToSet():
    '''returns MboRemote\n\n
    addLongDescriptionRowToSet(final MboRemote baseCol)\n
    '''
def addHasLDRowToSet():
    '''returns MboRemote\n\n
    addHasLDRowToSet()\n
    '''
def getValueCHANGE():
    '''returns String\n\n
    getValueCHANGE()\n
    '''
def setBypassSameasPush():
    '''returns None\n\n
    setBypassSameasPush(final boolean value)\n
    '''
def getBypassSameasPush():
    '''returns boolean\n\n
    getBypassSameasPush()\n
    '''
def applySameAsValuesWithinThisTable():
    '''returns None\n\n
    applySameAsValuesWithinThisTable(final MboRemote sameasMbo)\n
    '''
def LDOwnerExists():
    '''returns boolean\n\n
    LDOwnerExists()\n
    '''
def textSearchAttrExists():
    '''returns boolean\n\n
    textSearchAttrExists()\n
    '''
def attributeExists():
    '''returns MboRemote\n\n
    attributeExists(final String attrName)\n
    '''
def columnExists():
    '''returns MboRemote\n\n
    columnExists(final String colName)\n
    '''
def LDKeyExists():
    '''returns boolean\n\n
    LDKeyExists()\n
    '''
def getLangOrAuditColumn():
    '''returns MboRemote\n\n
    getLangOrAuditColumn(final MboRemote baseCol, final boolean anyStatus)\n
    '''
def getLongDescriptionAttribute():
    '''returns MboRemote\n\n
    getLongDescriptionAttribute(final MboRemote baseCol)\n
    '''
def addKeyColumn():
    '''returns MboRemote\n\n
    addKeyColumn(final String keyColumnName)\n
    '''
def changeKeyColumn():
    '''returns MboRemote\n\n
    changeKeyColumn(final MboRemote mbo, final String keyColumnName)\n
    '''
def getValidName():
    '''returns String\n\n
    getValidName(String root, final boolean attrName)\n
    '''
def addLanguageColumn():
    '''returns MboRemote\n\n
    addLanguageColumn(final String attributeName)\n
    '''
def resetForObjectValidation():
    '''returns None\n\n
    resetForObjectValidation()\n
    '''
def validate():
    '''returns None\n\n
    validate()\n
    '''
