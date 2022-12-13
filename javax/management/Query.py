GT = "int  0"
LT = "int  1"
GE = "int  2"
LE = "int  3"
EQ = "int  4"
PLUS = "int  0"
MINUS = "int  1"
TIMES = "int  2"
DIV = "int  3"
def classattr():
'''public static AttributeValueExp classattr()
'''
pass
def value():
'''public static ValueExp value(final double value)
public static ValueExp value(final float n)
public static ValueExp value(final int n)
public static ValueExp value(final long value)
public static ValueExp value(final boolean b)
public static StringValueExp value(final String s)
public static ValueExp value(final Number n)
'''
pass
def attr():
'''public static AttributeValueExp attr(final String s)
public static AttributeValueExp attr(final String s, final String s2)
'''
pass
def not():
'''public static QueryExp not(final QueryExp queryExp)
'''
pass
def and():
'''public static QueryExp and(final QueryExp queryExp, final QueryExp queryExp2)
'''
pass
def or():
'''public static QueryExp or(final QueryExp queryExp, final QueryExp queryExp2)
'''
pass
def anySubString():
'''public static QueryExp anySubString(final AttributeValueExp attributeValueExp, final StringValueExp stringValueExp)
'''
pass
def finalSubString():
'''public static QueryExp finalSubString(final AttributeValueExp attributeValueExp, final StringValueExp stringValueExp)
'''
pass
def initialSubString():
'''public static QueryExp initialSubString(final AttributeValueExp attributeValueExp, final StringValueExp stringValueExp)
'''
pass
def match():
'''public static QueryExp match(final AttributeValueExp attributeValueExp, final StringValueExp stringValueExp)
'''
pass
def eq():
'''public static QueryExp eq(final ValueExp valueExp, final ValueExp valueExp2)
'''
pass
def geq():
'''public static QueryExp geq(final ValueExp valueExp, final ValueExp valueExp2)
'''
pass
def gt():
'''public static QueryExp gt(final ValueExp valueExp, final ValueExp valueExp2)
'''
pass
def leq():
'''public static QueryExp leq(final ValueExp valueExp, final ValueExp valueExp2)
'''
pass
def lt():
'''public static QueryExp lt(final ValueExp valueExp, final ValueExp valueExp2)
'''
pass
def in():
'''public static QueryExp in(final ValueExp valueExp, final ValueExp[] array)
'''
pass
def div():
'''public static ValueExp div(final ValueExp valueExp, final ValueExp valueExp2)
'''
pass
def minus():
'''public static ValueExp minus(final ValueExp valueExp, final ValueExp valueExp2)
'''
pass
def plus():
'''public static ValueExp plus(final ValueExp valueExp, final ValueExp valueExp2)
'''
pass
def times():
'''public static ValueExp times(final ValueExp valueExp, final ValueExp valueExp2)
'''
pass
def between():
'''public static QueryExp between(final ValueExp valueExp, final ValueExp valueExp2, final ValueExp valueExp3)
'''
pass
