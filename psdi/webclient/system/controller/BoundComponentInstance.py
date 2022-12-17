ID = "String  \"id\""
CSS_CLASS = "String  \"cssclass\""
DATA_ATTRIBUTE = "String  \"dataattribute\""
DOMAIN = "String  \"domain\""
KEY = "String  \"key\""
TYPEAHEADATTRS = "String  \"ta_attrs\""
REMARKS = "String  \"remarks\""
TITLE = "String  \"title\""
QUERY = "String  \"query\""
LENGTH = "String  \"length\""
TRUELENGTH = "String  \"truelength\""
SCALE = "String  \"scale\""
IS_NUMERIC = "String  \"isnumeric\""
HAS_LONG_DESCRIPTION = "String  \"haslongdescription\""
INT_TYPE = "String  \"inttype\""
IS_PERSISTENT = "String  \"ispersistent\""
ENTITY_NAME = "String  \"entityname\""
OBJECT_NAME = "String  \"objectname\""
ATTRIBUTE_NAME = "String  \"attributename\""
COLUMN_NAME = "String  \"columnname\""
BOUND_LABEL = "String  \"boundlabel\""
FIELD_LABEL = "String  \"fieldlabel\""
HIDE_LABEL = "String  \"hidelabel\""
INTERNAL = "String  \"internal\""
LABEL = "String  \"label\""
DEFAULT_LABEL = "String  \"defaultlabel\""
SIZE = "String  \"size\""
LABELFORMAT = "String  \"labelformat\""
INVALID_BINDING = "String  \"Invalid Binding\""
BAD_BINDING_CSS = "String  \"unbound\""
LONGDESC_ATTRIBUTE_SUFFIX = "String  \"_longdescription\""
EVENT_PRIORITY = "String  \"eventpriority\""
TAKESVALUE = "String  \"takesvalue\""
SYNCHRONOUS = "String  \"synchronous\""
PRIORITY_DATATYPE = "int  0"
PRIORITY_VALIDATION = "int  1"
PRIORITY_FLUSH = "int  2"
def ():
    '''returns BoundComponentInstance\n\n
    ()\n
    '''
def updateCachedDataValue():
    '''returns None\n\n
    updateCachedDataValue(final String value)\n
    '''
def hasChanged():
    '''returns boolean\n\n
    hasChanged()\n
    '''
def hasDataChanged():
    '''returns boolean\n\n
    hasDataChanged()\n
    '''
def hasLongDescChanged():
    '''returns boolean\n\n
    hasLongDescChanged()\n
    '''
def hasReadonlyChanged():
    '''returns boolean\n\n
    hasReadonlyChanged()\n
    '''
def hasRequiredChanged():
    '''returns boolean\n\n
    hasRequiredChanged()\n
    '''
def setDataValid():
    '''returns None\n\n
    setDataValid(final boolean isDataValid)\n
    '''
def isDataValid():
    '''returns boolean\n\n
    isDataValid()\n
    '''
def getInputMode():
    '''returns String\n\n
    getInputMode()\n
    '''
