def getFactory():
'''public static QueryEngineFactory getFactory()
'''
pass
def register():
'''public static void register()
'''
pass
def unregister():
'''public static void unregister()
'''
pass
def eval():
'''public QueryIterator eval(Op op, DatasetGraph dsg, final Binding input, final Context context)
'''
pass
def getMillis():
'''public long getMillis()
'''
pass
def TransformGraphRename():
'''public TransformGraphRename(final Node oldGraphName, final Node newGraphName)
'''
pass
def transform():
'''public Op transform(OpGraph opGraph, final Op x)
public Op transform(OpQuadPattern opQuadPattern)
'''
pass
def accept():
'''public boolean accept(final Query query, final DatasetGraph dataset, final Context context)
public boolean accept(final Op op, final DatasetGraph dataset, final Context context)
'''
pass
def create():
'''public Plan create(final Query query, final DatasetGraph ds, final Binding input, final Context context)
public Plan create(final Op op, final DatasetGraph dataset, final Binding binding, final Context context)
'''
pass
