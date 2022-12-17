def ():
    '''returns StaticListableBeanFactory\n\n
    ()\n
    '''
def addBean():
    '''returns None\n\n
    addBean(final String name, final Object bean)\n
    '''
def getBean():
    '''returns Object\n\n
    getBean(final String name)\n
    getBean(final String name, final Class requiredType)\n
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
def containsBeanDefinition():
    '''returns boolean\n\n
    containsBeanDefinition(final String name)\n
    '''
def getBeanDefinitionCount():
    '''returns int\n\n
    getBeanDefinitionCount()\n
    '''
def getBeanDefinitionNames():
    '''returns String[]\n\n
    getBeanDefinitionNames()\n
    getBeanDefinitionNames(final Class type)\n
    '''
def getBeanNamesForType():
    '''returns String[]\n\n
    getBeanNamesForType(final Class type)\n
    getBeanNamesForType(final Class type, final boolean includePrototypes, final boolean includeFactoryBeans)\n
    '''
def getBeansOfType():
    '''returns Map\n\n
    getBeansOfType(final Class type)\n
    getBeansOfType(final Class type, final boolean includePrototypes, final boolean includeFactoryBeans)\n
    '''
