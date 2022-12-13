def outer():
    '''public JClass outer()
    '''
def owner():
    '''public final JCodeModel owner()
    '''
def typeParams():
    '''public JTypeVar[] typeParams()
    '''
def getPrimitiveType():
    '''public JPrimitiveType getPrimitiveType()
    '''
def boxify():
    '''public JClass boxify()
    '''
def unboxify():
    '''public JType unboxify()
    '''
def erasure():
    '''public JClass erasure()
    '''
def isAssignableFrom():
    '''public final boolean isAssignableFrom(final JClass derived)
    '''
def getBaseClass():
    '''public final JClass getBaseClass(final JClass baseType)
    public final JClass getBaseClass(final Class<?> baseType)
    '''
def array():
    '''public JClass array()
    '''
def narrow():
    '''public JClass narrow(final Class<?> clazz)
    public JClass narrow(final Class<?>... clazz)
    public JClass narrow(final JClass clazz)
    public JClass narrow(final JType type)
    public JClass narrow(final JClass... clazz)
    public JClass narrow(final List<? extends JClass> clazz)
    '''
def getTypeParameters():
    '''public List<JClass> getTypeParameters()
    '''
def isParameterized():
    '''public final boolean isParameterized()
    '''
def wildcard():
    '''public final JClass wildcard()
    '''
def toString():
    '''public String toString()
    '''
def dotclass():
    '''public final JExpression dotclass()
    '''
def staticInvoke():
    '''public final JInvocation staticInvoke(final JMethod method)
    public final JInvocation staticInvoke(final String method)
    '''
def staticRef():
    '''public final JFieldRef staticRef(final String field)
    public final JFieldRef staticRef(final JVar field)
    '''
def generate():
    '''public void generate(final JFormatter f)
    '''
