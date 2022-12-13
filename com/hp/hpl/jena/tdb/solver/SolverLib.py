def execute():
    '''public static QueryIterator execute(final GraphTDB graph, final BasicPattern pattern, final QueryIterator input, final Filter<Tuple<NodeId>> filter, final ExecutionContext execCxt)
    public static QueryIterator execute(final DatasetGraphTDB ds, final Node graphNode, final BasicPattern pattern, final QueryIterator input, final Filter<Tuple<NodeId>> filter, final ExecutionContext execCxt)
    '''
def convertToIds():
    '''public static Iterator<BindingNodeId> convertToIds(final Iterator<Binding> iterBindings, final NodeTable nodeTable)
    '''
def convertToNodes():
    '''public static Iterator<Binding> convertToNodes(final Iterator<BindingNodeId> iterBindingIds, final NodeTable nodeTable)
    public static Set<Node> convertToNodes(final Collection<String> uris)
    '''
def convert():
    '''public Binding convert(final BindingNodeId bindingNodeIds)
    public BindingNodeId convert(final Binding binding)
    public Binding convert(final Node node)
    public Iterator<Binding> convert(final NodeTable nodeTable, final Iterator<BindingNodeId> iterBindingIds)
    '''
def convToBinding():
    '''public static Binding convToBinding(final NodeTable nodeTable, final BindingNodeId bindingNodeIds)
    '''
def graphNames():
    '''public static QueryIterator graphNames(final DatasetGraphTDB ds, final Node graphNode, final QueryIterator input, final Filter<Tuple<NodeId>> filter, final ExecutionContext execCxt)
    '''
def strPattern():
    '''public static String strPattern(final BasicPattern pattern)
    '''
def convertToNodeIds():
    '''public static Set<NodeId> convertToNodeIds(final Collection<Node> nodes, final DatasetGraphTDB dataset)
    '''
