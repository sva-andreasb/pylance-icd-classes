def ():
    '''returns PackageRelationshipCollection\n\n
    (final PackageRelationshipCollection coll, final String filter)\n
    (final OPCPackage container)\n
    (final PackagePart part)\n
    (final OPCPackage container, final PackagePart part)\n
    '''
def addRelationship():
    '''returns PackageRelationship\n\n
    addRelationship(final PackageRelationship relPart)\n
    addRelationship(final URI targetUri, final TargetMode targetMode, final String relationshipType, String id)\n
    '''
def removeRelationship():
    '''returns None\n\n
    removeRelationship(final String id)\n
    '''
def getRelationship():
    '''returns PackageRelationship\n\n
    getRelationship(final int index)\n
    '''
def getRelationshipByID():
    '''returns PackageRelationship\n\n
    getRelationshipByID(final String id)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def parseRelationshipsPart():
    '''returns None\n\n
    parseRelationshipsPart(final PackagePart relPart)\n
    '''
def getRelationships():
    '''returns PackageRelationshipCollection\n\n
    getRelationships(final String typeFilter)\n
    '''
def iterator():
    '''returns Iterator<PackageRelationship>\n\n
    iterator()\n
    iterator(final String typeFilter)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def findExistingInternalRelation():
    '''returns PackageRelationship\n\n
    findExistingInternalRelation(final PackagePart packagePart)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
