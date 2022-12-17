def getCopyrightText():
    '''returns String\n\n
    getCopyrightText()\n
    '''
def setCopyrightText():
    '''returns None\n\n
    setCopyrightText(final String newCopyrightText)\n
    '''
def getModelDirectory():
    '''returns String\n\n
    getModelDirectory()\n
    '''
def getModelDirectoryGen():
    '''returns String\n\n
    getModelDirectoryGen()\n
    '''
def setModelDirectory():
    '''returns None\n\n
    setModelDirectory(final String newModelDirectory)\n
    '''
def isCreationCommands():
    '''returns boolean\n\n
    isCreationCommands()\n
    '''
def setCreationCommands():
    '''returns None\n\n
    setCreationCommands(final boolean newCreationCommands)\n
    '''
def isCreationIcons():
    '''returns boolean\n\n
    isCreationIcons()\n
    '''
def setCreationIcons():
    '''returns None\n\n
    setCreationIcons(final boolean newCreationIcons)\n
    '''
def markImportLocation():
    '''returns None\n\n
    markImportLocation(final StringBuffer stringBuffer, final GenPackage genPackage)\n
    markImportLocation(final StringBuffer stringBuffer)\n
    '''
def emitSortedImports():
    '''returns None\n\n
    emitSortedImports()\n
    '''
def getImportedName():
    '''returns String\n\n
    getImportedName(final String qualifiedName)\n
    '''
def addImport():
    '''returns None\n\n
    addImport(final String qualifiedName)\n
    '''
def addPseudoImport():
    '''returns None\n\n
    addPseudoImport(final String qualifiedName)\n
    '''
def getDriverNumber():
    '''returns String\n\n
    getDriverNumber()\n
    '''
def getDate():
    '''returns String\n\n
    getDate()\n
    '''
def getNonNLS():
    '''returns String\n\n
    getNonNLS()\n
    getNonNLS(final int i)\n
    getNonNLS(final String s)\n
    getNonNLS(final String s, int i)\n
    '''
def initialize():
    '''returns None\n\n
    initialize(final Collection ePackages)\n
    initialize(final IProgressMonitor progressMonitor)\n
    '''
def getJControlModel():
    '''returns JControlModel\n\n
    getJControlModel()\n
    '''
def setMethod():
    '''returns None\n\n
    setMethod(final JETEmitter jetEmitter, final String className)\n
    '''
def getInterfaceEmitter():
    '''returns JETEmitter\n\n
    getInterfaceEmitter()\n
    '''
def getClassEmitter():
    '''returns JETEmitter\n\n
    getClassEmitter()\n
    '''
def getEnumClassEmitter():
    '''returns JETEmitter\n\n
    getEnumClassEmitter()\n
    '''
def getFactoryInterfaceEmitter():
    '''returns JETEmitter\n\n
    getFactoryInterfaceEmitter()\n
    '''
def getFactoryClassEmitter():
    '''returns JETEmitter\n\n
    getFactoryClassEmitter()\n
    '''
def getPackageInterfaceEmitter():
    '''returns JETEmitter\n\n
    getPackageInterfaceEmitter()\n
    '''
def getPackageClassEmitter():
    '''returns JETEmitter\n\n
    getPackageClassEmitter()\n
    '''
def getAdapterFactoryClassEmitter():
    '''returns JETEmitter\n\n
    getAdapterFactoryClassEmitter()\n
    '''
def getSwitchClassEmitter():
    '''returns JETEmitter\n\n
    getSwitchClassEmitter()\n
    '''
def getValidatorClassEmitter():
    '''returns JETEmitter\n\n
    getValidatorClassEmitter()\n
    '''
def getPluginXMLEmitter():
    '''returns JETEmitter\n\n
    getPluginXMLEmitter()\n
    '''
def getManifestMFEmitter():
    '''returns JETEmitter\n\n
    getManifestMFEmitter()\n
    '''
def getPluginPropertiesEmitter():
    '''returns JETEmitter\n\n
    getPluginPropertiesEmitter()\n
    '''
def getBuildPropertiesEmitter():
    '''returns JETEmitter\n\n
    getBuildPropertiesEmitter()\n
    '''
