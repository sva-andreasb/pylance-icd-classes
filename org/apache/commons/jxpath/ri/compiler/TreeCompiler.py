def number():
    '''    public Object number(final String value)
    '''
def literal():
    '''    public Object literal(final String value)
    '''
def qname():
    '''    public Object qname(final String prefix, final String name)
    '''
def sum():
    '''    public Object sum(final Object[] arguments)
    '''
def minus():
    '''    public Object minus(final Object left, final Object right)
    public Object minus(final Object argument)
    '''
def multiply():
    '''    public Object multiply(final Object left, final Object right)
    '''
def divide():
    '''    public Object divide(final Object left, final Object right)
    '''
def mod():
    '''    public Object mod(final Object left, final Object right)
    '''
def lessThan():
    '''    public Object lessThan(final Object left, final Object right)
    '''
def lessThanOrEqual():
    '''    public Object lessThanOrEqual(final Object left, final Object right)
    '''
def greaterThan():
    '''    public Object greaterThan(final Object left, final Object right)
    '''
def greaterThanOrEqual():
    '''    public Object greaterThanOrEqual(final Object left, final Object right)
    '''
def equal():
    '''    public Object equal(final Object left, final Object right)
    '''
def notEqual():
    '''    public Object notEqual(final Object left, final Object right)
    '''
def variableReference():
    '''    public Object variableReference(final Object qName)
    '''
def function():
    '''    public Object function(final int code, final Object[] args)
    public Object function(final Object name, final Object[] args)
    '''
def and():
    '''    public Object and(final Object[] arguments)
    '''
def or():
    '''    public Object or(final Object[] arguments)
    '''
def union():
    '''    public Object union(final Object[] arguments)
    '''
def locationPath():
    '''    public Object locationPath(final boolean absolute, final Object[] steps)
    '''
def expressionPath():
    '''    public Object expressionPath(final Object expression, final Object[] predicates, final Object[] steps)
    '''
def nodeNameTest():
    '''    public Object nodeNameTest(final Object qname)
    '''
def nodeTypeTest():
    '''    public Object nodeTypeTest(final int nodeType)
    '''
def processingInstructionTest():
    '''    public Object processingInstructionTest(final String instruction)
    '''
def step():
    '''    public Object step(final int axis, final Object nodeTest, final Object[] predicates)
    '''
