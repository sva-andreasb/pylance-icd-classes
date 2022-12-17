SYMBOL_RESOURCE = "String  \"symbolResource\""
SYMBOL_RESOURCE_PREFIX = "String  \"@|symbolResource(\""
VARIABLES_RULE_NAME = "String  \"VARIABLES\""
SUBOBJECT_TYPE = "String  \"Subobject\""
SYMBOL_METAINFO_TYPE = "String  \"MetaInfo\""
SYMBOL_PARAMETER_TYPE = "String  \"Parameter\""
CSS_ID = "String  \"__ID\""
CSS_TYPE = "String  \"__TYPE\""
CSS_LOCALE = "String  \"__Locale\""
CSS_COMPONENT_ORIENTATION = "String  \"__ComponentOrientation\""
OBJECT_PARAMETER = "String  \"CSS.Beans.Object\""
RULE_PARAMETER = "String  \"CSS.Beans.Rule\""
RULE_SELECTOR_PARAMETER = "String  \"CSS.Beans.RuleSelector\""
BEAN_PARAMETER = "String  \"CSS.Beans.Bean\""
PROPERTY_PARAMETER = "String  \"CSS.Beans.Property\""
CLASS_PARAMETER = "String  \"CSS.Beans.Class\""
VALUE_PARAMETER = "String  \"CSS.Beans.Value\""
RESULT_PARAMETER = "String  \"CSS.Beans.Result\""
EXCEPTION_PARAMETER = "String  \"CSS.Beans.Exception\""
MODEL_PROPERTY_PARAMETER = "String  \"CSS.Beans.ModelProperty\""
OBJECT_TYPE_PARAMETER = "String  \"CSS.Beans.ObjectType\""
ENGINE_PARAMETER = "String  \"CSS.Beans.CSSEngine\""
CONTEXT_UNDEFINED = "int  0"
CONTEXT_SYMBOL = "int  25"
def setBeanInfoFlags():
    '''returns None\n\n
    setBeanInfoFlags(final int beanInfoFlags)\n
    '''
def unsetBeanInfoFlags():
    '''returns None\n\n
    unsetBeanInfoFlags()\n
    '''
def getDebugMask():
    '''returns int\n\n
    getDebugMask()\n
    '''
def setDebugMask():
    '''returns None\n\n
    setDebugMask(final int styleSheetDebugMask)\n
    '''
def isClearExternalContext():
    '''returns boolean\n\n
    isClearExternalContext()\n
    '''
def setClearExternalContext():
    '''returns None\n\n
    setClearExternalContext(final boolean v)\n
    '''
def getAppliedDeclarationHook():
    '''returns AppliedDeclarationHook\n\n
    getAppliedDeclarationHook()\n
    '''
def setAppliedDeclarationHook():
    '''returns None\n\n
    setAppliedDeclarationHook(final AppliedDeclarationHook w)\n
    '''
def getInitPseudoClass():
    '''returns String\n\n
    getInitPseudoClass()\n
    '''
def setInitPseudoClass():
    '''returns None\n\n
    setInitPseudoClass(final String x)\n
    '''
def getFunctionClosure():
    '''returns Object\n\n
    getFunctionClosure()\n
    '''
def setFunctionClosure():
    '''returns None\n\n
    setFunctionClosure(final Object z)\n
    '''
def getCssClassPropertyName():
    '''returns String\n\n
    getCssClassPropertyName()\n
    '''
def setCssClassPropertyName():
    '''returns None\n\n
    setCssClassPropertyName(final String s)\n
    '''
def getExternalBeanClassLoaders():
    '''returns ClassLoader[]\n\n
    getExternalBeanClassLoaders()\n
    '''
def addExternalBeanClassLoader():
    '''returns None\n\n
    addExternalBeanClassLoader(final ClassLoader e)\n
    '''
def removeExternalBeanClassLoader():
    '''returns None\n\n
    removeExternalBeanClassLoader(final ClassLoader o)\n
    '''
