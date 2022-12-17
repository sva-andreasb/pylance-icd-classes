DEFAULT_PATH = "String  \"file:location-mapping.rdf;file:location-mapping.n3;file:location-mapping.ttl;file:etc/location-mapping.rdf;file:etc/location-mapping.n3;file:etc/location-mapping.ttl\""
GlobalMapperSystemProperty1 = "String  \"http://jena.hpl.hp.com/2004/08/LocationMap\""
GlobalMapperSystemProperty2 = "String  \"LocationMap\""
def ():
    '''returns LocationMapper\n\n
    ()\n
    (final LocationMapper locMapper)\n
    (final Model model)\n
    (final String config)\n
    '''
def altMapping():
    '''returns String\n\n
    altMapping(final String uri)\n
    altMapping(final String uri, final String otherwise)\n
    '''
def addAltEntry():
    '''returns None\n\n
    addAltEntry(final String uri, final String alt)\n
    '''
def addAltPrefix():
    '''returns None\n\n
    addAltPrefix(final String uriPrefix, final String altPrefix)\n
    '''
def listAltEntries():
    '''returns Iterator<String>\n\n
    listAltEntries()\n
    '''
def listAltPrefixes():
    '''returns Iterator<String>\n\n
    listAltPrefixes()\n
    '''
def removeAltEntry():
    '''returns None\n\n
    removeAltEntry(final String uri)\n
    '''
def removeAltPrefix():
    '''returns None\n\n
    removeAltPrefix(final String uriPrefix)\n
    '''
def getAltEntry():
    '''returns String\n\n
    getAltEntry(final String uri)\n
    '''
def getAltPrefix():
    '''returns String\n\n
    getAltPrefix(final String uriPrefix)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def toModel():
    '''returns None\n\n
    toModel()\n
    toModel(final Model model)\n
    '''
def processConfig():
    '''returns None\n\n
    processConfig(final Model m)\n
    '''
