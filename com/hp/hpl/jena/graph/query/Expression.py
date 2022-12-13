TRUE = "Expression  new BoolConstant(true)"
FALSE = "Expression  new BoolConstant(false)"
def isVariable():
'''public boolean isVariable()
public boolean isVariable()
'''
pass
def isApply():
'''public boolean isApply()
public boolean isApply()
'''
pass
def isConstant():
'''public boolean isConstant()
public boolean isConstant()
public boolean isConstant()
'''
pass
def getName():
'''public String getName()
'''
pass
def getValue():
'''public Object getValue()
public Object getValue()
public Object getValue()
'''
pass
def argCount():
'''public int argCount()
'''
pass
def getFun():
'''public String getFun()
'''
pass
def getArg():
'''public Expression getArg(final int i)
'''
pass
def equals():
'''public boolean equals(final Object other)
public static boolean equals(final Expression L, final Expression R)
'''
pass
def Fixed():
'''public Fixed(final Object value)
'''
pass
def prepare():
'''public Valuator prepare(final VariableIndexes vi)
public Valuator prepare(final VariableIndexes vi)
'''
pass
def toString():
'''public String toString()
'''
pass
def variablesOf():
'''public static Set<String> variablesOf(final Expression e)
'''
pass
def addVariablesOf():
'''public static Set<String> addVariablesOf(final Set<String> s, final Expression e)
'''
pass
def containsAllVariablesOf():
'''public static boolean containsAllVariablesOf(final Set<String> variables, final Expression e)
'''
pass
def sameApply():
'''public static boolean sameApply(final Expression L, final Expression R)
'''
pass
def sameArgs():
'''public static boolean sameArgs(final Expression L, final Expression R)
'''
pass
def Valof():
'''public Valof(final VariableIndexes map)
'''
pass
def get():
'''public final Object get(final String name)
'''
pass
def setDomain():
'''public final Valof setDomain(final IndexValues d)
'''
pass
def BoolConstant():
'''public BoolConstant(final boolean value)
'''
pass
def evalBool():
'''public boolean evalBool(final VariableValues vv)
public boolean evalBool(final IndexValues vv)
'''
pass
def evalObject():
'''public Object evalObject(final IndexValues iv)
'''
pass