def convertExternalCSSParameterDefaultFromString():
    '''returns Object\n\n
    convertExternalCSSParameterDefaultFromString(final String s, final String s2)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def isProcessingSymbol():
    '''returns boolean\n\n
    isProcessingSymbol()\n
    '''
def clearShared():
    '''returns boolean\n\n
    clearShared()\n
    clearShared(final String s)\n
    '''
def createBeanAndApplyDeclarations():
    '''returns Object\n\n
    createBeanAndApplyDeclarations(final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3, final boolean b, final String[] array)\n
    createBeanAndApplyDeclarations(final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3, final boolean b, final String[] array, final boolean b2, final Collection<String> collection)\n
    createBeanAndApplyDeclarations(final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3, final boolean b, final String[] array, final boolean b2, final Object[] array2, final Collection<String> collection)\n
    '''
def createBean():
    '''returns Object\n\n
    createBean(final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final String[] array)\n
    createBean(final IlvCSSModel ilvCSSModel, final Object o, final Object obj, final String[] array, final Collection<String> collection)\n
    createBean(final IlvCSSModel ilvCSSModel, final Object o, final boolean b, final IlvApplicableDeclarationCollection collection, final IlvApplicableDeclarationsStatus ilvApplicableDeclarationsStatus, final Collection<String> collection2)\n
    '''
def applyDeclarations():
    '''returns boolean\n\n
    applyDeclarations(final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final IlvApplicableDeclarationCollection collection, final IlvApplicableDeclarationsStatus ilvApplicableDeclarationsStatus, final Collection<String> collection2)\n
    applyDeclarations(final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final IlvApplicableDeclarationCollection collection, final String[] array, final IlvApplicableDeclarationsStatus ilvApplicableDeclarationsStatus, final Collection<String> collection2)\n
    '''
def createSingletonCSSModel():
    '''returns SingletonModel\n\n
    createSingletonCSSModel(final IlvCSSModel ilvCSSModel, final Object o, final String s)\n
    '''
def getDeclarationValue():
    '''returns Object\n\n
    getDeclarationValue(final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final String s, final int n, final String[] array, final Class clazz)\n
    '''
def getPropertyClass():
    '''returns Class\n\n
    getPropertyClass(final Class clazz, final String s)\n
    '''
def refreshVariables():
    '''returns None\n\n
    refreshVariables()\n
    '''
def getFunction():
    '''returns IlvCSSFunction\n\n
    getFunction(final String s)\n
    '''
def getDefaultFunctions():
    '''returns String[]\n\n
    getDefaultFunctions()\n
    '''
def getAllFunctions():
    '''returns IlvCSSFunction[]\n\n
    getAllFunctions()\n
    '''
def registerFunction():
    '''returns None\n\n
    registerFunction(final IlvCSSFunction value)\n
    '''
def unregisterFunction():
    '''returns None\n\n
    unregisterFunction(final IlvCSSFunction ilvCSSFunction)\n
    '''
def unregisterAllFunction():
    '''returns None\n\n
    unregisterAllFunction()\n
    '''
def setFunctionList():
    '''returns None\n\n
    setFunctionList(final String str)\n
    '''
def getFunctionList():
    '''returns String\n\n
    getFunctionList()\n
    '''
def computeAttributeNameValue():
    '''returns Object\n\n
    computeAttributeNameValue(final IlvCSSModel ilvCSSModel, final Object o, final String s)\n
    '''
def evaluateAttributeSelector():
    '''returns int\n\n
    evaluateAttributeSelector(final IlvCSSModel ilvCSSModel, final Object o, final AttributeSelector attributeSelector)\n
    '''
def usesModelAttributes():
    '''returns boolean\n\n
    usesModelAttributes(final Set<String> set, final AttributeSelector attributeSelector)\n
    usesModelAttributes(final Set<String> set)\n
    usesModelAttributes(final Rule rule, final Set<String> set)\n
    usesModelAttributes(final String s, final Set<String> set)\n
    '''
def collectUsedAttributeNames():
    '''returns None\n\n
    collectUsedAttributeNames(final AttributeSelector attributeSelector, final Set<String> set, final Set<String> set2)\n
    '''
def convertDeclarationsForEvaluation():
    '''returns IlvApplicableDeclarationCollection\n\n
    convertDeclarationsForEvaluation(final Map<String, String> map)\n
    '''
def ():
    '''returns EmptyString\n\n
    (final Reader reader, final URL url)\n
    (final Reader reader, final URL url, final URL[] array)\n
    (final IlvCSSEngine ilvCSSEngine)\n
    ()\n
    (final String message)\n
    ()\n
    ()\n
    ()\n
    (final IlvCSSModel ilvCSSModel, final Object refObject, final String node, final int debugMask)\n
    (final IlvCSSModel a, final Object b, final String c, final ExternalCSSContext d, final HashMap<String, IlvParameterValue> e, final Object f)\n
    (final Object o, final Rule[] array)\n
    (final Object o)\n
    (final String a, final String b)\n
    ()\n
    ()\n
    ()\n
    ()\n
    ()\n
    '''
def collectSubobjectIds():
    '''returns None\n\n
    collectSubobjectIds(final String s, final Set<String> set)\n
    '''
def rulesChanged():
    '''returns None\n\n
    rulesChanged(final RuleSetEvent ruleSetEvent)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getCompiledClassName():
    '''returns String\n\n
    getCompiledClassName()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    getName()\n
    getName()\n
    getName()\n
    getName()\n
    getName()\n
    getName()\n
    getName()\n
    getName()\n
    getName()\n
    getName()\n
    getName()\n
    getName()\n
    getName()\n
    getName()\n
    getName()\n
    getName()\n
    getName()\n
    getName()\n
    getName()\n
    getName()\n
    getName()\n
    getName()\n
    '''
