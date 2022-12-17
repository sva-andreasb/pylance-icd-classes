def ():
    '''returns ModelMakerImpl\n\n
    (final GraphMaker maker)\n
    '''
def getGraphMaker():
    '''returns GraphMaker\n\n
    getGraphMaker()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def openModel():
    '''returns Model\n\n
    openModel()\n
    openModel(final String name, final boolean strict)\n
    openModel(final String name)\n
    '''
def openModelIfPresent():
    '''returns Model\n\n
    openModelIfPresent(final String name)\n
    '''
def createModel():
    '''returns Model\n\n
    createModel(final String name, final boolean strict)\n
    createModel(final String name)\n
    '''
def createModelOver():
    '''returns Model\n\n
    createModelOver(final String name)\n
    '''
def createFreshModel():
    '''returns Model\n\n
    createFreshModel()\n
    '''
def createDefaultModel():
    '''returns Model\n\n
    createDefaultModel()\n
    '''
def removeModel():
    '''returns None\n\n
    removeModel(final String name)\n
    '''
def hasModel():
    '''returns boolean\n\n
    hasModel(final String name)\n
    '''
def listModels():
    '''returns ExtendedIterator<String>\n\n
    listModels()\n
    '''
def getModel():
    '''returns Model\n\n
    getModel(final String URL)\n
    getModel(final String URL, final ModelReader loadIfAbsent)\n
    '''
