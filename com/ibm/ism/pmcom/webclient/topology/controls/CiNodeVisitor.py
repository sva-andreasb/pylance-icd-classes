COPYRIGHT = "String  \n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n""
def getImpactedCI():
'''public Hashtable<String, Boolean> getImpactedCI()
'''
pass
def setImpactedCI():
'''public void setImpactedCI(final Hashtable<String, Boolean> impactedCI)
'''
pass
def CiNodeVisitor():
'''public CiNodeVisitor(final CiTopologyViewInfo model, final int maxNodeDepth, final int maxCiDepth, final int maxNodes, final boolean showEvents, final String application)
public CiNodeVisitor(final IlvDefaultSDMModel model, final int maxNodeDepth, final int maxCiDepth, final int maxNodes, final boolean showEvents, final String application)
'''
pass
def atMaxNodeDepth():
'''public boolean atMaxNodeDepth()
'''
pass
def maxNodesReached():
'''public boolean maxNodesReached()
'''
pass
def atMaxCiDepth():
'''public boolean atMaxCiDepth()
'''
pass
def notVisited():
'''public boolean notVisited(final String cinum)
'''
pass
def push():
'''public void push(final String ciNum, final Object node)
public void push(final String ciNum, final HashSet<String> fromRelations, final HashSet<String> toRelations)
public void push(final String ciNum, final Object node, final HashSet<String> inRelations, final HashSet<String> outRelations)
'''
pass
def pop():
'''public void pop()
'''
pass
def createNode_new():
'''public Object[] createNode_new(final MboRemote ciMbo, final String tag)
'''
pass
def createNode():
'''public Object[] createNode(final MboRemote ciMbo, final String tag)
'''
pass
def isCiImpacted():
'''public boolean isCiImpacted(final String cinum)
'''
pass
def createLink_new():
'''public void createLink_new(final Object from, final Object to, final String relation)
'''
pass
def createLink():
'''public void createLink(final Object from, final Object to, final String relation)
'''
pass
def createLinks_new():
'''public void createLinks_new(final Object node, final HashSet<String> inRelations, final HashSet<String> outRelations, final String tag, final boolean detailView)
'''
pass
def createLinks():
'''public void createLinks(final Object node, final HashSet<String> inRelations, final HashSet<String> outRelations, final String tag, final boolean detailView)
'''
pass
def getClassificationId():
'''public String getClassificationId(final MboRemote ciMbo)
'''
pass
def isTopLevelCi():
'''public boolean isTopLevelCi(final MboRemote ciMbo)
'''
pass
def getNodeImage():
'''public String getNodeImage(final MboRemote ciMbo)
'''
pass
def getNodeToolTip():
'''public String getNodeToolTip(final MboRemote ciMbo, final boolean showStatus, final String ciNum, final String ciName)
'''
pass
def getLinkToolTip():
'''public String getLinkToolTip(final String relations)
'''
pass
def getScheduledTasks():
'''public int getScheduledTasks(final MboRemote ciMbo)
'''
pass
def getIncidentAndEventCounts():
'''public Object[] getIncidentAndEventCounts(final MboRemote ciMbo, final boolean mappedToOSLC)
'''
pass
def getStatusToolTip():
'''public String getStatusToolTip(final MboRemote ciMbo, final String status)
'''
pass
def getIncidentToolTip():
'''public String getIncidentToolTip(final MboRemote ciMbo, final String cinum, final String ciName, final int size, final int eventCount)
'''
pass
def getInPrgTasksToolTip():
'''public String getInPrgTasksToolTip(final MboRemote ciMbo, final String cinum, final String ciName, final int size)
'''
pass
def generateLinkId():
'''public String generateLinkId(final Object from, final Object to, final String relation)
'''
pass
def getModel():
'''public IlvDefaultSDMModel getModel()
'''
pass
def getModel_new():
'''public CiTopologyViewInfo getModel_new()
'''
pass
def getBundle():
'''public ResourceBundle getBundle()
'''
pass
def setBundle():
'''public void setBundle(final ResourceBundle bundle)
'''
pass
def toString():
'''public String toString()
'''
pass