def call():
    '''returns Object\n\n
    call(final Object[] array, final Class clazz, final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3)\n
    call(final Object[] array, final Class clazz, final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3)\n
    call(final Object[] array, final Class clazz, final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3)\n
    call(final Object[] array, final Class clazz, final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3)\n
    call(final Object[] array, final Class clazz, final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3)\n
    call(final Object[] array, final Class clazz, final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3)\n
    call(final Object[] array, final Class clazz, final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3)\n
    call(final Object[] array, final Class clazz, final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3)\n
    call(final Object[] array, final Class clazz, final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3)\n
    call(final Object[] array, final Class clazz, final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3)\n
    call(final Object[] array, final Class clazz, final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3)\n
    call(final Object[] array, final Class clazz, final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3)\n
    call(final Object[] array, final Class clazz, final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3)\n
    call(final Object[] array, final Class clazz, final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3)\n
    call(final Object[] array, final Class clazz, final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3)\n
    call(final Object[] array, final Class clazz, final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3)\n
    call(final Object[] array, final Class clazz, final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3)\n
    call(final Object[] array, final Class clazz, final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3)\n
    call(final Object[] array, final Class clazz, final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3)\n
    call(final Object[] array, final Class clazz, final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3)\n
    call(final Object[] array, final Class clazz, final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3)\n
    call(final Object[] array, final Class clazz, final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3)\n
    call(final Object[] array, final Class clazz, final IlvCSSModel ilvCSSModel, final Object o, final Object o2, final Object o3)\n
    '''
def getShortDescription():
    '''returns String\n\n
    getShortDescription()\n
    getShortDescription()\n
    getShortDescription()\n
    getShortDescription()\n
    getShortDescription()\n
    getShortDescription()\n
    getShortDescription()\n
    getShortDescription()\n
    getShortDescription()\n
    getShortDescription()\n
    getShortDescription()\n
    getShortDescription()\n
    getShortDescription()\n
    getShortDescription()\n
    getShortDescription()\n
    getShortDescription()\n
    getShortDescription()\n
    getShortDescription()\n
    getShortDescription()\n
    getShortDescription()\n
    getShortDescription()\n
    getShortDescription()\n
    getShortDescription()\n
    '''
def getDependencies():
    '''returns Collection<String>\n\n
    getDependencies(final String[] array)\n
    getDependencies(final String[] array)\n
    getDependencies(final String[] array)\n
    '''
def getRefModel():
    '''returns IlvCSSModel\n\n
    getRefModel()\n
    '''
def getRefObject():
    '''returns Object\n\n
    getRefObject()\n
    '''
def matchAndFindDeclarations():
    '''returns IlvApplicableDeclarationCollection\n\n
    matchAndFindDeclarations(final IlvCSSEngine ilvCSSEngine, final String[] array)\n
    '''
def getType():
    '''returns String\n\n
    getType(final Object o)\n
    getType(final Object o)\n
    '''
def getID():
    '''returns String\n\n
    getID(final Object o)\n
    getID(final Object o)\n
    '''
def getCSSclasses():
    '''returns String\n\n
    getCSSclasses(final Object o)\n
    getCSSclasses(final Object o)\n
    '''
def getValue():
    '''returns String\n\n
    getValue(final Object o, final String s)\n
    getValue(final Object o, final String s)\n
    '''
def getValueAsObject():
    '''returns Object\n\n
    getValueAsObject(final Object o, final String s)\n
    getValueAsObject(final Object o, final String s)\n
    '''
def getChildrenAsArray():
    '''returns Object[]\n\n
    getChildrenAsArray(final Object o)\n
    getChildrenAsArray(final Object o)\n
    '''
def getULocale():
    '''returns ULocale\n\n
    getULocale(final Object o)\n
    getULocale(final Object o)\n
    '''
def getComponentOrientation():
    '''returns ComponentOrientation\n\n
    getComponentOrientation(final Object o)\n
    getComponentOrientation(final Object o)\n
    '''
def setDeclarationContext():
    '''returns None\n\n
    setDeclarationContext(final boolean declarationContext)\n
    '''
def isDeclarationContext():
    '''returns boolean\n\n
    isDeclarationContext()\n
    '''
def cacheSymbolTopRule():
    '''returns None\n\n
    cacheSymbolTopRule(final String s, final IlvApplicableDeclarationCollection collection)\n
    '''
def getSymbolTopDeclarations():
    '''returns IlvApplicableDeclarationCollection\n\n
    getSymbolTopDeclarations(final String s)\n
    '''
def getRulesState():
    '''returns Object\n\n
    getRulesState()\n
    '''
def setSharedMap():
    '''returns None\n\n
    setSharedMap(final Map<String, Object> d)\n
    '''
def getPrototype():
    '''returns Object\n\n
    getPrototype()\n
    '''
def setPrototype():
    '''returns None\n\n
    setPrototype(final Object f)\n
    '''
def getClassName():
    '''returns String\n\n
    getClassName()\n
    '''
def getDefaultValue():
    '''returns Object\n\n
    getDefaultValue(final IlvCSSBeans ilvCSSBeans)\n
    '''
def getDelimiters():
    '''returns String\n\n
    getDelimiters()\n
    getDelimiters()\n
    getDelimiters()\n
    getDelimiters()\n
    '''
def newDef():
    '''returns None\n\n
    newDef()\n
    '''
def getImportance():
    '''returns float\n\n
    getImportance()\n
    getImportance()\n
    '''
def returnDelimitersAsToken():
    '''returns boolean\n\n
    returnDelimitersAsToken()\n
    returnDelimitersAsToken()\n
    '''
