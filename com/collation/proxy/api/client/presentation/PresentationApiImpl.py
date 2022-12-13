def PresentationApiImpl():
    '''public PresentationApiImpl(final ApiSession sess)
    '''
def getDetailsPanel():
    '''public DetailPanelModel getDetailsPanel(final ObjectRef ref)
    public DetailPanelModel getDetailsPanel(final ObjectRef ref, final Locale locale)
    '''
def getGraphViewImage():
    '''public ImageStream getGraphViewImage(final ViewDefiner view)
    '''
def getGraphView():
    '''public TopologyGraphModel getGraphView(final ViewDefiner graphView)
    '''
def getTreeView():
    '''public TopologyTreeModel getTreeView(final ViewDefiner treeView)
    '''
def getNodeInfoMap():
    '''public Map getNodeInfoMap()
    '''
def compare():
    '''public ComparisonResult compare(final ObjectRef obj1, final ObjectRef[] objs, final CompareOptions opts)
    public ComparisonResult compare(final ModelObject left, final ModelObject[] right, final CompareOptions opts)
    '''
def findImpactedBusinessApplications():
    '''public Application[] findImpactedBusinessApplications(final Guid[] objects)
    '''
def findImpactedBusinessServices():
    '''public BusinessSystem[] findImpactedBusinessServices(final Guid[] objects)
    '''
