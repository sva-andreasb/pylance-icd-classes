NODE_ID = "String  id""
NODE_ROW = "String  row""
NODE_COL = "String  col""
NODE_TITLE = "String  title""
NODE_TYPE = "String  type""
NODE_STATE = "String  state""
NODE_ERROR_KEY = "String  errorkey""
REL_FROMID = "String  fromid""
REL_TOID = "String  toid""
REL_NEGATIVE = "String  negative""
def Workflow():
'''public Workflow(final Object id)
'''
pass
def getTitle():
'''public String getTitle()
'''
pass
def setTitle():
'''public void setTitle(final String title)
'''
pass
def getDocumentType():
'''public Object getDocumentType()
'''
pass
def setDocumentType():
'''public void setDocumentType(final Object documentType)
'''
pass
def isValidated():
'''public boolean isValidated()
'''
pass
def setValidated():
'''public void setValidated(final boolean validated)
'''
pass
def getId():
'''public Object getId()
'''
pass
def setId():
'''public void setId(final Object id)
'''
pass
def addNode():
'''public void addNode(final WorkflowNode node)
'''
pass
def removeAllNodes():
'''public void removeAllNodes()
'''
pass
def removeNode():
'''public void removeNode(final WorkflowNode node)
'''
pass
def getNode():
'''public WorkflowNode getNode(final Object nodeID)
'''
pass
def getNodes():
'''public Vector getNodes()
'''
pass
def addRelationship():
'''public void addRelationship(final WorkflowRelationship relationship)
'''
pass
def removeAllRelationships():
'''public void removeAllRelationships()
'''
pass
def removeRelationship():
'''public void removeRelationship(final WorkflowRelationship relationship)
'''
pass
def getRelationships():
'''public Vector getRelationships()
public Vector getRelationships(final WorkflowNode node)
'''
pass
def getRowCount():
'''public int getRowCount()
'''
pass
def getColumnCount():
'''public int getColumnCount()
'''
pass
def getNextNodeId():
'''public Object getNextNodeId()
'''
pass
def getNodeById():
'''public WorkflowNode getNodeById(final Object nodeID)
'''
pass
def toString():
'''public String toString()
'''
pass
def buildFromProperties():
'''public void buildFromProperties(final Vector nodeList, final Vector rels)
'''
pass
def getRelationshipsAsProperties():
'''public Vector<Hashtable<String, Object>> getRelationshipsAsProperties()
'''
pass
def getNodesAsProperties():
'''public Vector getNodesAsProperties()
'''
pass
