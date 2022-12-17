def flush():
    '''returns None\n\n
    flush()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def revert():
    '''returns None\n\n
    revert()\n
    '''
def addThumbnail():
    '''returns None\n\n
    addThumbnail(final String path)\n
    addThumbnail(final String filename, final InputStream data)\n
    '''
def getPackageProperties():
    '''returns PackageProperties\n\n
    getPackageProperties()\n
    '''
def getPart():
    '''returns PackagePart\n\n
    getPart(final PackagePartName partName)\n
    getPart(final PackageRelationship partRel)\n
    '''
def getPartsByContentType():
    '''returns ArrayList<PackagePart>\n\n
    getPartsByContentType(final String contentType)\n
    '''
def getPartsByRelationshipType():
    '''returns ArrayList<PackagePart>\n\n
    getPartsByRelationshipType(final String relationshipType)\n
    '''
def getPartsByName():
    '''returns List<PackagePart>\n\n
    getPartsByName(final Pattern namePattern)\n
    '''
def getParts():
    '''returns ArrayList<PackagePart>\n\n
    getParts()\n
    '''
def createPart():
    '''returns PackagePart\n\n
    createPart(final PackagePartName partName, final String contentType)\n
    createPart(final PackagePartName partName, final String contentType, final ByteArrayOutputStream content)\n
    '''
def removePart():
    '''returns None\n\n
    removePart(final PackagePart part)\n
    removePart(final PackagePartName partName)\n
    '''
def removePartRecursive():
    '''returns None\n\n
    removePartRecursive(final PackagePartName partName)\n
    '''
def deletePart():
    '''returns None\n\n
    deletePart(final PackagePartName partName)\n
    '''
def deletePartRecursive():
    '''returns None\n\n
    deletePartRecursive(final PackagePartName partName)\n
    '''
def containPart():
    '''returns boolean\n\n
    containPart(final PackagePartName partName)\n
    '''
def addRelationship():
    '''returns PackageRelationship\n\n
    addRelationship(final PackagePartName targetPartName, final TargetMode targetMode, final String relationshipType, final String relID)\n
    addRelationship(final PackagePartName targetPartName, final TargetMode targetMode, final String relationshipType)\n
    '''
def addExternalRelationship():
    '''returns PackageRelationship\n\n
    addExternalRelationship(final String target, final String relationshipType)\n
    addExternalRelationship(final String target, final String relationshipType, final String id)\n
    '''
def removeRelationship():
    '''returns None\n\n
    removeRelationship(final String id)\n
    '''
def getRelationships():
    '''returns PackageRelationshipCollection\n\n
    getRelationships()\n
    '''
def getRelationshipsByType():
    '''returns PackageRelationshipCollection\n\n
    getRelationshipsByType(final String relationshipType)\n
    '''
def clearRelationships():
    '''returns None\n\n
    clearRelationships()\n
    '''
def ensureRelationships():
    '''returns None\n\n
    ensureRelationships()\n
    '''
def getRelationship():
    '''returns PackageRelationship\n\n
    getRelationship(final String id)\n
    '''
def hasRelationships():
    '''returns boolean\n\n
    hasRelationships()\n
    '''
def isRelationshipExists():
    '''returns boolean\n\n
    isRelationshipExists(final PackageRelationship rel)\n
    '''
def addMarshaller():
    '''returns None\n\n
    addMarshaller(final String contentType, final PartMarshaller marshaller)\n
    '''
def addUnmarshaller():
    '''returns None\n\n
    addUnmarshaller(final String contentType, final PartUnmarshaller unmarshaller)\n
    '''
def removeMarshaller():
    '''returns None\n\n
    removeMarshaller(final String contentType)\n
    '''
def removeUnmarshaller():
    '''returns None\n\n
    removeUnmarshaller(final String contentType)\n
    '''
def getPackageAccess():
    '''returns PackageAccess\n\n
    getPackageAccess()\n
    '''
def validatePackage():
    '''returns boolean\n\n
    validatePackage(final OPCPackage pkg)\n
    '''
def save():
    '''returns None\n\n
    save(final File targetFile)\n
    save(final OutputStream outputStream)\n
    '''
def replaceContentType():
    '''returns boolean\n\n
    replaceContentType(final String oldContentType, final String newContentType)\n
    '''
def registerPartAndContentType():
    '''returns None\n\n
    registerPartAndContentType(final PackagePart part)\n
    '''
def unregisterPartAndContentType():
    '''returns None\n\n
    unregisterPartAndContentType(final PackagePartName partName)\n
    '''
