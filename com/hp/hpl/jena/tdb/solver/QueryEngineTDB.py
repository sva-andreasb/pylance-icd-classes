def getFactory():
    '''public static QueryEngineFactory getFactory()
    '''
def register():
    '''public static void register()
    '''
def unregister():
    '''public static void unregister()
    '''
def eval():
    '''public QueryIterator eval(Op op, DatasetGraph dsg, final Binding input, final Context context)
    '''
def getMillis():
    '''public long getMillis()
    '''
def TransformGraphRename():
    '''public TransformGraphRename(final Node oldGraphName, final Node newGraphName)
    '''
def transform():
    '''public Op transform(OpGraph opGraph, final Op x)
    public Op transform(OpQuadPattern opQuadPattern)
    '''
def accept():
    '''public boolean accept(final Query query, final DatasetGraph dataset, final Context context)
    public boolean accept(final Op op, final DatasetGraph dataset, final Context context)
    '''
def create():
    '''public Plan create(final Query query, final DatasetGraph ds, final Binding input, final Context context)
    public Plan create(final Op op, final DatasetGraph dataset, final Binding binding, final Context context)
    '''
