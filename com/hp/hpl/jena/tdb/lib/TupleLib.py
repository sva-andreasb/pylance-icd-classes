def convertToNodes():
    '''public static Iterator<Tuple<Node>> convertToNodes(final NodeTable nodeTable, final Iterator<Tuple<NodeId>> iter)
    '''
def convert():
    '''public Tuple<Node> convert(final Tuple<NodeId> item)
    public Tuple<NodeId> convert(final Tuple<Node> item)
    public Triple convert(final Tuple<NodeId> item)
    public Quad convert(final Tuple<NodeId> item)
    '''
def convertToNodeId():
    '''public static Iterator<Tuple<NodeId>> convertToNodeId(final NodeTable nodeTable, final Iterator<Tuple<Node>> iter)
    '''
def convertToTriples():
    '''public static Iterator<Triple> convertToTriples(final NodeTable nodeTable, final Iterator<Tuple<NodeId>> iter)
    '''
def convertToQuads():
    '''public static Iterator<Quad> convertToQuads(final NodeTable nodeTable, final Iterator<Tuple<NodeId>> iter)
    '''
def tupleNodes():
    '''public static Tuple<Node> tupleNodes(final NodeTable nodeTable, final Tuple<NodeId> ids)
    '''
def tupleNodeIds():
    '''public static Tuple<NodeId> tupleNodeIds(final NodeTable nodeTable, final Tuple<Node> nodes)
    '''
def tuple():
    '''public static Tuple<NodeId> tuple(final Record r, final ColumnMap cMap)
    '''
def record():
    '''public static Record record(final RecordFactory factory, final Tuple<NodeId> tuple, final ColumnMap cMap)
    '''
