CACHE_NAME = "String  \"BMX.MAXIMODD.MSI\""
SYSTEMLEVEL0 = "int  0"
SITELEVEL1 = "int  1"
ORGLEVEL2 = "int  2"
ITEMSET3 = "int  3"
COMPANYSET4 = "int  4"
SYSTEMSITE5 = "int  5"
SYSTEMAPPFILTER6 = "int  6"
ORGAPPFILTER7 = "int  7"
SITEAPPFILTER8 = "int  8"
SYSTEMORGSITE9 = "int  9"
ORGSITE10 = "int  10"
SYSTEMORG11 = "int  11"
RestrictionEvalSystem = "int  0"
RestrictionEvalBySite = "int  1"
RestrictionEvalByOrg = "int  2"
RestrictionEvalBySiteOrg = "int  3"
INTNOTINITIALIZED = "int  -200"
INTNOLIMIT = "int  -1"
def getTypedReference():
    '''    public MboSetInfoBase getTypedReference()
    '''
def isTenantOwned():
    '''    public boolean isTenantOwned()
    '''
def getKeyRelationshipWhere():
    '''    public String getKeyRelationshipWhere()
    '''
def getUniqueEntityColumns():
    '''    public HashSet<String> getUniqueEntityColumns()
    '''
def isIncludedParentRelationship():
    '''    public boolean isIncludedParentRelationship()
    '''
def getUniqueIDName():
    '''    public String getUniqueIDName()
    '''
def getContentAttrName():
    '''    public String getContentAttrName()
    '''
def getClassName():
    '''    public String getClassName()
    '''
def getDescription():
    '''    public String getDescription()
    '''
def isMainObject():
    '''    public boolean isMainObject()
    '''
def isEAuditEnabled():
    '''    public boolean isEAuditEnabled()
    '''
def getEAuditFilter():
    '''    public String getEAuditFilter()
    '''
def getESigFilter():
    '''    public String getESigFilter()
    '''
def getEntityName():
    '''    public String getEntityName()
    '''
def getExtendsObject():
    '''    public String getExtendsObject()
    '''
def getResourceType():
    '''    public String getResourceType()
    '''
def isNOSql():
    '''    public boolean isNOSql()
    '''
def isView():
    '''    public boolean isView()
    '''
def getObjectName():
    '''    public String getObjectName()
    '''
def isPersistent():
    '''    public boolean isPersistent()
    '''
def getServiceName():
    '''    public String getServiceName()
    '''
def getSiteOrgType():
    '''    public int getSiteOrgType()
    '''
def getSiteOrgTypeAsString():
    '''    public String getSiteOrgTypeAsString()
    '''
def isUserdefined():
    '''    public boolean isUserdefined()
    '''
def isImported():
    '''    public boolean isImported()
    '''
def isInternal():
    '''    public boolean isInternal()
    '''
def setInternal():
    '''    public void setInternal(final boolean flag)
    '''
def getName():
    '''    public String getName()
    '''
def getInitEventName():
    '''    public String getInitEventName()
    '''
def getAppValidateEventName():
    '''    public String getAppValidateEventName()
    '''
def getFetchStopLimit():
    '''    public int getFetchStopLimit()
    '''
def getTextdirection():
    '''    public String getTextdirection()
    '''
def setHierarchyList():
    '''    public void setHierarchyList(final List<String> hierarchyList)
    '''
def getHierarchyList():
    '''    public List<String> getHierarchyList()
    '''
def evalForDataRestriction():
    '''    public int evalForDataRestriction()
    '''
def getAttributeDetails():
    '''    public Map getAttributeDetails()
    '''
def clearAttributes():
    '''    public void clearAttributes()
    '''
def addAttribute():
    '''    public void addAttribute(final MboValueInfo attributeInfo)
    '''
def getAttribute():
    '''    public MboValueInfo getAttribute(final String attributeName)
    '''
def getEntity():
    '''    public Entity getEntity()
    '''
def setEntity():
    '''    public void setEntity(final Entity entity)
    '''
def getAttributeCount():
    '''    public int getAttributeCount()
    '''
def getPersistentAttributeCount():
    '''    public int getPersistentAttributeCount()
    '''
def getExtendedAttributeCount():
    '''    public int getExtendedAttributeCount()
    '''
def getFetchAttributeCount():
    '''    public int getFetchAttributeCount()
    '''
def getAttributes():
    '''    public Iterator getAttributes()
    '''
def getPersistentAttributes():
    '''    public Iterator getPersistentAttributes()
    '''
def getExtendedAttributes():
    '''    public Iterator getExtendedAttributes()
    '''
def getFetchAttributes():
    '''    public Iterator getFetchAttributes()
    '''
def getKeyAttributeIterator():
    '''    public Iterator getKeyAttributeIterator()
    '''
def getLongDescriptionAttributes():
    '''    public Iterator getLongDescriptionAttributes()
    '''
def getKeySize():
    '''    public int getKeySize()
    '''
