def ():
    '''returns OntModelImpl\n\n
    (final OntModelSpec spec, final Model model)\n
    (final OntModelSpec spec)\n
    '''
def getDocumentManager():
    '''returns OntDocumentManager\n\n
    getDocumentManager()\n
    '''
def listOntologies():
    '''returns ExtendedIterator<Ontology>\n\n
    listOntologies()\n
    '''
def listOntProperties():
    '''returns ExtendedIterator<OntProperty>\n\n
    listOntProperties()\n
    '''
def listAllOntProperties():
    '''returns ExtendedIterator<OntProperty>\n\n
    listAllOntProperties()\n
    '''
def listObjectProperties():
    '''returns ExtendedIterator<ObjectProperty>\n\n
    listObjectProperties()\n
    '''
def listDatatypeProperties():
    '''returns ExtendedIterator<DatatypeProperty>\n\n
    listDatatypeProperties()\n
    '''
def listFunctionalProperties():
    '''returns ExtendedIterator<FunctionalProperty>\n\n
    listFunctionalProperties()\n
    '''
def listTransitiveProperties():
    '''returns ExtendedIterator<TransitiveProperty>\n\n
    listTransitiveProperties()\n
    '''
def listSymmetricProperties():
    '''returns ExtendedIterator<SymmetricProperty>\n\n
    listSymmetricProperties()\n
    '''
def listInverseFunctionalProperties():
    '''returns ExtendedIterator<InverseFunctionalProperty>\n\n
    listInverseFunctionalProperties()\n
    '''
def listIndividuals():
    '''returns ExtendedIterator<Individual>\n\n
    listIndividuals()\n
    listIndividuals(final Resource cls)\n
    '''
def listClasses():
    '''returns ExtendedIterator<OntClass>\n\n
    listClasses()\n
    '''
def listHierarchyRootClasses():
    '''returns ExtendedIterator<OntClass>\n\n
    listHierarchyRootClasses()\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final OntClass o)\n
    accept(final OntClass o)\n
    accept(final OntClass x)\n
    accept(final Node x)\n
    accept(final T x)\n
    '''
def listEnumeratedClasses():
    '''returns ExtendedIterator<EnumeratedClass>\n\n
    listEnumeratedClasses()\n
    '''
def listUnionClasses():
    '''returns ExtendedIterator<UnionClass>\n\n
    listUnionClasses()\n
    '''
def listComplementClasses():
    '''returns ExtendedIterator<ComplementClass>\n\n
    listComplementClasses()\n
    '''
def listIntersectionClasses():
    '''returns ExtendedIterator<IntersectionClass>\n\n
    listIntersectionClasses()\n
    '''
def listNamedClasses():
    '''returns ExtendedIterator<OntClass>\n\n
    listNamedClasses()\n
    '''
def listRestrictions():
    '''returns ExtendedIterator<Restriction>\n\n
    listRestrictions()\n
    '''
def listAllDifferent():
    '''returns ExtendedIterator<AllDifferent>\n\n
    listAllDifferent()\n
    '''
def listDataRanges():
    '''returns ExtendedIterator<DataRange>\n\n
    listDataRanges()\n
    '''
def listAnnotationProperties():
    '''returns ExtendedIterator<AnnotationProperty>\n\n
    listAnnotationProperties()\n
    '''
def getOntology():
    '''returns Ontology\n\n
    getOntology(final String uri)\n
    '''
def getIndividual():
    '''returns Individual\n\n
    getIndividual(final String uri)\n
    '''
def getOntProperty():
    '''returns OntProperty\n\n
    getOntProperty(final String uri)\n
    '''
def getObjectProperty():
    '''returns ObjectProperty\n\n
    getObjectProperty(final String uri)\n
    '''
def getTransitiveProperty():
    '''returns TransitiveProperty\n\n
    getTransitiveProperty(final String uri)\n
    '''
def getSymmetricProperty():
    '''returns SymmetricProperty\n\n
    getSymmetricProperty(final String uri)\n
    '''
