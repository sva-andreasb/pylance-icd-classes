NODE_ID = "String  \"id\""
NODE_ROW = "String  \"row\""
NODE_COL = "String  \"col\""
NODE_TITLE = "String  \"title\""
NODE_TYPE = "String  \"type\""
NODE_STATE = "String  \"state\""
NODE_ERROR_KEY = "String  \"errorkey\""
REL_FROMID = "String  \"fromid\""
REL_TOID = "String  \"toid\""
REL_NEGATIVE = "String  \"negative\""
def ():
    '''returns Workflow\n\n
    (final Object id)\n
    (final String id, final String title, final boolean enabled)\n
    '''
def getTitle():
    '''returns String\n\n
    getTitle()\n
    '''
def getNodeIndex():
    '''returns Hashtable\n\n
    getNodeIndex()\n
    '''
def setTitle():
    '''returns None\n\n
    setTitle(final String title)\n
    '''
def getDocumentType():
    '''returns Object\n\n
    getDocumentType()\n
    '''
def setDocumentType():
    '''returns None\n\n
    setDocumentType(final Object documentType)\n
    '''
def isValidated():
    '''returns boolean\n\n
    isValidated()\n
    '''
def setValidated():
    '''returns None\n\n
    setValidated(final boolean validated)\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
def setId():
    '''returns None\n\n
    setId(final String id)\n
    '''
def getEnabled():
    '''returns boolean\n\n
    getEnabled()\n
    '''
def addNode():
    '''returns None\n\n
    addNode(final WorkflowNode node)\n
    '''
def removeAllNodes():
    '''returns None\n\n
    removeAllNodes()\n
    '''
def removeNode():
    '''returns None\n\n
    removeNode(final WorkflowNode node)\n
    '''
def getNode():
    '''returns WorkflowNode\n\n
    getNode(final Object id)\n
    getNode(final int row)\n
    '''
def getNodes():
    '''returns Vector\n\n
    getNodes()\n
    '''
def addRelationship():
    '''returns None\n\n
    addRelationship(final WorkflowRelationship relationship)\n
    '''
def getRelationship():
    '''returns WorkflowRelationship\n\n
    getRelationship(final int index)\n
    getRelationship(final int nodeRow, final int actionRow)\n
    '''
def removeAllRelationships():
    '''returns None\n\n
    removeAllRelationships()\n
    '''
def removeRelationship():
    '''returns None\n\n
    removeRelationship(final WorkflowRelationship relationship)\n
    '''
def getRelationships():
    '''returns Vector\n\n
    getRelationships()\n
    getRelationships(final WorkflowNode node)\n
    '''
def getAction():
    '''returns WorkflowRelationship\n\n
    getAction(final int row)\n
    '''
def getRowCount():
    '''returns int\n\n
    getRowCount()\n
    '''
def getColumnCount():
    '''returns int\n\n
    getColumnCount()\n
    '''
def getNextNodeId():
    '''returns Object\n\n
    getNextNodeId()\n
    '''
def getNodeById():
    '''returns WorkflowNode\n\n
    getNodeById(final Object id)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getRelationshipsAsProperties():
    '''returns Vector\n\n
    getRelationshipsAsProperties()\n
    '''
def getNodesAsProperties():
    '''returns Vector\n\n
    getNodesAsProperties()\n
    '''
