def init():
    '''public JVar init(final JExpression init)
    '''
def name():
    '''public String name()
    public void name(final String name)
    '''
def type():
    '''public JType type()
    public JType type(final JType newType)
    '''
def mods():
    '''public JMods mods()
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
def bind():
    '''public void bind(final JFormatter f)
    '''
def declare():
    '''public void declare(final JFormatter f)
    '''
def generate():
    '''public void generate(final JFormatter f)
    '''
def assign():
    '''public JExpression assign(final JExpression rhs)
    '''
def assignPlus():
    '''public JExpression assignPlus(final JExpression rhs)
    '''
