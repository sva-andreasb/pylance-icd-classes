def ():
    '''returns GenericApplicationContext\n\n
    ()\n
    (final DefaultListableBeanFactory beanFactory)\n
    (final ApplicationContext parent)\n
    (final DefaultListableBeanFactory beanFactory, final ApplicationContext parent)\n
    '''
def setParent():
    '''returns None\n\n
    setParent(final ApplicationContext parent)\n
    '''
def setResourceLoader():
    '''returns None\n\n
    setResourceLoader(final ResourceLoader resourceLoader)\n
    '''
def getResource():
    '''returns Resource\n\n
    getResource(final String location)\n
    '''
def getResources():
    '''returns Resource[]\n\n
    getResources(final String locationPattern)\n
    '''
def getBeanFactory():
    '''returns ConfigurableListableBeanFactory\n\n
    getBeanFactory()\n
    '''
def getDefaultListableBeanFactory():
    '''returns DefaultListableBeanFactory\n\n
    getDefaultListableBeanFactory()\n
    '''
def getBeanDefinition():
    '''returns BeanDefinition\n\n
    getBeanDefinition(final String beanName)\n
    '''
def registerBeanDefinition():
    '''returns None\n\n
    registerBeanDefinition(final String beanName, final BeanDefinition beanDefinition)\n
    '''
def registerAlias():
    '''returns None\n\n
    registerAlias(final String beanName, final String alias)\n
    '''
