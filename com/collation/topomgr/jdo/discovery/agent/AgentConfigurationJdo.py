def getClassName():
    '''returns String\n\n
    getClassName()\n
    '''
def ():
    '''returns AgentConfigurationJdo\n\n
    (final Guid guid, final TopologyActionContext ctx)\n
    ()\n
    '''
def getBidiConfigFlag():
    '''returns int\n\n
    getBidiConfigFlag()\n
    '''
def setBidiConfigFlag():
    '''returns None\n\n
    setBidiConfigFlag(final int a)\n
    '''
def hasBidiConfigFlag():
    '''returns boolean\n\n
    hasBidiConfigFlag()\n
    '''
def getClassPath():
    '''returns ClassPathEntry[]\n\n
    getClassPath()\n
    '''
def setClassPath():
    '''returns None\n\n
    setClassPath(final ClassPathEntry[] a)\n
    '''
def hasClassPath():
    '''returns boolean\n\n
    hasClassPath()\n
    '''
def addClassPath():
    '''returns boolean\n\n
    addClassPath(final ClassPathEntry obj)\n
    '''
def removeClassPath():
    '''returns boolean\n\n
    removeClassPath(final ClassPathEntry obj)\n
    '''
def getTemplateClassName():
    '''returns String\n\n
    getTemplateClassName()\n
    '''
def setTemplateClassName():
    '''returns None\n\n
    setTemplateClassName(final String a)\n
    '''
def hasTemplateClassName():
    '''returns boolean\n\n
    hasTemplateClassName()\n
    '''
def getAgentClassName():
    '''returns String\n\n
    getAgentClassName()\n
    '''
def setAgentClassName():
    '''returns None\n\n
    setAgentClassName(final String a)\n
    '''
def hasAgentClassName():
    '''returns boolean\n\n
    hasAgentClassName()\n
    '''
def getScopeSetName():
    '''returns String\n\n
    getScopeSetName()\n
    '''
def setScopeSetName():
    '''returns None\n\n
    setScopeSetName(final String a)\n
    '''
def hasScopeSetName():
    '''returns boolean\n\n
    hasScopeSetName()\n
    '''
def getBidiConfigFormat():
    '''returns String\n\n
    getBidiConfigFormat()\n
    '''
def setBidiConfigFormat():
    '''returns None\n\n
    setBidiConfigFormat(final String a)\n
    '''
def hasBidiConfigFormat():
    '''returns boolean\n\n
    hasBidiConfigFormat()\n
    '''
def getOriginalName():
    '''returns String\n\n
    getOriginalName()\n
    '''
def setOriginalName():
    '''returns None\n\n
    setOriginalName(final String a)\n
    '''
def hasOriginalName():
    '''returns boolean\n\n
    hasOriginalName()\n
    '''
def getSeedClassName():
    '''returns String\n\n
    getSeedClassName()\n
    '''
def setSeedClassName():
    '''returns None\n\n
    setSeedClassName(final String a)\n
    '''
def hasSeedClassName():
    '''returns boolean\n\n
    hasSeedClassName()\n
    '''
def getBidiProfile():
    '''returns String\n\n
    getBidiProfile()\n
    '''
def setBidiProfile():
    '''returns None\n\n
    setBidiProfile(final String a)\n
    '''
def hasBidiProfile():
    '''returns boolean\n\n
    hasBidiProfile()\n
    '''
def getObjectVersion():
    '''returns int\n\n
    getObjectVersion()\n
    '''
def setObjectVersion():
    '''returns None\n\n
    setObjectVersion(final int a)\n
    '''
def hasObjectVersion():
    '''returns boolean\n\n
    hasObjectVersion()\n
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
    sameJdo(final AgentConfiguration obj, final Map objKeys, final TopologyActionContext ctx, final JdoUpdateMap updateMap)\n
    '''
def sameJdoTest():
    '''returns boolean\n\n
    sameJdoTest(final AgentConfiguration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)\n
    '''
def similarJdo():
    '''returns boolean\n\n
    similarJdo(final AgentConfigurationJdo obj)\n
    '''
def updateJdoByObj():
    '''returns None\n\n
    updateJdoByObj(final AgentConfiguration obj, final List guidMap, final TopologyActionContext ctx, final Set processedObjs, final JdoUpdateMap updateMap, final Map stknGuidMap, final String attrPriosFromDb)\n
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
