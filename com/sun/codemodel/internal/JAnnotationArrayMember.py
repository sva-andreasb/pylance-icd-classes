def param():
    '''returns JAnnotationArrayMember\n\n
    param(final String value)\n
    param(final boolean value)\n
    param(final byte value)\n
    param(final char value)\n
    param(final double value)\n
    param(final long value)\n
    param(final short value)\n
    param(final int value)\n
    param(final float value)\n
    param(final Enum<?> value)\n
    param(final JEnumConstant value)\n
    param(final JExpression value)\n
    param(final Class<?> value)\n
    param(final JType type)\n
    param(final JAnnotationUse value)\n
    '''
def generate():
    '''returns None\n\n
    generate(final JFormatter f)\n
    generate(final JFormatter f)\n
    generate(final JFormatter f)\n
    '''
def annotate():
    '''returns JAnnotationUse\n\n
    annotate(final Class<? extends Annotation> clazz)\n
    annotate(final JClass clazz)\n
    '''
def annotations():
    '''returns Collection<JAnnotationUse>\n\n
    annotations()\n
    '''