def getBaseMboInfo():
    '''    public MboSetInfo getBaseMboInfo()
    '''
def setBaseMboInfo():
    '''    public void setBaseMboInfo(final MboSetInfo info)
    '''
def isBasedOn():
    '''    public boolean isBasedOn(final String name)
    '''
def setPresistentAttributeNumber():
    '''    public void setPresistentAttributeNumber(final int persistentAttributeNumber)
    '''
def setExtendedAttributeNumber():
    '''    public void setExtendedAttributeNumber(final int extendedAttributeNumber)
    '''
def setFetchAttributeNumber():
    '''    public void setFetchAttributeNumber(final int fetchAttributeNumber)
    '''
def getPresistentAttributeNumber():
    '''    public int getPresistentAttributeNumber()
    '''
def getExtendedAttributeNumber():
    '''    public int getExtendedAttributeNumber()
    '''
def getFetchAttributeNumber():
    '''    public int getFetchAttributeNumber()
    '''
def getMboLogger():
    '''    public MXLogger getMboLogger()
    '''
def getSecurityLogger():
    '''    public MXLogger getSecurityLogger()
    '''
def getSqlLogger():
    '''    public MXLogger getSqlLogger()
    '''
def getServiceInfo():
    '''    public ServiceInfo getServiceInfo()
    '''
def setServiceInfo():
    '''    public void setServiceInfo(final ServiceInfo si)
    '''
def getMboSetClass():
    '''    public Class getMboSetClass()
    '''
def getMboValueCount():
    '''    public int getMboValueCount()
    '''
def getKeyAttributes():
    '''    public String[] getKeyAttributes()
    '''
def getKeyRelationship():
    '''    public String getKeyRelationship()
    '''
def getMboValueInfo():
    '''    public MboValueInfo getMboValueInfo(final String attributeName)
    '''
def getMboValuesInfo():
    '''    public Enumeration getMboValuesInfo()
    '''
def setRelationships():
    '''    public void setRelationships(final HashMap<String, RelationInfo> relationships)
    '''
def getRelationInfo():
    '''    public RelationInfo getRelationInfo(final String relationshipName)
    '''
def getRelationshipToChild():
    '''    public RelationInfo getRelationshipToChild(final String child)
    '''
def getRelationsInfo():
    '''    public Iterator getRelationsInfo()
    '''
def getEAuditAttributes():
    '''    public Iterator getEAuditAttributes()
    '''
def getLangTableNames():
    '''    public HashMap<String, String> getLangTableNames()
    '''
def getTableAndColumn():
    '''    public String[] getTableAndColumn(final String attr)
    '''
def isMLInUse():
    '''    public boolean isMLInUse()
    '''
def isAuditTable():
    '''    public boolean isAuditTable()
    '''
def isLanguageTable():
    '''    public boolean isLanguageTable()
    '''
def isTextSearchEnabled():
    '''    public boolean isTextSearchEnabled()
    '''
def getInitEventTopic():
    '''    public EventTopic[] getInitEventTopic()
    '''
def getAppValidateEventTopic():
    '''    public EventTopic[] getAppValidateEventTopic()
    '''
def getAllUniqueColumns():
    '''    public HashSet<String> getAllUniqueColumns()
    '''
def isAsUniqueId():
    '''    public boolean isAsUniqueId(final String attrName)
    '''
def getTransactionLogger():
    '''    public MXLogger getTransactionLogger()
    '''
def hasNullableKeyAttr():
    '''    public boolean hasNullableKeyAttr()
    '''
def resolveReferences():
    '''    public void resolveReferences()
    '''
def hasExtendedAttrs():
    '''    public boolean hasExtendedAttrs()
    '''
def setHasExtendedAttrs():
    '''    public void setHasExtendedAttrs(final boolean hasExtendedAttrs)
    '''
def getLatitude():
    '''    public String getLatitude()
    '''
def getLongtitude():
    '''    public String getLongtitude()
    '''
def setLatitude():
    '''    public void setLatitude(final String refy)
    '''
def setLongtitude():
    '''    public void setLongtitude(final String refx)
    '''
def getExtendedViewName():
    '''    public String getExtendedViewName()
    '''
def getCacheName():
    '''    public String getCacheName()
    '''
def compare():
    '''    public int compare(final Object o1, final Object o2)
    public int compare(final Object o1, final Object o2)
    public int compare(final Object o1, final Object o2)
    public int compare(final Object o1, final Object o2)
    public int compare(final Object o1, final Object o2)
    '''
def AttributeIterator():
    '''    public AttributeIterator(final Iterator iterator)
    '''
def remove():
    '''    public void remove()
    public void remove()
    '''
def RelationIterator():
    '''    public RelationIterator(final Iterator iterator)
    '''
def MboValueInfoEnumerator():
    '''    public MboValueInfoEnumerator()
    '''
def hasMoreElements():
    '''    public boolean hasMoreElements()
    '''
def nextElement():
    '''    public Object nextElement()
    '''
