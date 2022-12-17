TRUE_VALUE = "String  \"true\""
SEPARATOR = "String  \".\""
CLASS_KEY = "String  \"class\""
PARENT_KEY = "String  \"parent\""
ABSTRACT_KEY = "String  \"(abstract)\""
SINGLETON_KEY = "String  \"(singleton)\""
LAZY_INIT_KEY = "String  \"(lazy-init)\""
REF_SUFFIX = "String  \"(ref)\""
REF_PREFIX = "String  \"*\""
def ():
    '''returns PropertiesBeanDefinitionReader\n\n
    (final BeanDefinitionRegistry beanFactory)\n
    '''
def setDefaultParentBean():
    '''returns None\n\n
    setDefaultParentBean(final String defaultParentBean)\n
    '''
def getDefaultParentBean():
    '''returns String\n\n
    getDefaultParentBean()\n
    '''
def loadBeanDefinitions():
    '''returns int\n\n
    loadBeanDefinitions(final Resource resource)\n
    loadBeanDefinitions(final Resource resource, final String prefix)\n
    '''
def registerBeanDefinitions():
    '''returns int\n\n
    registerBeanDefinitions(final ResourceBundle rb)\n
    registerBeanDefinitions(final ResourceBundle rb, final String prefix)\n
    registerBeanDefinitions(final Map map)\n
    registerBeanDefinitions(final Map map, final String prefix)\n
    registerBeanDefinitions(final Map map, String prefix, final String resourceDescription)\n
    '''
