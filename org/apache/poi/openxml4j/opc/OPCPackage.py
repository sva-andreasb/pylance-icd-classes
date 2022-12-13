def open():
'''public static OPCPackage open(final String path)
public static OPCPackage open(final File file)
public static OPCPackage open(final ZipEntrySource zipEntry)
public static OPCPackage open(final String path, final PackageAccess access)
public static OPCPackage open(final File file, final PackageAccess access)
public static OPCPackage open(final InputStream in)
'''
pass
def openOrCreate():
'''public static OPCPackage openOrCreate(final File file)
'''
pass
def create():
'''public static OPCPackage create(final String path)
public static OPCPackage create(final File file)
public static OPCPackage create(final OutputStream output)
'''
pass
def flush():
'''public void flush()
'''
pass
def close():
'''public void close()
'''
pass
def revert():
'''public void revert()
'''
pass
def addThumbnail():
'''public void addThumbnail(final String path)
public void addThumbnail(final String filename, final InputStream data)
'''
pass
def getPackageProperties():
'''public PackageProperties getPackageProperties()
'''
pass
def getPart():
'''public PackagePart getPart(final PackagePartName partName)
public PackagePart getPart(final PackageRelationship partRel)
'''
pass
def getPartsByContentType():
'''public ArrayList<PackagePart> getPartsByContentType(final String contentType)
'''
pass
def getPartsByRelationshipType():
'''public ArrayList<PackagePart> getPartsByRelationshipType(final String relationshipType)
'''
pass
def getPartsByName():
'''public List<PackagePart> getPartsByName(final Pattern namePattern)
'''
pass
def getParts():
'''public ArrayList<PackagePart> getParts()
'''
pass
def createPart():
'''public PackagePart createPart(final PackagePartName partName, final String contentType)
public PackagePart createPart(final PackagePartName partName, final String contentType, final ByteArrayOutputStream content)
'''
pass
def removePart():
'''public void removePart(final PackagePart part)
public void removePart(final PackagePartName partName)
'''
pass
def removePartRecursive():
'''public void removePartRecursive(final PackagePartName partName)
'''
pass
def deletePart():
'''public void deletePart(final PackagePartName partName)
'''
pass
def deletePartRecursive():
'''public void deletePartRecursive(final PackagePartName partName)
'''
pass
def containPart():
'''public boolean containPart(final PackagePartName partName)
'''
pass
def addRelationship():
'''public PackageRelationship addRelationship(final PackagePartName targetPartName, final TargetMode targetMode, final String relationshipType, final String relID)
public PackageRelationship addRelationship(final PackagePartName targetPartName, final TargetMode targetMode, final String relationshipType)
'''
pass
def addExternalRelationship():
'''public PackageRelationship addExternalRelationship(final String target, final String relationshipType)
public PackageRelationship addExternalRelationship(final String target, final String relationshipType, final String id)
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
def getRelationshipsByType():
'''public PackageRelationshipCollection getRelationshipsByType(final String relationshipType)
'''
pass
def clearRelationships():
'''public void clearRelationships()
'''
pass
def ensureRelationships():
'''public void ensureRelationships()
'''
pass
def getRelationship():
'''public PackageRelationship getRelationship(final String id)
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
def addMarshaller():
'''public void addMarshaller(final String contentType, final PartMarshaller marshaller)
'''
pass
def addUnmarshaller():
'''public void addUnmarshaller(final String contentType, final PartUnmarshaller unmarshaller)
'''
pass
def removeMarshaller():
'''public void removeMarshaller(final String contentType)
'''
pass
def removeUnmarshaller():
'''public void removeUnmarshaller(final String contentType)
'''
pass
def getPackageAccess():
'''public PackageAccess getPackageAccess()
'''
pass
def validatePackage():
'''public boolean validatePackage(final OPCPackage pkg)
'''
pass
def save():
'''public void save(final File targetFile)
public void save(final OutputStream outputStream)
'''
pass
def replaceContentType():
'''public boolean replaceContentType(final String oldContentType, final String newContentType)
'''
pass
def registerPartAndContentType():
'''public void registerPartAndContentType(final PackagePart part)
'''
pass
def unregisterPartAndContentType():
'''public void unregisterPartAndContentType(final PackagePartName partName)
'''
pass