def getModelPluginClassEmitter():
    '''returns JETEmitter\n\n
    getModelPluginClassEmitter()\n
    '''
def getResourceClassEmitter():
    '''returns JETEmitter\n\n
    getResourceClassEmitter()\n
    '''
def getResourceFactoryClassEmitter():
    '''returns JETEmitter\n\n
    getResourceFactoryClassEmitter()\n
    '''
def canGenerate():
    '''returns boolean\n\n
    canGenerate()\n
    '''
def setCanGenerate():
    '''returns None\n\n
    setCanGenerate(final boolean canGenerate)\n
    '''
def validate():
    '''returns IStatus\n\n
    validate()\n
    '''
def getExtendedMetaData():
    '''returns ExtendedMetaData\n\n
    getExtendedMetaData()\n
    '''
def hasPluginSupport():
    '''returns boolean\n\n
    hasPluginSupport()\n
    '''
def generate():
    '''returns None\n\n
    generate(final IProgressMonitor progressMonitor)\n
    '''
def hasEditSupport():
    '''returns boolean\n\n
    hasEditSupport()\n
    '''
def canGenerateEdit():
    '''returns boolean\n\n
    canGenerateEdit()\n
    '''
def generateEdit():
    '''returns None\n\n
    generateEdit(final IProgressMonitor progressMonitor)\n
    '''
def hasEditorSupport():
    '''returns boolean\n\n
    hasEditorSupport()\n
    '''
def canGenerateEditor():
    '''returns boolean\n\n
    canGenerateEditor()\n
    '''
def generateEditor():
    '''returns None\n\n
    generateEditor(final IProgressMonitor progressMonitor)\n
    '''
def canGenerateSchema():
    '''returns boolean\n\n
    canGenerateSchema()\n
    '''
def generateSchema():
    '''returns None\n\n
    generateSchema(final IProgressMonitor progressMonitor)\n
    '''
def hasTestSupport():
    '''returns boolean\n\n
    hasTestSupport()\n
    '''
def canGenerateTests():
    '''returns boolean\n\n
    canGenerateTests()\n
    '''
def generateTests():
    '''returns None\n\n
    generateTests(final IProgressMonitor progressMonitor)\n
    '''
def getItemProviderEmitter():
    '''returns JETEmitter\n\n
    getItemProviderEmitter()\n
    '''
def getItemProviderAdapterFactoryEmitter():
    '''returns JETEmitter\n\n
    getItemProviderAdapterFactoryEmitter()\n
    '''
def getEditPluginClassEmitter():
    '''returns JETEmitter\n\n
    getEditPluginClassEmitter()\n
    '''
def getEditPluginXMLEmitter():
    '''returns JETEmitter\n\n
    getEditPluginXMLEmitter()\n
    '''
def getEditManifestMFEmitter():
    '''returns JETEmitter\n\n
    getEditManifestMFEmitter()\n
    '''
def getEditPluginPropertiesEmitter():
    '''returns JETEmitter\n\n
    getEditPluginPropertiesEmitter()\n
    '''
def getEditBuildPropertiesEmitter():
    '''returns JETEmitter\n\n
    getEditBuildPropertiesEmitter()\n
    '''
def getItemGIFEmitter():
    '''returns GIFEmitter\n\n
    getItemGIFEmitter()\n
    '''
def getCreateChildGIFEmitter():
    '''returns GIFEmitter\n\n
    getCreateChildGIFEmitter()\n
    '''
def getModelGIFEmitter():
    '''returns GIFEmitter\n\n
    getModelGIFEmitter()\n
    '''
def getModelWizardGIFEmitter():
    '''returns GIFEmitter\n\n
    getModelWizardGIFEmitter()\n
    '''
def getEditorEmitter():
    '''returns JETEmitter\n\n
    getEditorEmitter()\n
    '''
def getActionBarContributorEmitter():
    '''returns JETEmitter\n\n
    getActionBarContributorEmitter()\n
    '''
def getModelWizardEmitter():
    '''returns JETEmitter\n\n
    getModelWizardEmitter()\n
    '''
def getEditorAdvisorEmitter():
    '''returns JETEmitter\n\n
    getEditorAdvisorEmitter()\n
    '''
