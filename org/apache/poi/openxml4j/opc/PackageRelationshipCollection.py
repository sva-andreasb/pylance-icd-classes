def PackageRelationshipCollection():
'''public PackageRelationshipCollection(final PackageRelationshipCollection coll, final String filter)
public PackageRelationshipCollection(final OPCPackage container)
public PackageRelationshipCollection(final PackagePart part)
public PackageRelationshipCollection(final OPCPackage container, final PackagePart part)
'''
pass
def addRelationship():
'''public void addRelationship(final PackageRelationship relPart)
public PackageRelationship addRelationship(final URI targetUri, final TargetMode targetMode, final String relationshipType, String id)
'''
pass
def removeRelationship():
'''public void removeRelationship(final String id)
'''
pass
def getRelationship():
'''public PackageRelationship getRelationship(final int index)
'''
pass
def getRelationshipByID():
'''public PackageRelationship getRelationshipByID(final String id)
'''
pass
def size():
'''public int size()
'''
pass
def parseRelationshipsPart():
'''public void parseRelationshipsPart(final PackagePart relPart)
'''
pass
def getRelationships():
'''public PackageRelationshipCollection getRelationships(final String typeFilter)
'''
pass
def iterator():
'''public Iterator<PackageRelationship> iterator()
public Iterator<PackageRelationship> iterator(final String typeFilter)
'''
pass
def clear():
'''public void clear()
'''
pass
def findExistingInternalRelation():
'''public PackageRelationship findExistingInternalRelation(final PackagePart packagePart)
'''
pass
def toString():
'''public String toString()
'''
pass
