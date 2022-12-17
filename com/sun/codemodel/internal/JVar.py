def init():
    '''returns JVar\n\n
    init(final JExpression init)\n
    '''
def name():
    '''returns None\n\n
    name()\n
    name(final String name)\n
    '''
def type():
    '''returns JType\n\n
    type()\n
    type(final JType newType)\n
    '''
def mods():
    '''returns JMods\n\n
    mods()\n
    '''
def annotate():
    '''returns JAnnotationUse\n\n
    annotate(final JClass clazz)\n
    annotate(final Class<? extends Annotation> clazz)\n
    '''
def annotations():
    '''returns Collection<JAnnotationUse>\n\n
    annotations()\n
    '''
def bind():
    '''returns None\n\n
    bind(final JFormatter f)\n
    '''
def declare():
    '''returns None\n\n
    declare(final JFormatter f)\n
    '''
def generate():
    '''returns None\n\n
    generate(final JFormatter f)\n
    '''
def assign():
    '''returns JExpression\n\n
    assign(final JExpression rhs)\n
    '''
def assignPlus():
    '''returns JExpression\n\n
    assignPlus(final JExpression rhs)\n
    '''
