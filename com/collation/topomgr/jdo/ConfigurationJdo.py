def getClassName():
    '''public String getClassName()
    '''
def ConfigurationJdo():
    '''public ConfigurationJdo(final Guid guid, final TopologyActionContext ctx)
    public ConfigurationJdo()
    '''
def getVersion():
    '''public long getVersion()
    '''
def setVersion():
    '''public void setVersion(final long version)
    '''
def getPk():
    '''public String getPk()
    '''
def setPk():
    '''public void setPk(final String pk)
    '''
def getDeleted():
    '''public boolean getDeleted()
    '''
def setDeleted():
    '''public void setDeleted(final boolean d)
    '''
def delete():
    '''public void delete()
    public void delete(final Set removedGuidSet)
    '''
def undelete():
    '''public void undelete()
    '''
def getRunId():
    '''public long getRunId()
    '''
def setRunId():
    '''public void setRunId(final long id)
    '''
def getPriority():
    '''public int getPriority()
    '''
def setPriority():
    '''public void setPriority(final int priority)
    '''
def getCreatedBy():
    '''public String getCreatedBy()
    '''
def getLastModifiedTime():
    '''public long getLastModifiedTime()
    '''
def getLastModifiedBy():
    '''public String getLastModifiedBy()
    '''
def setCreatedBy():
    '''public void setCreatedBy(final String s)
    '''
def setLastModifiedTime():
    '''public void setLastModifiedTime(final long l)
    '''
def setLastModifiedBy():
    '''public void setLastModifiedBy(final String s)
    '''
def getDisplayName():
    '''public String getDisplayName()
    '''
def setDisplayName():
    '''public void setDisplayName(final String a)
    '''
def hasDisplayName():
    '''public boolean hasDisplayName()
    '''
def setAttrPrios():
    '''public void setAttrPrios(final String attrPrios)
    '''
def getAttrPrios():
    '''public String getAttrPrios()
    '''
def hasAttrPrios():
    '''public boolean hasAttrPrios()
    '''
def getName():
    '''public String getName()
    '''
def setName():
    '''public void setName(final String a)
    '''
def hasName():
    '''public boolean hasName()
    '''
def getMssGuid():
    '''public String getMssGuid()
    '''
def setMssGuid():
    '''public void setMssGuid(final String a)
    '''
def hasMssGuid():
    '''public boolean hasMssGuid()
    '''
def getOperationalStatus():
    '''public int getOperationalStatus()
    '''
def setOperationalStatus():
    '''public void setOperationalStatus(final int a)
    '''
def hasOperationalStatus():
    '''public boolean hasOperationalStatus()
    '''
def getEnabled():
    '''public boolean getEnabled()
    '''
def setEnabled():
    '''public void setEnabled(final boolean a)
    '''
def hasEnabled():
    '''public boolean hasEnabled()
    '''
def getRejectionReason():
    '''public String getRejectionReason()
    '''
def setRejectionReason():
    '''public void setRejectionReason(final String a)
    '''
def hasRejectionReason():
    '''public boolean hasRejectionReason()
    '''
def getFamilyName():
    '''public String getFamilyName()
    '''
def setFamilyName():
    '''public void setFamilyName(final String a)
    '''
def hasFamilyName():
    '''public boolean hasFamilyName()
    '''
def getObjectType():
    '''public String getObjectType()
    '''
def setObjectType():
    '''public void setObjectType(final String a)
    '''
def hasObjectType():
    '''public boolean hasObjectType()
    '''
def getExtendedAttributes():
    '''public byte[] getExtendedAttributes()
    '''
def setExtendedAttributes():
    '''public void setExtendedAttributes(final byte[] a)
    '''
def hasExtendedAttributes():
    '''public boolean hasExtendedAttributes()
    '''
def getBidiFlag():
    '''public int getBidiFlag()
    '''
def setBidiFlag():
    '''public void setBidiFlag(final int a)
    '''
def hasBidiFlag():
    '''public boolean hasBidiFlag()
    '''
def getDescription():
    '''public String getDescription()
    '''
def setDescription():
    '''public void setDescription(final String a)
    '''
def hasDescription():
    '''public boolean hasDescription()
    '''
def getCmdbSource():
    '''public Guid getCmdbSource()
    '''
def setCmdbSource():
    '''public void setCmdbSource(final Guid guid)
    '''
def hasCmdbSource():
    '''public boolean hasCmdbSource()
    '''
def getGuid():
    '''public Guid getGuid()
    '''
def setGuid():
    '''public void setGuid(final Guid guid)
    '''
def hasGuid():
    '''public boolean hasGuid()
    '''
def getCDMSource():
    '''public String getCDMSource()
    '''
