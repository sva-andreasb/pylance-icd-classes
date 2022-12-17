def getAnnotationClass():
    '''returns JClass\n\n
    getAnnotationClass()\n
    '''
def param():
    '''returns JAnnotationUse\n\n
    param(final String name, final boolean value)\n
    param(final String name, final byte value)\n
    param(final String name, final char value)\n
    param(final String name, final double value)\n
    param(final String name, final float value)\n
    param(final String name, final long value)\n
    param(final String name, final short value)\n
    param(final String name, final int value)\n
    param(final String name, final String value)\n
    param(final String name, final Enum<?> value)\n
    param(final String name, final JEnumConstant value)\n
    param(final String name, final Class<?> value)\n
    param(final String name, final JType type)\n
    param(final String name, final JExpression value)\n
    '''
def annotationParam():
    '''returns JAnnotationUse\n\n
    annotationParam(final String name, final Class<? extends Annotation> value)\n
    '''
def generate():
    '''returns None\n\n
    generate(final JFormatter f)\n
    generate(final JFormatter f)\n
    generate(final JFormatter f)\n
    '''
def paramArray():
    '''returns JAnnotationArrayMember\n\n
    paramArray(final String name)\n
    '''
def annotate():
    '''returns JAnnotationUse\n\n
    annotate(final Class<? extends Annotation> clazz)\n
    '''
