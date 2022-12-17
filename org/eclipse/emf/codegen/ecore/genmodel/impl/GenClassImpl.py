def getProvider():
    '''returns GenProviderKind\n\n
    getProvider()\n
    '''
def isProviderSingleton():
    '''returns boolean\n\n
    isProviderSingleton()\n
    '''
def setProvider():
    '''returns None\n\n
    setProvider(final GenProviderKind newProvider)\n
    '''
def isImage():
    '''returns boolean\n\n
    isImage()\n
    '''
def setImage():
    '''returns None\n\n
    setImage(final boolean newImage)\n
    '''
def getEcoreClass():
    '''returns EClass\n\n
    getEcoreClass()\n
    '''
def basicGetEcoreClass():
    '''returns EClass\n\n
    basicGetEcoreClass()\n
    '''
def setEcoreClass():
    '''returns None\n\n
    setEcoreClass(final EClass newEcoreClass)\n
    '''
def getGenFeatures():
    '''returns EList\n\n
    getGenFeatures()\n
    '''
def getGenOperations():
    '''returns EList\n\n
    getGenOperations()\n
    '''
def getEcoreClassifier():
    '''returns EClassifier\n\n
    getEcoreClassifier()\n
    '''
def getImportedMetaType():
    '''returns String\n\n
    getImportedMetaType()\n
    '''
def getInterfaceName():
    '''returns String\n\n
    getInterfaceName()\n
    '''
def getQualifiedInterfaceName():
    '''returns String\n\n
    getQualifiedInterfaceName()\n
    '''
def getImportedInstanceClassName():
    '''returns String\n\n
    getImportedInstanceClassName()\n
    '''
def getImportedInterfaceName():
    '''returns String\n\n
    getImportedInterfaceName()\n
    '''
def getClassName():
    '''returns String\n\n
    getClassName()\n
    '''
def getQualifiedClassName():
    '''returns String\n\n
    getQualifiedClassName()\n
    '''
def getImportedClassName():
    '''returns String\n\n
    getImportedClassName()\n
    '''
def getBaseGenClasses():
    '''returns List\n\n
    getBaseGenClasses()\n
    '''
def getAllBaseGenClasses():
    '''returns List\n\n
    getAllBaseGenClasses()\n
    '''
def getSwitchGenClasses():
    '''returns List\n\n
    getSwitchGenClasses()\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final GenClass genClass)\n
    accept(final GenFeature genFeature)\n
    accept(final GenFeature genFeature)\n
    accept(final GenFeature genFeature)\n
    accept(final GenFeature genFeature)\n
    accept(final GenFeature genFeature)\n
    accept(final GenFeature genFeature)\n
    accept(final GenFeature genFeature)\n
    accept(final GenFeature genFeature)\n
    accept(final GenFeature genFeature)\n
    accept(final GenFeature genFeature)\n
    accept(final GenFeature genFeature)\n
    accept(final GenFeature genFeature)\n
    accept(final GenFeature genFeature)\n
    accept(final GenFeature genFeature)\n
    accept(final GenFeature genFeature)\n
    accept(final GenFeature genFeature)\n
    accept(GenFeature genFeature)\n
    accept(final GenFeature genFeature)\n
    accept(final GenOperation genOperation)\n
    '''
def getBaseGenClass():
    '''returns GenClass\n\n
    getBaseGenClass()\n
    '''
def getClassExtendsGenClass():
    '''returns GenClass\n\n
    getClassExtendsGenClass()\n
    '''
def getClassExtends():
    '''returns String\n\n
    getClassExtends()\n
    '''
def needsRootImplementsInterfaceOperations():
    '''returns boolean\n\n
    needsRootImplementsInterfaceOperations()\n
    '''
def getClassImplements():
    '''returns String\n\n
    getClassImplements()\n
    '''
def needsRootExtendsInterfaceExtendsTag():
    '''returns boolean\n\n
    needsRootExtendsInterfaceExtendsTag()\n
    '''
def getInterfaceExtends():
    '''returns String\n\n
    getInterfaceExtends()\n
    '''
