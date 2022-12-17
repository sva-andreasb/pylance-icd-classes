COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
PARENT_TAG = "String  \"_parent_\""
AUFOFILL_TAG = "String  \"_auto_\""
ACTIVE_TAG = "String  \"_active_\""
TRUE_VALUE_TAG = "String  \"_true_\""
FALSE_VALUE_TAG = "String  \"_false_\""
DIRECTION_OPL_TO_RM = "int  1"
DIRECTION_RM_TO_OPL = "int  2"
MAPPING_TYPE_REGULAR = "int  0"
MAPPING_TYPE_SKIP = "int  1"
MAPPING_TYPE_SKIP_DEFAULT_MAP_VALUES = "int  2"
MAPPING_TYPE_INTERNAL = "int  3"
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def ():
    '''returns IloMappingDefinition\n\n
    (final String oplElementName, final String tableID, final int direction, final int mappingType)\n
    '''
def getMappingType():
    '''returns int\n\n
    getMappingType()\n
    '''
def setMappingType():
    '''returns None\n\n
    setMappingType(final int mappingType)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    clone()\n
    '''
def setInvokeOplScriptMethodName():
    '''returns None\n\n
    setInvokeOplScriptMethodName(final String script)\n
    '''
def isSubMapping():
    '''returns boolean\n\n
    isSubMapping()\n
    '''
def getOplElementName():
    '''returns String\n\n
    getOplElementName()\n
    '''
def getTableID():
    '''returns String\n\n
    getTableID()\n
    '''
def getMappedColumns():
    '''returns Collection<String>\n\n
    getMappedColumns()\n
    '''
def getOplFieldForColumn():
    '''returns String\n\n
    getOplFieldForColumn(final String columnId)\n
    '''
def getDirection():
    '''returns int\n\n
    getDirection()\n
    '''
def setDirection():
    '''returns None\n\n
    setDirection(final int direction)\n
    '''
def isRMToOpl():
    '''returns boolean\n\n
    isRMToOpl()\n
    '''
def isOplToRM():
    '''returns boolean\n\n
    isOplToRM()\n
    '''
def getColumnOrTableID():
    '''returns String\n\n
    getColumnOrTableID(final String fieldID)\n
    '''
def getFirstFieldPart():
    '''returns String\n\n
    getFirstFieldPart(final String fieldID)\n
    '''
def addFieldMapping():
    '''returns None\n\n
    addFieldMapping(final String columnOrTableID, String prefix, final String fieldName, final String defaultOplValue)\n
    '''
def getPrefixes():
    '''returns Collection<String>\n\n
    getPrefixes(final String rootPrefix)\n
    '''
def getInvokeOplScriptMethodName():
    '''returns String\n\n
    getInvokeOplScriptMethodName()\n
    '''
