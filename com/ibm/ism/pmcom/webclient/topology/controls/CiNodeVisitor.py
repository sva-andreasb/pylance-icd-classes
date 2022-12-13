COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
def getImpactedCI():
    '''    public Hashtable<String, Boolean> getImpactedCI()
    '''
def setImpactedCI():
    '''    public void setImpactedCI(final Hashtable<String, Boolean> impactedCI)
    '''
def CiNodeVisitor():
    '''    public CiNodeVisitor(final CiTopologyViewInfo model, final int maxNodeDepth, final int maxCiDepth, final int maxNodes, final boolean showEvents, final String application)
    public CiNodeVisitor(final IlvDefaultSDMModel model, final int maxNodeDepth, final int maxCiDepth, final int maxNodes, final boolean showEvents, final String application)
    '''
def atMaxNodeDepth():
    '''    public boolean atMaxNodeDepth()
    '''
def maxNodesReached():
    '''    public boolean maxNodesReached()
    '''
def atMaxCiDepth():
    '''    public boolean atMaxCiDepth()
    '''
def notVisited():
    '''    public boolean notVisited(final String cinum)
    '''
def push():
    '''    public void push(final String ciNum, final Object node)
    public void push(final String ciNum, final HashSet<String> fromRelations, final HashSet<String> toRelations)
    public void push(final String ciNum, final Object node, final HashSet<String> inRelations, final HashSet<String> outRelations)
    '''
def pop():
    '''    public void pop()
    '''
def createNode_new():
    '''    public Object[] createNode_new(final MboRemote ciMbo, final String tag)
    '''
def createNode():
    '''    public Object[] createNode(final MboRemote ciMbo, final String tag)
    '''
def isCiImpacted():
    '''    public boolean isCiImpacted(final String cinum)
    '''
def createLink_new():
    '''    public void createLink_new(final Object from, final Object to, final String relation)
    '''
def createLink():
    '''    public void createLink(final Object from, final Object to, final String relation)
    '''
def createLinks_new():
    '''    public void createLinks_new(final Object node, final HashSet<String> inRelations, final HashSet<String> outRelations, final String tag, final boolean detailView)
    '''
def createLinks():
    '''    public void createLinks(final Object node, final HashSet<String> inRelations, final HashSet<String> outRelations, final String tag, final boolean detailView)
    '''
def getClassificationId():
    '''    public String getClassificationId(final MboRemote ciMbo)
    '''
def isTopLevelCi():
    '''    public boolean isTopLevelCi(final MboRemote ciMbo)
    '''
def getNodeImage():
    '''    public String getNodeImage(final MboRemote ciMbo)
    '''
def getNodeToolTip():
    '''    public String getNodeToolTip(final MboRemote ciMbo, final boolean showStatus, final String ciNum, final String ciName)
    '''
def getLinkToolTip():
    '''    public String getLinkToolTip(final String relations)
    '''
def getScheduledTasks():
    '''    public int getScheduledTasks(final MboRemote ciMbo)
    '''
def getIncidentAndEventCounts():
    '''    public Object[] getIncidentAndEventCounts(final MboRemote ciMbo, final boolean mappedToOSLC)
    '''
def getStatusToolTip():
    '''    public String getStatusToolTip(final MboRemote ciMbo, final String status)
    '''
def getIncidentToolTip():
    '''    public String getIncidentToolTip(final MboRemote ciMbo, final String cinum, final String ciName, final int size, final int eventCount)
    '''
def getInPrgTasksToolTip():
    '''    public String getInPrgTasksToolTip(final MboRemote ciMbo, final String cinum, final String ciName, final int size)
    '''
def generateLinkId():
    '''    public String generateLinkId(final Object from, final Object to, final String relation)
    '''
def getModel():
    '''    public IlvDefaultSDMModel getModel()
    '''
def getModel_new():
    '''    public CiTopologyViewInfo getModel_new()
    '''
def getBundle():
    '''    public ResourceBundle getBundle()
    '''
def setBundle():
    '''    public void setBundle(final ResourceBundle bundle)
    '''
def toString():
    '''    public String toString()
    '''
