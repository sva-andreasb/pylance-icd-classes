COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloDomEcoreBuilderImpl\n\n
    ()\n
    '''
def initStandalone():
    '''returns None\n\n
    initStandalone()\n
    '''
def setReuseMode():
    '''returns None\n\n
    setReuseMode(final boolean reuse)\n
    '''
def getReuseMode():
    '''returns boolean\n\n
    getReuseMode()\n
    '''
def createEcoreResource():
    '''returns Resource\n\n
    createEcoreResource(final File ecoreFile)\n
    '''
def getEcoreResource():
    '''returns Resource\n\n
    getEcoreResource()\n
    '''
def createPackage():
    '''returns EPackage\n\n
    createPackage(final String modelName, final String modelid, final String collectorName, final String rootPackage)\n
    '''
def implementInterfaces():
    '''returns None\n\n
    implementInterfaces(final EClass cls, final String[] externalInterfaces)\n
    '''
def setAbstract():
    '''returns None\n\n
    setAbstract(final EClass cls, final boolean isAbstract)\n
    '''
def setConfigurationClass():
    '''returns None\n\n
    setConfigurationClass(final String className)\n
    '''
def getPackage():
    '''returns EPackage\n\n
    getPackage()\n
    '''
def getCollector():
    '''returns EClass\n\n
    getCollector()\n
    '''
def setDocumentation():
    '''returns None\n\n
    setDocumentation(final EModelElement obj, final String documentation)\n
    '''
def setDisplayName():
    '''returns None\n\n
    setDisplayName(final EModelElement obj, final String name)\n
    '''
def caseBooleanDataType():
    '''returns Object\n\n
    caseBooleanDataType(final BooleanDataType type)\n
    caseBooleanDataType(final BooleanDataType type)\n
    '''
def caseIntegerDataType():
    '''returns Object\n\n
    caseIntegerDataType(final IntegerDataType type)\n
    caseIntegerDataType(final IntegerDataType type)\n
    '''
def caseNumericalDataType():
    '''returns Object\n\n
    caseNumericalDataType(final NumericalDataType type)\n
    caseNumericalDataType(final NumericalDataType type)\n
    '''
def caseCharacterStringDataType():
    '''returns Object\n\n
    caseCharacterStringDataType(final CharacterStringDataType type)\n
    caseCharacterStringDataType(final CharacterStringDataType type)\n
    '''
def caseDateDataType():
    '''returns Object\n\n
    caseDateDataType(final DateDataType type)\n
    caseDateDataType(final DateDataType type)\n
    '''
def caseTimeDataType():
    '''returns Object\n\n
    caseTimeDataType(final TimeDataType type)\n
    caseTimeDataType(final TimeDataType type)\n
    '''
def createEntity():
    '''returns EClass\n\n
    createEntity(final String name, final PersistentTable table)\n
    '''
def setDefaultEntity():
    '''returns None\n\n
    setDefaultEntity(final EClass entity, final EClass defaultEntity)\n
    '''
def addOperation():
    '''returns EOperation\n\n
    addOperation(final EClass eclass, final String name, final EClassifier[] parameterType, final String[] parameterNames, final EClassifier returnType, final boolean isMany, final String body)\n
    addOperation(final EClass eclass, final String name, final String body)\n
    addOperation(final EClass eclass, final String name, final EClassifier returnType, final boolean isMany, final String body)\n
    addOperation(final EClass eclass, final String name, final EClassifier parameterType, final String parameterName, final String body)\n
    '''
def updateCollector():
    '''returns None\n\n
    updateCollector(final EClass eclass, final PersistentTable table, final String collectionName)\n
    updateCollector(final EClass eclass, final PersistentTable table, final String collectionName, final String entityName)\n
    updateCollector(final EClass eclass, final PersistentTable table, final String collectionName, final List<EClass> concreteEntities, final List<String> concreteCollectionNames)\n
    updateCollector(final EClass eclass, final PersistentTable table, final String collectionName, final List<EClass> concreteEntities, final List<String> concreteCollectionNames, final String entityName)\n
    '''
def updateRenamedCollector():
    '''returns None\n\n
    updateRenamedCollector(final EClass eclass, final PersistentTable table, final String collectionName, final String entityName, final String externalInterface, final String originalCollectionName, final String originalEntityName)\n
    '''
def createAttribute():
    '''returns EAttribute\n\n
    createAttribute(final EClass eclass, final String name, final Column col, final String javaType)\n
    '''
def createReference():
    '''returns EReference\n\n
    createReference(final EClass sourceClass, final String name, final EClass targetClass, final ForeignKey fk)\n
    '''
def createInvertedReference():
    '''returns EReference\n\n
    createInvertedReference(final EClass sourceClass, final String name, final EClass targetClass, final String otherName, final ForeignKey fk)\n
    '''
def createVirtualReference():
    '''returns EReference\n\n
    createVirtualReference(final EClass sourceClass, final String name, final EClass targetClass, final ForeignKey fk)\n
    '''
def createVirtualInvertedReference():
    '''returns EReference\n\n
    createVirtualInvertedReference(final EClass sourceClass, final String name, final EClass targetClass, final String otherName, final ForeignKey fk)\n
    '''
def createVirtualEntity():
    '''returns EClass\n\n
    createVirtualEntity(final String name, final PersistentTable table)\n
    '''
def extendsEntity():
    '''returns None\n\n
    extendsEntity(final EClass entity, final EClass superEntity)\n
    '''
def setObjectKey():
    '''returns None\n\n
    setObjectKey(final EClass entity, final List<String> features)\n
    '''
def getJavaType():
    '''returns EDataType\n\n
    getJavaType(final String javaType)\n
    '''
def getPrimitiveType():
    '''returns EDataType\n\n
    getPrimitiveType(final IloDomPrimitiveType type)\n
    '''
def createDerivedAttribute():
    '''returns List<EOperation>\n\n
    createDerivedAttribute(final EClass eclass, final String name, final EDataType eType, final boolean readonly, final String getBody, final String setBody, final String isSetBody, final String unsetBody)\n
    '''
def createNotApplicableAttribute():
    '''returns List<EOperation>\n\n
    createNotApplicableAttribute(final EClass eclass, final String name, final EDataType eType, final boolean readonly)\n
    '''
def createRenamedAttribute():
    '''returns List<EOperation>\n\n
    createRenamedAttribute(final EClass eclass, final String name, final EDataType eType, final boolean readonly, final String originalName, final EDataType originalType)\n
    '''
def createDerivedReference():
    '''returns List<EOperation>\n\n
    createDerivedReference(final EClass sourceClass, final String name, final EClass targetClass, final boolean isMany, final boolean readonly, final String getterBody, final String setterBody)\n
    '''
def createRenamedReference():
    '''returns List<EOperation>\n\n
    createRenamedReference(final EClass sourceClass, final String name, final EClass targetClass, final boolean isMany, final boolean readonly, final String originalName)\n
    '''
def createNotApplicableReference():
    '''returns List<EOperation>\n\n
    createNotApplicableReference(final EClass sourceClass, final String name, final EClass targetClass, final boolean isMany, final boolean readonly)\n
    '''
def setNotApplicable():
    '''returns None\n\n
    setNotApplicable(final EClass entity)\n
    '''
def validateEcore():
    '''returns Diagnostic\n\n
    validateEcore()\n
    '''
def saveEcore():
    '''returns None\n\n
    saveEcore()\n
    '''
def createGenModelResource():
    '''returns Resource\n\n
    createGenModelResource(final File genmodelfile)\n
    '''
def getGenModelResource():
    '''returns Resource\n\n
    getGenModelResource()\n
    '''
def createGenModel():
    '''returns GenModel\n\n
    createGenModel(final String modelDirectory)\n
    '''
def getGenModel():
    '''returns GenModel\n\n
    getGenModel()\n
    '''
def validateGenModel():
    '''returns Diagnostic\n\n
    validateGenModel()\n
    '''
def reconcileGenModel():
    '''returns None\n\n
    reconcileGenModel(final File oldGenModelFile)\n
    '''
def saveGenModel():
    '''returns None\n\n
    saveGenModel()\n
    '''
