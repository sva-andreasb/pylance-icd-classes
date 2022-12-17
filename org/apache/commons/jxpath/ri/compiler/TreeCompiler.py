def number():
    '''returns Object\n\n
    number(final String value)\n
    '''
def literal():
    '''returns Object\n\n
    literal(final String value)\n
    '''
def qname():
    '''returns Object\n\n
    qname(final String prefix, final String name)\n
    '''
def sum():
    '''returns Object\n\n
    sum(final Object[] arguments)\n
    '''
def minus():
    '''returns Object\n\n
    minus(final Object left, final Object right)\n
    minus(final Object argument)\n
    '''
def multiply():
    '''returns Object\n\n
    multiply(final Object left, final Object right)\n
    '''
def divide():
    '''returns Object\n\n
    divide(final Object left, final Object right)\n
    '''
def mod():
    '''returns Object\n\n
    mod(final Object left, final Object right)\n
    '''
def lessThan():
    '''returns Object\n\n
    lessThan(final Object left, final Object right)\n
    '''
def lessThanOrEqual():
    '''returns Object\n\n
    lessThanOrEqual(final Object left, final Object right)\n
    '''
def greaterThan():
    '''returns Object\n\n
    greaterThan(final Object left, final Object right)\n
    '''
def greaterThanOrEqual():
    '''returns Object\n\n
    greaterThanOrEqual(final Object left, final Object right)\n
    '''
def equal():
    '''returns Object\n\n
    equal(final Object left, final Object right)\n
    '''
def notEqual():
    '''returns Object\n\n
    notEqual(final Object left, final Object right)\n
    '''
def variableReference():
    '''returns Object\n\n
    variableReference(final Object qName)\n
    '''
def function():
    '''returns Object\n\n
    function(final int code, final Object[] args)\n
    function(final Object name, final Object[] args)\n
    '''
def and():
    '''returns Object\n\n
    and(final Object[] arguments)\n
    '''
def or():
    '''returns Object\n\n
    or(final Object[] arguments)\n
    '''
def union():
    '''returns Object\n\n
    union(final Object[] arguments)\n
    '''
def locationPath():
    '''returns Object\n\n
    locationPath(final boolean absolute, final Object[] steps)\n
    '''
def expressionPath():
    '''returns Object\n\n
    expressionPath(final Object expression, final Object[] predicates, final Object[] steps)\n
    '''
def nodeNameTest():
    '''returns Object\n\n
    nodeNameTest(final Object qname)\n
    '''
def nodeTypeTest():
    '''returns Object\n\n
    nodeTypeTest(final int nodeType)\n
    '''
def processingInstructionTest():
    '''returns Object\n\n
    processingInstructionTest(final String instruction)\n
    '''
def step():
    '''returns Object\n\n
    step(final int axis, final Object nodeTest, final Object[] predicates)\n
    '''
