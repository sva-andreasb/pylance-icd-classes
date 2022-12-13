def Catalog():
'''public Catalog()
public Catalog(final CatalogManager manager)
'''
pass
def getCatalogManager():
'''public CatalogManager getCatalogManager()
'''
pass
def setCatalogManager():
'''public void setCatalogManager(final CatalogManager manager)
'''
pass
def setupReaders():
'''public void setupReaders()
'''
pass
def addReader():
'''public void addReader(final String mimeType, final CatalogReader reader)
'''
pass
def getCurrentBase():
'''public String getCurrentBase()
'''
pass
def getDefaultOverride():
'''public String getDefaultOverride()
'''
pass
def loadSystemCatalogs():
'''public void loadSystemCatalogs()
'''
pass
def parseCatalog():
'''public synchronized void parseCatalog(final String fileName)
public synchronized void parseCatalog(final String mimeType, final InputStream is)
public synchronized void parseCatalog(final URL aUrl)
'''
pass
def addEntry():
'''public void addEntry(final CatalogEntry entry)
'''
pass
def unknownEntry():
'''public void unknownEntry(final Vector strings)
'''
pass
def parseAllCatalogs():
'''public void parseAllCatalogs()
'''
pass
def resolveDoctype():
'''public String resolveDoctype(final String entityName, String publicId, String systemId)
'''
pass
def resolveDocument():
'''public String resolveDocument()
'''
pass
def resolveEntity():
'''public String resolveEntity(final String entityName, String publicId, String systemId)
'''
pass
def resolveNotation():
'''public String resolveNotation(final String notationName, String publicId, String systemId)
'''
pass
def resolvePublic():
'''public String resolvePublic(String publicId, String systemId)
'''
pass
def resolveSystem():
'''public String resolveSystem(String systemId)
'''
pass
def resolveURI():
'''public String resolveURI(String uri)
'''
pass
