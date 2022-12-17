def ():
    '''returns DatasetGraphTDB\n\n
    (final TripleTable tripleTable, final QuadTable quadTable, final DatasetPrefixStorage prefixes, final ReorderTransformation transform, final Location location, final Properties config)\n
    '''
def duplicate():
    '''returns DatasetGraphTDB\n\n
    duplicate()\n
    '''
def getQuadTable():
    '''returns QuadTable\n\n
    getQuadTable()\n
    '''
def getTripleTable():
    '''returns TripleTable\n\n
    getTripleTable()\n
    '''
def containsGraph():
    '''returns boolean\n\n
    containsGraph(final Node graphNode)\n
    '''
def getDefaultGraphTDB():
    '''returns GraphTDB\n\n
    getDefaultGraphTDB()\n
    '''
def getGraphTDB():
    '''returns GraphTDB\n\n
    getGraphTDB(final Node graphNode)\n
    '''
def setEffectiveDefaultGraph():
    '''returns None\n\n
    setEffectiveDefaultGraph(final GraphTDB g)\n
    '''
def getEffectiveDefaultGraph():
    '''returns GraphTDB\n\n
    getEffectiveDefaultGraph()\n
    '''
def getConfig():
    '''returns Properties\n\n
    getConfig()\n
    '''
def getConfigValue():
    '''returns String\n\n
    getConfigValue(final String key)\n
    '''
def getConfigValueAsInt():
    '''returns int\n\n
    getConfigValueAsInt(final String key, final int dftValue)\n
    '''
def getTransform():
    '''returns ReorderTransformation\n\n
    getTransform()\n
    '''
def getPrefixes():
    '''returns DatasetPrefixStorage\n\n
    getPrefixes()\n
    '''
def listGraphNodes():
    '''returns Iterator<Node>\n\n
    listGraphNodes()\n
    '''
def size():
    '''returns long\n\n
    size()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def getLocation():
    '''returns Location\n\n
    getLocation()\n
    '''
def sync():
    '''returns None\n\n
    sync()\n
    sync(final boolean force)\n
    '''
def startRequest():
    '''returns None\n\n
    startRequest()\n
    '''
def finishRequest():
    '''returns None\n\n
    finishRequest()\n
    '''
def toDataset():
    '''returns Dataset\n\n
    toDataset()\n
    '''
def addGraph():
    '''returns None\n\n
    addGraph(final Node graphName, final Graph graph)\n
    '''
def setDefaultGraph():
    '''returns None\n\n
    setDefaultGraph(final Graph g)\n
    '''
def convert():
    '''returns NodeId\n\n
    convert(final Tuple<NodeId> item)\n
    '''