def setCDMSource():
    '''public void setCDMSource(final String a)
    '''
def hasCDMSource():
    '''public boolean hasCDMSource()
    '''
def getAdminState():
    '''public int getAdminState()
    '''
def setAdminState():
    '''public void setAdminState(final int a)
    '''
def hasAdminState():
    '''public boolean hasAdminState()
    '''
def getSourceToken():
    '''public String getSourceToken()
    '''
def setSourceToken():
    '''public void setSourceToken(final String a)
    '''
def hasSourceToken():
    '''public boolean hasSourceToken()
    '''
def getContextIp():
    '''public String getContextIp()
    '''
def setContextIp():
    '''public void setContextIp(final String a)
    '''
def hasContextIp():
    '''public boolean hasContextIp()
    '''
def getLabel():
    '''public String getLabel()
    '''
def setLabel():
    '''public void setLabel(final String a)
    '''
def hasLabel():
    '''public boolean hasLabel()
    '''
def getBidiFormat():
    '''public String getBidiFormat()
    '''
def setBidiFormat():
    '''public void setBidiFormat(final String a)
    '''
def hasBidiFormat():
    '''public boolean hasBidiFormat()
    '''
def getAll():
    '''public static Collection getAll(final TopologyActionContext ctx, final boolean excludeSubclass)
    '''
def getAllWithRunId():
    '''public static Collection getAllWithRunId(final TopologyActionContext ctx, final boolean excludeSubclass)
    '''
def gcJdo():
    '''public static void gcJdo(final TopologyActionContext ctx)
    '''
def getAllAttributes():
    '''public Map getAllAttributes()
    '''
def generateDisplayName():
    '''public String generateDisplayName()
    '''
def persistJdo():
    '''public static ConfigurationJdo persistJdo(final Configuration obj, final TopologyActionContext ctx)
    public static ConfigurationJdo persistJdo(final Configuration obj, final Map stknGuidMap, final TopologyActionContext ctx)
    public static ConfigurationJdo persistJdo(final Configuration obj, final List guidMap, final TopologyActionContext ctx, final Set processedObjs, final JdoUpdateMap updateMap, final Map stknGuidMap)
    '''
def persistJdo3():
    '''public static ConfigurationJdo persistJdo3(final Configuration obj, final TopologyActionContext ctx, final Map stknGuidMap)
    '''
def getJdoByGuid():
    '''public static BaseJdo getJdoByGuid(final Configuration obj, final TopologyActionContext ctx)
    public static BaseJdo getJdoByGuid(final Guid guid, final TopologyActionContext ctx)
    '''
def getJdo():
    '''public static BaseJdo getJdo(final Configuration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    '''
def findJdo():
    '''public static BaseJdo findJdo(final Configuration obj, final List guidMap, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    public static BaseJdo findJdo(final Configuration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    '''
def findSpecificJdo():
    '''public static BaseJdo findSpecificJdo(final Configuration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    '''
def findJdoTest():
    '''public static BaseJdo findJdoTest(final Configuration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    '''
def findSpecificJdoTest():
    '''public static BaseJdo findSpecificJdoTest(final Configuration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    '''
def sameJdo():
    '''public boolean sameJdo(final Configuration obj, final Map objKeys, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    '''
def sameJdoTest():
    '''public boolean sameJdoTest(final Configuration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    '''
def getJdoKeys():
    '''public static Map getJdoKeys(final Configuration obj, final TopologyActionContext ctx, final JdoUpdateMap updateMap)
    '''
def similarJdo():
    '''public boolean similarJdo(final ConfigurationJdo obj)
    '''
def updateJdoByObj():
    '''public void updateJdoByObj(final Configuration obj, final List guidMap, final TopologyActionContext ctx, final Set processedObjs, final JdoUpdateMap updateMap, final Map stknGuidMap, final String attrPriosFromDb)
    '''
def copyJdo():
    '''public void copyJdo(final BaseJdo copyToJdo, final JdoUpdateMap updateMap)
    '''
def removeJdoRefs():
    '''public void removeJdoRefs(final TopologyActionContext ctx)
    public void removeJdoRefs(final TopologyActionContext ctx, final Set removedGuidSet)
    '''
def deleteJdoRefs():
    '''public void deleteJdoRefs(final TopologyActionContext ctx)
    public void deleteJdoRefs(final TopologyActionContext ctx, final Set removedGuidSet)
    '''
def restoreJdo():
    '''public void restoreJdo(final TopologyActionContext ctx)
    '''
def compareJdo():
    '''public ObjectCompareResults compareJdo(final BaseJdo o, final boolean includeDynamic, final boolean includeDeep)
    public ObjectCompareResults compareJdo(final BaseJdo o, final boolean includeDynamic, final boolean includeDeep, final TwoDimensionalMap refMap)
    '''
