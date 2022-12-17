ID_ATTRIBUTE_NAME = "String  \"Id\""
RELATIONSHIPS_TAG_NAME = "String  \"Relationships\""
RELATIONSHIP_TAG_NAME = "String  \"Relationship\""
TARGET_ATTRIBUTE_NAME = "String  \"Target\""
TARGET_MODE_ATTRIBUTE_NAME = "String  \"TargetMode\""
TYPE_ATTRIBUTE_NAME = "String  \"Type\""
def ():
    '''returns PackageRelationship\n\n
    (final OPCPackage pkg, final PackagePart sourcePart, final URI targetUri, final TargetMode targetMode, final String relationshipType, final String id)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def getPackage():
    '''returns OPCPackage\n\n
    getPackage()\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
def getRelationshipType():
    '''returns String\n\n
    getRelationshipType()\n
    '''
def getSource():
    '''returns PackagePart\n\n
    getSource()\n
    '''
def getSourceURI():
    '''returns URI\n\n
    getSourceURI()\n
    '''
def getTargetMode():
    '''returns TargetMode\n\n
    getTargetMode()\n
    '''
def getTargetURI():
    '''returns URI\n\n
    getTargetURI()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
