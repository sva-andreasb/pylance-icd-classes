def ():
    '''returns RDFListImpl\n\n
    (final Node n, final EnhGraph g)\n
    '''
def listType():
    '''returns Resource\n\n
    listType()\n
    '''
def listNil():
    '''returns Resource\n\n
    listNil()\n
    '''
def listFirst():
    '''returns Property\n\n
    listFirst()\n
    '''
def listRest():
    '''returns Property\n\n
    listRest()\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def getHead():
    '''returns RDFNode\n\n
    getHead()\n
    '''
def setHead():
    '''returns RDFNode\n\n
    setHead(final RDFNode value)\n
    '''
def getTail():
    '''returns RDFList\n\n
    getTail()\n
    '''
def setTail():
    '''returns RDFList\n\n
    setTail(final RDFList tail)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def cons():
    '''returns RDFList\n\n
    cons(final RDFNode value)\n
    '''
def add():
    '''returns None\n\n
    add(final RDFNode value)\n
    '''
def with():
    '''returns RDFList\n\n
    with(final RDFNode value)\n
    '''
def get():
    '''returns RDFNode\n\n
    get(final int i)\n
    '''
def replace():
    '''returns RDFNode\n\n
    replace(final int i, final RDFNode value)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final RDFNode value)\n
    '''
def indexOf():
    '''returns int\n\n
    indexOf(final RDFNode value)\n
    indexOf(final RDFNode value, final int start)\n
    '''
def append():
    '''returns RDFList\n\n
    append(final Iterator<? extends RDFNode> nodes)\n
    append(final RDFList list)\n
    '''
def concatenate():
    '''returns None\n\n
    concatenate(final RDFList list)\n
    concatenate(final Iterator<? extends RDFNode> nodes)\n
    '''
def copy():
    '''returns RDFList\n\n
    copy()\n
    '''
def apply():
    '''returns None\n\n
    apply(final ApplyFn fn)\n
    '''
def reduce():
    '''returns Object\n\n
    reduce(final ReduceFn fn, final Object initial)\n
    '''
def removeHead():
    '''returns RDFList\n\n
    removeHead()\n
    '''
def remove():
    '''returns None\n\n
    remove(final RDFNode val)\n
    remove()\n
    '''
def removeAll():
    '''returns None\n\n
    removeAll()\n
    '''
def removeList():
    '''returns None\n\n
    removeList()\n
    '''
def collectStatements():
    '''returns Set<Statement>\n\n
    collectStatements()\n
    '''
def iterator():
    '''returns ExtendedIterator<RDFNode>\n\n
    iterator()\n
    '''
def asJavaList():
    '''returns List<RDFNode>\n\n
    asJavaList()\n
    '''
def sameListAs():
    '''returns boolean\n\n
    sameListAs(final RDFList list)\n
    '''
def getStrict():
    '''returns boolean\n\n
    getStrict()\n
    '''
def setStrict():
    '''returns None\n\n
    setStrict(final boolean strict)\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid()\n
    '''
def getValidityErrorMessage():
    '''returns String\n\n
    getValidityErrorMessage()\n
    '''
def newListCell():
    '''returns Resource\n\n
    newListCell(final RDFNode value, final Resource tail)\n
    '''
def wrap():
    '''returns EnhNode\n\n
    wrap(final Node n, final EnhGraph eg)\n
    '''
def canWrap():
    '''returns boolean\n\n
    canWrap(final Node node, final EnhGraph eg)\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns RDFNode\n\n
    next()\n
    '''