def compareJdoForMerge():
    '''public ObjectCompareResults compareJdoForMerge(final BaseJdo o, final boolean includeDynamic, final boolean includeDeep)
    public ObjectCompareResults compareJdoForMerge(final BaseJdo o, final boolean includeDynamic, final boolean includeDeep, final TwoDimensionalMap refMap)
    '''
def versionedJdoExists():
    '''public boolean versionedJdoExists(final TopologyActionContext ctx)
    '''
def jdoNewInstance():
    '''public PersistenceCapable jdoNewInstance(final StateManager jdoStateManager, final Object o)
    public PersistenceCapable jdoNewInstance(final StateManager jdoStateManager)
    '''
def jdoReplaceField():
    '''public void jdoReplaceField(final int n)
    '''
def jdoReplaceFields():
    '''public void jdoReplaceFields(final int[] array)
    '''
def jdoProvideField():
    '''public void jdoProvideField(final int n)
    '''
def jdoProvideFields():
    '''public void jdoProvideFields(final int[] array)
    '''
def jdoCopyFields():
    '''public void jdoCopyFields(final Object o, final int[] array)
    '''
def jdoGetPersistenceManager():
    '''public PersistenceManager jdoGetPersistenceManager()
    '''
def jdoGetObjectId():
    '''public Object jdoGetObjectId()
    '''
def jdoGetTransactionalObjectId():
    '''public Object jdoGetTransactionalObjectId()
    '''
def jdoIsDeleted():
    '''public boolean jdoIsDeleted()
    '''
def jdoIsDirty():
    '''public boolean jdoIsDirty()
    '''
def jdoIsNew():
    '''public boolean jdoIsNew()
    '''
def jdoIsPersistent():
    '''public boolean jdoIsPersistent()
    '''
def jdoIsTransactional():
    '''public boolean jdoIsTransactional()
    '''
def jdoPreSerialize():
    '''public void jdoPreSerialize()
    '''
def jdoMakeDirty():
    '''public void jdoMakeDirty(final String s)
    '''
def jdoReplaceFlags():
    '''public void jdoReplaceFlags()
    '''
def jdoReplaceStateManager():
    '''public synchronized void jdoReplaceStateManager(final StateManager jdoStateManager)
    '''
def jdoCopyKeyFieldsToObjectId():
    '''public void jdoCopyKeyFieldsToObjectId(final PersistenceCapable$ObjectIdFieldSupplier persistenceCapable$ObjectIdFieldSupplier, final Object o)
    public void jdoCopyKeyFieldsToObjectId(final Object o)
    '''
def jdoCopyKeyFieldsFromObjectId():
    '''public void jdoCopyKeyFieldsFromObjectId(final PersistenceCapable$ObjectIdFieldConsumer persistenceCapable$ObjectIdFieldConsumer, final Object o)
    public void jdoCopyKeyFieldsFromObjectId(final Object o)
    '''
def jdoNewObjectIdInstance():
    '''public Object jdoNewObjectIdInstance(final String pk)
    public Object jdoNewObjectIdInstance()
    '''
def jdoGetCDMSource_():
    '''public static final String jdoGetCDMSource_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetCDMSource_():
    '''public static final void jdoSetCDMSource_(final ConfigurationJdo configurationJdo, final String s)
    '''
def jdoGetadminState_():
    '''public static final Integer jdoGetadminState_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetadminState_():
    '''public static final void jdoSetadminState_(final ConfigurationJdo configurationJdo, final Integer n)
    '''
def jdoGetattrPrios_():
    '''public static final String jdoGetattrPrios_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetattrPrios_():
    '''public static final void jdoSetattrPrios_(final ConfigurationJdo configurationJdo, final String s)
    '''
def jdoGetbidiFlag_():
    '''public static final Integer jdoGetbidiFlag_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetbidiFlag_():
    '''public static final void jdoSetbidiFlag_(final ConfigurationJdo configurationJdo, final Integer n)
    '''
def jdoGetbidiFormat_():
    '''public static final String jdoGetbidiFormat_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetbidiFormat_():
    '''public static final void jdoSetbidiFormat_(final ConfigurationJdo configurationJdo, final String s)
    '''
def jdoGetcmdbSource_():
    '''public static final String jdoGetcmdbSource_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetcmdbSource_():
    '''public static final void jdoSetcmdbSource_(final ConfigurationJdo configurationJdo, final String s)
    '''
