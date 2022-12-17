sid = "short  4177"
LINK_TYPE_TITLE_OR_TEXT = "byte  0"
LINK_TYPE_VALUES = "byte  1"
LINK_TYPE_CATEGORIES = "byte  2"
LINK_TYPE_SECONDARY_CATEGORIES = "byte  3"
REFERENCE_TYPE_DEFAULT_CATEGORIES = "byte  0"
REFERENCE_TYPE_DIRECT = "byte  1"
REFERENCE_TYPE_WORKSHEET = "byte  2"
REFERENCE_TYPE_NOT_USED = "byte  3"
REFERENCE_TYPE_ERROR_REPORTED = "byte  4"
def ():
    '''returns LinkedDataRecord\n\n
    ()\n
    (final RecordInputStream in)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final LittleEndianOutput out)\n
    '''
def getSid():
    '''returns short\n\n
    getSid()\n
    '''
def clone():
    '''returns LinkedDataRecord\n\n
    clone()\n
    '''
def getLinkType():
    '''returns byte\n\n
    getLinkType()\n
    '''
def setLinkType():
    '''returns None\n\n
    setLinkType(final byte field_1_linkType)\n
    '''
def getReferenceType():
    '''returns byte\n\n
    getReferenceType()\n
    '''
def setReferenceType():
    '''returns None\n\n
    setReferenceType(final byte field_2_referenceType)\n
    '''
def getOptions():
    '''returns short\n\n
    getOptions()\n
    '''
def setOptions():
    '''returns None\n\n
    setOptions(final short field_3_options)\n
    '''
def getIndexNumberFmtRecord():
    '''returns short\n\n
    getIndexNumberFmtRecord()\n
    '''
def setIndexNumberFmtRecord():
    '''returns None\n\n
    setIndexNumberFmtRecord(final short field_4_indexNumberFmtRecord)\n
    '''
def getFormulaOfLink():
    '''returns Ptg[]\n\n
    getFormulaOfLink()\n
    '''
def setFormulaOfLink():
    '''returns None\n\n
    setFormulaOfLink(final Ptg[] ptgs)\n
    '''
def setCustomNumberFormat():
    '''returns None\n\n
    setCustomNumberFormat(final boolean value)\n
    '''
def isCustomNumberFormat():
    '''returns boolean\n\n
    isCustomNumberFormat()\n
    '''
