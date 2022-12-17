def ():
    '''returns KafkaMbean\n\n
    ()\n
    (final String prefix)\n
    (final String mbeanName)\n
    '''
def configure():
    '''returns None\n\n
    configure(final Map<String, ?> configs)\n
    '''
def init():
    '''returns None\n\n
    init(final List<KafkaMetric> metrics)\n
    '''
def metricChange():
    '''returns None\n\n
    metricChange(final KafkaMetric metric)\n
    '''
def metricRemoval():
    '''returns None\n\n
    metricRemoval(final KafkaMetric metric)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def name():
    '''returns ObjectName\n\n
    name()\n
    '''
def setAttribute():
    '''returns None\n\n
    setAttribute(final String name, final KafkaMetric metric)\n
    setAttribute(final Attribute attribute)\n
    '''
def getAttribute():
    '''returns Object\n\n
    getAttribute(final String name)\n
    '''
def getAttributes():
    '''returns AttributeList\n\n
    getAttributes(final String[] names)\n
    '''
def removeAttribute():
    '''returns KafkaMetric\n\n
    removeAttribute(final String name)\n
    '''
def getMBeanInfo():
    '''returns MBeanInfo\n\n
    getMBeanInfo()\n
    '''
def invoke():
    '''returns Object\n\n
    invoke(final String name, final Object[] params, final String[] sig)\n
    '''
def setAttributes():
    '''returns AttributeList\n\n
    setAttributes(final AttributeList list)\n
    '''
