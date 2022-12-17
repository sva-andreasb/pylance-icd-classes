COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloMappingDefinitionsList\n\n
    (final IloReportHandler reportHandler)\n
    '''
def clearMappings():
    '''returns None\n\n
    clearMappings()\n
    '''
def addMapping():
    '''returns None\n\n
    addMapping(final IloMappingDefinition mappingDef, final boolean replace)\n
    '''
def checkAndReportConform():
    '''returns boolean\n\n
    checkAndReportConform()\n
    '''
def removeMapping():
    '''returns boolean\n\n
    removeMapping(final IloMappingDefinition mappingDef)\n
    '''
def write():
    '''returns None\n\n
    write(final Writer writer, final boolean writeConnection)\n
    '''
def read():
    '''returns None\n\n
    read(final Reader reader)\n
    '''
def getMappings():
    '''returns Collection<IloMappingDefinition>\n\n
    getMappings()\n
    '''
def getPrepareOplScript():
    '''returns String\n\n
    getPrepareOplScript()\n
    '''
def getRMToOplMappingFor():
    '''returns IloMappingDefinition\n\n
    getRMToOplMappingFor(final String oplElementName)\n
    '''
def getAnyMappingFor():
    '''returns IloMappingDefinition\n\n
    getAnyMappingFor(final String oplElementName)\n
    '''
def getOplElementsWithRMToOPLSkippedMapping():
    '''returns Collection<String>\n\n
    getOplElementsWithRMToOPLSkippedMapping()\n
    '''
def getOplElementsWithRMToOPLInternalMapping():
    '''returns Collection<String>\n\n
    getOplElementsWithRMToOPLInternalMapping()\n
    '''
def getAnyMappingForTable():
    '''returns IloMappingDefinition\n\n
    getAnyMappingForTable(final String tableID)\n
    '''
def getOplToRMMappingFor():
    '''returns IloMappingDefinition\n\n
    getOplToRMMappingFor(final String oplElementName)\n
    '''
def addChangeListener():
    '''returns None\n\n
    addChangeListener(final ChangeListener listener)\n
    '''
def removeChangeListener():
    '''returns None\n\n
    removeChangeListener(final ChangeListener listener)\n
    '''
def getParentElement():
    '''returns IloModelElement\n\n
    getParentElement()\n
    '''
def fireChangedEvent():
    '''returns None\n\n
    fireChangedEvent()\n
    fireChangedEvent(final ModelModificationEvent event)\n
    '''
