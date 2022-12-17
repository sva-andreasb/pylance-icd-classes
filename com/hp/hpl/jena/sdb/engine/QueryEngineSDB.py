def ():
    '''returns QueryEngineSDB\n\n
    (final Store store, final Query q)\n
    (final DatasetStoreGraph dsg, final Query query, final Binding initialBinding, final Context context)\n
    (final DatasetStoreGraph dsg, final Op op, final Binding initialBinding, final Context context)\n
    '''
def getRequest():
    '''returns SDBRequest\n\n
    getRequest()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def eval():
    '''returns QueryIterator\n\n
    eval(final Op op, final DatasetGraph dsg, final Binding binding, final Context context)\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final Query query, final DatasetGraph dataset, final Context context)\n
    accept(final Op op, final DatasetGraph dataset, final Context context)\n
    '''
def create():
    '''returns Plan\n\n
    create(final Query query, final DatasetGraph dataset, final Binding inputBinding, final Context context)\n
    create(final Op op, final DatasetGraph dataset, Binding inputBinding, final Context context)\n
    '''