def getEditorPluginClassEmitter():
    '''returns JETEmitter\n\n
    getEditorPluginClassEmitter()\n
    '''
def getEditorPluginXMLEmitter():
    '''returns JETEmitter\n\n
    getEditorPluginXMLEmitter()\n
    '''
def getEditorManifestMFEmitter():
    '''returns JETEmitter\n\n
    getEditorManifestMFEmitter()\n
    '''
def getEditorPluginPropertiesEmitter():
    '''returns JETEmitter\n\n
    getEditorPluginPropertiesEmitter()\n
    '''
def getEditorBuildPropertiesEmitter():
    '''returns JETEmitter\n\n
    getEditorBuildPropertiesEmitter()\n
    '''
def getTestCaseEmitter():
    '''returns JETEmitter\n\n
    getTestCaseEmitter()\n
    '''
def getModelTestSuiteEmitter():
    '''returns JETEmitter\n\n
    getModelTestSuiteEmitter()\n
    '''
def getPackageTestSuiteEmitter():
    '''returns JETEmitter\n\n
    getPackageTestSuiteEmitter()\n
    '''
def getPackageExampleEmitter():
    '''returns JETEmitter\n\n
    getPackageExampleEmitter()\n
    '''
def getTestsPluginXMLEmitter():
    '''returns JETEmitter\n\n
    getTestsPluginXMLEmitter()\n
    '''
def getTestsManifestMFEmitter():
    '''returns JETEmitter\n\n
    getTestsManifestMFEmitter()\n
    '''
def getTestsPluginPropertiesEmitter():
    '''returns JETEmitter\n\n
    getTestsPluginPropertiesEmitter()\n
    '''
def getTestsBuildPropertiesEmitter():
    '''returns JETEmitter\n\n
    getTestsBuildPropertiesEmitter()\n
    '''
def getEditDirectory():
    '''returns String\n\n
    getEditDirectory()\n
    '''
def getEditDirectoryGen():
    '''returns String\n\n
    getEditDirectoryGen()\n
    '''
def setEditDirectory():
    '''returns None\n\n
    setEditDirectory(final String newEditDirectory)\n
    '''
def unsetEditDirectory():
    '''returns None\n\n
    unsetEditDirectory()\n
    '''
def isSetEditDirectory():
    '''returns boolean\n\n
    isSetEditDirectory()\n
    '''
def getEditorDirectory():
    '''returns String\n\n
    getEditorDirectory()\n
    '''
def getEditorDirectoryGen():
    '''returns String\n\n
    getEditorDirectoryGen()\n
    '''
def setEditorDirectory():
    '''returns None\n\n
    setEditorDirectory(final String newEditorDirectory)\n
    '''
def unsetEditorDirectory():
    '''returns None\n\n
    unsetEditorDirectory()\n
    '''
def isSetEditorDirectory():
    '''returns boolean\n\n
    isSetEditorDirectory()\n
    '''
def getModelPluginID():
    '''returns String\n\n
    getModelPluginID()\n
    '''
def setModelPluginID():
    '''returns None\n\n
    setModelPluginID(final String newModelPluginID)\n
    '''
def getTemplateDirectory():
    '''returns String\n\n
    getTemplateDirectory()\n
    '''
def setTemplateDirectory():
    '''returns None\n\n
    setTemplateDirectory(final String newTemplateDirectory)\n
    '''
def isRuntimeJar():
    '''returns boolean\n\n
    isRuntimeJar()\n
    '''
def setRuntimeJar():
    '''returns None\n\n
    setRuntimeJar(final boolean newRuntimeJar)\n
    '''
def getForeignModel():
    '''returns EList\n\n
    getForeignModel()\n
    '''
def isDynamicTemplates():
    '''returns boolean\n\n
    isDynamicTemplates()\n
    '''
def setDynamicTemplates():
    '''returns None\n\n
    setDynamicTemplates(final boolean newDynamicTemplates)\n
    '''
def getRedirection():
    '''returns String\n\n
    getRedirection()\n
    '''
def setRedirection():
    '''returns None\n\n
    setRedirection(final String newRedirection)\n
    '''
def isForceOverwrite():
    '''returns boolean\n\n
    isForceOverwrite()\n
    '''
