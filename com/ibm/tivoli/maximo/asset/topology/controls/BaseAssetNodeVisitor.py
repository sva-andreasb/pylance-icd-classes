def getImpactedAsset():
    '''    public Hashtable<String, Boolean> getImpactedAsset()
    '''
def setImpactedASset():
    '''    public void setImpactedASset(final Hashtable<String, Boolean> impactedAsset)
    '''
def BaseAssetNodeVisitor():
    '''    public BaseAssetNodeVisitor(final IlvDefaultSDMModel model, final int maxNodeDepth, final int maxAssetDepth, final int maxNodes)
    '''
def nativeInit():
    '''    public static synchronized void nativeInit(final MboRemote mbo)
    '''
def atMaxNodeDepth():
    '''    public boolean atMaxNodeDepth()
    '''
def maxNodesReached():
    '''    public boolean maxNodesReached()
    '''
def atMaxAssetDepth():
    '''    public boolean atMaxAssetDepth()
    '''
def notVisited():
    '''    public boolean notVisited(final String assetnum)
    '''
def proceedDeepForEncounteredNode():
    '''    public boolean proceedDeepForEncounteredNode(final String assetnum)
    '''
def push():
    '''    public void push(final String assetNum, final Object ilvNode)
    public void push(final String assetNum, final HashSet<String> fromRelations, final HashSet<String> toRelations)
    public void push(final String assetNum, final Object ilvNode, final HashSet<String> inRelations, final HashSet<String> outRelations)
    '''
def pop():
    '''    public void pop()
    '''
def generateIlvNode():
    '''    public Object generateIlvNode(final MboRemote assetMbo, final String tag)
    '''
def setupMouseOverInfo():
    '''    public void setupMouseOverInfo(final MboRemote mbo)
    '''
def isCiImpacted():
    '''    public boolean isCiImpacted(final String assetnum)
    '''
def generateLinks():
    '''    public void generateLinks(final Object ilvNode, final HashSet<String> inRelations, final HashSet<String> outRelations, final String tag)
    '''
def getCLASSSTRUCTURE_CLASSIFICATIONID():
    '''    public String getCLASSSTRUCTURE_CLASSIFICATIONID(final MboRemote assetMbo)
    '''
def getClassificationId():
    '''    public String getClassificationId(final MboRemote assetMbo)
    '''
def getCLASSSTRUCTURE_DESCRIPTION():
    '''    public String getCLASSSTRUCTURE_DESCRIPTION(final MboRemote assetMbo)
    '''
def isTopLevelAsset():
    '''    public boolean isTopLevelAsset(final MboRemote assetMbo)
    '''
def getNodeImage():
    '''    public String getNodeImage(final MboRemote assetMbo)
    '''
def getLinkToolTip():
    '''    public String getLinkToolTip(final String relations)
    '''
def getScheduledTaskIndicator():
    '''    public TaskIndicator getScheduledTaskIndicator(final MboRemote assetMbo)
    '''
def setNodeDegree():
    '''    public void setNodeDegree(final String assetnum, final int degree)
    '''
def compare():
    '''    public int compare(final NodeTooltipInfo object1, final NodeTooltipInfo object2)
    '''
def toString():
    '''    public String toString()
    public String toString()
    public String toString()
    '''
def NodeTooltipInfo():
    '''    public NodeTooltipInfo()
    '''
def getName():
    '''    public String getName()
    '''
def getMoObject():
    '''    public String getMoObject()
    '''
def getMoAttribute():
    '''    public String getMoAttribute()
    '''
def getDisplayTitle():
    '''    public String getDisplayTitle()
    '''
def getDisplayOrder():
    '''    public int getDisplayOrder()
    '''
def ValueDetail():
    '''    public ValueDetail()
    public ValueDetail(final String valuelabel)
    public ValueDetail(final String valuelabel, final LinearData startLinearData, final LinearData endLinearData)
    '''
def getValuelabel():
    '''    public String getValuelabel()
    '''
def getStartLinearData():
    '''    public LinearData getStartLinearData()
    '''
def getEndLinearData():
    '''    public LinearData getEndLinearData()
    '''
def LinearData():
    '''    public LinearData(final boolean isRTL)
    '''
def getLinearLabel():
    '''    public String getLinearLabel()
    '''
def getLinearMeasure():
    '''    public String getLinearMeasure()
    '''
def getLinearMeasureUnitID():
    '''    public String getLinearMeasureUnitID()
    '''