def getInverseFunctionalProperty():
    '''returns InverseFunctionalProperty\n\n
    getInverseFunctionalProperty(final String uri)\n
    '''
def getDatatypeProperty():
    '''returns DatatypeProperty\n\n
    getDatatypeProperty(final String uri)\n
    '''
def getAnnotationProperty():
    '''returns AnnotationProperty\n\n
    getAnnotationProperty(final String uri)\n
    '''
def getOntClass():
    '''returns OntClass\n\n
    getOntClass(final String uri)\n
    '''
def getComplementClass():
    '''returns ComplementClass\n\n
    getComplementClass(final String uri)\n
    '''
def getEnumeratedClass():
    '''returns EnumeratedClass\n\n
    getEnumeratedClass(final String uri)\n
    '''
def getUnionClass():
    '''returns UnionClass\n\n
    getUnionClass(final String uri)\n
    '''
def getIntersectionClass():
    '''returns IntersectionClass\n\n
    getIntersectionClass(final String uri)\n
    '''
def getRestriction():
    '''returns Restriction\n\n
    getRestriction(final String uri)\n
    '''
def getHasValueRestriction():
    '''returns HasValueRestriction\n\n
    getHasValueRestriction(final String uri)\n
    '''
def getSomeValuesFromRestriction():
    '''returns SomeValuesFromRestriction\n\n
    getSomeValuesFromRestriction(final String uri)\n
    '''
def getAllValuesFromRestriction():
    '''returns AllValuesFromRestriction\n\n
    getAllValuesFromRestriction(final String uri)\n
    '''
def getCardinalityRestriction():
    '''returns CardinalityRestriction\n\n
    getCardinalityRestriction(final String uri)\n
    '''
def getMinCardinalityRestriction():
    '''returns MinCardinalityRestriction\n\n
    getMinCardinalityRestriction(final String uri)\n
    '''
def getMaxCardinalityRestriction():
    '''returns MaxCardinalityRestriction\n\n
    getMaxCardinalityRestriction(final String uri)\n
    '''
def getQualifiedRestriction():
    '''returns QualifiedRestriction\n\n
    getQualifiedRestriction(final String uri)\n
    '''
def getCardinalityQRestriction():
    '''returns CardinalityQRestriction\n\n
    getCardinalityQRestriction(final String uri)\n
    '''
def getMinCardinalityQRestriction():
    '''returns MinCardinalityQRestriction\n\n
    getMinCardinalityQRestriction(final String uri)\n
    '''
def getMaxCardinalityQRestriction():
    '''returns MaxCardinalityQRestriction\n\n
    getMaxCardinalityQRestriction(final String uri)\n
    '''
def createOntology():
    '''returns Ontology\n\n
    createOntology(final String uri)\n
    '''
def createIndividual():
    '''returns Individual\n\n
    createIndividual(final Resource cls)\n
    createIndividual(final String uri, final Resource cls)\n
    '''
def createOntProperty():
    '''returns OntProperty\n\n
    createOntProperty(final String uri)\n
    '''
def createObjectProperty():
    '''returns ObjectProperty\n\n
    createObjectProperty(final String uri)\n
    createObjectProperty(final String uri, final boolean functional)\n
    '''
def createTransitiveProperty():
    '''returns TransitiveProperty\n\n
    createTransitiveProperty(final String uri)\n
    createTransitiveProperty(final String uri, final boolean functional)\n
    '''
def createSymmetricProperty():
    '''returns SymmetricProperty\n\n
    createSymmetricProperty(final String uri)\n
    createSymmetricProperty(final String uri, final boolean functional)\n
    '''
def createInverseFunctionalProperty():
    '''returns InverseFunctionalProperty\n\n
    createInverseFunctionalProperty(final String uri)\n
    createInverseFunctionalProperty(final String uri, final boolean functional)\n
    '''
def createDatatypeProperty():
    '''returns DatatypeProperty\n\n
    createDatatypeProperty(final String uri)\n
    createDatatypeProperty(final String uri, final boolean functional)\n
    '''
def createAnnotationProperty():
    '''returns AnnotationProperty\n\n
    createAnnotationProperty(final String uri)\n
    '''
