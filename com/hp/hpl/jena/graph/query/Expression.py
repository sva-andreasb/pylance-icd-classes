TRUE = "Expression  new BoolConstant(true)"
FALSE = "Expression  new BoolConstant(false)"
def isVariable():
    '''    public boolean isVariable()
    public boolean isVariable()
    '''
def isApply():
    '''    public boolean isApply()
    public boolean isApply()
    '''
def isConstant():
    '''    public boolean isConstant()
    public boolean isConstant()
    public boolean isConstant()
    '''
def getName():
    '''    public String getName()
    '''
def getValue():
    '''    public Object getValue()
    public Object getValue()
    public Object getValue()
    '''
def argCount():
    '''    public int argCount()
    '''
def getFun():
    '''    public String getFun()
    '''
def getArg():
    '''    public Expression getArg(final int i)
    '''
def equals():
    '''    public boolean equals(final Object other)
    public static boolean equals(final Expression L, final Expression R)
    '''
def Fixed():
    '''    public Fixed(final Object value)
    '''
def prepare():
    '''    public Valuator prepare(final VariableIndexes vi)
    public Valuator prepare(final VariableIndexes vi)
    '''
def toString():
    '''    public String toString()
    '''
def variablesOf():
    '''    public static Set<String> variablesOf(final Expression e)
    '''
def addVariablesOf():
    '''    public static Set<String> addVariablesOf(final Set<String> s, final Expression e)
    '''
def containsAllVariablesOf():
    '''    public static boolean containsAllVariablesOf(final Set<String> variables, final Expression e)
    '''
def sameApply():
    '''    public static boolean sameApply(final Expression L, final Expression R)
    '''
def sameArgs():
    '''    public static boolean sameArgs(final Expression L, final Expression R)
    '''
def Valof():
    '''    public Valof(final VariableIndexes map)
    '''
def get():
    '''    public final Object get(final String name)
    '''
def setDomain():
    '''    public final Valof setDomain(final IndexValues d)
    '''
def BoolConstant():
    '''    public BoolConstant(final boolean value)
    '''
def evalBool():
    '''    public boolean evalBool(final VariableValues vv)
    public boolean evalBool(final IndexValues vv)
    '''
def evalObject():
    '''    public Object evalObject(final IndexValues iv)
    '''
