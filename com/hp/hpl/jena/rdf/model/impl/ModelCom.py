def ():
    '''returns ModelCom\n\n
    (final Graph base)\n
    (final Graph base, final Personality<RDFNode> personality)\n
    '''
def map1():
    '''returns Statement\n\n
    map1(final Statement s)\n
    map1(final Triple t)\n
    '''
def queryHandler():
    '''returns QueryHandler\n\n
    queryHandler()\n
    '''
def getGraph():
    '''returns Graph\n\n
    getGraph()\n
    '''
def asRDFNode():
    '''returns RDFNode\n\n
    asRDFNode(final Node n)\n
    '''
def wrapAsResource():
    '''returns Resource\n\n
    wrapAsResource(final Node n)\n
    '''
def getResource():
    '''returns Resource\n\n
    getResource(final String uri, final ResourceF f)\n
    getResource(final String uri)\n
    '''
def addLiteral():
    '''returns Model\n\n
    addLiteral(final Resource s, final Property p, final boolean o)\n
    addLiteral(final Resource s, final Property p, final long o)\n
    addLiteral(final Resource s, final Property p, final int o)\n
    addLiteral(final Resource s, final Property p, final char o)\n
    addLiteral(final Resource s, final Property p, final float o)\n
    addLiteral(final Resource s, final Property p, final double o)\n
    addLiteral(final Resource s, final Property p, final Object o)\n
    addLiteral(final Resource s, final Property p, final Literal o)\n
    '''
def add():
    '''returns Model\n\n
    add(final Resource s, final Property p, final String o)\n
    add(final Resource s, final Property p, final String o, final boolean wellFormed)\n
    add(final Resource s, final Property p, final String o, final String lang, final boolean wellFormed)\n
    add(final Resource s, final Property p, final String lex, final RDFDatatype datatype)\n
    add(final Resource s, final Property p, final String o, final String l)\n
    add(final StmtIterator iter)\n
    add(final Model m)\n
    add(final Model m, final boolean suppressReifications)\n
    add(final Statement s)\n
    add(final Statement[] statements)\n
    add(final List<Statement> statements)\n
    add(final Resource s, final Property p, final RDFNode o)\n
    '''
def getReader():
    '''returns RDFReader\n\n
    getReader()\n
    getReader(final String lang)\n
    '''
def setReaderClassName():
    '''returns String\n\n
    setReaderClassName(final String lang, final String className)\n
    '''
def read():
    '''returns Model\n\n
    read(final String url)\n
    read(final Reader reader, final String base)\n
    read(final InputStream reader, final String base)\n
    read(final String url, final String lang)\n
    read(final String url, final String base, final String lang)\n
    read(final Reader reader, final String base, final String lang)\n
    read(final InputStream reader, final String base, final String lang)\n
    '''
def getWriter():
    '''returns RDFWriter\n\n
    getWriter()\n
    getWriter(final String lang)\n
    '''
def setWriterClassName():
    '''returns String\n\n
    setWriterClassName(final String lang, final String className)\n
    '''
def write():
    '''returns Model\n\n
    write(final Writer writer)\n
    write(final Writer writer, final String lang)\n
    write(final Writer writer, final String lang, final String base)\n
    write(final OutputStream writer)\n
    write(final OutputStream writer, final String lang)\n
    write(final OutputStream writer, final String lang, final String base)\n
    '''
def remove():
    '''returns Model\n\n
    remove(final Statement s)\n
    remove(final Resource s, final Property p, final RDFNode o)\n
    remove(final StmtIterator iter)\n
    remove(final Model m)\n
    remove(final Model m, final boolean suppressReifications)\n
    remove(final Statement[] statements)\n
    remove(final List<Statement> statements)\n
    '''
def removeAll():
    '''returns Model\n\n
    removeAll()\n
    removeAll(final Resource s, final Property p, final RDFNode o)\n
    '''
