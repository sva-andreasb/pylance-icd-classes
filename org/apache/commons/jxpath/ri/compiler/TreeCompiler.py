def number():
'''public Object number(final String value)
'''
pass
def literal():
'''public Object literal(final String value)
'''
pass
def qname():
'''public Object qname(final String prefix, final String name)
'''
pass
def sum():
'''public Object sum(final Object[] arguments)
'''
pass
def minus():
'''public Object minus(final Object left, final Object right)
public Object minus(final Object argument)
'''
pass
def multiply():
'''public Object multiply(final Object left, final Object right)
'''
pass
def divide():
'''public Object divide(final Object left, final Object right)
'''
pass
def mod():
'''public Object mod(final Object left, final Object right)
'''
pass
def lessThan():
'''public Object lessThan(final Object left, final Object right)
'''
pass
def lessThanOrEqual():
'''public Object lessThanOrEqual(final Object left, final Object right)
'''
pass
def greaterThan():
'''public Object greaterThan(final Object left, final Object right)
'''
pass
def greaterThanOrEqual():
'''public Object greaterThanOrEqual(final Object left, final Object right)
'''
pass
def equal():
'''public Object equal(final Object left, final Object right)
'''
pass
def notEqual():
'''public Object notEqual(final Object left, final Object right)
'''
pass
def variableReference():
'''public Object variableReference(final Object qName)
'''
pass
def function():
'''public Object function(final int code, final Object[] args)
public Object function(final Object name, final Object[] args)
'''
pass
def and():
'''public Object and(final Object[] arguments)
'''
pass
def or():
'''public Object or(final Object[] arguments)
'''
pass
def union():
'''public Object union(final Object[] arguments)
'''
pass
def locationPath():
'''public Object locationPath(final boolean absolute, final Object[] steps)
'''
pass
def expressionPath():
'''public Object expressionPath(final Object expression, final Object[] predicates, final Object[] steps)
'''
pass
def nodeNameTest():
'''public Object nodeNameTest(final Object qname)
'''
pass
def nodeTypeTest():
'''public Object nodeTypeTest(final int nodeType)
'''
pass
def processingInstructionTest():
'''public Object processingInstructionTest(final String instruction)
'''
pass
def step():
'''public Object step(final int axis, final Object nodeTest, final Object[] predicates)
'''
pass
