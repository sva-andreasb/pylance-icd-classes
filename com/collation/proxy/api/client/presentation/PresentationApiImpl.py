def ():
    '''returns PresentationApiImpl\n\n
    (final ApiSession sess)\n
    '''
def getDetailsPanel():
    '''returns DetailPanelModel\n\n
    getDetailsPanel(final ObjectRef ref)\n
    getDetailsPanel(final ObjectRef ref, final Locale locale)\n
    '''
def getGraphViewImage():
    '''returns ImageStream\n\n
    getGraphViewImage(final ViewDefiner view)\n
    '''
def getGraphView():
    '''returns TopologyGraphModel\n\n
    getGraphView(final ViewDefiner graphView)\n
    '''
def getTreeView():
    '''returns TopologyTreeModel\n\n
    getTreeView(final ViewDefiner treeView)\n
    '''
def getNodeInfoMap():
    '''returns Map\n\n
    getNodeInfoMap()\n
    '''
def compare():
    '''returns ComparisonResult\n\n
    compare(final ObjectRef obj1, final ObjectRef[] objs, final CompareOptions opts)\n
    compare(final ModelObject left, final ModelObject[] right, final CompareOptions opts)\n
    '''
def findImpactedBusinessApplications():
    '''returns Application[]\n\n
    findImpactedBusinessApplications(final Guid[] objects)\n
    '''
def findImpactedBusinessServices():
    '''returns BusinessSystem[]\n\n
    findImpactedBusinessServices(final Guid[] objects)\n
    '''
