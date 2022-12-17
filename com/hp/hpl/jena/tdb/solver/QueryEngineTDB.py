def eval():
    '''returns QueryIterator\n\n
    eval(Op op, DatasetGraph dsg, final Binding input, final Context context)\n
    '''
def getMillis():
    '''returns long\n\n
    getMillis()\n
    '''
def ():
    '''returns TransformGraphRename\n\n
    (final Node oldGraphName, final Node newGraphName)\n
    '''
def transform():
    '''returns Op\n\n
    transform(OpGraph opGraph, final Op x)\n
    transform(OpQuadPattern opQuadPattern)\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final Query query, final DatasetGraph dataset, final Context context)\n
    accept(final Op op, final DatasetGraph dataset, final Context context)\n
    '''
def create():
    '''returns Plan\n\n
    create(final Query query, final DatasetGraph ds, final Binding input, final Context context)\n
    create(final Op op, final DatasetGraph dataset, final Binding binding, final Context context)\n
    '''