def setForceOverwrite():
    '''returns None\n\n
    setForceOverwrite(final boolean newForceOverwrite)\n
    '''
def getNonExternalizedStringTag():
    '''returns String\n\n
    getNonExternalizedStringTag()\n
    '''
def setNonExternalizedStringTagGen():
    '''returns None\n\n
    setNonExternalizedStringTagGen(final String newNonExternalizedStringTag)\n
    '''
def setNonExternalizedStringTag():
    '''returns None\n\n
    setNonExternalizedStringTag(final String newNonExternalizedStringTag)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getModelName():
    '''returns String\n\n
    getModelName()\n
    '''
def setModelName():
    '''returns None\n\n
    setModelName(final String newModelName)\n
    '''
def getModelPluginClass():
    '''returns String\n\n
    getModelPluginClass()\n
    '''
def setModelPluginClass():
    '''returns None\n\n
    setModelPluginClass(final String newModelPluginClass)\n
    '''
def getEditPluginClass():
    '''returns String\n\n
    getEditPluginClass()\n
    '''
def getEditPluginClassGen():
    '''returns String\n\n
    getEditPluginClassGen()\n
    '''
def setEditPluginClass():
    '''returns None\n\n
    setEditPluginClass(final String newEditPluginClass)\n
    '''
def unsetEditPluginClass():
    '''returns None\n\n
    unsetEditPluginClass()\n
    '''
def isSetEditPluginClass():
    '''returns boolean\n\n
    isSetEditPluginClass()\n
    '''
def getEditorPluginClass():
    '''returns String\n\n
    getEditorPluginClass()\n
    '''
def getEditorPluginClassGen():
    '''returns String\n\n
    getEditorPluginClassGen()\n
    '''
def setEditorPluginClass():
    '''returns None\n\n
    setEditorPluginClass(final String newEditorPluginClass)\n
    '''
def unsetEditorPluginClass():
    '''returns None\n\n
    unsetEditorPluginClass()\n
    '''
def isSetEditorPluginClass():
    '''returns boolean\n\n
    isSetEditorPluginClass()\n
    '''
def isUpdateClasspath():
    '''returns boolean\n\n
    isUpdateClasspath()\n
    '''
def setUpdateClasspath():
    '''returns None\n\n
    setUpdateClasspath(final boolean newUpdateClasspath)\n
    '''
def isGenerateSchema():
    '''returns boolean\n\n
    isGenerateSchema()\n
    '''
def setGenerateSchema():
    '''returns None\n\n
    setGenerateSchema(final boolean newGenerateSchema)\n
    '''
def isNonNLSMarkers():
    '''returns boolean\n\n
    isNonNLSMarkers()\n
    '''
def setNonNLSMarkersGen():
    '''returns None\n\n
    setNonNLSMarkersGen(final boolean newNonNLSMarkers)\n
    '''
def setNonNLSMarkers():
    '''returns None\n\n
    setNonNLSMarkers(final boolean newNonNLSMarkers)\n
    '''
def getStaticPackages():
    '''returns EList\n\n
    getStaticPackages()\n
    '''
def getModelPluginVariables():
    '''returns EList\n\n
    getModelPluginVariables()\n
    '''
def getRootExtendsInterface():
    '''returns String\n\n
    getRootExtendsInterface()\n
    '''
def setRootExtendsInterface():
    '''returns None\n\n
    setRootExtendsInterface(final String newRootExtendsInterface)\n
    '''
def getRootExtendsClass():
    '''returns String\n\n
    getRootExtendsClass()\n
    '''
def setRootExtendsClass():
    '''returns None\n\n
    setRootExtendsClass(final String newRootExtendsClass)\n
    '''
def getRootImplementsInterface():
    '''returns String\n\n
    getRootImplementsInterface()\n
    '''
def getRootImplementsInterfaceGenClass():
    '''returns GenClass\n\n
    getRootImplementsInterfaceGenClass()\n
    '''
def setRootImplementsInterfaceGen():
    '''returns None\n\n
    setRootImplementsInterfaceGen(final String newRootImplementsInterface)\n
    '''
def setRootImplementsInterface():
    '''returns None\n\n
    setRootImplementsInterface(final String newRootImplementsInterface)\n
    '''
def getEffectiveModelPluginVariables():
    '''returns List\n\n
    getEffectiveModelPluginVariables()\n
    '''
def getEffectiveModelPluginIDs():
    '''returns List\n\n
    getEffectiveModelPluginIDs()\n
    '''
def isSuppressEMFTypes():
    '''returns boolean\n\n
    isSuppressEMFTypes()\n
    '''
def setSuppressEMFTypes():
    '''returns None\n\n
    setSuppressEMFTypes(final boolean newSuppressEMFTypes)\n
    '''
def getFeatureMapWrapperInterface():
    '''returns String\n\n
    getFeatureMapWrapperInterface()\n
    '''
def setFeatureMapWrapperInterface():
    '''returns None\n\n
    setFeatureMapWrapperInterface(final String newFeatureMapWrapperInterface)\n
    '''
def getFeatureMapWrapperInternalInterface():
    '''returns String\n\n
    getFeatureMapWrapperInternalInterface()\n
    '''
def setFeatureMapWrapperInternalInterface():
    '''returns None\n\n
    setFeatureMapWrapperInternalInterface(final String newFeatureMapWrapperInternalInterface)\n
    '''
def getFeatureMapWrapperClass():
    '''returns String\n\n
    getFeatureMapWrapperClass()\n
    '''
def setFeatureMapWrapperClass():
    '''returns None\n\n
    setFeatureMapWrapperClass(final String newFeatureMapWrapperClass)\n
    '''
def isRuntimeCompatibility():
    '''returns boolean\n\n
    isRuntimeCompatibility()\n
    '''
def needsRuntimeCompatibility():
    '''returns boolean\n\n
    needsRuntimeCompatibility()\n
    '''
def setRuntimeCompatibility():
    '''returns None\n\n
    setRuntimeCompatibility(final boolean newRuntimeCompatibility)\n
    '''
def isRichClientPlatform():
    '''returns boolean\n\n
    isRichClientPlatform()\n
    '''
def setRichClientPlatform():
    '''returns None\n\n
    setRichClientPlatform(final boolean newRichClientPlatform)\n
    '''
def isReflectiveDelegation():
    '''returns boolean\n\n
    isReflectiveDelegation()\n
    '''
def setReflectiveDelegation():
    '''returns None\n\n
    setReflectiveDelegation(final boolean newReflectiveDelegation)\n
    '''
def isCodeFormatting():
    '''returns boolean\n\n
    isCodeFormatting()\n
    '''
def setCodeFormatting():
    '''returns None\n\n
    setCodeFormatting(final boolean newCodeFormatting)\n
    '''
def getTestsDirectory():
    '''returns String\n\n
    getTestsDirectory()\n
    '''
def getTestsDirectoryGen():
    '''returns String\n\n
    getTestsDirectoryGen()\n
    '''
def setTestsDirectory():
    '''returns None\n\n
    setTestsDirectory(final String newTestsDirectory)\n
    '''
def unsetTestsDirectory():
    '''returns None\n\n
    unsetTestsDirectory()\n
    '''
def isSetTestsDirectory():
    '''returns boolean\n\n
    isSetTestsDirectory()\n
    '''
def getTestSuiteClass():
    '''returns String\n\n
    getTestSuiteClass()\n
    '''
def getTestSuiteClassGen():
    '''returns String\n\n
    getTestSuiteClassGen()\n
    '''
def setTestSuiteClass():
    '''returns None\n\n
    setTestSuiteClass(final String newTestSuiteClass)\n
    '''
def unsetTestSuiteClass():
    '''returns None\n\n
    unsetTestSuiteClass()\n
    '''
def isSetTestSuiteClass():
    '''returns boolean\n\n
    isSetTestSuiteClass()\n
    '''
def getBooleanFlagsField():
    '''returns String\n\n
    getBooleanFlagsField()\n
    '''
def setBooleanFlagsField():
    '''returns None\n\n
    setBooleanFlagsField(final String newBooleanFlagsField)\n
    '''
def getBooleanFlagsReservedBits():
    '''returns int\n\n
    getBooleanFlagsReservedBits()\n
    '''
def setBooleanFlagsReservedBits():
    '''returns None\n\n
    setBooleanFlagsReservedBits(final int newBooleanFlagsReservedBits)\n
    '''
def getImporterID():
    '''returns String\n\n
    getImporterID()\n
    '''
def setImporterID():
    '''returns None\n\n
    setImporterID(final String newImporterID)\n
    '''
def isBundleManifest():
    '''returns boolean\n\n
    isBundleManifest()\n
    '''
def setBundleManifest():
    '''returns None\n\n
    setBundleManifest(final boolean newBundleManifest)\n
    '''
def getGenPackages():
    '''returns EList\n\n
    getGenPackages()\n
    '''
def getStaticGenPackages():
    '''returns EList\n\n
    getStaticGenPackages()\n
    '''
def getUsedGenPackages():
    '''returns EList\n\n
    getUsedGenPackages()\n
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
def getModelProjectDirectory():
    '''returns String\n\n
    getModelProjectDirectory()\n
    '''
