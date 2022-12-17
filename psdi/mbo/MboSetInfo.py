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
    '''returns MboSetInfoBase\n\n
    getTypedReference()\n
    '''
def isTenantOwned():
    '''returns boolean\n\n
    isTenantOwned()\n
    '''
def getKeyRelationshipWhere():
    '''returns String\n\n
    getKeyRelationshipWhere()\n
    '''
def getUniqueEntityColumns():
    '''returns HashSet<String>\n\n
    getUniqueEntityColumns()\n
    '''
def isIncludedParentRelationship():
    '''returns boolean\n\n
    isIncludedParentRelationship()\n
    '''
def getUniqueIDName():
    '''returns String\n\n
    getUniqueIDName()\n
    '''
def getContentAttrName():
    '''returns String\n\n
    getContentAttrName()\n
    '''
def getClassName():
    '''returns String\n\n
    getClassName()\n
    '''
def getDescription():
    '''returns String\n\n
    getDescription()\n
    '''
def isMainObject():
    '''returns boolean\n\n
    isMainObject()\n
    '''
def isEAuditEnabled():
    '''returns boolean\n\n
    isEAuditEnabled()\n
    '''
def getEAuditFilter():
    '''returns String\n\n
    getEAuditFilter()\n
    '''
def getESigFilter():
    '''returns String\n\n
    getESigFilter()\n
    '''
def getEntityName():
    '''returns String\n\n
    getEntityName()\n
    '''
def getExtendsObject():
    '''returns String\n\n
    getExtendsObject()\n
    '''
def getResourceType():
    '''returns String\n\n
    getResourceType()\n
    '''
def isNOSql():
    '''returns boolean\n\n
    isNOSql()\n
    '''
def isView():
    '''returns boolean\n\n
    isView()\n
    '''
def getObjectName():
    '''returns String\n\n
    getObjectName()\n
    '''
def isPersistent():
    '''returns boolean\n\n
    isPersistent()\n
    '''
def getServiceName():
    '''returns String\n\n
    getServiceName()\n
    '''
def getSiteOrgType():
    '''returns int\n\n
    getSiteOrgType()\n
    '''
def getSiteOrgTypeAsString():
    '''returns String\n\n
    getSiteOrgTypeAsString()\n
    '''
def isUserdefined():
    '''returns boolean\n\n
    isUserdefined()\n
    '''
def isImported():
    '''returns boolean\n\n
    isImported()\n
    '''
def isInternal():
    '''returns boolean\n\n
    isInternal()\n
    '''
