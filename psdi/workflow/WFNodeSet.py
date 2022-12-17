def ():
    '''returns WFNodeSet\n\n
    (final MboServerInterface ms)\n
    '''
def getStartNode():
    '''returns WFNode\n\n
    getStartNode()\n
    '''
def getNode():
    '''returns WFNode\n\n
    getNode(final int nodeid)\n
    '''
def buildSubProcessList():
    '''returns None\n\n
    buildSubProcessList(final Hashtable<String, String> h, final String processName, final String processrev)\n
    '''
def wfValidate():
    '''returns None\n\n
    wfValidate(final Vector<MXException> v, final Hashtable<String, String> hinfo)\n
    '''
def hasPositiveStop():
    '''returns boolean\n\n
    hasPositiveStop(final String processName, final String processrev)\n
    '''
def hasNegativeStop():
    '''returns boolean\n\n
    hasNegativeStop(final String processName, final String processrev)\n
    '''
def getNextNodeNum():
    '''returns int\n\n
    getNextNodeNum()\n
    '''
def duplicateNodes():
    '''returns None\n\n
    duplicateNodes(final WFNodeSet originalNodes)\n
    '''
