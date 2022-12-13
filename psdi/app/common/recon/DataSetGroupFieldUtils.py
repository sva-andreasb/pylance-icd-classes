def resetField():
    '''    public static void resetField(final MboRemote mbovField, final String fldName, final boolean isReadOnly, final boolean isRequired)
    public static void resetField(final MboValue mbv, final String fldName, final boolean isReadOnly, final boolean isRequired)
    public static void resetField(final MboRemote mbo, final String fldName)
    public static void resetField(final MboValue mbv, final String fldName)
    '''
def hasSpecs():
    '''    public static boolean hasSpecs(final MboValue mbvObjName, final String fldDataSetOwner)
    '''
def getRootSpecID():
    '''    public static String getRootSpecID(final MboValue mbvObjName, final String fldDataSetOwner)
    '''
def getSpecs():
    '''    public static String getSpecs(final MboValue mbvObjName, final String fldDataSetOwner)
    '''
def checkIfRootClassIsSet():
    '''    public static boolean checkIfRootClassIsSet(final MboValue mbvObjName, final String fldDataSetOwner)
    '''
def getAllLevelAncestorIds():
    '''    public static String[] getAllLevelAncestorIds(final MboRemote mbo, final String classStructId, final boolean includingSelf)
    '''
def setAllAttributesReadOnly():
    '''    public static void setAllAttributesReadOnly(final Mbo mbo, final boolean readOnly)
    '''
def validateTaskFilterType():
    '''    public static void validateTaskFilterType(final Mbo mboTask)
    '''
def setDataSetsReadOnly():
    '''    public static void setDataSetsReadOnly(final MboRemote mbo, final boolean readOnly)
    '''
def checkValueExists():
    '''    public static void checkValueExists(final MboRemote mbo, final String attribute)
    '''
def countAfterSave():
    '''    public static int countAfterSave(final MboSetRemote mbos)
    '''
def updateTaskComparisonResultStatus():
    '''    public static void updateTaskComparisonResultStatus(final MboRemote task)
    public static void updateTaskComparisonResultStatus(final MboRemote task, final boolean required)
    '''
def getTranslatedValue():
    '''    public static String getTranslatedValue(final Translate translator, final String domainId, final String value)
    public static String getTranslatedValue(final Translate translator, final String domainId, final MboRemote mbo, final String attribute)
    '''
