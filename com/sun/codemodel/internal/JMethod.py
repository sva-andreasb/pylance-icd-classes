def _throws():
    '''public JMethod _throws(final JClass exception)
    public JMethod _throws(final Class<? extends Throwable> exception)
    '''
def params():
    '''public List<JVar> params()
    '''
def param():
    '''public JVar param(final int mods, final JType type, final String name)
    public JVar param(final JType type, final String name)
    public JVar param(final int mods, final Class<?> type, final String name)
    public JVar param(final Class<?> type, final String name)
    '''
def varParam():
    '''public JVar varParam(final Class<?> type, final String name)
    public JVar varParam(final JType type, final String name)
    '''
def annotate():
    '''public JAnnotationUse annotate(final JClass clazz)
    public JAnnotationUse annotate(final Class<? extends Annotation> clazz)
    '''
def annotate2():
    '''public <W extends JAnnotationWriter> W annotate2(final Class<W> clazz)
    '''
def annotations():
    '''public Collection<JAnnotationUse> annotations()
    '''
def hasVarArgs():
    '''public boolean hasVarArgs()
    '''
def name():
    '''public String name()
    public void name(final String n)
    '''
def type():
    '''public JType type()
    public void type(final JType t)
    '''
def listParamTypes():
    '''public JType[] listParamTypes()
    '''
def listVarParamType():
    '''public JType listVarParamType()
    '''
def listParams():
    '''public JVar[] listParams()
    '''
def listVarParam():
    '''public JVar listVarParam()
    '''
def hasSignature():
    '''public boolean hasSignature(final JType[] argTypes)
    '''
def body():
    '''public JBlock body()
    '''
def declareDefaultValue():
    '''public void declareDefaultValue(final JExpression value)
    '''
def javadoc():
    '''public JDocComment javadoc()
    '''
def declare():
    '''public void declare(final JFormatter f)
    '''
def mods():
    '''public JMods mods()
    '''
def getMods():
    '''public JMods getMods()
    '''
