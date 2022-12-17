APACHE_RESOLVER = "String  \"org.apache.tools.ant.types.resolver.ApacheCatalogResolver\""
CATALOG_RESOLVER = "String  \"org.apache.xml.resolver.tools.CatalogResolver\""
def ():
    '''returns ExternalResolver\n\n
    ()\n
    ()\n
    (final Class resolverImplClass, final Object resolverImpl)\n
    '''
def createClasspath():
    '''returns Path\n\n
    createClasspath()\n
    '''
def setClasspath():
    '''returns None\n\n
    setClasspath(final Path classpath)\n
    '''
def setClasspathRef():
    '''returns None\n\n
    setClasspathRef(final Reference r)\n
    '''
def createCatalogPath():
    '''returns Path\n\n
    createCatalogPath()\n
    '''
def setCatalogPathRef():
    '''returns None\n\n
    setCatalogPathRef(final Reference r)\n
    '''
def getCatalogPath():
    '''returns Path\n\n
    getCatalogPath()\n
    '''
def addDTD():
    '''returns None\n\n
    addDTD(final ResourceLocation dtd)\n
    '''
def addEntity():
    '''returns None\n\n
    addEntity(final ResourceLocation entity)\n
    '''
def addConfiguredXMLCatalog():
    '''returns None\n\n
    addConfiguredXMLCatalog(final XMLCatalog catalog)\n
    '''
def setRefid():
    '''returns None\n\n
    setRefid(final Reference r)\n
    '''
def resolveEntity():
    '''returns InputSource\n\n
    resolveEntity(final String publicId, final String systemId)\n
    resolveEntity(final String publicId, final String systemId)\n
    resolveEntity(final String publicId, final String systemId)\n
    '''
def resolve():
    '''returns Source\n\n
    resolve(final String href, final String base)\n
    resolve(final String href, final String base)\n
    resolve(final String href, final String base)\n
    '''
