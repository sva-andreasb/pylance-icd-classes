def getCopyrightText():
    '''    public String getCopyrightText()
    '''
def setCopyrightText():
    '''    public void setCopyrightText(final String newCopyrightText)
    '''
def getModelDirectory():
    '''    public String getModelDirectory()
    '''
def getModelDirectoryGen():
    '''    public String getModelDirectoryGen()
    '''
def setModelDirectory():
    '''    public void setModelDirectory(final String newModelDirectory)
    '''
def isCreationCommands():
    '''    public boolean isCreationCommands()
    '''
def setCreationCommands():
    '''    public void setCreationCommands(final boolean newCreationCommands)
    '''
def isCreationIcons():
    '''    public boolean isCreationIcons()
    '''
def setCreationIcons():
    '''    public void setCreationIcons(final boolean newCreationIcons)
    '''
def markImportLocation():
    '''    public void markImportLocation(final StringBuffer stringBuffer, final GenPackage genPackage)
    public void markImportLocation(final StringBuffer stringBuffer)
    '''
def emitSortedImports():
    '''    public void emitSortedImports()
    '''
def getImportedName():
    '''    public String getImportedName(final String qualifiedName)
    '''
def addImport():
    '''    public void addImport(final String qualifiedName)
    '''
def addPseudoImport():
    '''    public void addPseudoImport(final String qualifiedName)
    '''
def getDriverNumber():
    '''    public String getDriverNumber()
    '''
def getDate():
    '''    public String getDate()
    '''
def getNonNLS():
    '''    public String getNonNLS()
    public String getNonNLS(final int i)
    public String getNonNLS(final String s)
    public String getNonNLS(final String s, int i)
    '''
def initialize():
    '''    public void initialize(final Collection ePackages)
    public void initialize(final IProgressMonitor progressMonitor)
    '''
def getJControlModel():
    '''    public JControlModel getJControlModel()
    '''
def setMethod():
    '''    public void setMethod(final JETEmitter jetEmitter, final String className)
    '''
def getInterfaceEmitter():
    '''    public JETEmitter getInterfaceEmitter()
    '''
def getClassEmitter():
    '''    public JETEmitter getClassEmitter()
    '''
def getEnumClassEmitter():
    '''    public JETEmitter getEnumClassEmitter()
    '''
def getFactoryInterfaceEmitter():
    '''    public JETEmitter getFactoryInterfaceEmitter()
    '''
def getFactoryClassEmitter():
    '''    public JETEmitter getFactoryClassEmitter()
    '''
def getPackageInterfaceEmitter():
    '''    public JETEmitter getPackageInterfaceEmitter()
    '''
def getPackageClassEmitter():
    '''    public JETEmitter getPackageClassEmitter()
    '''
def getAdapterFactoryClassEmitter():
    '''    public JETEmitter getAdapterFactoryClassEmitter()
    '''
def getSwitchClassEmitter():
    '''    public JETEmitter getSwitchClassEmitter()
    '''
def getValidatorClassEmitter():
    '''    public JETEmitter getValidatorClassEmitter()
    '''
def getPluginXMLEmitter():
    '''    public JETEmitter getPluginXMLEmitter()
    '''
def getManifestMFEmitter():
    '''    public JETEmitter getManifestMFEmitter()
    '''
def getPluginPropertiesEmitter():
    '''    public JETEmitter getPluginPropertiesEmitter()
    '''
def getBuildPropertiesEmitter():
    '''    public JETEmitter getBuildPropertiesEmitter()
    '''
def getModelPluginClassEmitter():
    '''    public JETEmitter getModelPluginClassEmitter()
    '''
def getResourceClassEmitter():
    '''    public JETEmitter getResourceClassEmitter()
    '''
def getResourceFactoryClassEmitter():
    '''    public JETEmitter getResourceFactoryClassEmitter()
    '''
def canGenerate():
    '''    public boolean canGenerate()
    '''
def setCanGenerate():
    '''    public void setCanGenerate(final boolean canGenerate)
    '''
def validate():
    '''    public IStatus validate()
    '''
def getExtendedMetaData():
    '''    public ExtendedMetaData getExtendedMetaData()
    '''
def hasPluginSupport():
    '''    public boolean hasPluginSupport()
    '''
