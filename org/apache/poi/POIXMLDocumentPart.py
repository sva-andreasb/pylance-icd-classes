def POIXMLDocumentPart():
'''public POIXMLDocumentPart(final OPCPackage pkg)
public POIXMLDocumentPart(final OPCPackage pkg, final String coreDocumentRel)
public POIXMLDocumentPart()
public POIXMLDocumentPart(final PackagePart part)
public POIXMLDocumentPart(final POIXMLDocumentPart parent, final PackagePart part)
'''
pass
def getPackagePart():
'''public final PackagePart getPackagePart()
'''
pass
def getRelations():
'''public final List<POIXMLDocumentPart> getRelations()
'''
pass
def getRelationParts():
'''public final List<RelationPart> getRelationParts()
'''
pass
def getRelationById():
'''public final POIXMLDocumentPart getRelationById(final String id)
'''
pass
def getRelationId():
'''public final String getRelationId(final POIXMLDocumentPart part)
'''
pass
def addRelation():
'''public final RelationPart addRelation(final String relId, final POIXMLRelation relationshipType, final POIXMLDocumentPart part)
'''
pass
def getParent():
'''public final POIXMLDocumentPart getParent()
'''
pass
def toString():
'''public String toString()
'''
pass
def createRelationship():
'''public final POIXMLDocumentPart createRelationship(final POIXMLRelation descriptor, final POIXMLFactory factory)
public final POIXMLDocumentPart createRelationship(final POIXMLRelation descriptor, final POIXMLFactory factory, final int idx)
'''
pass
def _invokeOnDocumentRead():
'''public static void _invokeOnDocumentRead(final POIXMLDocumentPart part)
'''
pass
def getRelationship():
'''public PackageRelationship getRelationship()
'''
pass
def getDocumentPart():
'''public <T extends POIXMLDocumentPart> T getDocumentPart()
'''
pass
