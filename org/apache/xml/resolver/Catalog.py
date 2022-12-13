def Catalog():
    '''public Catalog()
    public Catalog(final CatalogManager manager)
    '''
def getCatalogManager():
    '''public CatalogManager getCatalogManager()
    '''
def setCatalogManager():
    '''public void setCatalogManager(final CatalogManager manager)
    '''
def setupReaders():
    '''public void setupReaders()
    '''
def addReader():
    '''public void addReader(final String mimeType, final CatalogReader reader)
    '''
def getCurrentBase():
    '''public String getCurrentBase()
    '''
def getDefaultOverride():
    '''public String getDefaultOverride()
    '''
def loadSystemCatalogs():
    '''public void loadSystemCatalogs()
    '''
def parseCatalog():
    '''public synchronized void parseCatalog(final String fileName)
    public synchronized void parseCatalog(final String mimeType, final InputStream is)
    public synchronized void parseCatalog(final URL aUrl)
    '''
def addEntry():
    '''public void addEntry(final CatalogEntry entry)
    '''
def unknownEntry():
    '''public void unknownEntry(final Vector strings)
    '''
def parseAllCatalogs():
    '''public void parseAllCatalogs()
    '''
def resolveDoctype():
    '''public String resolveDoctype(final String entityName, String publicId, String systemId)
    '''
def resolveDocument():
    '''public String resolveDocument()
    '''
def resolveEntity():
    '''public String resolveEntity(final String entityName, String publicId, String systemId)
    '''
def resolveNotation():
    '''public String resolveNotation(final String notationName, String publicId, String systemId)
    '''
def resolvePublic():
    '''public String resolvePublic(String publicId, String systemId)
    '''
def resolveSystem():
    '''public String resolveSystem(String systemId)
    '''
def resolveURI():
    '''public String resolveURI(String uri)
    '''