def setInternal():
    '''returns None\n\n
    setInternal(final boolean flag)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getInitEventName():
    '''returns String\n\n
    getInitEventName()\n
    '''
def getAppValidateEventName():
    '''returns String\n\n
    getAppValidateEventName()\n
    '''
def getFetchStopLimit():
    '''returns int\n\n
    getFetchStopLimit()\n
    '''
def getTextdirection():
    '''returns String\n\n
    getTextdirection()\n
    '''
def setHierarchyList():
    '''returns None\n\n
    setHierarchyList(final List<String> hierarchyList)\n
    '''
def getHierarchyList():
    '''returns List<String>\n\n
    getHierarchyList()\n
    '''
def evalForDataRestriction():
    '''returns int\n\n
    evalForDataRestriction()\n
    '''
def getAttributeDetails():
    '''returns Map\n\n
    getAttributeDetails()\n
    '''
def clearAttributes():
    '''returns None\n\n
    clearAttributes()\n
    '''
def addAttribute():
    '''returns None\n\n
    addAttribute(final MboValueInfo attributeInfo)\n
    '''
def getAttribute():
    '''returns MboValueInfo\n\n
    getAttribute(final String attributeName)\n
    '''
def getEntity():
    '''returns Entity\n\n
    getEntity()\n
    '''
def setEntity():
    '''returns None\n\n
    setEntity(final Entity entity)\n
    '''
def getAttributeCount():
    '''returns int\n\n
    getAttributeCount()\n
    '''
def getPersistentAttributeCount():
    '''returns int\n\n
    getPersistentAttributeCount()\n
    '''
def getExtendedAttributeCount():
    '''returns int\n\n
    getExtendedAttributeCount()\n
    '''
def getFetchAttributeCount():
    '''returns int\n\n
    getFetchAttributeCount()\n
    '''
def getAttributes():
    '''returns Iterator\n\n
    getAttributes()\n
    '''
def getPersistentAttributes():
    '''returns Iterator\n\n
    getPersistentAttributes()\n
    '''
def getExtendedAttributes():
    '''returns Iterator\n\n
    getExtendedAttributes()\n
    '''
def getFetchAttributes():
    '''returns Iterator\n\n
    getFetchAttributes()\n
    '''
def getKeyAttributeIterator():
    '''returns Iterator\n\n
    getKeyAttributeIterator()\n
    '''
def getLongDescriptionAttributes():
    '''returns Iterator\n\n
    getLongDescriptionAttributes()\n
    '''
def getKeySize():
    '''returns int\n\n
    getKeySize()\n
    '''
def getBaseMboInfo():
    '''returns MboSetInfo\n\n
    getBaseMboInfo()\n
    '''
def setBaseMboInfo():
    '''returns None\n\n
    setBaseMboInfo(final MboSetInfo info)\n
    '''
def isBasedOn():
    '''returns boolean\n\n
    isBasedOn(final String name)\n
    '''
def setPresistentAttributeNumber():
    '''returns None\n\n
    setPresistentAttributeNumber(final int persistentAttributeNumber)\n
    '''
def setExtendedAttributeNumber():
    '''returns None\n\n
    setExtendedAttributeNumber(final int extendedAttributeNumber)\n
    '''
def setFetchAttributeNumber():
    '''returns None\n\n
    setFetchAttributeNumber(final int fetchAttributeNumber)\n
    '''
def getPresistentAttributeNumber():
    '''returns int\n\n
    getPresistentAttributeNumber()\n
    '''
def getExtendedAttributeNumber():
    '''returns int\n\n
    getExtendedAttributeNumber()\n
    '''
def getFetchAttributeNumber():
    '''returns int\n\n
    getFetchAttributeNumber()\n
    '''
def getMboLogger():
    '''returns MXLogger\n\n
    getMboLogger()\n
    '''
def getSecurityLogger():
    '''returns MXLogger\n\n
    getSecurityLogger()\n
    '''
def getSqlLogger():
    '''returns MXLogger\n\n
    getSqlLogger()\n
    '''
def getServiceInfo():
    '''returns ServiceInfo\n\n
    getServiceInfo()\n
    '''
def setServiceInfo():
    '''returns None\n\n
    setServiceInfo(final ServiceInfo si)\n
    '''
def getMboSetClass():
    '''returns Class\n\n
    getMboSetClass()\n
    '''
def getMboValueCount():
    '''returns int\n\n
    getMboValueCount()\n
    '''
def getKeyAttributes():
    '''returns String[]\n\n
    getKeyAttributes()\n
    '''
def getKeyRelationship():
    '''returns String\n\n
    getKeyRelationship()\n
    '''
def getMboValueInfo():
    '''returns MboValueInfo\n\n
    getMboValueInfo(final String attributeName)\n
    '''
def getMboValuesInfo():
    '''returns Enumeration\n\n
    getMboValuesInfo()\n
    '''
def setRelationships():
    '''returns None\n\n
    setRelationships(final HashMap<String, RelationInfo> relationships)\n
    '''
def getRelationInfo():
    '''returns RelationInfo\n\n
    getRelationInfo(final String relationshipName)\n
    '''
def getRelationshipToChild():
    '''returns RelationInfo\n\n
    getRelationshipToChild(final String child)\n
    '''
def getRelationsInfo():
    '''returns Iterator\n\n
    getRelationsInfo()\n
    '''
def getEAuditAttributes():
    '''returns Iterator\n\n
    getEAuditAttributes()\n
    '''
def getTableAndColumn():
    '''returns String[]\n\n
    getTableAndColumn(final String attr)\n
    '''
def isMLInUse():
    '''returns boolean\n\n
    isMLInUse()\n
    '''
def isAuditTable():
    '''returns boolean\n\n
    isAuditTable()\n
    '''
def isLanguageTable():
    '''returns boolean\n\n
    isLanguageTable()\n
    '''
def isTextSearchEnabled():
    '''returns boolean\n\n
    isTextSearchEnabled()\n
    '''
def getInitEventTopic():
    '''returns EventTopic[]\n\n
    getInitEventTopic()\n
    '''
def getAppValidateEventTopic():
    '''returns EventTopic[]\n\n
    getAppValidateEventTopic()\n
    '''
def getAllUniqueColumns():
    '''returns HashSet<String>\n\n
    getAllUniqueColumns()\n
    '''
def isAsUniqueId():
    '''returns boolean\n\n
    isAsUniqueId(final String attrName)\n
    '''
def getTransactionLogger():
    '''returns MXLogger\n\n
    getTransactionLogger()\n
    '''
def hasNullableKeyAttr():
    '''returns boolean\n\n
    hasNullableKeyAttr()\n
    '''
def resolveReferences():
    '''returns None\n\n
    resolveReferences()\n
    '''
def hasExtendedAttrs():
    '''returns boolean\n\n
    hasExtendedAttrs()\n
    '''
def setHasExtendedAttrs():
    '''returns None\n\n
    setHasExtendedAttrs(final boolean hasExtendedAttrs)\n
    '''
def getLatitude():
    '''returns String\n\n
    getLatitude()\n
    '''
def getLongtitude():
    '''returns String\n\n
    getLongtitude()\n
    '''
def setLatitude():
    '''returns None\n\n
    setLatitude(final String refy)\n
    '''
def setLongtitude():
    '''returns None\n\n
    setLongtitude(final String refx)\n
    '''
def getExtendedViewName():
    '''returns String\n\n
    getExtendedViewName()\n
    '''
def getCacheName():
    '''returns String\n\n
    getCacheName()\n
    '''
def compare():
    '''returns int\n\n
    compare(final Object o1, final Object o2)\n
    compare(final Object o1, final Object o2)\n
    compare(final Object o1, final Object o2)\n
    compare(final Object o1, final Object o2)\n
    compare(final Object o1, final Object o2)\n
    '''
def ():
    '''returns MboValueInfoEnumerator\n\n
    (final Iterator iterator)\n
    (final Iterator iterator)\n
    ()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    remove()\n
    '''
def hasMoreElements():
    '''returns boolean\n\n
    hasMoreElements()\n
    '''
def nextElement():
    '''returns Object\n\n
    nextElement()\n
    '''
