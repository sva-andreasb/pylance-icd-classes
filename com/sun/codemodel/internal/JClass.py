def outer():
    '''returns JClass\n\n
    outer()\n
    '''
def typeParams():
    '''returns JTypeVar[]\n\n
    typeParams()\n
    '''
def getPrimitiveType():
    '''returns JPrimitiveType\n\n
    getPrimitiveType()\n
    '''
def boxify():
    '''returns JClass\n\n
    boxify()\n
    '''
def unboxify():
    '''returns JType\n\n
    unboxify()\n
    '''
def erasure():
    '''returns JClass\n\n
    erasure()\n
    '''
def array():
    '''returns JClass\n\n
    array()\n
    '''
def narrow():
    '''returns JClass\n\n
    narrow(final Class<?> clazz)\n
    narrow(final Class<?>... clazz)\n
    narrow(final JClass clazz)\n
    narrow(final JType type)\n
    narrow(final JClass... clazz)\n
    narrow(final List<? extends JClass> clazz)\n
    '''
def getTypeParameters():
    '''returns List<JClass>\n\n
    getTypeParameters()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def generate():
    '''returns None\n\n
    generate(final JFormatter f)\n
    '''
