def PackagePart():
    '''    public PackagePart(final OPCPackage pack, final PackagePartName partName, final String contentType)
    '''
def findExistingRelation():
    '''    public PackageRelationship findExistingRelation(final PackagePart packagePart)
    '''
def addExternalRelationship():
    '''    public PackageRelationship addExternalRelationship(final String target, final String relationshipType)
    public PackageRelationship addExternalRelationship(final String target, final String relationshipType, final String id)
    '''
def addRelationship():
    '''    public PackageRelationship addRelationship(final PackagePartName targetPartName, final TargetMode targetMode, final String relationshipType)
    public PackageRelationship addRelationship(final PackagePartName targetPartName, final TargetMode targetMode, final String relationshipType, final String id)
    public PackageRelationship addRelationship(final URI targetURI, final TargetMode targetMode, final String relationshipType)
    public PackageRelationship addRelationship(final URI targetURI, final TargetMode targetMode, final String relationshipType, final String id)
    '''
def clearRelationships():
    '''    public void clearRelationships()
    '''
def removeRelationship():
    '''    public void removeRelationship(final String id)
    '''
def getRelationships():
    '''    public PackageRelationshipCollection getRelationships()
    '''
def getRelationship():
    '''    public PackageRelationship getRelationship(final String id)
    '''
def getRelationshipsByType():
    '''    public PackageRelationshipCollection getRelationshipsByType(final String relationshipType)
    '''
def hasRelationships():
    '''    public boolean hasRelationships()
    '''
def isRelationshipExists():
    '''    public boolean isRelationshipExists(final PackageRelationship rel)
    '''
def getRelatedPart():
    '''    public PackagePart getRelatedPart(final PackageRelationship rel)
    '''
def getInputStream():
    '''    public InputStream getInputStream()
    '''
def getOutputStream():
    '''    public OutputStream getOutputStream()
    '''
def getPartName():
    '''    public PackagePartName getPartName()
    '''
def getContentType():
    '''    public String getContentType()
    '''
def getContentTypeDetails():
    '''    public ContentType getContentTypeDetails()
    '''
def setContentType():
    '''    public void setContentType(final String contentType)
    '''
def getPackage():
    '''    public OPCPackage getPackage()
    '''
def isRelationshipPart():
    '''    public boolean isRelationshipPart()
    '''
def isDeleted():
    '''    public boolean isDeleted()
    '''
def setDeleted():
    '''    public void setDeleted(final boolean isDeleted)
    '''
def getSize():
    '''    public long getSize()
    '''
def toString():
    '''    public String toString()
    '''
def compareTo():
    '''    public int compareTo(final PackagePart other)
    '''
def clear():
    '''    public void clear()
    '''