def getAllGenFeatures():
    '''returns List\n\n
    getAllGenFeatures()\n
    '''
def getInheritedGenFeatures():
    '''returns List\n\n
    getInheritedGenFeatures()\n
    '''
def getAllGenOperations():
    '''returns List\n\n
    getAllGenOperations()\n
    '''
def getFeatureID():
    '''returns String\n\n
    getFeatureID(final GenFeature genFeature)\n
    '''
def getQualifiedFeatureID():
    '''returns String\n\n
    getQualifiedFeatureID(final GenFeature genFeature)\n
    '''
def getOperationID():
    '''returns String\n\n
    getOperationID(final GenOperation genOperation)\n
    '''
def getFeatureValue():
    '''returns String\n\n
    getFeatureValue(final GenFeature genFeature)\n
    '''
def getLocalFeatureIndex():
    '''returns String\n\n
    getLocalFeatureIndex(final GenFeature genFeature)\n
    '''
def getFlagsField():
    '''returns String\n\n
    getFlagsField(final GenFeature genFeature)\n
    '''
def getFlagIndex():
    '''returns int\n\n
    getFlagIndex(final GenFeature genFeature)\n
    '''
def getESetFlagsField():
    '''returns String\n\n
    getESetFlagsField(final GenFeature genFeature)\n
    '''
def getESetFlagIndex():
    '''returns int\n\n
    getESetFlagIndex(final GenFeature genFeature)\n
    '''
def getFeatureCountID():
    '''returns String\n\n
    getFeatureCountID()\n
    '''
def getQualifiedFeatureCountID():
    '''returns String\n\n
    getQualifiedFeatureCountID()\n
    '''
def getFeatureCountValue():
    '''returns String\n\n
    getFeatureCountValue()\n
    '''
def getFeatureCount():
    '''returns int\n\n
    getFeatureCount()\n
    '''
def isEObject():
    '''returns boolean\n\n
    isEObject()\n
    '''
def isEObjectExtension():
    '''returns boolean\n\n
    isEObjectExtension()\n
    '''
def isAbstract():
    '''returns boolean\n\n
    isAbstract()\n
    '''
def getAbstractFlag():
    '''returns String\n\n
    getAbstractFlag()\n
    '''
def isInterface():
    '''returns boolean\n\n
    isInterface()\n
    '''
def getInterfaceFlag():
    '''returns String\n\n
    getInterfaceFlag()\n
    '''
def getGeneratedInstanceClassFlag():
    '''returns String\n\n
    getGeneratedInstanceClassFlag()\n
    '''
def isExternalInterface():
    '''returns boolean\n\n
    isExternalInterface()\n
    '''
def isMapEntry():
    '''returns boolean\n\n
    isMapEntry()\n
    '''
def getMapEntryKeyFeature():
    '''returns GenFeature\n\n
    getMapEntryKeyFeature()\n
    '''
def getMapEntryValueFeature():
    '''returns GenFeature\n\n
    getMapEntryValueFeature()\n
    '''
def getImplementedGenClasses():
    '''returns List\n\n
    getImplementedGenClasses()\n
    '''
def getImplementedGenFeatures():
    '''returns List\n\n
    getImplementedGenFeatures()\n
    '''
def getImplementedGenOperations():
    '''returns List\n\n
    getImplementedGenOperations()\n
    '''
def getExtendedGenClasses():
    '''returns List\n\n
    getExtendedGenClasses()\n
    '''
def getExtendedGenFeatures():
    '''returns List\n\n
    getExtendedGenFeatures()\n
    '''
def getExtendedGenOperations():
    '''returns List\n\n
    getExtendedGenOperations()\n
    '''
def getDeclaredGenFeatures():
    '''returns List\n\n
    getDeclaredGenFeatures()\n
    '''
def getDeclaredGenOperations():
    '''returns List\n\n
    getDeclaredGenOperations()\n
    '''
def getFlagGenFeatures():
    '''returns List\n\n
    getFlagGenFeatures()\n
    getFlagGenFeatures(final String staticDefaultValue)\n
    '''
def getESetGenFeatures():
    '''returns List\n\n
    getESetGenFeatures()\n
    '''
