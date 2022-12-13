def registerManagementSoftwareSystem():
'''public Guid registerManagementSoftwareSystem(final ManagementSoftwareSystem mss)
'''
pass
def updateManagementSoftwareSystem():
'''public Guid updateManagementSoftwareSystem(final ManagementSoftwareSystem mss)
'''
pass
def deleteManagementSoftwareSystem():
'''public void deleteManagementSoftwareSystem(final Guid mssGuid)
'''
pass
def getManagementSoftwareSystemLinks():
'''public MSSObjectLink[] getManagementSoftwareSystemLinks(final Guid guid, final Guid mss, final String[] permissions)
'''
pass
def getManagementSoftwareSystems():
'''public ManagementSoftwareSystem[] getManagementSoftwareSystems(final Guid guid, final String[] permissions)
'''
pass
def find():
'''public ModelObject find(final Guid guid, final int depth, final Guid mss, final String[] permissions)
'''
pass
def addRelationships():
'''public Guid[] addRelationships(final Relationship[] relationships, final Guid mss)
'''
pass
def deleteRelationships():
'''public void deleteRelationships(final Guid[] guids, final Guid mss)
public void deleteRelationships(final String type, final Guid source, final Guid target, final Guid mss)
'''
pass
def findRelationships():
'''public Relationship[] findRelationships(final Guid managedElementGuid, final int direction, final String type, final int scope, final String[] permissions)
'''
pass
def deleteStale():
'''public void deleteStale(final Guid mss, final long date)
'''
pass
def addCollectionMembers():
'''public void addCollectionMembers(final Guid collectionGuid, final Guid[] guids)
'''
pass
def removeCollectionMembers():
'''public void removeCollectionMembers(final Guid collectionGuid, final Guid[] guids)
'''
pass
def findCollections():
'''public Collection[] findCollections(final Guid guid, final String[] permissions)
'''
pass
def printRelationship():
'''public static void printRelationship(final String title, final ModelObject[] relArray)
'''
pass
def getValidRelationshipTypes():
'''public RelationshipType[] getValidRelationshipTypes(final String sourceClass, final String targetClass)
'''
pass
