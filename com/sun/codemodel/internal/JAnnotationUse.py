def getAnnotationClass():
    '''public JClass getAnnotationClass()
    '''
def getAnnotationMembers():
    '''public Map<String, JAnnotationValue> getAnnotationMembers()
    '''
def param():
    '''public JAnnotationUse param(final String name, final boolean value)
    public JAnnotationUse param(final String name, final byte value)
    public JAnnotationUse param(final String name, final char value)
    public JAnnotationUse param(final String name, final double value)
    public JAnnotationUse param(final String name, final float value)
    public JAnnotationUse param(final String name, final long value)
    public JAnnotationUse param(final String name, final short value)
    public JAnnotationUse param(final String name, final int value)
    public JAnnotationUse param(final String name, final String value)
    public JAnnotationUse param(final String name, final Enum<?> value)
    public JAnnotationUse param(final String name, final JEnumConstant value)
    public JAnnotationUse param(final String name, final Class<?> value)
    public JAnnotationUse param(final String name, final JType type)
    public JAnnotationUse param(final String name, final JExpression value)
    '''
def annotationParam():
    '''public JAnnotationUse annotationParam(final String name, final Class<? extends Annotation> value)
    '''
def generate():
    '''public void generate(final JFormatter f)
    public void generate(final JFormatter f)
    public void generate(final JFormatter f)
    '''
def paramArray():
    '''public JAnnotationArrayMember paramArray(final String name)
    '''
def annotate():
    '''public JAnnotationUse annotate(final Class<? extends Annotation> clazz)
    '''