def getInputModeWithoutPasswordPrefix():
    '''returns String\n\n
    getInputModeWithoutPasswordPrefix()\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def getString():
    '''returns String\n\n
    getString()\n
    '''
def getBoolean():
    '''returns boolean\n\n
    getBoolean()\n
    '''
def readOnlyCheck():
    '''returns None\n\n
    readOnlyCheck()\n
    '''
def isReadOnly():
    '''returns boolean\n\n
    isReadOnly()\n
    '''
def isRequired():
    '''returns boolean\n\n
    isRequired()\n
    '''
def getLongDescription():
    '''returns String\n\n
    getLongDescription()\n
    '''
def hasLongDescription():
    '''returns boolean\n\n
    hasLongDescription()\n
    '''
def applink():
    '''returns int\n\n
    applink()\n
    '''
def selectvalue():
    '''returns int\n\n
    selectvalue()\n
    '''
def isOnCurrentRow():
    '''returns boolean\n\n
    isOnCurrentRow()\n
    '''
def isRowDeleted():
    '''returns boolean\n\n
    isRowDeleted()\n
    '''
def getQbeNameWithPrepend():
    '''returns String\n\n
    getQbeNameWithPrepend()\n
    '''
def processProfile():
    '''returns int\n\n
    processProfile(final String profileName)\n
    '''
def getDataBean():
    '''returns DataBean\n\n
    getDataBean()\n
    '''
def exceptionhandled():
    '''returns int\n\n
    exceptionhandled()\n
    '''
def datelookup():
    '''returns int\n\n
    datelookup()\n
    '''
def getLookupName():
    '''returns String\n\n
    getLookupName()\n
    '''
def getApplink():
    '''returns String\n\n
    getApplink()\n
    '''
def isDefault():
    '''returns boolean\n\n
    isDefault()\n
    '''
def isQuery():
    '''returns boolean\n\n
    isQuery()\n
    '''
def instantiatedatasrc():
    '''returns None\n\n
    instantiatedatasrc()\n
    '''
def getDataType():
    '''returns int\n\n
    getDataType()\n
    '''
def cleanup():
    '''returns None\n\n
    cleanup()\n
    '''
def isMasked():
    '''returns boolean\n\n
    isMasked()\n
    '''
def createChangedPropList():
    '''returns None\n\n
    createChangedPropList()\n
    '''
def render():
    '''returns int\n\n
    render()\n
    '''
def getDataValueInError():
    '''returns String\n\n
    getDataValueInError()\n
    '''
def setDataValueInError():
    '''returns None\n\n
    setDataValueInError(final String s)\n
    '''
def getLinkBack():
    '''returns ComponentInstance\n\n
    getLinkBack()\n
    '''
def dataRestrictionCheck():
    '''returns boolean\n\n
    dataRestrictionCheck()\n
    '''
def increment():
    '''returns int\n\n
    increment()\n
    '''
def decrement():
    '''returns int\n\n
    decrement()\n
    '''
def setcurrentdate():
    '''returns int\n\n
    setcurrentdate()\n
    '''
def setBoundAsRequired():
    '''returns None\n\n
    setBoundAsRequired()\n
    '''
def popexception():
    '''returns int\n\n
    popexception()\n
    '''
def getExceptionType():
    '''returns int\n\n
    getExceptionType()\n
    '''
def removeCurrentError():
    '''returns None\n\n
    removeCurrentError()\n
    '''
def getWarningMessages():
    '''returns String\n\n
    getWarningMessages()\n
    '''
def processAsyncYesNoCancel():
    '''returns int\n\n
    processAsyncYesNoCancel()\n
    '''
def processRevert():
    '''returns int\n\n
    processRevert()\n
    '''
def processIgnoreWarning():
    '''returns int\n\n
    processIgnoreWarning()\n
    '''
def processEdit():
    '''returns int\n\n
    processEdit()\n
    '''
def isRevert():
    '''returns boolean\n\n
    isRevert()\n
    '''
def resetIsRevert():
    '''returns None\n\n
    resetIsRevert()\n
    '''
def hasWarnings():
    '''returns boolean\n\n
    hasWarnings()\n
    '''
def getCurrentError():
    '''returns SetValueError\n\n
    getCurrentError()\n
    '''
def addAttributeError():
    '''returns None\n\n
    addAttributeError(final ERMAttributeError attributeError)\n
    '''
def addSetValueError():
    '''returns None\n\n
    addSetValueError(final SetValueError error)\n
    '''
def getWarningList():
    '''returns List<MXException>\n\n
    getWarningList()\n
    '''
def getHighestErrorLevel():
    '''returns int\n\n
    getHighestErrorLevel()\n
    '''
def clearErrors():
    '''returns None\n\n
    clearErrors()\n
    '''
def getExcDialogIcon():
    '''returns String\n\n
    getExcDialogIcon(final int exceptionType)\n
    '''
def isPasswordField():
    '''returns boolean\n\n
    isPasswordField()\n
    '''
def retryErrorValues():
    '''returns boolean\n\n
    retryErrorValues()\n
    '''
def getErrorForRow():
    '''returns SetValueError\n\n
    getErrorForRow(final int row)\n
    '''
def isSmartFillEnabled():
    '''returns boolean\n\n
    isSmartFillEnabled(final MboValueData mvd)\n
    '''
def getFieldInfo():
    '''returns JSONObject\n\n
    getFieldInfo()\n
    '''
def useMaxLength():
    '''returns boolean\n\n
    useMaxLength()\n
    '''
def getRenderIdForAutoFill():
    '''returns String\n\n
    getRenderIdForAutoFill()\n
    '''
def clearClassification():
    '''returns int\n\n
    clearClassification()\n
    '''
def getReadonlyStateMap():
    '''returns HashMap\n\n
    getReadonlyStateMap()\n
    '''
