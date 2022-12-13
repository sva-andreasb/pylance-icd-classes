def open():
    '''    public static OPCPackage open(final String path)
    public static OPCPackage open(final File file)
    public static OPCPackage open(final ZipEntrySource zipEntry)
    public static OPCPackage open(final String path, final PackageAccess access)
    public static OPCPackage open(final File file, final PackageAccess access)
    public static OPCPackage open(final InputStream in)
    '''
def openOrCreate():
    '''    public static OPCPackage openOrCreate(final File file)
    '''
def create():
    '''    public static OPCPackage create(final String path)
    public static OPCPackage create(final File file)
    public static OPCPackage create(final OutputStream output)
    '''
def flush():
    '''    public void flush()
    '''
def close():
    '''    public void close()
    '''
def revert():
    '''    public void revert()
    '''
def addThumbnail():
    '''    public void addThumbnail(final String path)
    public void addThumbnail(final String filename, final InputStream data)
    '''
def getPackageProperties():
    '''    public PackageProperties getPackageProperties()
    '''
def getPart():
    '''    public PackagePart getPart(final PackagePartName partName)
    public PackagePart getPart(final PackageRelationship partRel)
    '''
def getPartsByContentType():
    '''    public ArrayList<PackagePart> getPartsByContentType(final String contentType)
    '''
def getPartsByRelationshipType():
    '''    public ArrayList<PackagePart> getPartsByRelationshipType(final String relationshipType)
    '''
def getPartsByName():
    '''    public List<PackagePart> getPartsByName(final Pattern namePattern)
    '''
def getParts():
    '''    public ArrayList<PackagePart> getParts()
    '''
def createPart():
    '''    public PackagePart createPart(final PackagePartName partName, final String contentType)
    public PackagePart createPart(final PackagePartName partName, final String contentType, final ByteArrayOutputStream content)
    '''
def removePart():
    '''    public void removePart(final PackagePart part)
    public void removePart(final PackagePartName partName)
    '''
def removePartRecursive():
    '''    public void removePartRecursive(final PackagePartName partName)
    '''
def deletePart():
    '''    public void deletePart(final PackagePartName partName)
    '''
def deletePartRecursive():
    '''    public void deletePartRecursive(final PackagePartName partName)
    '''
def containPart():
    '''    public boolean containPart(final PackagePartName partName)
    '''
def addRelationship():
    '''    public PackageRelationship addRelationship(final PackagePartName targetPartName, final TargetMode targetMode, final String relationshipType, final String relID)
    public PackageRelationship addRelationship(final PackagePartName targetPartName, final TargetMode targetMode, final String relationshipType)
    '''
def addExternalRelationship():
    '''    public PackageRelationship addExternalRelationship(final String target, final String relationshipType)
    public PackageRelationship addExternalRelationship(final String target, final String relationshipType, final String id)
    '''
def removeRelationship():
    '''    public void removeRelationship(final String id)
    '''
def getRelationships():
    '''    public PackageRelationshipCollection getRelationships()
    '''
def getRelationshipsByType():
    '''    public PackageRelationshipCollection getRelationshipsByType(final String relationshipType)
    '''
def clearRelationships():
    '''    public void clearRelationships()
    '''
def ensureRelationships():
    '''    public void ensureRelationships()
    '''
def getRelationship():
    '''    public PackageRelationship getRelationship(final String id)
    '''
def hasRelationships():
    '''    public boolean hasRelationships()
    '''
def isRelationshipExists():
    '''    public boolean isRelationshipExists(final PackageRelationship rel)
    '''
def addMarshaller():
    '''    public void addMarshaller(final String contentType, final PartMarshaller marshaller)
    '''
def addUnmarshaller():
    '''    public void addUnmarshaller(final String contentType, final PartUnmarshaller unmarshaller)
    '''
def removeMarshaller():
    '''    public void removeMarshaller(final String contentType)
    '''
def removeUnmarshaller():
    '''    public void removeUnmarshaller(final String contentType)
    '''
def getPackageAccess():
    '''    public PackageAccess getPackageAccess()
    '''
def validatePackage():
    '''    public boolean validatePackage(final OPCPackage pkg)
    '''
def save():
    '''    public void save(final File targetFile)
    public void save(final OutputStream outputStream)
    '''
def replaceContentType():
    '''    public boolean replaceContentType(final String oldContentType, final String newContentType)
    '''
def registerPartAndContentType():
    '''    public void registerPartAndContentType(final PackagePart part)
    '''
def unregisterPartAndContentType():
    '''    public void unregisterPartAndContentType(final PackagePartName partName)
    '''
