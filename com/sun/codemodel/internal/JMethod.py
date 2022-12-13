def _throws():
'''public JMethod _throws(final JClass exception)
public JMethod _throws(final Class<? extends Throwable> exception)
'''
pass
def params():
'''public List<JVar> params()
'''
pass
def param():
'''public JVar param(final int mods, final JType type, final String name)
public JVar param(final JType type, final String name)
public JVar param(final int mods, final Class<?> type, final String name)
public JVar param(final Class<?> type, final String name)
'''
pass
def varParam():
'''public JVar varParam(final Class<?> type, final String name)
public JVar varParam(final JType type, final String name)
'''
pass
def annotate():
'''public JAnnotationUse annotate(final JClass clazz)
public JAnnotationUse annotate(final Class<? extends Annotation> clazz)
'''
pass
def annotate2():
'''public <W extends JAnnotationWriter> W annotate2(final Class<W> clazz)
'''
pass
def annotations():
'''public Collection<JAnnotationUse> annotations()
'''
pass
def hasVarArgs():
'''public boolean hasVarArgs()
'''
pass
def name():
'''public String name()
public void name(final String n)
'''
pass
def type():
'''public JType type()
public void type(final JType t)
'''
pass
def listParamTypes():
'''public JType[] listParamTypes()
'''
pass
def listVarParamType():
'''public JType listVarParamType()
'''
pass
def listParams():
'''public JVar[] listParams()
'''
pass
def listVarParam():
'''public JVar listVarParam()
'''
pass
def hasSignature():
'''public boolean hasSignature(final JType[] argTypes)
'''
pass
def body():
'''public JBlock body()
'''
pass
def declareDefaultValue():
'''public void declareDefaultValue(final JExpression value)
'''
pass
def javadoc():
'''public JDocComment javadoc()
'''
pass
def declare():
'''public void declare(final JFormatter f)
'''
pass
def mods():
'''public JMods mods()
'''
pass
def getMods():
'''public JMods getMods()
'''
pass