def getEditProjectDirectory():
    '''returns String\n\n
    getEditProjectDirectory()\n
    '''
def getEditorProjectDirectory():
    '''returns String\n\n
    getEditorProjectDirectory()\n
    '''
def getTestsProjectDirectory():
    '''returns String\n\n
    getTestsProjectDirectory()\n
    '''
def sameModelEditProject():
    '''returns boolean\n\n
    sameModelEditProject()\n
    '''
def sameEditEditorProject():
    '''returns boolean\n\n
    sameEditEditorProject()\n
    '''
def sameModelEditorProject():
    '''returns boolean\n\n
    sameModelEditorProject()\n
    '''
def sameModelTestsProject():
    '''returns boolean\n\n
    sameModelTestsProject()\n
    '''
def getEditIconsDirectory():
    '''returns String\n\n
    getEditIconsDirectory()\n
    '''
def getEditorIconsDirectory():
    '''returns String\n\n
    getEditorIconsDirectory()\n
    '''
def getEditPluginID():
    '''returns String\n\n
    getEditPluginID()\n
    '''
def getEditorPluginID():
    '''returns String\n\n
    getEditorPluginID()\n
    '''
def getTestsPluginID():
    '''returns String\n\n
    getTestsPluginID()\n
    '''
def hasModelPluginClass():
    '''returns boolean\n\n
    hasModelPluginClass()\n
    '''