def createClass():
    '''returns OntClass\n\n
    createClass()\n
    createClass(final String uri)\n
    '''
def createComplementClass():
    '''returns ComplementClass\n\n
    createComplementClass(final String uri, final Resource cls)\n
    '''
def createEnumeratedClass():
    '''returns EnumeratedClass\n\n
    createEnumeratedClass(final String uri, final RDFList members)\n
    '''
def createUnionClass():
    '''returns UnionClass\n\n
    createUnionClass(final String uri, final RDFList members)\n
    '''
def createIntersectionClass():
    '''returns IntersectionClass\n\n
    createIntersectionClass(final String uri, final RDFList members)\n
    '''
def createRestriction():
    '''returns Restriction\n\n
    createRestriction(final Property p)\n
    createRestriction(final String uri, final Property p)\n
    '''
def createHasValueRestriction():
    '''returns HasValueRestriction\n\n
    createHasValueRestriction(final String uri, final Property prop, final RDFNode value)\n
    '''
def createSomeValuesFromRestriction():
    '''returns SomeValuesFromRestriction\n\n
    createSomeValuesFromRestriction(final String uri, final Property prop, final Resource cls)\n
    '''
def createAllValuesFromRestriction():
    '''returns AllValuesFromRestriction\n\n
    createAllValuesFromRestriction(final String uri, final Property prop, final Resource cls)\n
    '''
def createCardinalityRestriction():
    '''returns CardinalityRestriction\n\n
    createCardinalityRestriction(final String uri, final Property prop, final int cardinality)\n
    '''
def createMinCardinalityRestriction():
    '''returns MinCardinalityRestriction\n\n
    createMinCardinalityRestriction(final String uri, final Property prop, final int cardinality)\n
    '''
def createMaxCardinalityRestriction():
    '''returns MaxCardinalityRestriction\n\n
    createMaxCardinalityRestriction(final String uri, final Property prop, final int cardinality)\n
    '''
def createMaxCardinalityQRestriction():
    '''returns MaxCardinalityQRestriction\n\n
    createMaxCardinalityQRestriction(final String uri, final Property prop, final int cardinality, final OntClass cls)\n
    '''
def createMinCardinalityQRestriction():
    '''returns MinCardinalityQRestriction\n\n
    createMinCardinalityQRestriction(final String uri, final Property prop, final int cardinality, final OntClass cls)\n
    '''
def createCardinalityQRestriction():
    '''returns CardinalityQRestriction\n\n
    createCardinalityQRestriction(final String uri, final Property prop, final int cardinality, final OntClass cls)\n
    '''
def createDataRange():
    '''returns DataRange\n\n
    createDataRange(final RDFList literals)\n
    '''
def createAllDifferent():
    '''returns AllDifferent\n\n
    createAllDifferent()\n
    createAllDifferent(final RDFList differentMembers)\n
    '''
def createOntResource():
    '''returns OntResource\n\n
    createOntResource(final String uri)\n
    '''
def createList():
    '''returns RDFList\n\n
    createList()\n
    '''
def getProfile():
    '''returns Profile\n\n
    getProfile()\n
    '''
def loadImports():
    '''returns None\n\n
    loadImports()\n
    '''
def hasLoadedImport():
    '''returns boolean\n\n
    hasLoadedImport(final String uri)\n
    '''
def addLoadedImport():
    '''returns None\n\n
    addLoadedImport(final String uri)\n
    '''
def removeLoadedImport():
    '''returns None\n\n
    removeLoadedImport(final String uri)\n
    '''
def listImportedOntologyURIs():
    '''returns Set<String>\n\n
    listImportedOntologyURIs()\n
    listImportedOntologyURIs(final boolean closure)\n
    '''
def getImportModelMaker():
    '''returns ModelMaker\n\n
    getImportModelMaker()\n
    '''
def getModelMaker():
    '''returns ModelMaker\n\n
    getModelMaker()\n
    '''
