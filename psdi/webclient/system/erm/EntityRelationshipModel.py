def ():
    '''returns EntityRelationshipModel\n\n
    (final String id)\n
    ()\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
def putTopLevelEntity():
    '''returns None\n\n
    putTopLevelEntity(final String datasrc, final UIERMEntity entity)\n
    '''
def putEntity():
    '''returns None\n\n
    putEntity(final String datasrc, final UIERMEntity entity)\n
    '''
def findEntity():
    '''returns UIERMEntity\n\n
    findEntity(final String datasrc)\n
    '''
def generateERMXML():
    '''returns StringBuilder\n\n
    generateERMXML()\n
    '''
def dialogEntityExists():
    '''returns boolean\n\n
    dialogEntityExists(final String id)\n
    '''
def hasDialogEntity():
    '''returns boolean\n\n
    hasDialogEntity(final String id)\n
    '''
def addDialogEntity():
    '''returns None\n\n
    addDialogEntity(final String id)\n
    '''
def removeDialogEntity():
    '''returns None\n\n
    removeDialogEntity(final String id)\n
    '''
def setConditionalSigOptions():
    '''returns None\n\n
    setConditionalSigOptions(final List<String> sigOptions)\n
    '''
def sigOptionHaveCondInputmode():
    '''returns boolean\n\n
    sigOptionHaveCondInputmode(final String sigOption)\n
    '''
def generateDataStores():
    '''returns None\n\n
    generateDataStores(final Element presentationElement, final MXSession mxSession)\n
    '''
def addDataStoreInfo():
    '''returns None\n\n
    addDataStoreInfo(final DataStoreInfo dataStoreInfo)\n
    '''
def getDataStore():
    '''returns DataStoreInfo\n\n
    getDataStore(final String dataStoreId)\n
    '''
def addToCheckForDataStoresList():
    '''returns None\n\n
    addToCheckForDataStoresList(final UIERMEntity currentEntity)\n
    '''
def addRepLibraryEntity():
    '''returns None\n\n
    addRepLibraryEntity(final UIERMEntity currentEntity)\n
    '''
def removeRepLibraryEntitites():
    '''returns None\n\n
    removeRepLibraryEntitites()\n
    '''