def getModelPluginPackageName():
    '''returns String\n\n
    getModelPluginPackageName()\n
    '''
def getModelPluginClassName():
    '''returns String\n\n
    getModelPluginClassName()\n
    '''
def getQualifiedModelPluginClassName():
    '''returns String\n\n
    getQualifiedModelPluginClassName()\n
    '''
def getEditPluginPackageName():
    '''returns String\n\n
    getEditPluginPackageName()\n
    '''
def getEditPluginClassName():
    '''returns String\n\n
    getEditPluginClassName()\n
    '''
def getQualifiedEditPluginClassName():
    '''returns String\n\n
    getQualifiedEditPluginClassName()\n
    '''
def getEditorPluginPackageName():
    '''returns String\n\n
    getEditorPluginPackageName()\n
    '''
def getEditorPluginClassName():
    '''returns String\n\n
    getEditorPluginClassName()\n
    '''
def getQualifiedEditorPluginClassName():
    '''returns String\n\n
    getQualifiedEditorPluginClassName()\n
    '''
def getQualifiedEditorAdvisorClassName():
    '''returns String\n\n
    getQualifiedEditorAdvisorClassName()\n
    '''
def getEditorAdvisorClassName():
    '''returns String\n\n
    getEditorAdvisorClassName()\n
    '''
def getTestSuitePackageName():
    '''returns String\n\n
    getTestSuitePackageName()\n
    '''
def getTestSuiteClassName():
    '''returns String\n\n
    getTestSuiteClassName()\n
    '''
def getQualifiedTestSuiteClassName():
    '''returns String\n\n
    getQualifiedTestSuiteClassName()\n
    '''
def getAllGenPackagesWithClassifiers():
    '''returns List\n\n
    getAllGenPackagesWithClassifiers()\n
    '''
def getAllUsedGenPackagesWithClassifiers():
    '''returns List\n\n
    getAllUsedGenPackagesWithClassifiers()\n
    '''