def containsLiteral():
    '''returns boolean\n\n
    containsLiteral(final Resource s, final Property p, final boolean o)\n
    containsLiteral(final Resource s, final Property p, final long o)\n
    containsLiteral(final Resource s, final Property p, final int o)\n
    containsLiteral(final Resource s, final Property p, final char o)\n
    containsLiteral(final Resource s, final Property p, final float o)\n
    containsLiteral(final Resource s, final Property p, final double o)\n
    containsLiteral(final Resource s, final Property p, final Object o)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final Resource s, final Property p, final String o)\n
    contains(final Resource s, final Property p, final String o, final String l)\n
    contains(final Statement s)\n
    contains(final Resource s, final Property p)\n
    contains(final Resource s, final Property p, final RDFNode o)\n
    '''
def containsAny():
    '''returns boolean\n\n
    containsAny(final Model model)\n
    containsAny(final StmtIterator iter)\n
    '''
def containsAll():
    '''returns boolean\n\n
    containsAll(final Model model)\n
    containsAll(final StmtIterator iter)\n
    '''
def listStatements():
    '''returns StmtIterator\n\n
    listStatements(final Resource S, final Property P, final RDFNode O)\n
    listStatements(final Resource S, final Property P, final String O)\n
    listStatements(final Resource S, final Property P, final String O, final String L)\n
    listStatements()\n
    listStatements(final Selector selector)\n
    '''
def listLiteralStatements():
    '''returns StmtIterator\n\n
    listLiteralStatements(final Resource S, final Property P, final boolean O)\n
    listLiteralStatements(final Resource S, final Property P, final long O)\n
    listLiteralStatements(final Resource S, final Property P, final char O)\n
    listLiteralStatements(final Resource S, final Property P, final float O)\n
    listLiteralStatements(final Resource S, final Property P, final double O)\n
    '''
def listResourcesWithProperty():
    '''returns ResIterator\n\n
    listResourcesWithProperty(final Property p, final boolean o)\n
    listResourcesWithProperty(final Property p, final char o)\n
    listResourcesWithProperty(final Property p, final long o)\n
    listResourcesWithProperty(final Property p, final float o)\n
    listResourcesWithProperty(final Property p, final double o)\n
    listResourcesWithProperty(final Property p, final Object o)\n
    listResourcesWithProperty(final Property p)\n
    listResourcesWithProperty(final Property p, final RDFNode o)\n
    '''
def listSubjectsWithProperty():
    '''returns ResIterator\n\n
    listSubjectsWithProperty(final Property p, final RDFNode o)\n
    listSubjectsWithProperty(final Property p, final String o)\n
    listSubjectsWithProperty(final Property p, final String o, final String l)\n
    listSubjectsWithProperty(final Property p)\n
    '''
def createResource():
    '''returns Resource\n\n
    createResource(final Resource type)\n
    createResource(final String uri, final Resource type)\n
    createResource(final ResourceF f)\n
    createResource(final AnonId id)\n
    createResource(final String uri, final ResourceF f)\n
    createResource()\n
    createResource(final String uri)\n
    '''
def createTypedLiteral():
    '''returns Literal\n\n
    createTypedLiteral(final boolean v)\n
    createTypedLiteral(final int v)\n
    createTypedLiteral(final long v)\n
    createTypedLiteral(final char v)\n
    createTypedLiteral(final float v)\n
    createTypedLiteral(final double v)\n
    createTypedLiteral(final String v)\n
    createTypedLiteral(final Calendar cal)\n
    createTypedLiteral(final String lex, final RDFDatatype dtype)\n
    createTypedLiteral(final Object value, final RDFDatatype dtype)\n
    createTypedLiteral(final String lex, final String typeURI)\n
    createTypedLiteral(final Object value, final String typeURI)\n
    createTypedLiteral(final Object value)\n
    '''
def createLiteral():
    '''returns Literal\n\n
    createLiteral(final String v)\n
    createLiteral(final String v, final String l)\n
    createLiteral(final String v, final boolean wellFormed)\n
    createLiteral(final String v, final String l, final boolean wellFormed)\n
    '''
