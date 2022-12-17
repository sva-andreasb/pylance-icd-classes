xmlCatalogXSD = "String  \"http://www.oasis-open.org/committees/entity/release/1.0/catalog.xsd\""
xmlCatalogRNG = "String  \"http://www.oasis-open.org/committees/entity/release/1.0/catalog.rng\""
xmlCatalogPubId = "String  \"-//OASIS//DTD XML Catalogs V1.0//EN\""
xmlCatalogSysId = "String  \"http://www.oasis-open.org/committees/entity/release/1.0/catalog.dtd\""
xCatalogPubId = "String  \"-//DTD XCatalog//EN\""
def ():
    '''returns BootstrapResolver\n\n
    ()\n
    '''
def resolveEntity():
    '''returns InputSource\n\n
    resolveEntity(final String publicId, final String systemId)\n
    '''
def resolve():
    '''returns Source\n\n
    resolve(final String href, final String base)\n
    '''