def getEInverseAddGenFeatures():
    '''returns List\n\n
    getEInverseAddGenFeatures()\n
    '''
def getEInverseRemoveGenFeatures():
    '''returns List\n\n
    getEInverseRemoveGenFeatures()\n
    '''
def getEBasicRemoveFromContainerGenFeatures():
    '''returns List\n\n
    getEBasicRemoveFromContainerGenFeatures()\n
    '''
def getToStringGenFeatures():
    '''returns List\n\n
    getToStringGenFeatures()\n
    '''
def getMixinGenClasses():
    '''returns List\n\n
    getMixinGenClasses()\n
    '''
def getMixinGenFeatures():
    '''returns List\n\n
    getMixinGenFeatures()\n
    '''
def getMixinGenOperations():
    '''returns List\n\n
    getMixinGenOperations()\n
    '''
def initialize():
    '''returns None\n\n
    initialize(final EClass eClass)\n
    '''
def generate():
    '''returns None\n\n
    generate(final IProgressMonitor progressMonitor)\n
    '''
def getModelInfo():
    '''returns String\n\n
    getModelInfo()\n
    '''
def getProviderClassName():
    '''returns String\n\n
    getProviderClassName()\n
    '''
def getQualifiedProviderClassName():
    '''returns String\n\n
    getQualifiedProviderClassName()\n
    '''
def getImportedProviderClassName():
    '''returns String\n\n
    getImportedProviderClassName()\n
    '''
def getItemIconFileName():
    '''returns String\n\n
    getItemIconFileName()\n
    '''
def getCreateChildIconFileName():
    '''returns String\n\n
    getCreateChildIconFileName(final GenFeature feature, final GenClass childClass)\n
    '''
def getProviderBaseClassName():
    '''returns String\n\n
    getProviderBaseClassName()\n
    '''
def getProviderImplementedGenClasses():
    '''returns List\n\n
    getProviderImplementedGenClasses()\n
    '''
def getLabelFeatureCandidates():
    '''returns List\n\n
    getLabelFeatureCandidates()\n
    '''
def getPropertyFeatures():
    '''returns List\n\n
    getPropertyFeatures()\n
    '''
def getNotifyFeatures():
    '''returns List\n\n
    getNotifyFeatures()\n
    '''
def getLabelNotifyFeatures():
    '''returns List\n\n
    getLabelNotifyFeatures()\n
    '''
def getContentNotifyFeatures():
    '''returns List\n\n
    getContentNotifyFeatures()\n
    '''
def getLabelAndContentNotifyFeatures():
    '''returns List\n\n
    getLabelAndContentNotifyFeatures()\n
    '''
def getChildrenFeatures():
    '''returns List\n\n
    getChildrenFeatures()\n
    '''
def getAllChildrenFeatures():
    '''returns List\n\n
    getAllChildrenFeatures()\n
    '''
def getCreateChildFeatures():
    '''returns List\n\n
    getCreateChildFeatures()\n
    '''
def getAllCreateChildFeatures():
    '''returns List\n\n
    getAllCreateChildFeatures()\n
    '''
def getCrossPackageCreateChildFeatures():
    '''returns List\n\n
    getCrossPackageCreateChildFeatures()\n
    '''
def getSharedClassCreateChildFeatures():
    '''returns List\n\n
    getSharedClassCreateChildFeatures()\n
    '''
def hasFeatureMapCreateChildFeatures():
    '''returns boolean\n\n
    hasFeatureMapCreateChildFeatures()\n
    '''
def getChildrenClasses():
    '''returns List\n\n
    getChildrenClasses(final GenFeature genFeature)\n
    '''
def getCrossPackageChildrenClasses():
    '''returns List\n\n
    getCrossPackageChildrenClasses(final GenFeature genFeature)\n
    '''
def getLabelFeatureGen():
    '''returns GenFeature\n\n
    getLabelFeatureGen()\n
    '''
def getLabelFeature():
    '''returns GenFeature\n\n
    getLabelFeature()\n
    '''
def basicGetLabelFeature():
    '''returns GenFeature\n\n
    basicGetLabelFeature()\n
    '''
