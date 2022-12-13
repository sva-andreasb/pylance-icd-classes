def POIXMLDocumentPart():
    '''public POIXMLDocumentPart(final OPCPackage pkg)
    public POIXMLDocumentPart(final OPCPackage pkg, final String coreDocumentRel)
    public POIXMLDocumentPart()
    public POIXMLDocumentPart(final PackagePart part)
    public POIXMLDocumentPart(final POIXMLDocumentPart parent, final PackagePart part)
    '''
def getPackagePart():
    '''public final PackagePart getPackagePart()
    '''
def getRelations():
    '''public final List<POIXMLDocumentPart> getRelations()
    '''
def getRelationParts():
    '''public final List<RelationPart> getRelationParts()
    '''
def getRelationById():
    '''public final POIXMLDocumentPart getRelationById(final String id)
    '''
def getRelationId():
    '''public final String getRelationId(final POIXMLDocumentPart part)
    '''
def addRelation():
    '''public final RelationPart addRelation(final String relId, final POIXMLRelation relationshipType, final POIXMLDocumentPart part)
    '''
def getParent():
    '''public final POIXMLDocumentPart getParent()
    '''
def toString():
    '''public String toString()
    '''
def createRelationship():
    '''public final POIXMLDocumentPart createRelationship(final POIXMLRelation descriptor, final POIXMLFactory factory)
    public final POIXMLDocumentPart createRelationship(final POIXMLRelation descriptor, final POIXMLFactory factory, final int idx)
    '''
def _invokeOnDocumentRead():
    '''public static void _invokeOnDocumentRead(final POIXMLDocumentPart part)
    '''
def getRelationship():
    '''public PackageRelationship getRelationship()
    '''
def getDocumentPart():
    '''public <T extends POIXMLDocumentPart> T getDocumentPart()
    '''
