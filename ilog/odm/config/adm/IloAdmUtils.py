COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
ANNOTATION_PROPERTIES_NAME = "String  \"IBM_ILOG_ODM_PROPERTIES\""
ANNOTATION_CONTENTMANAGER_CLASSNAME_PROPERTY_NAME = "String  \"CONTENTMANAGER_CLASSNAME\""
ANNOTATION_MASTER_TABLES_PROPERTY_NAME = "String  \"MASTER_TABLES\""
ANNOTATION_INITARGS_PROPERTY_NAME = "String  \"INITARGS\""
ANNOTATION_DERIVED_COLUMNS_PROPERTY_NAME = "String  \"DERIVED_COLUMNS\""
ANNOTATION_SINGLE_ROW_PROPERTY_NAME = "String  \"SINGLE_ROW\""
ANNOTATION_MIN_BOUND_PROPERTY_NAME = "String  \"MIN_BOUND\""
ANNOTATION_MAX_BOUND_PROPERTY_NAME = "String  \"MAX_BOUND\""
ANNOTATION_LEGACY_NAMESPACE_PROPERTY_NAME = "String  \"LEGACY_NS\""
ANNOTATION_TIMESTAMP_PRECISION_PROPERTY_NAME = "String  \"odme.timestampPrecision\""
MODEL_EXTENSION = "String  \"dbm\""
AT = "String  \"@\""
CUSTOM_ANNOTATION_PROPERTIES_NAME = "String  \"UDP\""
ANNOTATION_OBJECT_MODEL_PROPERTIES_NAME = "String  \"IBM_ILOG_ODM_DOM_PROPERTIES\""
ODME_SCHEMA_PROPERTY_PROJECT = "String  \"odme.project\""
ODME_SCHEMA_PROPERTY_MODEL_ID = "String  \"odme.modelId\""
ODME_SCHEMA_PROPERTY_MODEL_NAME = "String  \"odme.modelName\""
ODME_SCHEMA_PROPERTY_JAVA_SOURCE_DIRECTORY = "String  \"odme.java.sourceDirectory\""
ODME_SCHEMA_PROPERTY_JAVA_PACKAGE_ROOT = "String  \"odme.java.packageRoot\""
ODME_SCHEMA_PROPERTY_JAVA_COLLECTOR_CLASS = "String  \"odme.java.collectorClass\""
ODME_SCHEMA_PROPERTY_JAVA_CONFIGURATION_CLASS = "String  \"odme.java.configurationClass\""
ODME_SCHEMA_PROPERTY_JAVA_COLLECTOR_INTERFACES = "String  \"odme.java.collectorInterfaces\""
ODME_SCHEMA_PROPERTY_JAVA_COLLECTOR_ABSTRACT = "String  \"odme.java.collectorAbstract\""
ODME_TABLE_PROPERTY_CLASS_NAME = "String  \"odme.java.className\""
ODME_TABLE_PROPERTY_EXTERNAL_INTERFACES = "String  \"odme.java.externalInterfaces\""
ODME_TABLE_PROPERTY_COLLECTION_NAME = "String  \"odme.java.collectionName\""
ODME_TABLE_PROPERTY_NOT_APPLICABLE = "String  \"odme.java.notApplicable\""
ODME_TABLE_PROPERTY_ABSTRACT = "String  \"odme.java.abstract\""
ODME_COLUMN_PROPERTY_ATTRIBUTE_NAME = "String  \"odme.java.attributeName\""
ODME_COLUMN_PROPERTY_JAVA_TYPE = "String  \"odme.java.type\""
ODME_FOREIGN_KEY_PROPERTY_REFERENCE_NAME = "String  \"odme.java.referenceName\""
ODME_FOREIGN_KEY_PROPERTY_INVERTED_REFERENCE_NAME = "String  \"odme.java.invertedReferenceName\""
ODME_FOREIGN_KEY_PROPERTY_IS_INVERTED = "String  \"odme.java.isReferenceInverted\""
ALL_COLUMNS = "String  \"*\""
def ():
    '''returns InitArg\n\n
    ()\n
    (final Resource pdmResource)\n
    ()\n
    (final String name, final String value)\n
    '''