def generate():
    '''    public void generate(final IProgressMonitor progressMonitor)
    '''
def hasEditSupport():
    '''    public boolean hasEditSupport()
    '''
def canGenerateEdit():
    '''    public boolean canGenerateEdit()
    '''
def generateEdit():
    '''    public void generateEdit(final IProgressMonitor progressMonitor)
    '''
def hasEditorSupport():
    '''    public boolean hasEditorSupport()
    '''
def canGenerateEditor():
    '''    public boolean canGenerateEditor()
    '''
def generateEditor():
    '''    public void generateEditor(final IProgressMonitor progressMonitor)
    '''
def canGenerateSchema():
    '''    public boolean canGenerateSchema()
    '''
def generateSchema():
    '''    public void generateSchema(final IProgressMonitor progressMonitor)
    '''
def hasTestSupport():
    '''    public boolean hasTestSupport()
    '''
def canGenerateTests():
    '''    public boolean canGenerateTests()
    '''
def generateTests():
    '''    public void generateTests(final IProgressMonitor progressMonitor)
    '''
def getItemProviderEmitter():
    '''    public JETEmitter getItemProviderEmitter()
    '''
def getItemProviderAdapterFactoryEmitter():
    '''    public JETEmitter getItemProviderAdapterFactoryEmitter()
    '''
def getEditPluginClassEmitter():
    '''    public JETEmitter getEditPluginClassEmitter()
    '''
def getEditPluginXMLEmitter():
    '''    public JETEmitter getEditPluginXMLEmitter()
    '''
def getEditManifestMFEmitter():
    '''    public JETEmitter getEditManifestMFEmitter()
    '''
def getEditPluginPropertiesEmitter():
    '''    public JETEmitter getEditPluginPropertiesEmitter()
    '''
def getEditBuildPropertiesEmitter():
    '''    public JETEmitter getEditBuildPropertiesEmitter()
    '''
def getItemGIFEmitter():
    '''    public GIFEmitter getItemGIFEmitter()
    '''
def getCreateChildGIFEmitter():
    '''    public GIFEmitter getCreateChildGIFEmitter()
    '''
def getModelGIFEmitter():
    '''    public GIFEmitter getModelGIFEmitter()
    '''
def getModelWizardGIFEmitter():
    '''    public GIFEmitter getModelWizardGIFEmitter()
    '''
def getEditorEmitter():
    '''    public JETEmitter getEditorEmitter()
    '''
def getActionBarContributorEmitter():
    '''    public JETEmitter getActionBarContributorEmitter()
    '''
def getModelWizardEmitter():
    '''    public JETEmitter getModelWizardEmitter()
    '''
def getEditorAdvisorEmitter():
    '''    public JETEmitter getEditorAdvisorEmitter()
    '''
def getEditorPluginClassEmitter():
    '''    public JETEmitter getEditorPluginClassEmitter()
    '''
def getEditorPluginXMLEmitter():
    '''    public JETEmitter getEditorPluginXMLEmitter()
    '''
def getEditorManifestMFEmitter():
    '''    public JETEmitter getEditorManifestMFEmitter()
    '''
def getEditorPluginPropertiesEmitter():
    '''    public JETEmitter getEditorPluginPropertiesEmitter()
    '''
def getEditorBuildPropertiesEmitter():
    '''    public JETEmitter getEditorBuildPropertiesEmitter()
    '''
def getTestCaseEmitter():
    '''    public JETEmitter getTestCaseEmitter()
    '''
def getModelTestSuiteEmitter():
    '''    public JETEmitter getModelTestSuiteEmitter()
    '''
def getPackageTestSuiteEmitter():
    '''    public JETEmitter getPackageTestSuiteEmitter()
    '''
def getPackageExampleEmitter():
    '''    public JETEmitter getPackageExampleEmitter()
    '''
def getTestsPluginXMLEmitter():
    '''    public JETEmitter getTestsPluginXMLEmitter()
    '''
def getTestsManifestMFEmitter():
    '''    public JETEmitter getTestsManifestMFEmitter()
    '''
def getTestsPluginPropertiesEmitter():
    '''    public JETEmitter getTestsPluginPropertiesEmitter()
    '''
