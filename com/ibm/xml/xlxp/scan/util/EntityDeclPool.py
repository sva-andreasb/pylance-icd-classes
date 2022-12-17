EntityType_Mask = "int  65535"
EntityType_Predefined = "int  0"
EntityType_InternalGeneral = "int  1"
EntityType_ExternalGeneral = "int  2"
EntityType_InternalParameter = "int  3"
EntityType_ExternalParameter = "int  4"
EntityType_Unparsed = "int  5"
EntityType_DeclaredExternally = "int  65536"
ENTITY_ENTITYTYPE_OFFSET = "int  0"
ENTITY_NAME_OFFSET = "int  1"
PREDEFINEDENTITY_CHARVALUE_OFFSET = "int  2"
PREDEFINEDENTITY_RECORD_SIZE = "int  3"
INTERNALENTITY_CONTENT_OFFSET = "int  2"
INTERNALENTITY_RECORD_SIZE = "int  3"
EXTERNALENTITY_BASEURI_OFFSET = "int  2"
EXTERNALENTITY_PUBLICID_OFFSET = "int  3"
EXTERNALENTITY_SYSTEMID_OFFSET = "int  4"
EXTERNALENTITY_RECORD_SIZE = "int  5"
UNPARSEDENTITY_RECORD_SIZE = "int  2"
def ():
    '''returns EntityDeclPool\n\n
    (final DataBufferFactory fBufferFactory, final SymbolTable fSymbolTable, final XMLStringBuffer fStringBuffer)\n
    '''
def reset():
    '''returns None\n\n
    reset(final boolean b)\n
    '''
def lookupEntity():
    '''returns int\n\n
    lookupEntity(final int n)\n
    '''
def lookupPE():
    '''returns int\n\n
    lookupPE(final int n)\n
    '''
def isUnparsedEntity():
    '''returns boolean\n\n
    isUnparsedEntity(final int n)\n
    '''
def getDeclArray():
    '''returns int[]\n\n
    getDeclArray(final int n)\n
    '''
def getDeclBase():
    '''returns int\n\n
    getDeclBase(final int n)\n
    '''
def getInternalEntityContent():
    '''returns XMLString\n\n
    getInternalEntityContent(final int n)\n
    '''
def getPublicID():
    '''returns XMLString\n\n
    getPublicID(final int n)\n
    '''
def getSystemID():
    '''returns XMLString\n\n
    getSystemID(final int n)\n
    '''
def getBaseURI():
    '''returns String\n\n
    getBaseURI(final int n)\n
    '''
def addInternalEntityDecl():
    '''returns boolean\n\n
    addInternalEntityDecl(final XMLString xmlString, final XMLString xmlString2, final boolean b)\n
    '''
def addExternalEntityDecl():
    '''returns boolean\n\n
    addExternalEntityDecl(final XMLString xmlString, final XMLString xmlString2, final XMLString xmlString3, final String s, final boolean b)\n
    '''
def addUnparsedEntityDecl():
    '''returns boolean\n\n
    addUnparsedEntityDecl(final XMLString xmlString)\n
    '''
def addInternalPEDecl():
    '''returns boolean\n\n
    addInternalPEDecl(final XMLString xmlString, final XMLString xmlString2, final boolean b)\n
    '''
def addExternalPEDecl():
    '''returns boolean\n\n
    addExternalPEDecl(final XMLString xmlString, final XMLString xmlString2, final XMLString xmlString3, final String s, final boolean b)\n
    '''