def createResource():
    '''returns Resource\n\n
    createResource(final URI uri)\n
    '''
def getXmiFactory():
    '''returns XMIResourceFactoryImpl\n\n
    getXmiFactory()\n
    '''
def getPdmStatus():
    '''returns IloPdmStatus\n\n
    getPdmStatus()\n
    '''
def setPdmStatus():
    '''returns None\n\n
    setPdmStatus(final IloPdmStatus _pdmStatus)\n
    '''
def getPdmResourceSet():
    '''returns ResourceSet\n\n
    getPdmResourceSet()\n
    '''
def setPdmResourceSet():
    '''returns None\n\n
    setPdmResourceSet(final ResourceSet _pdmResourceSet)\n
    '''
def getPdmResource():
    '''returns Resource\n\n
    getPdmResource()\n
    '''
def setPdmResource():
    '''returns None\n\n
    setPdmResource(final Resource _pdmResource)\n
    '''
def getPdmLastModified():
    '''returns long\n\n
    getPdmLastModified()\n
    '''
def setPdmLastModified():
    '''returns None\n\n
    setPdmLastModified(final long _pdmLastModified)\n
    '''
def refreshPdm():
    '''returns IloPdmStatus\n\n
    refreshPdm(final String path)\n
    '''
def loadPdm():
    '''returns IloPdmStatus\n\n
    loadPdm(final String pdmPath)\n
    '''
def resetPdmResource():
    '''returns None\n\n
    resetPdmResource()\n
    '''
def findSchema():
    '''returns None\n\n
    findSchema()\n
    '''
def getSchema():
    '''returns Schema\n\n
    getSchema()\n
    '''
def getTables():
    '''returns EList<Table>\n\n
    getTables()\n
    '''
def getSchemas():
    '''returns List<Schema>\n\n
    getSchemas()\n
    '''
def savePdmResoruce():
    '''returns None\n\n
    savePdmResoruce()\n
    '''
def getTableByName():
    '''returns BaseTable\n\n
    getTableByName(final String name)\n
    '''
def getTableByUUID():
    '''returns BaseTable\n\n
    getTableByUUID(final String uuid)\n
    '''
def getForeignKeyByUUID():
    '''returns ForeignKey\n\n
    getForeignKeyByUUID(final Table table, final String uuid)\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid()\n
    '''
def write():
    '''returns None\n\n
    write(final Table table)\n
    '''
def getDerivedCode():
    '''returns int\n\n
    getDerivedCode(final Column column)\n
    '''
def getContentManagerClassName():
    '''returns String\n\n
    getContentManagerClassName()\n
    '''
def setContentManagerClassName():
    '''returns None\n\n
    setContentManagerClassName(final String contentManagerClassName)\n
    '''
def getMasterTables():
    '''returns List<Table>\n\n
    getMasterTables()\n
    '''
def addMasterTable():
    '''returns None\n\n
    addMasterTable(final Table table)\n
    '''
def getDerivedColumns():
    '''returns List<Column>\n\n
    getDerivedColumns()\n
    '''
def addDerivedColumns():
    '''returns None\n\n
    addDerivedColumns(final Column column)\n
    '''
def isWholeTableDerived():
    '''returns boolean\n\n
    isWholeTableDerived()\n
    '''
def setWholeTableDerived():
    '''returns None\n\n
    setWholeTableDerived(final boolean wholeTableIsDerived)\n
    '''
def getInitArgs():
    '''returns List<InitArg>\n\n
    getInitArgs()\n
    '''
def addInitArgs():
    '''returns None\n\n
    addInitArgs(final String name, final String value)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def getValue():
    '''returns String\n\n
    getValue()\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final String value)\n
    '''
