def ():
    '''returns BIMProjectParser\n\n
    (final long flags)\n
    (final IdFactory idFactory, final MessageLogger logger, final Locale locale, final long flags)\n
    '''
def addConvertedField():
    '''returns None\n\n
    addConvertedField(final String tableName, final String fieldName, final String attributeName)\n
    '''
def getConvertedField():
    '''returns String\n\n
    getConvertedField(final String tableName, final String fieldName)\n
    '''
def addFile():
    '''returns None\n\n
    addFile(final InputFile cobieFile)\n
    '''
def addSkippedSpace():
    '''returns None\n\n
    addSkippedSpace(final String spaceName)\n
    '''
def isSpaceSkipped():
    '''returns boolean\n\n
    isSpaceSkipped(final String spaceName)\n
    '''
def addFilter():
    '''returns None\n\n
    addFilter(final Filter filter)\n
    '''
def filters():
    '''returns Iterator<Filter>\n\n
    filters()\n
    '''
def execute():
    '''returns None\n\n
    execute()\n
    '''
def deleteFiles():
    '''returns None\n\n
    deleteFiles(final String workingDirRoot)\n
    '''
def addPage():
    '''returns None\n\n
    addPage(final Page page)\n
    '''
def clenup():
    '''returns None\n\n
    clenup()\n
    '''
def resolveReferences():
    '''returns None\n\n
    resolveReferences()\n
    '''
def categoryFromAttribute():
    '''returns None\n\n
    categoryFromAttribute(String omniClassAttribute)\n
    '''
def spacesFromAttribute():
    '''returns None\n\n
    spacesFromAttribute(final String spaceAttrib)\n
    '''
def levelsFromAttribute():
    '''returns None\n\n
    levelsFromAttribute(final String levelAttrib)\n
    '''
def areaFromAttribute():
    '''returns None\n\n
    areaFromAttribute(final String areaAttribute)\n
    '''
def perimeterFromAttribute():
    '''returns None\n\n
    perimeterFromAttribute(final String perimeterAttribute)\n
    '''
def systemsFromAttribute():
    '''returns None\n\n
    systemsFromAttribute(String systemNameAttrib)\n
    '''
def associateCategoriesWithAttributeTypes():
    '''returns None\n\n
    associateCategoriesWithAttributeTypes(final String[] pageList)\n
    '''
def getValueList():
    '''returns ItemValueList\n\n
    getValueList(final HashSet<String> valueSet)\n
    '''
def caculateItemCount():
    '''returns None\n\n
    caculateItemCount()\n
    '''
def getPage():
    '''returns Page\n\n
    getPage(final String pageName)\n
    '''
def getItem():
    '''returns Item\n\n
    getItem(final String pageName, final String key)\n
    '''
def getAttributeType():
    '''returns ItemAttributeType\n\n
    getAttributeType(final String typeName)\n
    '''
def getCompanyFromContact():
    '''returns ItemCONTACT\n\n
    getCompanyFromContact(final String companyName)\n
    '''
def convertCase():
    '''returns String\n\n
    convertCase(final String s)\n
    '''
def getCategoryMap():
    '''returns AttributeTypeMap\n\n
    getCategoryMap()\n
    '''
def getLocale():
    '''returns Locale\n\n
    getLocale()\n
    '''
def getItemCount():
    '''returns int\n\n
    getItemCount()\n
    '''
def getVendorAttribute():
    '''returns String\n\n
    getVendorAttribute()\n
    '''
def printPage():
    '''returns None\n\n
    printPage(final Page page)\n
    '''
def printAll():
    '''returns None\n\n
    printAll()\n
    '''
def getLogger():
    '''returns MessageLogger\n\n
    getLogger()\n
    '''
def setLogger():
    '''returns None\n\n
    setLogger(final MessageLogger logger)\n
    '''
def setVendorAttribute():
    '''returns None\n\n
    setVendorAttribute(final String vendorAttribute)\n
    '''
def export():
    '''returns None\n\n
    export(final String fileName, final String[] pageList, final InputStream templateStream, final ExportProgressTracker tracker, final Exporter.ExportFormat fileFormat)\n
    '''
