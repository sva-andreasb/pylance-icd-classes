def createExpressionParser():
'''public static FMParser createExpressionParser(final String s)
'''
pass
def FMParser():
'''public FMParser(final Template template, final Reader reader, final boolean strictEscapeSyntax, final boolean stripWhitespace)
public FMParser(final Template template, final Reader reader, final boolean strictEscapeSyntax, final boolean stripWhitespace, final int tagSyntax)
public FMParser(final Template template, final Reader reader, final boolean strictEscapeSyntax, final boolean stripWhitespace, final int tagSyntax, final int incompatibleImprovements)
public FMParser(final String template)
public FMParser(final InputStream stream)
public FMParser(final Reader stream)
public FMParser(final FMParserTokenManager tm)
'''
pass
def _getLastTagSyntax():
'''public int _getLastTagSyntax()
'''
pass
def Expression():
'''public final Expression Expression()
'''
pass
def PrimaryExpression():
'''public final Expression PrimaryExpression()
'''
pass
def Parenthesis():
'''public final Expression Parenthesis()
'''
pass
def UnaryExpression():
'''public final Expression UnaryExpression()
'''
pass
def NotExpression():
'''public final Expression NotExpression()
'''
pass
def UnaryPlusMinusExpression():
'''public final Expression UnaryPlusMinusExpression()
'''
pass
def AdditiveExpression():
'''public final Expression AdditiveExpression()
'''
pass
def MultiplicativeExpression():
'''public final Expression MultiplicativeExpression()
'''
pass
def EqualityExpression():
'''public final Expression EqualityExpression()
'''
pass
def RelationalExpression():
'''public final Expression RelationalExpression()
'''
pass
def RangeExpression():
'''public final Expression RangeExpression()
'''
pass
def AndExpression():
'''public final Expression AndExpression()
'''
pass
def OrExpression():
'''public final Expression OrExpression()
'''
pass
def ListLiteral():
'''public final ListLiteral ListLiteral()
'''
pass
def NumberLiteral():
'''public final Expression NumberLiteral()
'''
pass
def Identifier():
'''public final Identifier Identifier()
'''
pass
def IdentifierOrStringLiteral():
'''public final Expression IdentifierOrStringLiteral()
'''
pass
def BuiltinVariable():
'''public final BuiltinVariable BuiltinVariable()
'''
pass
def AddSubExpression():
'''public final Expression AddSubExpression(final Expression exp)
'''
pass
def DefaultTo():
'''public final Expression DefaultTo(final Expression exp)
'''
pass
def Exists():
'''public final Expression Exists(final Expression exp)
'''
pass
def BuiltIn():
'''public final Expression BuiltIn(final Expression exp)
'''
pass
def DotVariable():
'''public final Expression DotVariable(final Expression exp)
'''
pass
def DynamicKey():
'''public final Expression DynamicKey(final Expression exp)
'''
pass
def MethodArgs():
'''public final MethodCall MethodArgs(final Expression exp)
'''
pass
def StringLiteral():
'''public final StringLiteral StringLiteral(final boolean interpolate)
'''
pass
def BooleanLiteral():
'''public final Expression BooleanLiteral()
'''
pass
def HashLiteral():
'''public final HashLiteral HashLiteral()
'''
pass
def StringOutput():
'''public final DollarVariable StringOutput()
'''
pass
def NumericalOutput():
'''public final NumericalOutput NumericalOutput()
'''
pass
def If():
'''public final TemplateElement If()
'''
pass
def Attempt():
'''public final AttemptBlock Attempt()
'''
pass
def Recover():
'''public final RecoveryBlock Recover()
'''
pass
def List():
'''public final IteratorBlock List()
'''
pass
def ForEach():
'''public final IteratorBlock ForEach()
'''
pass
def Visit():
'''public final VisitNode Visit()
'''
pass
def Recurse():
'''public final RecurseNode Recurse()
'''
pass
def FallBack():
'''public final FallbackInstruction FallBack()
'''
pass
def Break():
'''public final BreakInstruction Break()
'''
pass
def Return():
'''public final ReturnInstruction Return()
'''
pass
def Stop():
'''public final StopInstruction Stop()
'''
pass
def Nested():
'''public final TemplateElement Nested()
'''
pass
def Flush():
'''public final TemplateElement Flush()
'''
pass
def Trim():
'''public final TemplateElement Trim()
'''
pass
def Assign():
'''public final TemplateElement Assign()
'''
pass
def Include():
'''public final Include Include()
'''
pass
def Import():
'''public final LibraryLoad Import()
'''
pass
def Macro():
'''public final Macro Macro()
'''
pass
def Compress():
'''public final CompressedBlock Compress()
'''
pass
def UnifiedMacroTransform():
'''public final TemplateElement UnifiedMacroTransform()
'''
pass
def Call():
'''public final TemplateElement Call()
'''
pass
def NamedArgs():
'''public final HashMap NamedArgs()
'''
pass
def PositionalArgs():
'''public final ArrayList PositionalArgs()
'''
pass
def Comment():
'''public final Comment Comment()
'''
pass
def NoParse():
'''public final TextBlock NoParse()
'''
pass
def Transform():
'''public final TransformBlock Transform()
'''
pass
def Switch():
'''public final SwitchBlock Switch()
'''
pass
def Case():
'''public final Case Case()
'''
pass
def Escape():
'''public final EscapeBlock Escape()
'''
pass
def NoEscape():
'''public final NoEscapeBlock NoEscape()
'''
pass
def LooseDirectiveEnd():
'''public final Token LooseDirectiveEnd()
'''
pass
def Setting():
'''public final PropertySetting Setting()
'''
pass
def FreemarkerDirective():
'''public final TemplateElement FreemarkerDirective()
'''
pass
def PCData():
'''public final TextBlock PCData()
'''
pass
def UnparsedContent():
'''public final Token UnparsedContent(final Token start, final StringBuffer buf)
'''
pass
def MixedContent():
'''public final MixedContent MixedContent()
'''
pass
def FreeMarkerText():
'''public final TemplateElement FreeMarkerText()
'''
pass
def OptionalBlock():
'''public final TemplateElement OptionalBlock()
'''
pass
def HeaderElement():
'''public final void HeaderElement()
'''
pass
def ParamList():
'''public final Map ParamList()
'''
pass
def Root():
'''public final TemplateElement Root()
'''
pass
def ReInit():
'''public void ReInit(final InputStream stream)
public void ReInit(final Reader stream)
public void ReInit(final FMParserTokenManager tm)
'''
pass
def getNextToken():
'''public final Token getNextToken()
'''
pass
def getToken():
'''public final Token getToken(final int index)
'''
pass
def generateParseException():
'''public ParseException generateParseException()
'''
pass
def enable_tracing():
'''public final void enable_tracing()
'''
pass
def disable_tracing():
'''public final void disable_tracing()
'''
pass
