COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns FKColumn\n\n
    (final IloDefaultRecursiveHandler previous, final Map<String, IloTableHandler> tableHandlers, final String tableId, final String id, final String target, final String actionOnError, final String display)\n
    (final String srcCol, final String fIdCol, final IloXMLLocation loc)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String uri, final String localName, final String qName, final Attributes attributes)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String uri, final String localName, final String qName)\n
    '''
def getStartLocation():
    '''returns IloXMLLocation\n\n
    getStartLocation()\n
    '''
def getOrMakeFKDescriptor():
    '''returns IloForeignKeyDescriptorImpl\n\n
    getOrMakeFKDescriptor()\n
    '''
def getSrcCol():
    '''returns String\n\n
    getSrcCol()\n
    '''
def getFIdCol():
    '''returns String\n\n
    getFIdCol()\n
    '''
def getLine():
    '''returns IloXMLLocation\n\n
    getLine()\n
    '''
