def getClassName():
    '''returns String\n\n
    getClassName()\n
    '''
def ():
    '''returns ArtsAgentConfigurationJdo\n\n
    (final Guid guid, final TopologyActionContext ctx)\n
    ()\n
    '''
def getTimeDelay():
    '''returns String\n\n
    getTimeDelay()\n
    '''
def setTimeDelay():
    '''returns None\n\n
    setTimeDelay(final String a)\n
    '''
def hasTimeDelay():
    '''returns boolean\n\n
    hasTimeDelay()\n
    '''
def getAllAttributes():
    '''returns Map\n\n
    getAllAttributes()\n
    '''
def generateDisplayName():
    '''returns String\n\n
    generateDisplayName()\n
    '''
def sameJdo():
    '''returns boolean\n\n
    sameJdo(final ArtsAgentConfiguration obj, final Map objKeys, final TopologyActionContext ctx, final JdoUpdateMap updateMap)\n
    '''
def sameJdoTest():
    '''returns boolean\n\n
    sameJdoTest(final ArtsAgentConfiguration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)\n
    '''
def similarJdo():
    '''returns boolean\n\n
    similarJdo(final ArtsAgentConfigurationJdo obj)\n
    '''
def updateJdoByObj():
    '''returns None\n\n
    updateJdoByObj(final ArtsAgentConfiguration obj, final List guidMap, final TopologyActionContext ctx, final Set processedObjs, final JdoUpdateMap updateMap, final Map stknGuidMap, final String attrPriosFromDb)\n
    '''
def copyJdo():
    '''returns None\n\n
    copyJdo(final BaseJdo copyToJdo, final JdoUpdateMap updateMap)\n
    '''
def removeJdoRefs():
    '''returns None\n\n
    removeJdoRefs(final TopologyActionContext ctx)\n
    removeJdoRefs(final TopologyActionContext ctx, final Set removedGuidSet)\n
    '''
def deleteJdoRefs():
    '''returns None\n\n
    deleteJdoRefs(final TopologyActionContext ctx)\n
    deleteJdoRefs(final TopologyActionContext ctx, final Set removedGuidSet)\n
    '''
def restoreJdo():
    '''returns None\n\n
    restoreJdo(final TopologyActionContext ctx)\n
    '''
def compareJdo():
    '''returns ObjectCompareResults\n\n
    compareJdo(final BaseJdo o, final boolean includeDynamic, final boolean includeDeep)\n
    compareJdo(final BaseJdo o, final boolean includeDynamic, final boolean includeDeep, final TwoDimensionalMap refMap)\n
    '''
def compareJdoForMerge():
    '''returns ObjectCompareResults\n\n
    compareJdoForMerge(final BaseJdo o, final boolean includeDynamic, final boolean includeDeep)\n
    compareJdoForMerge(final BaseJdo o, final boolean includeDynamic, final boolean includeDeep, final TwoDimensionalMap refMap)\n
    '''
def versionedJdoExists():
    '''returns boolean\n\n
    versionedJdoExists(final TopologyActionContext ctx)\n
    '''
def jdoNewInstance():
    '''returns PersistenceCapable\n\n
    jdoNewInstance(final StateManager jdoStateManager, final Object o)\n
    jdoNewInstance(final StateManager jdoStateManager)\n
    '''
def jdoReplaceField():
    '''returns None\n\n
    jdoReplaceField(final int n)\n
    '''
def jdoReplaceFields():
    '''returns None\n\n
    jdoReplaceFields(final int[] array)\n
    '''
def jdoProvideField():
    '''returns None\n\n
    jdoProvideField(final int n)\n
    '''
def jdoProvideFields():
    '''returns None\n\n
    jdoProvideFields(final int[] array)\n
    '''
def jdoCopyFields():
    '''returns None\n\n
    jdoCopyFields(final Object o, final int[] array)\n
    '''