def read():
    '''returns Model\n\n
    read(final String uri)\n
    read(final Reader reader, final String base)\n
    read(final InputStream reader, final String base)\n
    read(final String uri, final String syntax)\n
    read(final String uri, final String base, final String syntax)\n
    read(final Reader reader, final String base, final String syntax)\n
    read(final InputStream reader, final String base, final String syntax)\n
    '''
def getSubGraphs():
    '''returns List<Graph>\n\n
    getSubGraphs()\n
    '''
def listImportedModels():
    '''returns ExtendedIterator<OntModel>\n\n
    listImportedModels()\n
    '''
def listSubModels():
    '''returns ExtendedIterator<OntModel>\n\n
    listSubModels(final boolean withImports)\n
    listSubModels()\n
    '''
def map1():
    '''returns Node\n\n
    map1(final Graph o)\n
    map1(final Triple x)\n
    map1(final Node x)\n
    map1(final Domain x)\n
    '''
def countSubModels():
    '''returns int\n\n
    countSubModels()\n
    '''
def getImportedModel():
    '''returns OntModel\n\n
    getImportedModel(final String uri)\n
    '''
def getBaseGraph():
    '''returns Graph\n\n
    getBaseGraph()\n
    '''
def getBaseModel():
    '''returns Model\n\n
    getBaseModel()\n
    '''
def addSubModel():
    '''returns None\n\n
    addSubModel(final Model model)\n
    addSubModel(final Model model, final boolean rebind)\n
    '''
def removeSubModel():
    '''returns None\n\n
    removeSubModel(final Model model)\n
    removeSubModel(final Model model, final boolean rebind)\n
    '''
def isInBaseModel():
    '''returns boolean\n\n
    isInBaseModel(final RDFNode node)\n
    isInBaseModel(final Statement stmt)\n
    '''
def strictMode():
    '''returns boolean\n\n
    strictMode()\n
    '''
def setStrictMode():
    '''returns None\n\n
    setStrictMode(final boolean strict)\n
    '''
def setDynamicImports():
    '''returns None\n\n
    setDynamicImports(final boolean dynamic)\n
    '''
def getDynamicImports():
    '''returns boolean\n\n
    getDynamicImports()\n
    '''
def getSpecification():
    '''returns OntModelSpec\n\n
    getSpecification()\n
    '''
def write():
    '''returns Model\n\n
    write(final Writer writer)\n
    write(final Writer writer, final String lang)\n
    write(final Writer writer, final String lang, final String base)\n
    write(final OutputStream out)\n
    write(final OutputStream out, final String lang)\n
    write(final OutputStream out, final String lang, final String base)\n
    '''
def writeAll():
    '''returns Model\n\n
    writeAll(final Writer writer, final String lang, final String base)\n
    writeAll(final OutputStream out, final String lang, final String base)\n
    '''
def getRawModel():
    '''returns Model\n\n
    getRawModel()\n
    '''
def getReasoner():
    '''returns Reasoner\n\n
    getReasoner()\n
    '''
def rebind():
    '''returns None\n\n
    rebind()\n
    '''
def prepare():
    '''returns None\n\n
    prepare()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def getDeductionsModel():
    '''returns Model\n\n
    getDeductionsModel()\n
    '''
def validate():
    '''returns ValidityReport\n\n
    validate()\n
    '''
def listStatements():
    '''returns StmtIterator\n\n
    listStatements(final Resource subject, final Property predicate, final RDFNode object, final Model posit)\n
    '''
def setDerivationLogging():
    '''returns None\n\n
    setDerivationLogging(final boolean logOn)\n
    '''
def getDerivation():
    '''returns Iterator<Derivation>\n\n
    getDerivation(final Statement statement)\n
    '''
def getOntResource():
    '''returns OntResource\n\n
    getOntResource(final String uri)\n
    getOntResource(final Resource res)\n
    '''
def reduce():
    '''returns Object\n\n
    reduce(final RDFNode node, final Object accumulator)\n
    '''
def addedStatement():
    '''returns None\n\n
    addedStatement(final Statement added)\n
    '''
def removedStatement():
    '''returns None\n\n
    removedStatement(final Statement removed)\n
    '''