def getTestsBuildPropertiesEmitter():
    '''    public JETEmitter getTestsBuildPropertiesEmitter()
    '''
def getEditDirectory():
    '''    public String getEditDirectory()
    '''
def getEditDirectoryGen():
    '''    public String getEditDirectoryGen()
    '''
def setEditDirectory():
    '''    public void setEditDirectory(final String newEditDirectory)
    '''
def unsetEditDirectory():
    '''    public void unsetEditDirectory()
    '''
def isSetEditDirectory():
    '''    public boolean isSetEditDirectory()
    '''
def getEditorDirectory():
    '''    public String getEditorDirectory()
    '''
def getEditorDirectoryGen():
    '''    public String getEditorDirectoryGen()
    '''
def setEditorDirectory():
    '''    public void setEditorDirectory(final String newEditorDirectory)
    '''
def unsetEditorDirectory():
    '''    public void unsetEditorDirectory()
    '''
def isSetEditorDirectory():
    '''    public boolean isSetEditorDirectory()
    '''
def getModelPluginID():
    '''    public String getModelPluginID()
    '''
def setModelPluginID():
    '''    public void setModelPluginID(final String newModelPluginID)
    '''
def getTemplateDirectory():
    '''    public String getTemplateDirectory()
    '''
def setTemplateDirectory():
    '''    public void setTemplateDirectory(final String newTemplateDirectory)
    '''
def isRuntimeJar():
    '''    public boolean isRuntimeJar()
    '''
def setRuntimeJar():
    '''    public void setRuntimeJar(final boolean newRuntimeJar)
    '''
def getForeignModel():
    '''    public EList getForeignModel()
    '''
def isDynamicTemplates():
    '''    public boolean isDynamicTemplates()
    '''
def setDynamicTemplates():
    '''    public void setDynamicTemplates(final boolean newDynamicTemplates)
    '''
def getRedirection():
    '''    public String getRedirection()
    '''
def setRedirection():
    '''    public void setRedirection(final String newRedirection)
    '''
def isForceOverwrite():
    '''    public boolean isForceOverwrite()
    '''
def setForceOverwrite():
    '''    public void setForceOverwrite(final boolean newForceOverwrite)
    '''
def getNonExternalizedStringTag():
    '''    public String getNonExternalizedStringTag()
    '''
def setNonExternalizedStringTagGen():
    '''    public void setNonExternalizedStringTagGen(final String newNonExternalizedStringTag)
    '''
def setNonExternalizedStringTag():
    '''    public void setNonExternalizedStringTag(final String newNonExternalizedStringTag)
    '''
def getName():
    '''    public String getName()
    '''
def getModelName():
    '''    public String getModelName()
    '''
def setModelName():
    '''    public void setModelName(final String newModelName)
    '''
def getModelPluginClass():
    '''    public String getModelPluginClass()
    '''
def setModelPluginClass():
    '''    public void setModelPluginClass(final String newModelPluginClass)
    '''
def getEditPluginClass():
    '''    public String getEditPluginClass()
    '''
def getEditPluginClassGen():
    '''    public String getEditPluginClassGen()
    '''
def setEditPluginClass():
    '''    public void setEditPluginClass(final String newEditPluginClass)
    '''
def unsetEditPluginClass():
    '''    public void unsetEditPluginClass()
    '''
def isSetEditPluginClass():
    '''    public boolean isSetEditPluginClass()
    '''
def getEditorPluginClass():
    '''    public String getEditorPluginClass()
    '''
def getEditorPluginClassGen():
    '''    public String getEditorPluginClassGen()
    '''
def setEditorPluginClass():
    '''    public void setEditorPluginClass(final String newEditorPluginClass)
    '''
def unsetEditorPluginClass():
    '''    public void unsetEditorPluginClass()
    '''
def isSetEditorPluginClass():
    '''    public boolean isSetEditorPluginClass()
    '''
def isUpdateClasspath():
    '''    public boolean isUpdateClasspath()
    '''
def setUpdateClasspath():
    '''    public void setUpdateClasspath(final boolean newUpdateClasspath)
    '''
def isGenerateSchema():
    '''    public boolean isGenerateSchema()
    '''
def setGenerateSchema():
    '''    public void setGenerateSchema(final boolean newGenerateSchema)
    '''