def getAllGenAndUsedGenPackagesWithClassifiers():
    '''returns List\n\n
    getAllGenAndUsedGenPackagesWithClassifiers()\n
    '''
def getAllGenUsedAndStaticGenPackagesWithClassifiers():
    '''returns List\n\n
    getAllGenUsedAndStaticGenPackagesWithClassifiers()\n
    '''
def getModelQualifiedPackageNames():
    '''returns List\n\n
    getModelQualifiedPackageNames()\n
    '''
def getModelRequiredPlugins():
    '''returns List\n\n
    getModelRequiredPlugins()\n
    '''
def getEditQualifiedPackageNames():
    '''returns List\n\n
    getEditQualifiedPackageNames()\n
    '''
def getEditRequiredPlugins():
    '''returns List\n\n
    getEditRequiredPlugins()\n
    '''
def getEditorQualifiedPackageNames():
    '''returns List\n\n
    getEditorQualifiedPackageNames()\n
    '''
def getEditorRequiredPlugins():
    '''returns List\n\n
    getEditorRequiredPlugins()\n
    '''
def getTestsQualifiedPackageNames():
    '''returns List\n\n
    getTestsQualifiedPackageNames()\n
    '''
def getTestsRequiredPlugins():
    '''returns List\n\n
    getTestsRequiredPlugins()\n
    '''
def getEditResourceDelegateImportedPluginClassNames():
    '''returns List\n\n
    getEditResourceDelegateImportedPluginClassNames()\n
    '''
def reconcile():
    '''returns boolean\n\n
    reconcile(final GenModel oldGenModelVersion)\n
    reconcile()\n
    '''
def computeMissingUsedGenPackages():
    '''returns List\n\n
    computeMissingUsedGenPackages()\n
    '''
def getMissingPackages():
    '''returns List\n\n
    getMissingPackages()\n
    '''
def hasXMLDependency():
    '''returns boolean\n\n
    hasXMLDependency()\n
    '''
def getXMLEncodingChoices():
    '''returns String\n\n
    getXMLEncodingChoices()\n
    '''
def getIndentation():
    '''returns String\n\n
    getIndentation(final StringBuffer stringBuffer)\n
    '''
def getEcoreModelElement():
    '''returns EModelElement\n\n
    getEcoreModelElement()\n
    '''
def getAllGenFeatures():
    '''returns List\n\n
    getAllGenFeatures()\n
    '''
def getFilteredAllGenFeatures():
    '''returns List\n\n
    getFilteredAllGenFeatures()\n
    '''
def setCodeFormatterOptions():
    '''returns None\n\n
    setCodeFormatterOptions(final Map options)\n
    '''
def createCodeFormatter():
    '''returns CodeFormatter\n\n
    createCodeFormatter()\n
    '''
def isBooleanFlagsEnabled():
    '''returns boolean\n\n
    isBooleanFlagsEnabled()\n
    '''
def createGenModel():
    '''returns GenModel\n\n
    createGenModel()\n
    '''
def createGenPackage():
    '''returns GenPackage\n\n
    createGenPackage()\n
    '''
def createGenClass():
    '''returns GenClass\n\n
    createGenClass()\n
    '''
def createGenFeature():
    '''returns GenFeature\n\n
    createGenFeature()\n
    '''
def createGenEnum():
    '''returns GenEnum\n\n
    createGenEnum()\n
    '''
def createGenEnumLiteral():
    '''returns GenEnumLiteral\n\n
    createGenEnumLiteral()\n
    '''
def createGenDataType():
    '''returns GenDataType\n\n
    createGenDataType()\n
    '''
def createGenOperation():
    '''returns GenOperation\n\n
    createGenOperation()\n
    '''
def createGenParameter():
    '''returns GenParameter\n\n
    createGenParameter()\n
    '''
def getPropertyCategories():
    '''returns Set\n\n
    getPropertyCategories()\n
    '''
def hasLocalGenModel():
    '''returns boolean\n\n
    hasLocalGenModel()\n
    '''
def getRelativeGenModelLocation():
    '''returns String\n\n
    getRelativeGenModelLocation()\n
    '''
def getPropertyCategoryKey():
    '''returns String\n\n
    getPropertyCategoryKey(final String category)\n
    '''
