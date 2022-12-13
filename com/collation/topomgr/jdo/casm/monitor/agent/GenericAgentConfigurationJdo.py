def getClassName():
    '''    public String getClassName()
    '''
def GenericAgentConfigurationJdo():
    '''    public GenericAgentConfigurationJdo(final Guid guid, final TopologyActionContext ctx)
    public GenericAgentConfigurationJdo()
    '''
def getRmiPort():
    '''    public int getRmiPort()
    '''
def setRmiPort():
    '''    public void setRmiPort(final int a)
    '''
def hasRmiPort():
    '''    public boolean hasRmiPort()
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
    '''    public static GenericAgentConfigurationJdo persistJdo(final GenericAgentConfiguration obj, final TopologyActionContext ctx)
    public static GenericAgentConfigurationJdo persistJdo(final GenericAgentConfiguration obj, final Map stknGuidMap, final TopologyActionContext ctx)
    public static GenericAgentConfigurationJdo persistJdo(final GenericAgentConfiguration obj, final List guidMap, final TopologyActionContext ctx, final Set processedObjs, final JdoUpdateMap updateMap, final Map stknGuidMap)
    '''
def persistJdo3():
    '''    public static GenericAgentConfigurationJdo persistJdo3(final GenericAgentConfiguration obj, final TopologyActionContext ctx, final Map stknGuidMap)
    '''
def getJdoByGuid():
    '''    public static BaseJdo getJdoByGuid(final GenericAgentConfiguration obj, final TopologyActionContext ctx)
    '''
def getJdo():
    '''    public static BaseJdo getJdo(final GenericAgentConfiguration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    '''
def findJdo():
    '''    public static BaseJdo findJdo(final GenericAgentConfiguration obj, final List guidMap, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    public static BaseJdo findJdo(final GenericAgentConfiguration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    '''
def findSpecificJdo():
    '''    public static BaseJdo findSpecificJdo(final GenericAgentConfiguration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    '''
def findJdoTest():
    '''    public static BaseJdo findJdoTest(final GenericAgentConfiguration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    '''
def findSpecificJdoTest():
    '''    public static BaseJdo findSpecificJdoTest(final GenericAgentConfiguration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    '''
def sameJdo():
    '''    public boolean sameJdo(final GenericAgentConfiguration obj, final Map objKeys, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    '''
def sameJdoTest():
    '''    public boolean sameJdoTest(final GenericAgentConfiguration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    '''
def getJdoKeys():
    '''    public static Map getJdoKeys(final GenericAgentConfiguration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    '''
def similarJdo():
    '''    public boolean similarJdo(final GenericAgentConfigurationJdo obj)
    '''
def updateJdoByObj():
    '''    public void updateJdoByObj(final GenericAgentConfiguration obj, final List guidMap, final TopologyActionContext ctx, final Set processedObjs, final JdoUpdateMap updateMap, final Map stknGuidMap, final String attrPriosFromDb)
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
def jdoGetrmiPort_():
    '''    public static final Integer jdoGetrmiPort_(final GenericAgentConfigurationJdo genericAgentConfigurationJdo)
    '''
def jdoSetrmiPort_():
    '''    public static final void jdoSetrmiPort_(final GenericAgentConfigurationJdo genericAgentConfigurationJdo, final Integer n)
    '''
