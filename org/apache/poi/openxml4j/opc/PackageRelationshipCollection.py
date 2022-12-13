def PackageRelationshipCollection():
    '''    public PackageRelationshipCollection(final PackageRelationshipCollection coll, final String filter)
    public PackageRelationshipCollection(final OPCPackage container)
    public PackageRelationshipCollection(final PackagePart part)
    public PackageRelationshipCollection(final OPCPackage container, final PackagePart part)
    '''
def addRelationship():
    '''    public void addRelationship(final PackageRelationship relPart)
    public PackageRelationship addRelationship(final URI targetUri, final TargetMode targetMode, final String relationshipType, String id)
    '''
def removeRelationship():
    '''    public void removeRelationship(final String id)
    '''
def getRelationship():
    '''    public PackageRelationship getRelationship(final int index)
    '''
def getRelationshipByID():
    '''    public PackageRelationship getRelationshipByID(final String id)
    '''
def size():
    '''    public int size()
    '''
def parseRelationshipsPart():
    '''    public void parseRelationshipsPart(final PackagePart relPart)
    '''
def getRelationships():
    '''    public PackageRelationshipCollection getRelationships(final String typeFilter)
    '''
def iterator():
    '''    public Iterator<PackageRelationship> iterator()
    public Iterator<PackageRelationship> iterator(final String typeFilter)
    '''
def clear():
    '''    public void clear()
    '''
def findExistingInternalRelation():
    '''    public PackageRelationship findExistingInternalRelation(final PackagePart packagePart)
    '''
def toString():
    '''    public String toString()
    '''