def isNonNLSMarkers():
    '''    public boolean isNonNLSMarkers()
    '''
def setNonNLSMarkersGen():
    '''    public void setNonNLSMarkersGen(final boolean newNonNLSMarkers)
    '''
def setNonNLSMarkers():
    '''    public void setNonNLSMarkers(final boolean newNonNLSMarkers)
    '''
def getStaticPackages():
    '''    public EList getStaticPackages()
    '''
def getModelPluginVariables():
    '''    public EList getModelPluginVariables()
    '''
def getRootExtendsInterface():
    '''    public String getRootExtendsInterface()
    '''
def setRootExtendsInterface():
    '''    public void setRootExtendsInterface(final String newRootExtendsInterface)
    '''
def getRootExtendsClass():
    '''    public String getRootExtendsClass()
    '''
def setRootExtendsClass():
    '''    public void setRootExtendsClass(final String newRootExtendsClass)
    '''
def getRootImplementsInterface():
    '''    public String getRootImplementsInterface()
    '''
def getRootImplementsInterfaceGenClass():
    '''    public GenClass getRootImplementsInterfaceGenClass()
    '''
def setRootImplementsInterfaceGen():
    '''    public void setRootImplementsInterfaceGen(final String newRootImplementsInterface)
    '''
def setRootImplementsInterface():
    '''    public void setRootImplementsInterface(final String newRootImplementsInterface)
    '''
def getEffectiveModelPluginVariables():
    '''    public List getEffectiveModelPluginVariables()
    '''
def getEffectiveModelPluginIDs():
    '''    public List getEffectiveModelPluginIDs()
    '''
def isSuppressEMFTypes():
    '''    public boolean isSuppressEMFTypes()
    '''
def setSuppressEMFTypes():
    '''    public void setSuppressEMFTypes(final boolean newSuppressEMFTypes)
    '''
def getFeatureMapWrapperInterface():
    '''    public String getFeatureMapWrapperInterface()
    '''
def setFeatureMapWrapperInterface():
    '''    public void setFeatureMapWrapperInterface(final String newFeatureMapWrapperInterface)
    '''
def getFeatureMapWrapperInternalInterface():
    '''    public String getFeatureMapWrapperInternalInterface()
    '''
def setFeatureMapWrapperInternalInterface():
    '''    public void setFeatureMapWrapperInternalInterface(final String newFeatureMapWrapperInternalInterface)
    '''
def getFeatureMapWrapperClass():
    '''    public String getFeatureMapWrapperClass()
    '''
def setFeatureMapWrapperClass():
    '''    public void setFeatureMapWrapperClass(final String newFeatureMapWrapperClass)
    '''
def isRuntimeCompatibility():
    '''    public boolean isRuntimeCompatibility()
    '''
def needsRuntimeCompatibility():
    '''    public boolean needsRuntimeCompatibility()
    '''
def setRuntimeCompatibility():
    '''    public void setRuntimeCompatibility(final boolean newRuntimeCompatibility)
    '''
def isRichClientPlatform():
    '''    public boolean isRichClientPlatform()
    '''
def setRichClientPlatform():
    '''    public void setRichClientPlatform(final boolean newRichClientPlatform)
    '''
def isReflectiveDelegation():
    '''    public boolean isReflectiveDelegation()
    '''
def setReflectiveDelegation():
    '''    public void setReflectiveDelegation(final boolean newReflectiveDelegation)
    '''
def isCodeFormatting():
    '''    public boolean isCodeFormatting()
    '''
def setCodeFormatting():
    '''    public void setCodeFormatting(final boolean newCodeFormatting)
    '''
def getTestsDirectory():
    '''    public String getTestsDirectory()
    '''
def getTestsDirectoryGen():
    '''    public String getTestsDirectoryGen()
    '''
def setTestsDirectory():
    '''    public void setTestsDirectory(final String newTestsDirectory)
    '''
def unsetTestsDirectory():
    '''    public void unsetTestsDirectory()
    '''
def isSetTestsDirectory():
    '''    public boolean isSetTestsDirectory()
    '''
def getTestSuiteClass():
    '''    public String getTestSuiteClass()
    '''
def getTestSuiteClassGen():
    '''    public String getTestSuiteClassGen()
    '''
