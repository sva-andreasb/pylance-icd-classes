def ():
    '''returns PropertyBasedObjectIdGenerator\n\n
    (final ObjectIdInfo oid, final BeanPropertyWriter prop)\n
    '''
def canUseFor():
    '''returns boolean\n\n
    canUseFor(final ObjectIdGenerator<?> gen)\n
    '''
def generateId():
    '''returns Object\n\n
    generateId(final Object forPojo)\n
    '''
def forScope():
    '''returns ObjectIdGenerator<Object>\n\n
    forScope(final Class<?> scope)\n
    '''
def newForSerialization():
    '''returns ObjectIdGenerator<Object>\n\n
    newForSerialization(final Object context)\n
    '''
