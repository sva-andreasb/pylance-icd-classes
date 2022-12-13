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
def Workflow():
    '''public Workflow(final Object id)
    public Workflow(final String id, final String title, final boolean enabled)
    '''
def getTitle():
    '''public String getTitle()
    '''
def getNodeIndex():
    '''public Hashtable getNodeIndex()
    '''
def setTitle():
    '''public void setTitle(final String title)
    '''
def getDocumentType():
    '''public Object getDocumentType()
    '''
def setDocumentType():
    '''public void setDocumentType(final Object documentType)
    '''
def isValidated():
    '''public boolean isValidated()
    '''
def setValidated():
    '''public void setValidated(final boolean validated)
    '''
def getId():
    '''public String getId()
    '''
def setId():
    '''public void setId(final String id)
    '''
def getEnabled():
    '''public boolean getEnabled()
    '''
def addNode():
    '''public void addNode(final WorkflowNode node)
    '''
def removeAllNodes():
    '''public void removeAllNodes()
    '''
def removeNode():
    '''public void removeNode(final WorkflowNode node)
    '''
def getNode():
    '''public WorkflowNode getNode(final Object id)
    public WorkflowNode getNode(final int row)
    '''
def getNodes():
    '''public Vector getNodes()
    '''
def addRelationship():
    '''public void addRelationship(final WorkflowRelationship relationship)
    '''
def getRelationship():
    '''public WorkflowRelationship getRelationship(final int index)
    public WorkflowRelationship getRelationship(final int nodeRow, final int actionRow)
    '''
def removeAllRelationships():
    '''public void removeAllRelationships()
    '''
def removeRelationship():
    '''public void removeRelationship(final WorkflowRelationship relationship)
    '''
def getRelationships():
    '''public Vector getRelationships()
    public Vector getRelationships(final WorkflowNode node)
    '''
def getAction():
    '''public WorkflowRelationship getAction(final int row)
    '''
def getRowCount():
    '''public int getRowCount()
    '''
def getColumnCount():
    '''public int getColumnCount()
    '''
def getNextNodeId():
    '''public Object getNextNodeId()
    '''
def getNodeById():
    '''public WorkflowNode getNodeById(final Object id)
    '''
def toString():
    '''public String toString()
    '''
def getRelationshipsAsProperties():
    '''public Vector getRelationshipsAsProperties()
    '''
def getNodesAsProperties():
    '''public Vector getNodesAsProperties()
    '''
