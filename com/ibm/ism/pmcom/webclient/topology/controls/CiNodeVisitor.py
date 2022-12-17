COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
def setImpactedCI():
    '''returns None\n\n
    setImpactedCI(final Hashtable<String, Boolean> impactedCI)\n
    '''
def ():
    '''returns CiNodeVisitor\n\n
    (final CiTopologyViewInfo model, final int maxNodeDepth, final int maxCiDepth, final int maxNodes, final boolean showEvents, final String application)\n
    (final IlvDefaultSDMModel model, final int maxNodeDepth, final int maxCiDepth, final int maxNodes, final boolean showEvents, final String application)\n
    '''
def atMaxNodeDepth():
    '''returns boolean\n\n
    atMaxNodeDepth()\n
    '''
def maxNodesReached():
    '''returns boolean\n\n
    maxNodesReached()\n
    '''
def atMaxCiDepth():
    '''returns boolean\n\n
    atMaxCiDepth()\n
    '''
def notVisited():
    '''returns boolean\n\n
    notVisited(final String cinum)\n
    '''
def push():
    '''returns None\n\n
    push(final String ciNum, final Object node)\n
    push(final String ciNum, final HashSet<String> fromRelations, final HashSet<String> toRelations)\n
    push(final String ciNum, final Object node, final HashSet<String> inRelations, final HashSet<String> outRelations)\n
    '''
def pop():
    '''returns None\n\n
    pop()\n
    '''
def createNode_new():
    '''returns Object[]\n\n
    createNode_new(final MboRemote ciMbo, final String tag)\n
    '''
def createNode():
    '''returns Object[]\n\n
    createNode(final MboRemote ciMbo, final String tag)\n
    '''
def isCiImpacted():
    '''returns boolean\n\n
    isCiImpacted(final String cinum)\n
    '''
def createLink_new():
    '''returns None\n\n
    createLink_new(final Object from, final Object to, final String relation)\n
    '''
def createLink():
    '''returns None\n\n
    createLink(final Object from, final Object to, final String relation)\n
    '''
def createLinks_new():
    '''returns None\n\n
    createLinks_new(final Object node, final HashSet<String> inRelations, final HashSet<String> outRelations, final String tag, final boolean detailView)\n
    '''
def createLinks():
    '''returns None\n\n
    createLinks(final Object node, final HashSet<String> inRelations, final HashSet<String> outRelations, final String tag, final boolean detailView)\n
    '''
def getClassificationId():
    '''returns String\n\n
    getClassificationId(final MboRemote ciMbo)\n
    '''
def isTopLevelCi():
    '''returns boolean\n\n
    isTopLevelCi(final MboRemote ciMbo)\n
    '''
def getNodeImage():
    '''returns String\n\n
    getNodeImage(final MboRemote ciMbo)\n
    '''
def getNodeToolTip():
    '''returns String\n\n
    getNodeToolTip(final MboRemote ciMbo, final boolean showStatus, final String ciNum, final String ciName)\n
    '''
def getLinkToolTip():
    '''returns String\n\n
    getLinkToolTip(final String relations)\n
    '''
def getScheduledTasks():
    '''returns int\n\n
    getScheduledTasks(final MboRemote ciMbo)\n
    '''
def getIncidentAndEventCounts():
    '''returns Object[]\n\n
    getIncidentAndEventCounts(final MboRemote ciMbo, final boolean mappedToOSLC)\n
    '''
def getStatusToolTip():
    '''returns String\n\n
    getStatusToolTip(final MboRemote ciMbo, final String status)\n
    '''
def getIncidentToolTip():
    '''returns String\n\n
    getIncidentToolTip(final MboRemote ciMbo, final String cinum, final String ciName, final int size, final int eventCount)\n
    '''
def getInPrgTasksToolTip():
    '''returns String\n\n
    getInPrgTasksToolTip(final MboRemote ciMbo, final String cinum, final String ciName, final int size)\n
    '''
def generateLinkId():
    '''returns String\n\n
    generateLinkId(final Object from, final Object to, final String relation)\n
    '''
def getModel():
    '''returns IlvDefaultSDMModel\n\n
    getModel()\n
    '''
def getModel_new():
    '''returns CiTopologyViewInfo\n\n
    getModel_new()\n
    '''
def getBundle():
    '''returns ResourceBundle\n\n
    getBundle()\n
    '''
def setBundle():
    '''returns None\n\n
    setBundle(final ResourceBundle bundle)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
