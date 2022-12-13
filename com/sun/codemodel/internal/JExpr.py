def assign():
    '''public static JExpression assign(final JAssignmentTarget lhs, final JExpression rhs)
    '''
def assignPlus():
    '''public static JExpression assignPlus(final JAssignmentTarget lhs, final JExpression rhs)
    '''
def _new():
    '''public static JInvocation _new(final JClass c)
    public static JInvocation _new(final JType t)
    '''
def invoke():
    '''public static JInvocation invoke(final String method)
    public static JInvocation invoke(final JMethod method)
    public static JInvocation invoke(final JExpression lhs, final JMethod method)
    public static JInvocation invoke(final JExpression lhs, final String method)
    '''
def ref():
    '''public static JFieldRef ref(final String field)
    public static JFieldRef ref(final JExpression lhs, final JVar field)
    public static JFieldRef ref(final JExpression lhs, final String field)
    '''
def refthis():
    '''public static JFieldRef refthis(final String field)
    '''
def dotclass():
    '''public static JExpression dotclass(final JClass cl)
    '''
def generate():
    '''public void generate(final JFormatter f)
    public void generate(final JFormatter f)
    '''
def component():
    '''public static JArrayCompRef component(final JExpression lhs, final JExpression index)
    '''
def cast():
    '''public static JCast cast(final JType type, final JExpression expr)
    '''
def newArray():
    '''public static JArray newArray(final JType type)
    public static JArray newArray(final JType type, final JExpression size)
    public static JArray newArray(final JType type, final int size)
    '''
def _this():
    '''public static JExpression _this()
    '''
def _super():
    '''public static JExpression _super()
    '''
def _null():
    '''public static JExpression _null()
    '''
def lit():
    '''public static JExpression lit(final boolean b)
    public static JExpression lit(final int n)
    public static JExpression lit(final long n)
    public static JExpression lit(final float f)
    public static JExpression lit(final double d)
    public static JExpression lit(final char c)
    public static JExpression lit(final String s)
    '''
def quotify():
    '''public static String quotify(final char quote, final String s)
    '''
def direct():
    '''public static JExpression direct(final String source)
    '''
