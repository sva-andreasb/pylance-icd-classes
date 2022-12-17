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
    '''
def getTitle():
    '''returns String\n\n
    getTitle()\n
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
    '''returns Object\n\n
    getId()\n
    '''
def setId():
    '''returns None\n\n
    setId(final Object id)\n
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
    getNode(final Object nodeID)\n
    '''
def getNodes():
    '''returns Vector\n\n
    getNodes()\n
    '''
def addRelationship():
    '''returns None\n\n
    addRelationship(final WorkflowRelationship relationship)\n
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
    getNodeById(final Object nodeID)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def buildFromProperties():
    '''returns None\n\n
    buildFromProperties(final Vector nodeList, final Vector rels)\n
    '''
def getNodesAsProperties():
    '''returns Vector\n\n
    getNodesAsProperties()\n
    '''