def jdoGetcontextIp_():
    '''public static final String jdoGetcontextIp_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetcontextIp_():
    '''public static final void jdoSetcontextIp_(final ConfigurationJdo configurationJdo, final String s)
    '''
def jdoGetcreatedBy_():
    '''public static final String jdoGetcreatedBy_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetcreatedBy_():
    '''public static final void jdoSetcreatedBy_(final ConfigurationJdo configurationJdo, final String s)
    '''
def jdoGetdeleted_():
    '''public static final boolean jdoGetdeleted_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetdeleted_():
    '''public static final void jdoSetdeleted_(final ConfigurationJdo configurationJdo, final boolean b)
    '''
def jdoGetdescription_():
    '''public static final String jdoGetdescription_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetdescription_():
    '''public static final void jdoSetdescription_(final ConfigurationJdo configurationJdo, final String s)
    '''
def jdoGetdisplayName_():
    '''public static final String jdoGetdisplayName_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetdisplayName_():
    '''public static final void jdoSetdisplayName_(final ConfigurationJdo configurationJdo, final String s)
    '''
def jdoGetenabled_():
    '''public static final Boolean jdoGetenabled_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetenabled_():
    '''public static final void jdoSetenabled_(final ConfigurationJdo configurationJdo, final Boolean b)
    '''
def jdoGetextendedAttributes_():
    '''public static final byte[] jdoGetextendedAttributes_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetextendedAttributes_():
    '''public static final void jdoSetextendedAttributes_(final ConfigurationJdo configurationJdo, final byte[] extendedAttributes_)
    '''
def jdoGetfamilyName_():
    '''public static final String jdoGetfamilyName_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetfamilyName_():
    '''public static final void jdoSetfamilyName_(final ConfigurationJdo configurationJdo, final String s)
    '''
def jdoGetguid_():
    '''public static final String jdoGetguid_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetguid_():
    '''public static final void jdoSetguid_(final ConfigurationJdo configurationJdo, final String s)
    '''
def jdoGetlabel_():
    '''public static final String jdoGetlabel_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetlabel_():
    '''public static final void jdoSetlabel_(final ConfigurationJdo configurationJdo, final String s)
    '''
def jdoGetlastModifiedBy_():
    '''public static final String jdoGetlastModifiedBy_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetlastModifiedBy_():
    '''public static final void jdoSetlastModifiedBy_(final ConfigurationJdo configurationJdo, final String s)
    '''
def jdoGetlastModifiedTime_():
    '''public static final Long jdoGetlastModifiedTime_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetlastModifiedTime_():
    '''public static final void jdoSetlastModifiedTime_(final ConfigurationJdo configurationJdo, final Long n)
    '''
def jdoGetmssGuid_():
    '''public static final String jdoGetmssGuid_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetmssGuid_():
    '''public static final void jdoSetmssGuid_(final ConfigurationJdo configurationJdo, final String s)
    '''
def jdoGetname_():
    '''public static final String jdoGetname_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetname_():
    '''public static final void jdoSetname_(final ConfigurationJdo configurationJdo, final String s)
    '''
def jdoGetobjectType_():
    '''public static final String jdoGetobjectType_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetobjectType_():
    '''public static final void jdoSetobjectType_(final ConfigurationJdo configurationJdo, final String s)
    '''
def jdoGetoperationalStatus_():
    '''public static final Integer jdoGetoperationalStatus_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetoperationalStatus_():
    '''public static final void jdoSetoperationalStatus_(final ConfigurationJdo configurationJdo, final Integer n)
    '''
def jdoGetpk_():
    '''public static final String jdoGetpk_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetpk_():
    '''public static final void jdoSetpk_(final ConfigurationJdo configurationJdo, final String pk_)
    '''
def jdoGetpriority_():
    '''public static final int jdoGetpriority_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetpriority_():
    '''public static final void jdoSetpriority_(final ConfigurationJdo configurationJdo, final int n)
    '''
def jdoGetrejectionReason_():
    '''public static final String jdoGetrejectionReason_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetrejectionReason_():
    '''public static final void jdoSetrejectionReason_(final ConfigurationJdo configurationJdo, final String s)
    '''
def jdoGetrunId_():
    '''public static final long jdoGetrunId_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetrunId_():
    '''public static final void jdoSetrunId_(final ConfigurationJdo configurationJdo, final long n)
    '''
def jdoGetsourceToken_():
    '''public static final String jdoGetsourceToken_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetsourceToken_():
    '''public static final void jdoSetsourceToken_(final ConfigurationJdo configurationJdo, final String s)
    '''
def jdoGetversion_():
    '''public static final long jdoGetversion_(final ConfigurationJdo configurationJdo)
    '''
def jdoSetversion_():
    '''public static final void jdoSetversion_(final ConfigurationJdo configurationJdo, final long n)
    '''