def createLiteralStatement():
    '''returns Statement\n\n
    createLiteralStatement(final Resource r, final Property p, final boolean o)\n
    createLiteralStatement(final Resource r, final Property p, final long o)\n
    createLiteralStatement(final Resource r, final Property p, final int o)\n
    createLiteralStatement(final Resource r, final Property p, final char o)\n
    createLiteralStatement(final Resource r, final Property p, final float o)\n
    createLiteralStatement(final Resource r, final Property p, final double o)\n
    createLiteralStatement(final Resource r, final Property p, final Object o)\n
    '''
def createStatement():
    '''returns Statement\n\n
    createStatement(final Resource r, final Property p, final String o)\n
    createStatement(final Resource r, final Property p, final String o, final boolean wellFormed)\n
    createStatement(final Resource r, final Property p, final String o, final String l)\n
    createStatement(final Resource r, final Property p, final String o, final String l, final boolean wellFormed)\n
    createStatement(final Resource r, final Property p, final RDFNode o)\n
    '''
def createBag():
    '''returns Bag\n\n
    createBag()\n
    createBag(final String uri)\n
    '''
def createAlt():
    '''returns Alt\n\n
    createAlt()\n
    createAlt(final String uri)\n
    '''
def createSeq():
    '''returns Seq\n\n
    createSeq()\n
    createSeq(final String uri)\n
    '''
def createList():
    '''returns RDFList\n\n
    createList()\n
    createList(final Iterator<? extends RDFNode> members)\n
    createList(final RDFNode[] members)\n
    '''
def getRDFNode():
    '''returns RDFNode\n\n
    getRDFNode(final Node n)\n
    '''
def getProperty():
    '''returns Statement\n\n
    getProperty(final String uri)\n
    getProperty(final String nameSpace, final String localName)\n
    getProperty(final Resource s, final Property p)\n
    '''
def getSeq():
    '''returns Seq\n\n
    getSeq(final String uri)\n
    getSeq(final Resource r)\n
    '''
def getBag():
    '''returns Bag\n\n
    getBag(final String uri)\n
    getBag(final Resource r)\n
    '''
def getAlt():
    '''returns Alt\n\n
    getAlt(final String uri)\n
    getAlt(final Resource r)\n
    '''
