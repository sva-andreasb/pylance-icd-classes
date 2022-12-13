def QueryEngineSDB():
'''public QueryEngineSDB(final Store store, final Query q)
public QueryEngineSDB(final DatasetStoreGraph dsg, final Query query, final Binding initialBinding, final Context context)
public QueryEngineSDB(final DatasetStoreGraph dsg, final Op op, final Binding initialBinding, final Context context)
'''
pass
def getRequest():
'''public SDBRequest getRequest()
'''
pass
def close():
'''public void close()
'''
pass
def eval():
'''public QueryIterator eval(final Op op, final DatasetGraph dsg, final Binding binding, final Context context)
'''
pass
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
def accept():
'''public boolean accept(final Query query, final DatasetGraph dataset, final Context context)
public boolean accept(final Op op, final DatasetGraph dataset, final Context context)
'''
pass
def create():
'''public Plan create(final Query query, final DatasetGraph dataset, final Binding inputBinding, final Context context)
public Plan create(final Op op, final DatasetGraph dataset, Binding inputBinding, final Context context)
'''
pass
