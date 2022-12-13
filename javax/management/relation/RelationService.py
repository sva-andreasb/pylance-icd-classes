def isActive():
    '''    public void isActive()
    '''
def postDeregister():
    '''    public void postDeregister()
    '''
def preDeregister():
    '''    public void preDeregister()
    '''
def purgeRelations():
    '''    public void purgeRelations()
    '''
def getPurgeFlag():
    '''    public boolean getPurgeFlag()
    '''
def RelationService():
    '''    public RelationService(final boolean purgeFlag)
    '''
def setPurgeFlag():
    '''    public void setPurgeFlag(final boolean myPurgeFlg)
    '''
def postRegister():
    '''    public void postRegister(final Boolean b)
    '''
def removeRelation():
    '''    public void removeRelation(final String s)
    '''
def removeRelationType():
    '''    public void removeRelationType(final String key)
    '''
def sendRelationCreationNotification():
    '''    public void sendRelationCreationNotification(final String str)
    '''
def getAllRelationIds():
    '''    public List getAllRelationIds()
    '''
def getAllRelationTypeNames():
    '''    public List getAllRelationTypeNames()
    '''
def getNotificationInfo():
    '''    public MBeanNotificationInfo[] getNotificationInfo()
    '''
def addRelation():
    '''    public void addRelation(final ObjectName objectName)
    '''
def addRelationType():
    '''    public void addRelationType(final RelationType relationType)
    '''
def hasRelation():
    '''    public Boolean hasRelation(final String s)
    '''
def handleNotification():
    '''    public void handleNotification(final Notification e, final Object o)
    '''
def getRelationTypeName():
    '''    public String getRelationTypeName(final String s)
    '''
def isRelation():
    '''    public String isRelation(final ObjectName key)
    '''
def findRelationsOfType():
    '''    public List findRelationsOfType(final String key)
    '''
def getRoleInfos():
    '''    public List getRoleInfos(final String s)
    '''
def sendRelationRemovalNotification():
    '''    public void sendRelationRemovalNotification(final String s, final List list)
    '''
def getReferencedMBeans():
    '''    public Map getReferencedMBeans(final String s)
    '''
def isRelationMBean():
    '''    public ObjectName isRelationMBean(final String s)
    '''
def setRole():
    '''    public void setRole(final String str, final Role role)
    '''
def createRelationType():
    '''    public void createRelationType(final String s, final RoleInfo[] array)
    '''
def getAllRoles():
    '''    public RoleResult getAllRoles(final String s)
    '''
def checkRoleReading():
    '''    public Integer checkRoleReading(final String str, final String str2)
    '''
def getRoleCardinality():
    '''    public Integer getRoleCardinality(final String str, final String str2)
    '''
def getRole():
    '''    public List getRole(final String str, final String str2)
    '''
def sendRoleUpdateNotification():
    '''    public void sendRoleUpdateNotification(final String str, final Role role, List c)
    '''
def updateRoleMap():
    '''    public void updateRoleMap(final String str, final Role role, final List c)
    '''
def preRegister():
    '''    public ObjectName preRegister(final MBeanServer myMBeanServer, final ObjectName myObjName)
    '''
def getRoleInfo():
    '''    public RoleInfo getRoleInfo(final String str, final String str2)
    '''
def createRelation():
    '''    public void createRelation(final String str, final String str2, final RoleList list)
    '''
def getRoles():
    '''    public RoleResult getRoles(final String s, final String[] array)
    '''
def setRoles():
    '''    public RoleResult setRoles(final String str, final RoleList list)
    '''
def checkRoleWriting():
    '''    public Integer checkRoleWriting(final Role role, final String str, final Boolean obj)
    '''
def findAssociatedMBeans():
    '''    public Map findAssociatedMBeans(final ObjectName objectName, final String str, final String str2)
    '''
def findReferencingRelations():
    '''    public Map findReferencingRelations(final ObjectName key, final String s, final String e)
    '''
