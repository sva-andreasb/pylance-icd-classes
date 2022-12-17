AUTOWIRE_NO = "int  0"
AUTOWIRE_BY_NAME = "int  1"
AUTOWIRE_BY_TYPE = "int  2"
AUTOWIRE_CONSTRUCTOR = "int  3"
AUTOWIRE_AUTODETECT = "int  4"
DEPENDENCY_CHECK_NONE = "int  0"
DEPENDENCY_CHECK_OBJECTS = "int  1"
DEPENDENCY_CHECK_SIMPLE = "int  2"
DEPENDENCY_CHECK_ALL = "int  3"
def overrideFrom():
    '''returns None\n\n
    overrideFrom(final AbstractBeanDefinition other)\n
    '''
def hasBeanClass():
    '''returns boolean\n\n
    hasBeanClass()\n
    '''
def setBeanClass():
    '''returns None\n\n
    setBeanClass(final Class beanClass)\n
    '''
def getBeanClass():
    '''returns Class\n\n
    getBeanClass()\n
    '''
def setBeanClassName():
    '''returns None\n\n
    setBeanClassName(final String beanClassName)\n
    '''
def getBeanClassName():
    '''returns String\n\n
    getBeanClassName()\n
    '''
def setAbstract():
    '''returns None\n\n
    setAbstract(final boolean abstractFlag)\n
    '''
def isAbstract():
    '''returns boolean\n\n
    isAbstract()\n
    '''
def setSingleton():
    '''returns None\n\n
    setSingleton(final boolean singleton)\n
    '''
def isSingleton():
    '''returns boolean\n\n
    isSingleton()\n
    '''
def setLazyInit():
    '''returns None\n\n
    setLazyInit(final boolean lazyInit)\n
    '''
def isLazyInit():
    '''returns boolean\n\n
    isLazyInit()\n
    '''
def setConstructorArgumentValues():
    '''returns None\n\n
    setConstructorArgumentValues(final ConstructorArgumentValues constructorArgumentValues)\n
    '''
def getConstructorArgumentValues():
    '''returns ConstructorArgumentValues\n\n
    getConstructorArgumentValues()\n
    '''
def hasConstructorArgumentValues():
    '''returns boolean\n\n
    hasConstructorArgumentValues()\n
    '''
def setPropertyValues():
    '''returns None\n\n
    setPropertyValues(final MutablePropertyValues propertyValues)\n
    '''
def getPropertyValues():
    '''returns MutablePropertyValues\n\n
    getPropertyValues()\n
    '''
def setMethodOverrides():
    '''returns None\n\n
    setMethodOverrides(final MethodOverrides methodOverrides)\n
    '''
def getMethodOverrides():
    '''returns MethodOverrides\n\n
    getMethodOverrides()\n
    '''
def setInitMethodName():
    '''returns None\n\n
    setInitMethodName(final String initMethodName)\n
    '''
def getInitMethodName():
    '''returns String\n\n
    getInitMethodName()\n
    '''
def setDestroyMethodName():
    '''returns None\n\n
    setDestroyMethodName(final String destroyMethodName)\n
    '''
def getDestroyMethodName():
    '''returns String\n\n
    getDestroyMethodName()\n
    '''
def setFactoryMethodName():
    '''returns None\n\n
    setFactoryMethodName(final String factoryMethodName)\n
    '''
def getFactoryMethodName():
    '''returns String\n\n
    getFactoryMethodName()\n
    '''
def setFactoryBeanName():
    '''returns None\n\n
    setFactoryBeanName(final String factoryBeanName)\n
    '''
def getFactoryBeanName():
    '''returns String\n\n
    getFactoryBeanName()\n
    '''
def setAutowireMode():
    '''returns None\n\n
    setAutowireMode(final int autowireMode)\n
    '''
def getAutowireMode():
    '''returns int\n\n
    getAutowireMode()\n
    '''
def getResolvedAutowireMode():
    '''returns int\n\n
    getResolvedAutowireMode()\n
    '''
def setDependencyCheck():
    '''returns None\n\n
    setDependencyCheck(final int dependencyCheck)\n
    '''
def getDependencyCheck():
    '''returns int\n\n
    getDependencyCheck()\n
    '''
def setDependsOn():
    '''returns None\n\n
    setDependsOn(final String[] dependsOn)\n
    '''
def getDependsOn():
    '''returns String[]\n\n
    getDependsOn()\n
    '''
def setResourceDescription():
    '''returns None\n\n
    setResourceDescription(final String resourceDescription)\n
    '''
def getResourceDescription():
    '''returns String\n\n
    getResourceDescription()\n
    '''
def validate():
    '''returns None\n\n
    validate()\n
    '''
