def outer():
'''public JClass outer()
'''
pass
def owner():
'''public final JCodeModel owner()
'''
pass
def typeParams():
'''public JTypeVar[] typeParams()
'''
pass
def getPrimitiveType():
'''public JPrimitiveType getPrimitiveType()
'''
pass
def boxify():
'''public JClass boxify()
'''
pass
def unboxify():
'''public JType unboxify()
'''
pass
def erasure():
'''public JClass erasure()
'''
pass
def isAssignableFrom():
'''public final boolean isAssignableFrom(final JClass derived)
'''
pass
def getBaseClass():
'''public final JClass getBaseClass(final JClass baseType)
public final JClass getBaseClass(final Class<?> baseType)
'''
pass
def array():
'''public JClass array()
'''
pass
def narrow():
'''public JClass narrow(final Class<?> clazz)
public JClass narrow(final Class<?>... clazz)
public JClass narrow(final JClass clazz)
public JClass narrow(final JType type)
public JClass narrow(final JClass... clazz)
public JClass narrow(final List<? extends JClass> clazz)
'''
pass
def getTypeParameters():
'''public List<JClass> getTypeParameters()
'''
pass
def isParameterized():
'''public final boolean isParameterized()
'''
pass
def wildcard():
'''public final JClass wildcard()
'''
pass
def toString():
'''public String toString()
'''
pass
def dotclass():
'''public final JExpression dotclass()
'''
pass
def staticInvoke():
'''public final JInvocation staticInvoke(final JMethod method)
public final JInvocation staticInvoke(final String method)
'''
pass
def staticRef():
'''public final JFieldRef staticRef(final String field)
public final JFieldRef staticRef(final JVar field)
'''
pass
def generate():
'''public void generate(final JFormatter f)
'''
pass
