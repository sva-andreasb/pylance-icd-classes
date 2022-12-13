def encodeStore():
    '''public static long encodeStore(final Node node, final StringFile file)
    public static long encodeStore(final Node node, final ObjectFile file)
    '''
def fetchDecode():
    '''public static Node fetchDecode(final long id, final StringFile file)
    public static Node fetchDecode(final long id, final ObjectFile file)
    '''
def hash():
    '''public static Hash hash(final Node n)
    '''
def setHash():
    '''public static void setHash(final Hash h, final Node n)
    '''
def getNodeId():
    '''public static NodeId getNodeId(final Record r, final int idx)
    '''
def termOrAny():
    '''public static Node termOrAny(final Node node)
    '''
def format():
    '''public static String format(final String sep, final Node[] nodes)
    '''
def nodes():
    '''public static Iterator<Node> nodes(final NodeTable nodeTable, final Iterator<NodeId> iter)
    '''
def convert():
    '''public Node convert(final NodeId item)
    '''
