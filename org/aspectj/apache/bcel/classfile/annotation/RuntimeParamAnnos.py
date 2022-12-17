def ():
    '''returns RuntimeParamAnnos\n\n
    (final byte attrid, final boolean visible, final int nameIdx, final int len, final ConstantPool cpool)\n
    (final byte attrid, final boolean visible, final int nameIdx, final int len, final byte[] data, final ConstantPool cpool)\n
    '''
def copy():
    '''returns Attribute\n\n
    copy(final ConstantPool constant_pool)\n
    '''
def getParameterAnnotations():
    '''returns List<AnnotationGen[]>\n\n
    getParameterAnnotations()\n
    '''
def getAnnotationsOnParameter():
    '''returns AnnotationGen[]\n\n
    getAnnotationsOnParameter(final int parameterIndex)\n
    '''
def areVisible():
    '''returns boolean\n\n
    areVisible()\n
    '''
def isInflated():
    '''returns boolean\n\n
    isInflated()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
