def ():
    '''returns DefaultListableBeanFactory\n\n
    ()\n
    (final BeanFactory parentBeanFactory)\n
    '''
def setAllowBeanDefinitionOverriding():
    '''returns None\n\n
    setAllowBeanDefinitionOverriding(final boolean allowBeanDefinitionOverriding)\n
    '''
def containsBeanDefinition():
    '''returns boolean\n\n
    containsBeanDefinition(final String beanName)\n
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
def preInstantiateSingletons():
    '''returns None\n\n
    preInstantiateSingletons()\n
    '''
def registerBeanDefinition():
    '''returns None\n\n
    registerBeanDefinition(final String beanName, final BeanDefinition beanDefinition)\n
    '''
def getBeanDefinition():
    '''returns BeanDefinition\n\n
    getBeanDefinition(final String beanName)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
