def createExpressionParser():
    '''    public static FMParser createExpressionParser(final String s)
    '''
def FMParser():
    '''    public FMParser(final Template template, final Reader reader, final boolean strictEscapeSyntax, final boolean stripWhitespace)
    public FMParser(final Template template, final Reader reader, final boolean strictEscapeSyntax, final boolean stripWhitespace, final int tagSyntax)
    public FMParser(final Template template, final Reader reader, final boolean strictEscapeSyntax, final boolean stripWhitespace, final int tagSyntax, final int incompatibleImprovements)
    public FMParser(final String template)
    public FMParser(final InputStream stream)
    public FMParser(final Reader stream)
    public FMParser(final FMParserTokenManager tm)
    '''
def _getLastTagSyntax():
    '''    public int _getLastTagSyntax()
    '''
def Expression():
    '''    public final Expression Expression()
    '''
def PrimaryExpression():
    '''    public final Expression PrimaryExpression()
    '''
def Parenthesis():
    '''    public final Expression Parenthesis()
    '''
def UnaryExpression():
    '''    public final Expression UnaryExpression()
    '''
def NotExpression():
    '''    public final Expression NotExpression()
    '''
def UnaryPlusMinusExpression():
    '''    public final Expression UnaryPlusMinusExpression()
    '''
def AdditiveExpression():
    '''    public final Expression AdditiveExpression()
    '''
def MultiplicativeExpression():
    '''    public final Expression MultiplicativeExpression()
    '''
def EqualityExpression():
    '''    public final Expression EqualityExpression()
    '''
def RelationalExpression():
    '''    public final Expression RelationalExpression()
    '''
def RangeExpression():
    '''    public final Expression RangeExpression()
    '''
def AndExpression():
    '''    public final Expression AndExpression()
    '''
def OrExpression():
    '''    public final Expression OrExpression()
    '''
def ListLiteral():
    '''    public final ListLiteral ListLiteral()
    '''
def NumberLiteral():
    '''    public final Expression NumberLiteral()
    '''
def Identifier():
    '''    public final Identifier Identifier()
    '''
def IdentifierOrStringLiteral():
    '''    public final Expression IdentifierOrStringLiteral()
    '''
def BuiltinVariable():
    '''    public final BuiltinVariable BuiltinVariable()
    '''
def AddSubExpression():
    '''    public final Expression AddSubExpression(final Expression exp)
    '''
def DefaultTo():
    '''    public final Expression DefaultTo(final Expression exp)
    '''
def Exists():
    '''    public final Expression Exists(final Expression exp)
    '''
def BuiltIn():
    '''    public final Expression BuiltIn(final Expression exp)
    '''
def DotVariable():
    '''    public final Expression DotVariable(final Expression exp)
    '''
def DynamicKey():
    '''    public final Expression DynamicKey(final Expression exp)
    '''
def MethodArgs():
    '''    public final MethodCall MethodArgs(final Expression exp)
    '''
def StringLiteral():
    '''    public final StringLiteral StringLiteral(final boolean interpolate)
    '''
def BooleanLiteral():
    '''    public final Expression BooleanLiteral()
    '''
def HashLiteral():
    '''    public final HashLiteral HashLiteral()
    '''
def StringOutput():
    '''    public final DollarVariable StringOutput()
    '''
def NumericalOutput():
    '''    public final NumericalOutput NumericalOutput()
    '''
def If():
    '''    public final TemplateElement If()
    '''
def Attempt():
    '''    public final AttemptBlock Attempt()
    '''
def Recover():
    '''    public final RecoveryBlock Recover()
    '''
def List():
    '''    public final IteratorBlock List()
    '''
def ForEach():
    '''    public final IteratorBlock ForEach()
    '''
def Visit():
    '''    public final VisitNode Visit()
    '''
def Recurse():
    '''    public final RecurseNode Recurse()
    '''
def FallBack():
    '''    public final FallbackInstruction FallBack()
    '''
def Break():
    '''    public final BreakInstruction Break()
    '''
def Return():
    '''    public final ReturnInstruction Return()
    '''
def Stop():
    '''    public final StopInstruction Stop()
    '''
def Nested():
    '''    public final TemplateElement Nested()
    '''
def Flush():
    '''    public final TemplateElement Flush()
    '''
def Trim():
    '''    public final TemplateElement Trim()
    '''
def Assign():
    '''    public final TemplateElement Assign()
    '''
def Include():
    '''    public final Include Include()
    '''
def Import():
    '''    public final LibraryLoad Import()
    '''
def Macro():
    '''    public final Macro Macro()
    '''
def Compress():
    '''    public final CompressedBlock Compress()
    '''
def UnifiedMacroTransform():
    '''    public final TemplateElement UnifiedMacroTransform()
    '''
def Call():
    '''    public final TemplateElement Call()
    '''
def NamedArgs():
    '''    public final HashMap NamedArgs()
    '''
def PositionalArgs():
    '''    public final ArrayList PositionalArgs()
    '''
def Comment():
    '''    public final Comment Comment()
    '''
def NoParse():
    '''    public final TextBlock NoParse()
    '''
def Transform():
    '''    public final TransformBlock Transform()
    '''
def Switch():
    '''    public final SwitchBlock Switch()
    '''
def Case():
    '''    public final Case Case()
    '''
def Escape():
    '''    public final EscapeBlock Escape()
    '''
def NoEscape():
    '''    public final NoEscapeBlock NoEscape()
    '''
def LooseDirectiveEnd():
    '''    public final Token LooseDirectiveEnd()
    '''
def Setting():
    '''    public final PropertySetting Setting()
    '''
def FreemarkerDirective():
    '''    public final TemplateElement FreemarkerDirective()
    '''
def PCData():
    '''    public final TextBlock PCData()
    '''
def UnparsedContent():
    '''    public final Token UnparsedContent(final Token start, final StringBuffer buf)
    '''
def MixedContent():
    '''    public final MixedContent MixedContent()
    '''
def FreeMarkerText():
    '''    public final TemplateElement FreeMarkerText()
    '''
def OptionalBlock():
    '''    public final TemplateElement OptionalBlock()
    '''
def HeaderElement():
    '''    public final void HeaderElement()
    '''
def ParamList():
    '''    public final Map ParamList()
    '''
def Root():
    '''    public final TemplateElement Root()
    '''
def ReInit():
    '''    public void ReInit(final InputStream stream)
    public void ReInit(final Reader stream)
    public void ReInit(final FMParserTokenManager tm)
    '''
def getNextToken():
    '''    public final Token getNextToken()
    '''
def getToken():
    '''    public final Token getToken(final int index)
    '''
def generateParseException():
    '''    public ParseException generateParseException()
    '''
def enable_tracing():
    '''    public final void enable_tracing()
    '''
def disable_tracing():
    '''    public final void disable_tracing()
    '''
