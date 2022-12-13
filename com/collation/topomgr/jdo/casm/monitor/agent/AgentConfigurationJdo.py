def getClassName():
'''public String getClassName()
'''
pass
def AgentConfigurationJdo():
'''public AgentConfigurationJdo(final Guid guid, final TopologyActionContext ctx)
public AgentConfigurationJdo()
'''
pass
def getAll():
'''public static Collection getAll(final TopologyActionContext ctx, final boolean excludeSubclass)
'''
pass
def getAllWithRunId():
'''public static Collection getAllWithRunId(final TopologyActionContext ctx, final boolean excludeSubclass)
'''
pass
def gcJdo():
'''public static void gcJdo(final TopologyActionContext ctx)
'''
pass
def getAllAttributes():
'''public Map getAllAttributes()
'''
pass
def generateDisplayName():
'''public String generateDisplayName()
'''
pass
def persistJdo():
'''public static AgentConfigurationJdo persistJdo(final AgentConfiguration obj, final TopologyActionContext ctx)
public static AgentConfigurationJdo persistJdo(final AgentConfiguration obj, final Map stknGuidMap, final TopologyActionContext ctx)
public static AgentConfigurationJdo persistJdo(final AgentConfiguration obj, final List guidMap, final TopologyActionContext ctx, final Set processedObjs, final JdoUpdateMap updateMap, final Map stknGuidMap)
'''
pass
def persistJdo3():
'''public static AgentConfigurationJdo persistJdo3(final AgentConfiguration obj, final TopologyActionContext ctx, final Map stknGuidMap)
'''
pass
def getJdoByGuid():
'''public static BaseJdo getJdoByGuid(final AgentConfiguration obj, final TopologyActionContext ctx)
'''
pass
def getJdo():
'''public static BaseJdo getJdo(final AgentConfiguration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
'''
pass
def findJdo():
'''public static BaseJdo findJdo(final AgentConfiguration obj, final List guidMap, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
public static BaseJdo findJdo(final AgentConfiguration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
'''
pass
def findSpecificJdo():
'''public static BaseJdo findSpecificJdo(final AgentConfiguration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
'''
pass
def findJdoTest():
'''public static BaseJdo findJdoTest(final AgentConfiguration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
'''
pass
def findSpecificJdoTest():
'''public static BaseJdo findSpecificJdoTest(final AgentConfiguration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
'''
pass
def sameJdo():
'''public boolean sameJdo(final AgentConfiguration obj, final Map objKeys, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
'''
pass
def sameJdoTest():
'''public boolean sameJdoTest(final AgentConfiguration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
'''
pass
def getJdoKeys():
'''public static Map getJdoKeys(final AgentConfiguration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
'''
pass
def similarJdo():
'''public boolean similarJdo(final AgentConfigurationJdo obj)
'''
pass
def updateJdoByObj():
'''public void updateJdoByObj(final AgentConfiguration obj, final List guidMap, final TopologyActionContext ctx, final Set processedObjs, final JdoUpdateMap updateMap, final Map stknGuidMap, final String attrPriosFromDb)
'''
pass
def copyJdo():
'''public void copyJdo(final BaseJdo copyToJdo, final JdoUpdateMap updateMap)
'''
pass
def removeJdoRefs():
'''public void removeJdoRefs(final TopologyActionContext ctx)
public void removeJdoRefs(final TopologyActionContext ctx, final Set removedGuidSet)
'''
pass
def deleteJdoRefs():
'''public void deleteJdoRefs(final TopologyActionContext ctx)
public void deleteJdoRefs(final TopologyActionContext ctx, final Set removedGuidSet)
'''
pass
def restoreJdo():
'''public void restoreJdo(final TopologyActionContext ctx)
'''
pass
def compareJdo():
'''public ObjectCompareResults compareJdo(final BaseJdo o, final boolean includeDynamic, final boolean includeDeep)
public ObjectCompareResults compareJdo(final BaseJdo o, final boolean includeDynamic, final boolean includeDeep, final TwoDimensionalMap refMap)
'''
pass
def compareJdoForMerge():
'''public ObjectCompareResults compareJdoForMerge(final BaseJdo o, final boolean includeDynamic, final boolean includeDeep)
public ObjectCompareResults compareJdoForMerge(final BaseJdo o, final boolean includeDynamic, final boolean includeDeep, final TwoDimensionalMap refMap)
'''
pass
def versionedJdoExists():
'''public boolean versionedJdoExists(final TopologyActionContext ctx)
'''
pass
def jdoNewInstance():
'''public PersistenceCapable jdoNewInstance(final StateManager jdoStateManager, final Object o)
public PersistenceCapable jdoNewInstance(final StateManager jdoStateManager)
'''
pass
def jdoReplaceField():
'''public void jdoReplaceField(final int n)
'''
pass
def jdoReplaceFields():
'''public void jdoReplaceFields(final int[] array)
'''
pass
def jdoProvideField():
'''public void jdoProvideField(final int n)
'''
pass
def jdoProvideFields():
'''public void jdoProvideFields(final int[] array)
'''
pass
def jdoCopyFields():
'''public void jdoCopyFields(final Object o, final int[] array)
'''
pass
