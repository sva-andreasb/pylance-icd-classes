MESSAGE_SOURCE_BEAN_NAME = "String  \"messageSource\""
APPLICATION_EVENT_MULTICASTER_BEAN_NAME = "String  \"applicationEventMulticaster\""
def ():
    '''returns BeanPostProcessorChecker\n\n
    ()\n
    (final ApplicationContext parent)\n
    (final int beanPostProcessorTargetCount)\n
    '''
def getParent():
    '''returns ApplicationContext\n\n
    getParent()\n
    '''
def setDisplayName():
    '''returns None\n\n
    setDisplayName(final String displayName)\n
    '''
def getDisplayName():
    '''returns String\n\n
    getDisplayName()\n
    '''
def getStartupDate():
    '''returns long\n\n
    getStartupDate()\n
    '''
def publishEvent():
    '''returns None\n\n
    publishEvent(final ApplicationEvent event)\n
    '''
def setParent():
    '''returns None\n\n
    setParent(final ApplicationContext parent)\n
    '''
def addBeanFactoryPostProcessor():
    '''returns None\n\n
    addBeanFactoryPostProcessor(final BeanFactoryPostProcessor beanFactoryPostProcessor)\n
    '''
def getBeanFactoryPostProcessors():
    '''returns List\n\n
    getBeanFactoryPostProcessors()\n
    '''
def refresh():
    '''returns None\n\n
    refresh()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
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
def getParentBeanFactory():
    '''returns BeanFactory\n\n
    getParentBeanFactory()\n
    '''
def getMessage():
    '''returns String\n\n
    getMessage(final String code, final Object[] args, final String defaultMessage, final Locale locale)\n
    getMessage(final String code, final Object[] args, final Locale locale)\n
    getMessage(final MessageSourceResolvable resolvable, final Locale locale)\n
    '''
def getResources():
    '''returns Resource[]\n\n
    getResources(final String locationPattern)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def postProcessBeforeInitialization():
    '''returns Object\n\n
    postProcessBeforeInitialization(final Object bean, final String beanName)\n
    '''
def postProcessAfterInitialization():
    '''returns Object\n\n
    postProcessAfterInitialization(final Object bean, final String beanName)\n
    '''
