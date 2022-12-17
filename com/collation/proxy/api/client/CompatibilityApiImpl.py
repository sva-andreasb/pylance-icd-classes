def registerManagementSoftwareSystem():
    '''returns Guid\n\n
    registerManagementSoftwareSystem(final ManagementSoftwareSystem mss)\n
    '''
def updateManagementSoftwareSystem():
    '''returns Guid\n\n
    updateManagementSoftwareSystem(final ManagementSoftwareSystem mss)\n
    '''
def deleteManagementSoftwareSystem():
    '''returns None\n\n
    deleteManagementSoftwareSystem(final Guid mssGuid)\n
    '''
def getManagementSoftwareSystemLinks():
    '''returns MSSObjectLink[]\n\n
    getManagementSoftwareSystemLinks(final Guid guid, final Guid mss, final String[] permissions)\n
    '''
def getManagementSoftwareSystems():
    '''returns ManagementSoftwareSystem[]\n\n
    getManagementSoftwareSystems(final Guid guid, final String[] permissions)\n
    '''
def find():
    '''returns ModelObject\n\n
    find(final Guid guid, final int depth, final Guid mss, final String[] permissions)\n
    '''
def addRelationships():
    '''returns Guid[]\n\n
    addRelationships(final Relationship[] relationships, final Guid mss)\n
    '''
def deleteRelationships():
    '''returns None\n\n
    deleteRelationships(final Guid[] guids, final Guid mss)\n
    deleteRelationships(final String type, final Guid source, final Guid target, final Guid mss)\n
    '''
def findRelationships():
    '''returns Relationship[]\n\n
    findRelationships(final Guid managedElementGuid, final int direction, final String type, final int scope, final String[] permissions)\n
    '''
def deleteStale():
    '''returns None\n\n
    deleteStale(final Guid mss, final long date)\n
    '''
def addCollectionMembers():
    '''returns None\n\n
    addCollectionMembers(final Guid collectionGuid, final Guid[] guids)\n
    '''
def removeCollectionMembers():
    '''returns None\n\n
    removeCollectionMembers(final Guid collectionGuid, final Guid[] guids)\n
    '''
def getValidRelationshipTypes():
    '''returns RelationshipType[]\n\n
    getValidRelationshipTypes(final String sourceClass, final String targetClass)\n
    '''
