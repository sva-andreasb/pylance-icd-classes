def registerManagementSoftwareSystem():
    '''    public Guid registerManagementSoftwareSystem(final ManagementSoftwareSystem mss)
    '''
def updateManagementSoftwareSystem():
    '''    public Guid updateManagementSoftwareSystem(final ManagementSoftwareSystem mss)
    '''
def deleteManagementSoftwareSystem():
    '''    public void deleteManagementSoftwareSystem(final Guid mssGuid)
    '''
def getManagementSoftwareSystemLinks():
    '''    public MSSObjectLink[] getManagementSoftwareSystemLinks(final Guid guid, final Guid mss, final String[] permissions)
    '''
def getManagementSoftwareSystems():
    '''    public ManagementSoftwareSystem[] getManagementSoftwareSystems(final Guid guid, final String[] permissions)
    '''
def find():
    '''    public ModelObject find(final Guid guid, final int depth, final Guid mss, final String[] permissions)
    '''
def addRelationships():
    '''    public Guid[] addRelationships(final Relationship[] relationships, final Guid mss)
    '''
def deleteRelationships():
    '''    public void deleteRelationships(final Guid[] guids, final Guid mss)
    public void deleteRelationships(final String type, final Guid source, final Guid target, final Guid mss)
    '''
def findRelationships():
    '''    public Relationship[] findRelationships(final Guid managedElementGuid, final int direction, final String type, final int scope, final String[] permissions)
    '''
def deleteStale():
    '''    public void deleteStale(final Guid mss, final long date)
    '''
def addCollectionMembers():
    '''    public void addCollectionMembers(final Guid collectionGuid, final Guid[] guids)
    '''
def removeCollectionMembers():
    '''    public void removeCollectionMembers(final Guid collectionGuid, final Guid[] guids)
    '''
def printRelationship():
    '''    public static void printRelationship(final String title, final ModelObject[] relArray)
    '''
def getValidRelationshipTypes():
    '''    public RelationshipType[] getValidRelationshipTypes(final String sourceClass, final String targetClass)
    '''