def setTestSuiteClass():
    '''    public void setTestSuiteClass(final String newTestSuiteClass)
    '''
def unsetTestSuiteClass():
    '''    public void unsetTestSuiteClass()
    '''
def isSetTestSuiteClass():
    '''    public boolean isSetTestSuiteClass()
    '''
def getBooleanFlagsField():
    '''    public String getBooleanFlagsField()
    '''
def setBooleanFlagsField():
    '''    public void setBooleanFlagsField(final String newBooleanFlagsField)
    '''
def getBooleanFlagsReservedBits():
    '''    public int getBooleanFlagsReservedBits()
    '''
def setBooleanFlagsReservedBits():
    '''    public void setBooleanFlagsReservedBits(final int newBooleanFlagsReservedBits)
    '''
def getImporterID():
    '''    public String getImporterID()
    '''
def setImporterID():
    '''    public void setImporterID(final String newImporterID)
    '''
def isBundleManifest():
    '''    public boolean isBundleManifest()
    '''
def setBundleManifest():
    '''    public void setBundleManifest(final boolean newBundleManifest)
    '''
def getGenPackages():
    '''    public EList getGenPackages()
    '''
def getStaticGenPackages():
    '''    public EList getStaticGenPackages()
    '''
def getUsedGenPackages():
    '''    public EList getUsedGenPackages()
    '''
def eInverseAdd():
    '''    public NotificationChain eInverseAdd(final InternalEObject otherEnd, final int featureID, final Class baseClass, NotificationChain msgs)
    '''
def eInverseRemove():
    '''    public NotificationChain eInverseRemove(final InternalEObject otherEnd, final int featureID, final Class baseClass, final NotificationChain msgs)
    '''
def eGet():
    '''    public Object eGet(final EStructuralFeature eFeature, final boolean resolve)
    '''
def eIsSet():
    '''    public boolean eIsSet(final EStructuralFeature eFeature)
    '''
def eSet():
    '''    public void eSet(final EStructuralFeature eFeature, final Object newValue)
    '''
def eUnset():
    '''    public void eUnset(final EStructuralFeature eFeature)
    '''
def toString():
    '''    public String toString()
    '''
def getModelProjectDirectory():
    '''    public String getModelProjectDirectory()
    '''
def getEditProjectDirectory():
    '''    public String getEditProjectDirectory()
    '''
def getEditorProjectDirectory():
    '''    public String getEditorProjectDirectory()
    '''
def getTestsProjectDirectory():
    '''    public String getTestsProjectDirectory()
    '''
def sameModelEditProject():
    '''    public boolean sameModelEditProject()
    '''
def sameEditEditorProject():
    '''    public boolean sameEditEditorProject()
    '''
def sameModelEditorProject():
    '''    public boolean sameModelEditorProject()
    '''
def sameModelTestsProject():
    '''    public boolean sameModelTestsProject()
    '''
def getEditIconsDirectory():
    '''    public String getEditIconsDirectory()
    '''
def getEditorIconsDirectory():
    '''    public String getEditorIconsDirectory()
    '''
def getEditPluginID():
    '''    public String getEditPluginID()
    '''
def getEditorPluginID():
    '''    public String getEditorPluginID()
    '''
def getTestsPluginID():
    '''    public String getTestsPluginID()
    '''
def hasModelPluginClass():
    '''    public boolean hasModelPluginClass()
    '''
def getModelPluginPackageName():
    '''    public String getModelPluginPackageName()
    '''
def getModelPluginClassName():
    '''    public String getModelPluginClassName()
    '''
def getQualifiedModelPluginClassName():
    '''    public String getQualifiedModelPluginClassName()
    '''
def getEditPluginPackageName():
    '''    public String getEditPluginPackageName()
    '''
def getEditPluginClassName():
    '''    public String getEditPluginClassName()
    '''
def getQualifiedEditPluginClassName():
    '''    public String getQualifiedEditPluginClassName()
    '''
def getEditorPluginPackageName():
    '''    public String getEditorPluginPackageName()
    '''
def getEditorPluginClassName():
    '''    public String getEditorPluginClassName()
    '''
def getQualifiedEditorPluginClassName():
    '''    public String getQualifiedEditorPluginClassName()
    '''
