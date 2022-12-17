def ():
    '''returns MaximoContentXmlVisitor\n\n
    ()\n
    (final XmlContent xmlContent)\n
    '''
def load():
    '''returns None\n\n
    load(final String contentPath)\n
    '''
def markXmlContentObjectAsChanged():
    '''returns None\n\n
    markXmlContentObjectAsChanged(final XmlContentObject object)\n
    '''
def getParentContentObject():
    '''returns XmlContentObject\n\n
    getParentContentObject(final XmlContentObject object)\n
    '''
def removeObject():
    '''returns None\n\n
    removeObject(final XmlContentObject object)\n
    '''
def getXmlFileNames():
    '''returns Set<String>\n\n
    getXmlFileNames()\n
    '''
def getXmlContentObjectsInFile():
    '''returns List<XmlContentObject>\n\n
    getXmlContentObjectsInFile(final String xmlFileName)\n
    '''
def getXmlContentObjectByXmlElement():
    '''returns XmlContentObject\n\n
    getXmlContentObjectByXmlElement(final Element element)\n
    '''
def getXmlContentObjectByTypeAndKey():
    '''returns XmlContentObject\n\n
    getXmlContentObjectByTypeAndKey(final String objectType, final String objectKey)\n
    '''
def setKeepRootElementsByFileName():
    '''returns None\n\n
    setKeepRootElementsByFileName(final boolean keepRootElementsByFileName)\n
    '''
def getRootElement():
    '''returns Element\n\n
    getRootElement(final String fileName)\n
    '''
def getIdentifyingWhereClause():
    '''returns String\n\n
    getIdentifyingWhereClause(final XmlContentObject object)\n
    '''