def setLabelFeature():
    '''returns None\n\n
    setLabelFeature(final GenFeature newLabelFeature)\n
    '''
def eInverseAdd():
    '''returns NotificationChain\n\n
    eInverseAdd(final InternalEObject otherEnd, final int featureID, final Class baseClass, NotificationChain msgs)\n
    '''
def eInverseRemove():
    '''returns NotificationChain\n\n
    eInverseRemove(final InternalEObject otherEnd, final int featureID, final Class baseClass, final NotificationChain msgs)\n
    '''
def eGet():
    '''returns Object\n\n
    eGet(final EStructuralFeature eFeature, final boolean resolve)\n
    '''
def eIsSet():
    '''returns boolean\n\n
    eIsSet(final EStructuralFeature eFeature)\n
    '''
def eSet():
    '''returns None\n\n
    eSet(final EStructuralFeature eFeature, final Object newValue)\n
    '''
def eUnset():
    '''returns None\n\n
    eUnset(final EStructuralFeature eFeature)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getItemProviderAdapterFactoryClassName():
    '''returns String\n\n
    getItemProviderAdapterFactoryClassName()\n
    '''
def getTestCaseClassName():
    '''returns String\n\n
    getTestCaseClassName()\n
    '''
def getQualifiedTestCaseClassName():
    '''returns String\n\n
    getQualifiedTestCaseClassName()\n
    '''
def getImportedTestCaseClassName():
    '''returns String\n\n
    getImportedTestCaseClassName()\n
    '''
def canGenerateEdit():
    '''returns boolean\n\n
    canGenerateEdit()\n
    '''
def canGenerateEditor():
    '''returns boolean\n\n
    canGenerateEditor()\n
    '''
def generateEdit():
    '''returns None\n\n
    generateEdit(final IProgressMonitor progressMonitor)\n
    '''
def hasTests():
    '''returns boolean\n\n
    hasTests()\n
    '''
def canGenerateTests():
    '''returns boolean\n\n
    canGenerateTests()\n
    '''
def generateTests():
    '''returns None\n\n
    generateTests(final IProgressMonitor progressMonitor)\n
    '''
def reconcile():
    '''returns boolean\n\n
    reconcile(final GenClass oldGenClassVersion)\n
    reconcile()\n
    '''
def getGenConstraints():
    '''returns List\n\n
    getGenConstraints()\n
    '''
def getAllGenConstraints():
    '''returns List\n\n
    getAllGenConstraints()\n
    '''
def getConstraintImplementor():
    '''returns GenClassifier\n\n
    getConstraintImplementor(final String constraint)\n
    '''
def getConstraintDelegate():
    '''returns GenClassifier\n\n
    getConstraintDelegate(final String constraint)\n
    '''
def hasOnlyDefaultConstraints():
    '''returns boolean\n\n
    hasOnlyDefaultConstraints()\n
    '''
def getInvariantOperation():
    '''returns GenOperation\n\n
    getInvariantOperation(final String constraint)\n
    '''
def isDocumentRoot():
    '''returns boolean\n\n
    isDocumentRoot()\n
    '''
def getMixedGenFeature():
    '''returns GenFeature\n\n
    getMixedGenFeature()\n
    '''
def getListConstructor():
    '''returns String\n\n
    getListConstructor(final GenFeature genFeature)\n
    '''
def isModelRoot():
    '''returns boolean\n\n
    isModelRoot()\n
    '''
def getDeclaredFieldGenFeatures():
    '''returns List\n\n
    getDeclaredFieldGenFeatures()\n
    '''
def isFlag():
    '''returns boolean\n\n
    isFlag(final GenFeature genFeature)\n
    '''
def isESetFlag():
    '''returns boolean\n\n
    isESetFlag(final GenFeature genFeature)\n
    '''
def isField():
    '''returns boolean\n\n
    isField(final GenFeature genFeature)\n
    '''
def isESetField():
    '''returns boolean\n\n
    isESetField(final GenFeature genFeature)\n
    '''
def ():
    '''returns CollidingGenOperationFilter\n\n
    ()\n
    '''
