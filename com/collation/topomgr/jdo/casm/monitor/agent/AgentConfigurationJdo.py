def getClassName():
    '''    public String getClassName()
    '''
def AgentConfigurationJdo():
    '''    public AgentConfigurationJdo(final Guid guid, final TopologyActionContext ctx)
    public AgentConfigurationJdo()
    '''
def getAll():
    '''    public static Collection getAll(final TopologyActionContext ctx, final boolean excludeSubclass)
    '''
def getAllWithRunId():
    '''    public static Collection getAllWithRunId(final TopologyActionContext ctx, final boolean excludeSubclass)
    '''
def gcJdo():
    '''    public static void gcJdo(final TopologyActionContext ctx)
    '''
def getAllAttributes():
    '''    public Map getAllAttributes()
    '''
def generateDisplayName():
    '''    public String generateDisplayName()
    '''
def persistJdo():
    '''    public static AgentConfigurationJdo persistJdo(final AgentConfiguration obj, final TopologyActionContext ctx)
    public static AgentConfigurationJdo persistJdo(final AgentConfiguration obj, final Map stknGuidMap, final TopologyActionContext ctx)
    public static AgentConfigurationJdo persistJdo(final AgentConfiguration obj, final List guidMap, final TopologyActionContext ctx, final Set processedObjs, final JdoUpdateMap updateMap, final Map stknGuidMap)
    '''
def persistJdo3():
    '''    public static AgentConfigurationJdo persistJdo3(final AgentConfiguration obj, final TopologyActionContext ctx, final Map stknGuidMap)
    '''
def getJdoByGuid():
    '''    public static BaseJdo getJdoByGuid(final AgentConfiguration obj, final TopologyActionContext ctx)
    '''
def getJdo():
    '''    public static BaseJdo getJdo(final AgentConfiguration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    '''
def findJdo():
    '''    public static BaseJdo findJdo(final AgentConfiguration obj, final List guidMap, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    public static BaseJdo findJdo(final AgentConfiguration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    '''
def findSpecificJdo():
    '''    public static BaseJdo findSpecificJdo(final AgentConfiguration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    '''
def findJdoTest():
    '''    public static BaseJdo findJdoTest(final AgentConfiguration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    '''
def findSpecificJdoTest():
    '''    public static BaseJdo findSpecificJdoTest(final AgentConfiguration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    '''
def sameJdo():
    '''    public boolean sameJdo(final AgentConfiguration obj, final Map objKeys, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    '''
def sameJdoTest():
    '''    public boolean sameJdoTest(final AgentConfiguration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    '''
def getJdoKeys():
    '''    public static Map getJdoKeys(final AgentConfiguration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    '''
def similarJdo():
    '''    public boolean similarJdo(final AgentConfigurationJdo obj)
    '''
def updateJdoByObj():
    '''    public void updateJdoByObj(final AgentConfiguration obj, final List guidMap, final TopologyActionContext ctx, final Set processedObjs, final JdoUpdateMap updateMap, final Map stknGuidMap, final String attrPriosFromDb)
    '''
def copyJdo():
    '''    public void copyJdo(final BaseJdo copyToJdo, final JdoUpdateMap updateMap)
    '''
def removeJdoRefs():
    '''    public void removeJdoRefs(final TopologyActionContext ctx)
    public void removeJdoRefs(final TopologyActionContext ctx, final Set removedGuidSet)
    '''
def deleteJdoRefs():
    '''    public void deleteJdoRefs(final TopologyActionContext ctx)
    public void deleteJdoRefs(final TopologyActionContext ctx, final Set removedGuidSet)
    '''
def restoreJdo():
    '''    public void restoreJdo(final TopologyActionContext ctx)
    '''
def compareJdo():
    '''    public ObjectCompareResults compareJdo(final BaseJdo o, final boolean includeDynamic, final boolean includeDeep)
    public ObjectCompareResults compareJdo(final BaseJdo o, final boolean includeDynamic, final boolean includeDeep, final TwoDimensionalMap refMap)
    '''
def compareJdoForMerge():
    '''    public ObjectCompareResults compareJdoForMerge(final BaseJdo o, final boolean includeDynamic, final boolean includeDeep)
    public ObjectCompareResults compareJdoForMerge(final BaseJdo o, final boolean includeDynamic, final boolean includeDeep, final TwoDimensionalMap refMap)
    '''
def versionedJdoExists():
    '''    public boolean versionedJdoExists(final TopologyActionContext ctx)
    '''
def jdoNewInstance():
    '''    public PersistenceCapable jdoNewInstance(final StateManager jdoStateManager, final Object o)
    public PersistenceCapable jdoNewInstance(final StateManager jdoStateManager)
    '''
def jdoReplaceField():
    '''    public void jdoReplaceField(final int n)
    '''
def jdoReplaceFields():
    '''    public void jdoReplaceFields(final int[] array)
    '''
def jdoProvideField():
    '''    public void jdoProvideField(final int n)
    '''
def jdoProvideFields():
    '''    public void jdoProvideFields(final int[] array)
    '''
def jdoCopyFields():
    '''    public void jdoCopyFields(final Object o, final int[] array)
    '''
