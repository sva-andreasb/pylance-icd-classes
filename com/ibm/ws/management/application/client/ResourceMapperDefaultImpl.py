def ():
    '''returns ResourceTaskTypeInfo\n\n
    ()\n
    (final String taskName, final Object resType, final Object taskAttr, final Object typeAttr, final String[] warningMsgInfo, final String[] misTypeWarningMsgInfo)\n
    (final String taskName, final Object resType, final Object taskAttr, final Object typeAttr, final boolean supportMultipleValues, final String[] warningMsgInfo, final String[] misTypeWarningMsgInfo)\n
    '''
def getConfigFilesToLoad():
    '''returns List\n\n
    getConfigFilesToLoad(final String operation)\n
    '''
def getInAppConfigFilesToLoad():
    '''returns List\n\n
    getInAppConfigFilesToLoad(final String operation)\n
    '''
def getChildTypesAndObjects():
    '''returns Hashtable\n\n
    getChildTypesAndObjects(final EObject ob)\n
    '''
def getSubtypes():
    '''returns List\n\n
    getSubtypes(final EObject ob)\n
    '''
def getTypesForTask():
    '''returns List\n\n
    getTypesForTask(final String taskName)\n
    getTypesForTask(final AppDeploymentTask task, final String[] taskData)\n
    '''
def getResourceTypeAttr():
    '''returns List\n\n
    getResourceTypeAttr(final String resType)\n
    '''
def getColumnValue():
    '''returns Hashtable\n\n
    getColumnValue(final AppDeploymentTask task, final String[] data)\n
    '''
def getResourceValuesWithAttrsAndObjects():
    '''returns Hashtable\n\n
    getResourceValuesWithAttrsAndObjects(final String resType, final List refO)\n
    '''
def getResourceValuesWithObjects():
    '''returns Hashtable\n\n
    getResourceValuesWithObjects(final String resType, final List refO)\n
    '''
def addValidationTypes():
    '''returns None\n\n
    addValidationTypes(final List types)\n
    '''
def validateInScopeResource():
    '''returns String[]\n\n
    validateInScopeResource(final AppDeploymentTask task, final String[] taskData, final Hashtable resObjTbl, final boolean searchInAllScope, final List targets, final List outOfScopeResInfo)\n
    '''
def validateMisTypeResource():
    '''returns String[]\n\n
    validateMisTypeResource(final AppDeploymentTask task, final String[] taskData, final Hashtable resValueTbl, final List targets, final List outOfScopeMsgs, final List misTypeMsgs)\n
    '''
def postDataToValidate():
    '''returns String[]\n\n
    postDataToValidate(final AppDeploymentTask task, final String[] data)\n
    '''
def buildWarningMsg():
    '''returns String\n\n
    buildWarningMsg(final String taskName, final Hashtable invalidResInfo)\n
    '''
def getInAppTaskResource():
    '''returns Hashtable\n\n
    getInAppTaskResource(final AppDeploymentController controller)\n
    '''
def resourceObjectsPostProcessing():
    '''returns None\n\n
    resourceObjectsPostProcessing(final Hashtable targetToNodeTbl, final String resType, final Hashtable valuesToObjectTbl)\n
    '''
def getTaskName():
    '''returns String\n\n
    getTaskName()\n
    '''
def getResType():
    '''returns Object\n\n
    getResType()\n
    '''
def getTaskAttr():
    '''returns Object\n\n
    getTaskAttr()\n
    '''
def getTypeAttr():
    '''returns Object\n\n
    getTypeAttr()\n
    '''
def getSupportMultipleValues():
    '''returns boolean\n\n
    getSupportMultipleValues()\n
    '''
def getValidationWarningMsgInfo():
    '''returns String[]\n\n
    getValidationWarningMsgInfo()\n
    '''
def getMisTypeWarningMsgInfo():
    '''returns String[]\n\n
    getMisTypeWarningMsgInfo()\n
    '''