def size():
    '''returns long\n\n
    size()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def listNameSpaces():
    '''returns NsIterator\n\n
    listNameSpaces()\n
    '''
def samePrefixMappingAs():
    '''returns boolean\n\n
    samePrefixMappingAs(final PrefixMapping other)\n
    '''
def lock():
    '''returns PrefixMapping\n\n
    lock()\n
    '''
def setNsPrefix():
    '''returns PrefixMapping\n\n
    setNsPrefix(final String prefix, final String uri)\n
    '''
def removeNsPrefix():
    '''returns PrefixMapping\n\n
    removeNsPrefix(final String prefix)\n
    '''
def setNsPrefixes():
    '''returns PrefixMapping\n\n
    setNsPrefixes(final PrefixMapping pm)\n
    setNsPrefixes(final Map<String, String> map)\n
    '''
def withDefaultMappings():
    '''returns PrefixMapping\n\n
    withDefaultMappings(final PrefixMapping other)\n
    '''
def getNsPrefixURI():
    '''returns String\n\n
    getNsPrefixURI(final String prefix)\n
    '''
def getNsURIPrefix():
    '''returns String\n\n
    getNsURIPrefix(final String uri)\n
    '''
def expandPrefix():
    '''returns String\n\n
    expandPrefix(final String prefixed)\n
    '''
def qnameFor():
    '''returns String\n\n
    qnameFor(final String uri)\n
    '''
def shortForm():
    '''returns String\n\n
    shortForm(final String uri)\n
    '''
def getReificationStyle():
    '''returns ReificationStyle\n\n
    getReificationStyle()\n
    '''
def listReifiedStatements():
    '''returns RSIterator\n\n
    listReifiedStatements()\n
    listReifiedStatements(final Statement st)\n
    '''
def isReified():
    '''returns boolean\n\n
    isReified(final Statement s)\n
    '''
def getAnyReifiedStatement():
    '''returns Resource\n\n
    getAnyReifiedStatement(final Statement s)\n
    '''
def removeAllReifications():
    '''returns None\n\n
    removeAllReifications(final Statement s)\n
    '''
def removeReification():
    '''returns None\n\n
    removeReification(final ReifiedStatement rs)\n
    '''
def createReifiedStatement():
    '''returns ReifiedStatement\n\n
    createReifiedStatement(final Statement s)\n
    createReifiedStatement(final String uri, final Statement s)\n
    '''
def containsResource():
    '''returns boolean\n\n
    containsResource(final RDFNode r)\n
    '''
def getRequiredProperty():
    '''returns Statement\n\n
    getRequiredProperty(final Resource s, final Property p)\n
    '''
def listSubjects():
    '''returns ResIterator\n\n
    listSubjects()\n
    '''
def listObjects():
    '''returns NodeIterator\n\n
    listObjects()\n
    '''
def listObjectsOfProperty():
    '''returns NodeIterator\n\n
    listObjectsOfProperty(final Property p)\n
    listObjectsOfProperty(final Resource s, final Property p)\n
    '''
def asFilter():
    '''returns Filter<Statement>\n\n
    asFilter(final Selector s)\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final Statement x)\n
    '''
def findTriplesFrom():
    '''returns ExtendedIterator<Triple>\n\n
    findTriplesFrom(final Selector s)\n
    '''
def supportsTransactions():
    '''returns boolean\n\n
    supportsTransactions()\n
    '''
def begin():
    '''returns Model\n\n
    begin()\n
    '''
def abort():
    '''returns Model\n\n
    abort()\n
    '''
def commit():
    '''returns Model\n\n
    commit()\n
    '''
def executeInTransaction():
    '''returns Object\n\n
    executeInTransaction(final Command cmd)\n
    '''
def independent():
    '''returns boolean\n\n
    independent()\n
    '''
def createProperty():
    '''returns Property\n\n
    createProperty(final String uri)\n
    createProperty(final String nameSpace, final String localName)\n
    '''
def asStatement():
    '''returns Statement\n\n
    asStatement(final Triple t)\n
    '''
def asStatements():
    '''returns StmtIterator\n\n
    asStatements(final Triple[] triples)\n
    asStatements(final List<Triple> triples)\n
    asStatements(final Iterator<Triple> it)\n
    '''
def asModel():
    '''returns Model\n\n
    asModel(final Graph g)\n
    '''
def listBySubject():
    '''returns StmtIterator\n\n
    listBySubject(final Container cont)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
def supportsSetOperations():
    '''returns boolean\n\n
    supportsSetOperations()\n
    '''
def query():
    '''returns Model\n\n
    query(final Selector selector)\n
    '''
def union():
    '''returns Model\n\n
    union(final Model model)\n
    '''
def intersection():
    '''returns Model\n\n
    intersection(final Model other)\n
    '''
def difference():
    '''returns Model\n\n
    difference(final Model model)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def reifiedToString():
    '''returns String\n\n
    reifiedToString()\n
    '''
def getHiddenStatements():
    '''returns Model\n\n
    getHiddenStatements()\n
    '''
def isIsomorphicWith():
    '''returns boolean\n\n
    isIsomorphicWith(final Model m)\n
    '''
def enterCriticalSection():
    '''returns None\n\n
    enterCriticalSection(final boolean requestReadLock)\n
    '''
def leaveCriticalSection():
    '''returns None\n\n
    leaveCriticalSection()\n
    '''
def register():
    '''returns Model\n\n
    register(final ModelChangedListener listener)\n
    '''
def unregister():
    '''returns Model\n\n
    unregister(final ModelChangedListener listener)\n
    '''
def adapt():
    '''returns GraphListener\n\n
    adapt(final ModelChangedListener L)\n
    '''
def notifyEvent():
    '''returns Model\n\n
    notifyEvent(final Object e)\n
    '''
