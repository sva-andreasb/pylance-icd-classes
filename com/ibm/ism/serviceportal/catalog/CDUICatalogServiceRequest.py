def ():
    '''returns CDUICatalogServiceRequest\n\n
    (final MboRemote sr)\n
    '''
def setAttributes():
    '''returns None\n\n
    setAttributes(final List<CDUICatalogAttribute> attributes, final boolean modifyFlags)\n
    '''
def getAllSpecAttributesName():
    '''returns Set<String>\n\n
    getAllSpecAttributesName()\n
    '''
def addSpecAttribute():
    '''returns None\n\n
    addSpecAttribute(final String attribute, final String specAttribute)\n
    '''
def getAttributeData():
    '''returns JSONObject\n\n
    getAttributeData(final CDUICatalogAttribute ca, final boolean paging, final int pageSize, final int pageNum, final String searchValueInTable, final boolean loadDomain)\n
    '''
def getAllAttributeData():
    '''returns JSONArray\n\n
    getAllAttributeData(final List<CDUICatalogAttribute> attributes)\n
    '''
def getTableAttributeData():
    '''returns JSONArray\n\n
    getTableAttributeData(final List<CDUICatalogTableAttribute> attributes)\n
    '''
def getSpecAttribute():
    '''returns String\n\n
    getSpecAttribute(final String attributeName)\n
    '''
def getSR():
    '''returns MboRemote\n\n
    getSR()\n
    '''
def getSpec():
    '''returns PmScCRSpecRemote\n\n
    getSpec()\n
    '''
def getCR():
    '''returns PmScCRRemote\n\n
    getCR()\n
    '''
def initialize():
    '''returns None\n\n
    initialize(final MboRemote sr)\n
    '''
def getRelativeMboSet():
    '''returns MboSetRemote\n\n
    getRelativeMboSet(final String attribute)\n
    '''
