def ():
    '''returns PackagePart\n\n
    (final OPCPackage pack, final PackagePartName partName, final String contentType)\n
    '''
def findExistingRelation():
    '''returns PackageRelationship\n\n
    findExistingRelation(final PackagePart packagePart)\n
    '''
def addExternalRelationship():
    '''returns PackageRelationship\n\n
    addExternalRelationship(final String target, final String relationshipType)\n
    addExternalRelationship(final String target, final String relationshipType, final String id)\n
    '''
def addRelationship():
    '''returns PackageRelationship\n\n
    addRelationship(final PackagePartName targetPartName, final TargetMode targetMode, final String relationshipType)\n
    addRelationship(final PackagePartName targetPartName, final TargetMode targetMode, final String relationshipType, final String id)\n
    addRelationship(final URI targetURI, final TargetMode targetMode, final String relationshipType)\n
    addRelationship(final URI targetURI, final TargetMode targetMode, final String relationshipType, final String id)\n
    '''
def clearRelationships():
    '''returns None\n\n
    clearRelationships()\n
    '''
def removeRelationship():
    '''returns None\n\n
    removeRelationship(final String id)\n
    '''
def getRelationships():
    '''returns PackageRelationshipCollection\n\n
    getRelationships()\n
    '''
def getRelationship():
    '''returns PackageRelationship\n\n
    getRelationship(final String id)\n
    '''
def getRelationshipsByType():
    '''returns PackageRelationshipCollection\n\n
    getRelationshipsByType(final String relationshipType)\n
    '''
def hasRelationships():
    '''returns boolean\n\n
    hasRelationships()\n
    '''
def isRelationshipExists():
    '''returns boolean\n\n
    isRelationshipExists(final PackageRelationship rel)\n
    '''
def getRelatedPart():
    '''returns PackagePart\n\n
    getRelatedPart(final PackageRelationship rel)\n
    '''
def getInputStream():
    '''returns InputStream\n\n
    getInputStream()\n
    '''
def getOutputStream():
    '''returns OutputStream\n\n
    getOutputStream()\n
    '''
def getPartName():
    '''returns PackagePartName\n\n
    getPartName()\n
    '''
def getContentType():
    '''returns String\n\n
    getContentType()\n
    '''
def getContentTypeDetails():
    '''returns ContentType\n\n
    getContentTypeDetails()\n
    '''
def setContentType():
    '''returns None\n\n
    setContentType(final String contentType)\n
    '''
def getPackage():
    '''returns OPCPackage\n\n
    getPackage()\n
    '''
def isRelationshipPart():
    '''returns boolean\n\n
    isRelationshipPart()\n
    '''
def isDeleted():
    '''returns boolean\n\n
    isDeleted()\n
    '''
def setDeleted():
    '''returns None\n\n
    setDeleted(final boolean isDeleted)\n
    '''
def getSize():
    '''returns long\n\n
    getSize()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final PackagePart other)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
