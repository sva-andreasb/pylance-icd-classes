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
public Workflow(final String id, final String title, final boolean enabled)
'''
pass
def getTitle():
'''public String getTitle()
'''
pass
def getNodeIndex():
'''public Hashtable getNodeIndex()
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
'''public String getId()
'''
pass
def setId():
'''public void setId(final String id)
'''
pass
def getEnabled():
'''public boolean getEnabled()
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
'''public WorkflowNode getNode(final Object id)
public WorkflowNode getNode(final int row)
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
def getRelationship():
'''public WorkflowRelationship getRelationship(final int index)
public WorkflowRelationship getRelationship(final int nodeRow, final int actionRow)
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
def getAction():
'''public WorkflowRelationship getAction(final int row)
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
'''public WorkflowNode getNodeById(final Object id)
'''
pass
def toString():
'''public String toString()
'''
pass
def getRelationshipsAsProperties():
'''public Vector getRelationshipsAsProperties()
'''
pass
def getNodesAsProperties():
'''public Vector getNodesAsProperties()
'''
pass
