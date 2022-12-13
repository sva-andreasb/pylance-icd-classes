def PackagePart():
'''public PackagePart(final OPCPackage pack, final PackagePartName partName, final String contentType)
'''
pass
def findExistingRelation():
'''public PackageRelationship findExistingRelation(final PackagePart packagePart)
'''
pass
def addExternalRelationship():
'''public PackageRelationship addExternalRelationship(final String target, final String relationshipType)
public PackageRelationship addExternalRelationship(final String target, final String relationshipType, final String id)
'''
pass
def addRelationship():
'''public PackageRelationship addRelationship(final PackagePartName targetPartName, final TargetMode targetMode, final String relationshipType)
public PackageRelationship addRelationship(final PackagePartName targetPartName, final TargetMode targetMode, final String relationshipType, final String id)
public PackageRelationship addRelationship(final URI targetURI, final TargetMode targetMode, final String relationshipType)
public PackageRelationship addRelationship(final URI targetURI, final TargetMode targetMode, final String relationshipType, final String id)
'''
pass
def clearRelationships():
'''public void clearRelationships()
'''
pass
def removeRelationship():
'''public void removeRelationship(final String id)
'''
pass
def getRelationships():
'''public PackageRelationshipCollection getRelationships()
'''
pass
def getRelationship():
'''public PackageRelationship getRelationship(final String id)
'''
pass
def getRelationshipsByType():
'''public PackageRelationshipCollection getRelationshipsByType(final String relationshipType)
'''
pass
def hasRelationships():
'''public boolean hasRelationships()
'''
pass
def isRelationshipExists():
'''public boolean isRelationshipExists(final PackageRelationship rel)
'''
pass
def getRelatedPart():
'''public PackagePart getRelatedPart(final PackageRelationship rel)
'''
pass
def getInputStream():
'''public InputStream getInputStream()
'''
pass
def getOutputStream():
'''public OutputStream getOutputStream()
'''
pass
def getPartName():
'''public PackagePartName getPartName()
'''
pass
def getContentType():
'''public String getContentType()
'''
pass
def getContentTypeDetails():
'''public ContentType getContentTypeDetails()
'''
pass
def setContentType():
'''public void setContentType(final String contentType)
'''
pass
def getPackage():
'''public OPCPackage getPackage()
'''
pass
def isRelationshipPart():
'''public boolean isRelationshipPart()
'''
pass
def isDeleted():
'''public boolean isDeleted()
'''
pass
def setDeleted():
'''public void setDeleted(final boolean isDeleted)
'''
pass
def getSize():
'''public long getSize()
'''
pass
def toString():
'''public String toString()
'''
pass
def compareTo():
'''public int compareTo(final PackagePart other)
'''
pass
def clear():
'''public void clear()
'''
pass