def getQualifiedEditorAdvisorClassName():
    '''    public String getQualifiedEditorAdvisorClassName()
    '''
def getEditorAdvisorClassName():
    '''    public String getEditorAdvisorClassName()
    '''
def getTestSuitePackageName():
    '''    public String getTestSuitePackageName()
    '''
def getTestSuiteClassName():
    '''    public String getTestSuiteClassName()
    '''
def getQualifiedTestSuiteClassName():
    '''    public String getQualifiedTestSuiteClassName()
    '''
def getAllGenPackagesWithClassifiers():
    '''    public List getAllGenPackagesWithClassifiers()
    '''
def getAllUsedGenPackagesWithClassifiers():
    '''    public List getAllUsedGenPackagesWithClassifiers()
    '''
def getAllGenAndUsedGenPackagesWithClassifiers():
    '''    public List getAllGenAndUsedGenPackagesWithClassifiers()
    '''
def getAllGenUsedAndStaticGenPackagesWithClassifiers():
    '''    public List getAllGenUsedAndStaticGenPackagesWithClassifiers()
    '''
def getModelQualifiedPackageNames():
    '''    public List getModelQualifiedPackageNames()
    '''
def getModelRequiredPlugins():
    '''    public List getModelRequiredPlugins()
    '''
def getEditQualifiedPackageNames():
    '''    public List getEditQualifiedPackageNames()
    '''
def getEditRequiredPlugins():
    '''    public List getEditRequiredPlugins()
    '''
def getEditorQualifiedPackageNames():
    '''    public List getEditorQualifiedPackageNames()
    '''
def getEditorRequiredPlugins():
    '''    public List getEditorRequiredPlugins()
    '''
def getTestsQualifiedPackageNames():
    '''    public List getTestsQualifiedPackageNames()
    '''
def getTestsRequiredPlugins():
    '''    public List getTestsRequiredPlugins()
    '''
def getEditResourceDelegateImportedPluginClassNames():
    '''    public List getEditResourceDelegateImportedPluginClassNames()
    '''
def reconcile():
    '''    public boolean reconcile(final GenModel oldGenModelVersion)
    public boolean reconcile()
    '''
def computeMissingUsedGenPackages():
    '''    public List computeMissingUsedGenPackages()
    '''
def getMissingPackages():
    '''    public List getMissingPackages()
    '''
def hasXMLDependency():
    '''    public boolean hasXMLDependency()
    '''
def getXMLEncodingChoices():
    '''    public String getXMLEncodingChoices()
    '''
def getIndentation():
    '''    public String getIndentation(final StringBuffer stringBuffer)
    '''
def getEcoreModelElement():
    '''    public EModelElement getEcoreModelElement()
    '''
def getAllGenFeatures():
    '''    public List getAllGenFeatures()
    '''
def getFilteredAllGenFeatures():
    '''    public List getFilteredAllGenFeatures()
    '''
def setCodeFormatterOptions():
    '''    public void setCodeFormatterOptions(final Map options)
    '''
def createCodeFormatter():
    '''    public CodeFormatter createCodeFormatter()
    '''
def isBooleanFlagsEnabled():
    '''    public boolean isBooleanFlagsEnabled()
    '''
def createGenModel():
    '''    public GenModel createGenModel()
    '''
def createGenPackage():
    '''    public GenPackage createGenPackage()
    '''
def createGenClass():
    '''    public GenClass createGenClass()
    '''
def createGenFeature():
    '''    public GenFeature createGenFeature()
    '''
def createGenEnum():
    '''    public GenEnum createGenEnum()
    '''
def createGenEnumLiteral():
    '''    public GenEnumLiteral createGenEnumLiteral()
    '''
def createGenDataType():
    '''    public GenDataType createGenDataType()
    '''
def createGenOperation():
    '''    public GenOperation createGenOperation()
    '''
def createGenParameter():
    '''    public GenParameter createGenParameter()
    '''
def getPropertyCategories():
    '''    public Set getPropertyCategories()
    '''
def hasLocalGenModel():
    '''    public boolean hasLocalGenModel()
    '''
def getRelativeGenModelLocation():
    '''    public String getRelativeGenModelLocation()
    '''
def getPropertyCategoryKey():
    '''    public String getPropertyCategoryKey(final String category)
    '''
