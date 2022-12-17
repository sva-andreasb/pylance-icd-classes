def ():
    '''returns ArgumentsHolder\n\n
    ()\n
    (final BeanFactory parentBeanFactory)\n
    (final int size)\n
    (final Object[] args)\n
    '''
def setInstantiationStrategy():
    '''returns None\n\n
    setInstantiationStrategy(final InstantiationStrategy instantiationStrategy)\n
    '''
def ignoreDependencyType():
    '''returns None\n\n
    ignoreDependencyType(final Class type)\n
    '''
def getIgnoredDependencyTypes():
    '''returns Set\n\n
    getIgnoredDependencyTypes()\n
    '''
def ignoreDependencyInterface():
    '''returns None\n\n
    ignoreDependencyInterface(final Class ifc)\n
    '''
def getIgnoredDependencyInterfaces():
    '''returns Set\n\n
    getIgnoredDependencyInterfaces()\n
    '''
def autowire():
    '''returns Object\n\n
    autowire(final Class beanClass, final int autowireMode, final boolean dependencyCheck)\n
    '''
def autowireBeanProperties():
    '''returns None\n\n
    autowireBeanProperties(final Object existingBean, final int autowireMode, final boolean dependencyCheck)\n
    '''
def applyBeanPropertyValues():
    '''returns None\n\n
    applyBeanPropertyValues(final Object existingBean, final String beanName)\n
    '''
def applyBeanPostProcessorsBeforeInitialization():
    '''returns Object\n\n
    applyBeanPostProcessorsBeforeInitialization(final Object existingBean, final String beanName)\n
    '''
def applyBeanPostProcessorsAfterInitialization():
    '''returns Object\n\n
    applyBeanPostProcessorsAfterInitialization(final Object existingBean, final String beanName)\n
    '''
def getTypeDifferenceWeight():
    '''returns int\n\n
    getTypeDifferenceWeight(final Class[] argTypes)\n
    '''
