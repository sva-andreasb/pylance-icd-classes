def ():
    '''returns AbstractBeanFactory\n\n
    ()\n
    (final BeanFactory parentBeanFactory)\n
    '''
def getBean():
    '''returns Object\n\n
    getBean(final String name)\n
    getBean(final String name, final Class requiredType)\n
    getBean(final String name, final Object[] args)\n
    getBean(final String name, final Class requiredType, final Object[] args)\n
    '''
def containsBean():
    '''returns boolean\n\n
    containsBean(final String name)\n
    '''
def isSingleton():
    '''returns boolean\n\n
    isSingleton(final String name)\n
    '''
def getType():
    '''returns Class\n\n
    getType(final String name)\n
    '''
def getAliases():
    '''returns String[]\n\n
    getAliases(final String name)\n
    '''
def getParentBeanFactory():
    '''returns BeanFactory\n\n
    getParentBeanFactory()\n
    '''
def setParentBeanFactory():
    '''returns None\n\n
    setParentBeanFactory(final BeanFactory parentBeanFactory)\n
    '''
def registerCustomEditor():
    '''returns None\n\n
    registerCustomEditor(final Class requiredType, final PropertyEditor propertyEditor)\n
    '''
def getCustomEditors():
    '''returns Map\n\n
    getCustomEditors()\n
    '''
def addBeanPostProcessor():
    '''returns None\n\n
    addBeanPostProcessor(final BeanPostProcessor beanPostProcessor)\n
    '''
def getBeanPostProcessorCount():
    '''returns int\n\n
    getBeanPostProcessorCount()\n
    '''
def getBeanPostProcessors():
    '''returns List\n\n
    getBeanPostProcessors()\n
    '''
def registerAlias():
    '''returns None\n\n
    registerAlias(final String beanName, final String alias)\n
    '''
def registerSingleton():
    '''returns None\n\n
    registerSingleton(final String beanName, final Object singletonObject)\n
    '''
def getSingletonCount():
    '''returns int\n\n
    getSingletonCount()\n
    '''
def getSingletonNames():
    '''returns String[]\n\n
    getSingletonNames()\n
    '''
def containsSingleton():
    '''returns boolean\n\n
    containsSingleton(final String beanName)\n
    '''
def destroySingletons():
    '''returns None\n\n
    destroySingletons()\n
    '''
def getMergedBeanDefinition():
    '''returns RootBeanDefinition\n\n
    getMergedBeanDefinition(final String beanName)\n
    '''
def isFactoryBean():
    '''returns boolean\n\n
    isFactoryBean(final String name)\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
