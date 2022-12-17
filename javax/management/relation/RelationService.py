def isActive():
    '''returns None\n\n
    isActive()\n
    '''
def postDeregister():
    '''returns None\n\n
    postDeregister()\n
    '''
def preDeregister():
    '''returns None\n\n
    preDeregister()\n
    '''
def purgeRelations():
    '''returns None\n\n
    purgeRelations()\n
    '''
def getPurgeFlag():
    '''returns boolean\n\n
    getPurgeFlag()\n
    '''
def ():
    '''returns RelationService\n\n
    (final boolean purgeFlag)\n
    '''
def setPurgeFlag():
    '''returns None\n\n
    setPurgeFlag(final boolean myPurgeFlg)\n
    '''
def postRegister():
    '''returns None\n\n
    postRegister(final Boolean b)\n
    '''
def removeRelation():
    '''returns None\n\n
    removeRelation(final String s)\n
    '''
def removeRelationType():
    '''returns None\n\n
    removeRelationType(final String key)\n
    '''
def sendRelationCreationNotification():
    '''returns None\n\n
    sendRelationCreationNotification(final String str)\n
    '''
def getAllRelationIds():
    '''returns List\n\n
    getAllRelationIds()\n
    '''
def getAllRelationTypeNames():
    '''returns List\n\n
    getAllRelationTypeNames()\n
    '''
def getNotificationInfo():
    '''returns MBeanNotificationInfo[]\n\n
    getNotificationInfo()\n
    '''
def addRelation():
    '''returns None\n\n
    addRelation(final ObjectName objectName)\n
    '''
def addRelationType():
    '''returns None\n\n
    addRelationType(final RelationType relationType)\n
    '''
def hasRelation():
    '''returns Boolean\n\n
    hasRelation(final String s)\n
    '''
def handleNotification():
    '''returns None\n\n
    handleNotification(final Notification e, final Object o)\n
    '''
def getRelationTypeName():
    '''returns String\n\n
    getRelationTypeName(final String s)\n
    '''
def isRelation():
    '''returns String\n\n
    isRelation(final ObjectName key)\n
    '''
def findRelationsOfType():
    '''returns List\n\n
    findRelationsOfType(final String key)\n
    '''
def getRoleInfos():
    '''returns List\n\n
    getRoleInfos(final String s)\n
    '''
def sendRelationRemovalNotification():
    '''returns None\n\n
    sendRelationRemovalNotification(final String s, final List list)\n
    '''
def getReferencedMBeans():
    '''returns Map\n\n
    getReferencedMBeans(final String s)\n
    '''
def isRelationMBean():
    '''returns ObjectName\n\n
    isRelationMBean(final String s)\n
    '''
def setRole():
    '''returns None\n\n
    setRole(final String str, final Role role)\n
    '''
def createRelationType():
    '''returns None\n\n
    createRelationType(final String s, final RoleInfo[] array)\n
    '''
def getAllRoles():
    '''returns RoleResult\n\n
    getAllRoles(final String s)\n
    '''
def checkRoleReading():
    '''returns Integer\n\n
    checkRoleReading(final String str, final String str2)\n
    '''
def getRoleCardinality():
    '''returns Integer\n\n
    getRoleCardinality(final String str, final String str2)\n
    '''
def getRole():
    '''returns List\n\n
    getRole(final String str, final String str2)\n
    '''
def sendRoleUpdateNotification():
    '''returns None\n\n
    sendRoleUpdateNotification(final String str, final Role role, List c)\n
    '''
def updateRoleMap():
    '''returns None\n\n
    updateRoleMap(final String str, final Role role, final List c)\n
    '''
def preRegister():
    '''returns ObjectName\n\n
    preRegister(final MBeanServer myMBeanServer, final ObjectName myObjName)\n
    '''
def getRoleInfo():
    '''returns RoleInfo\n\n
    getRoleInfo(final String str, final String str2)\n
    '''
def createRelation():
    '''returns None\n\n
    createRelation(final String str, final String str2, final RoleList list)\n
    '''
def getRoles():
    '''returns RoleResult\n\n
    getRoles(final String s, final String[] array)\n
    '''
def setRoles():
    '''returns RoleResult\n\n
    setRoles(final String str, final RoleList list)\n
    '''
def checkRoleWriting():
    '''returns Integer\n\n
    checkRoleWriting(final Role role, final String str, final Boolean obj)\n
    '''
def findAssociatedMBeans():
    '''returns Map\n\n
    findAssociatedMBeans(final ObjectName objectName, final String str, final String str2)\n
    '''
def findReferencingRelations():
    '''returns Map\n\n
    findReferencingRelations(final ObjectName key, final String s, final String e)\n
    '''
