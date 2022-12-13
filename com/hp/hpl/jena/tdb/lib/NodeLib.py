def encodeStore():
'''public static long encodeStore(final Node node, final StringFile file)
public static long encodeStore(final Node node, final ObjectFile file)
'''
pass
def fetchDecode():
'''public static Node fetchDecode(final long id, final StringFile file)
public static Node fetchDecode(final long id, final ObjectFile file)
'''
pass
def hash():
'''public static Hash hash(final Node n)
'''
pass
def setHash():
'''public static void setHash(final Hash h, final Node n)
'''
pass
def getNodeId():
'''public static NodeId getNodeId(final Record r, final int idx)
'''
pass
def termOrAny():
'''public static Node termOrAny(final Node node)
'''
pass
def format():
'''public static String format(final String sep, final Node[] nodes)
'''
pass
def nodes():
'''public static Iterator<Node> nodes(final NodeTable nodeTable, final Iterator<NodeId> iter)
'''
pass
def convert():
'''public Node convert(final NodeId item)
'''
pass
