def getPackageRootUri():
    '''public static URI getPackageRootUri()
    '''
def isRelationshipPartURI():
    '''public static boolean isRelationshipPartURI(final URI partUri)
    '''
def getFilename():
    '''public static String getFilename(final URI uri)
    '''
def getFilenameWithoutExtension():
    '''public static String getFilenameWithoutExtension(final URI uri)
    '''
def getPath():
    '''public static URI getPath(final URI uri)
    '''
def combine():
    '''public static URI combine(final URI prefix, final URI suffix)
    public static String combine(final String prefix, final String suffix)
    '''
def relativizeURI():
    '''public static URI relativizeURI(final URI sourceURI, URI targetURI, final boolean msCompatible)
    public static URI relativizeURI(final URI sourceURI, final URI targetURI)
    '''
def resolvePartUri():
    '''public static URI resolvePartUri(final URI sourcePartUri, final URI targetUri)
    '''
def getURIFromPath():
    '''public static URI getURIFromPath(final String path)
    '''
def getSourcePartUriFromRelationshipPartUri():
    '''public static URI getSourcePartUriFromRelationshipPartUri(final URI relationshipPartUri)
    '''
def createPartName():
    '''public static PackagePartName createPartName(final URI partUri)
    public static PackagePartName createPartName(final String partName)
    public static PackagePartName createPartName(final String partName, final PackagePart relativePart)
    public static PackagePartName createPartName(final URI partName, final PackagePart relativePart)
    '''
def isValidPartName():
    '''public static boolean isValidPartName(final URI partUri)
    '''
def decodeURI():
    '''public static String decodeURI(final URI uri)
    '''
def getRelationshipPartName():
    '''public static PackagePartName getRelationshipPartName(final PackagePartName partName)
    '''
def toURI():
    '''public static URI toURI(String value)
    '''
def encode():
    '''public static String encode(final String s)
    '''
