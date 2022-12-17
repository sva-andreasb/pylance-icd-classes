EXPOSE_ALL = "int  0"
EXPOSE_SAFE = "int  1"
EXPOSE_PROPERTIES_ONLY = "int  2"
EXPOSE_NOTHING = "int  3"
def ():
    '''returns BeansWrapper\n\n
    ()\n
    (final Version incompatibleImprovements)\n
    '''
def create():
    '''returns TemplateModel\n\n
    create(final Object object, final ObjectWrapper wrapper)\n
    create(final Object object, final ObjectWrapper wrapper)\n
    create(final Object object, final ObjectWrapper wrapper)\n
    '''
def process():
    '''returns None\n\n
    process(final MethodAppearanceDecisionInput in, final MethodAppearanceDecision out)\n
    '''
def writeProtect():
    '''returns None\n\n
    writeProtect()\n
    '''
def isWriteProtected():
    '''returns boolean\n\n
    isWriteProtected()\n
    '''
def isStrict():
    '''returns boolean\n\n
    isStrict()\n
    '''
def setStrict():
    '''returns None\n\n
    setStrict(final boolean strict)\n
    '''
def setOuterIdentity():
    '''returns None\n\n
    setOuterIdentity(final ObjectWrapper outerIdentity)\n
    '''
def getOuterIdentity():
    '''returns ObjectWrapper\n\n
    getOuterIdentity()\n
    '''
def setSimpleMapWrapper():
    '''returns None\n\n
    setSimpleMapWrapper(final boolean simpleMapWrapper)\n
    '''
def isSimpleMapWrapper():
    '''returns boolean\n\n
    isSimpleMapWrapper()\n
    '''
def setExposureLevel():
    '''returns None\n\n
    setExposureLevel(final int exposureLevel)\n
    '''
def getExposureLevel():
    '''returns int\n\n
    getExposureLevel()\n
    '''
def setExposeFields():
    '''returns None\n\n
    setExposeFields(final boolean exposeFields)\n
    '''
def isExposeFields():
    '''returns boolean\n\n
    isExposeFields()\n
    '''
def getMethodAppearanceFineTuner():
    '''returns MethodAppearanceFineTuner\n\n
    getMethodAppearanceFineTuner()\n
    '''
def setMethodAppearanceFineTuner():
    '''returns None\n\n
    setMethodAppearanceFineTuner(final MethodAppearanceFineTuner methodAppearanceFineTuner)\n
    '''
def isClassIntrospectionCacheRestricted():
    '''returns boolean\n\n
    isClassIntrospectionCacheRestricted()\n
    '''
def setMethodsShadowItems():
    '''returns None\n\n
    setMethodsShadowItems(final boolean methodsShadowItems)\n
    '''
def setDefaultDateType():
    '''returns None\n\n
    setDefaultDateType(final int defaultDateType)\n
    '''
def getDefaultDateType():
    '''returns int\n\n
    getDefaultDateType()\n
    '''
def setUseCache():
    '''returns None\n\n
    setUseCache(final boolean useCache)\n
    '''
def getUseCache():
    '''returns boolean\n\n
    getUseCache()\n
    '''
def setNullModel():
    '''returns None\n\n
    setNullModel(final TemplateModel nullModel)\n
    '''
def getIncompatibleImprovements():
    '''returns Version\n\n
    getIncompatibleImprovements()\n
    '''
def wrap():
    '''returns TemplateMethodModelEx\n\n
    wrap(final Object object)\n
    wrap(final Object object, final Method method)\n
    '''
def wrapAsAPI():
    '''returns TemplateHashModel\n\n
    wrapAsAPI(final Object obj)\n
    '''
def unwrap():
    '''returns Object\n\n
    unwrap(final TemplateModel model)\n
    unwrap(final TemplateModel model, final Class targetClass)\n
    '''
def tryUnwrapTo():
    '''returns Object\n\n
    tryUnwrapTo(final TemplateModel model, final Class targetClass)\n
    '''
def getStaticModels():
    '''returns TemplateHashModel\n\n
    getStaticModels()\n
    '''
def getEnumModels():
    '''returns TemplateHashModel\n\n
    getEnumModels()\n
    '''
def newInstance():
    '''returns Object\n\n
    newInstance(final Class clazz, final List arguments)\n
    '''
def removeFromClassIntrospectionCache():
    '''returns None\n\n
    removeFromClassIntrospectionCache(final Class clazz)\n
    '''
def clearClassIntrospecitonCache():
    '''returns None\n\n
    clearClassIntrospecitonCache()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getExposeAsProperty():
    '''returns PropertyDescriptor\n\n
    getExposeAsProperty()\n
    '''
def setExposeAsProperty():
    '''returns None\n\n
    setExposeAsProperty(final PropertyDescriptor exposeAsProperty)\n
    '''
def getExposeMethodAs():
    '''returns String\n\n
    getExposeMethodAs()\n
    '''
def setExposeMethodAs():
    '''returns None\n\n
    setExposeMethodAs(final String exposeAsMethod)\n
    '''
def getMethodShadowsProperty():
    '''returns boolean\n\n
    getMethodShadowsProperty()\n
    '''
def setMethodShadowsProperty():
    '''returns None\n\n
    setMethodShadowsProperty(final boolean shadowEarlierProperty)\n
    '''
def getMethod():
    '''returns Method\n\n
    getMethod()\n
    '''
def getContainingClass():
    '''returns Class\n\n
    getContainingClass()\n
    '''
