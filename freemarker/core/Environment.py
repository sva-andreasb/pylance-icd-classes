def getCurrentEnvironment():
'''public static Environment getCurrentEnvironment()
'''
pass
def Environment():
'''public Environment(final Template template, final TemplateHashModel rootDataModel, final Writer out)
'''
pass
def getTemplate():
'''public Template getTemplate()
public Template getTemplate()
'''
pass
def getMainTemplate():
'''public Template getMainTemplate()
'''
pass
def getCurrentDirectiveCallPlace():
'''public DirectiveCallPlace getCurrentDirectiveCallPlace()
'''
pass
def process():
'''public void process()
'''
pass
def visit():
'''public void visit(final TemplateElement element, final TemplateDirectiveModel directiveModel, final Map args, final List bodyParameterNames)
'''
pass
def getLocalVariable():
'''public TemplateModel getLocalVariable(final String name)
public TemplateModel getLocalVariable(final String name)
'''
pass
def getLocalVariableNames():
'''public Collection getLocalVariableNames()
'''
pass
def isInAttemptBlock():
'''public boolean isInAttemptBlock()
'''
pass
def setTemplateExceptionHandler():
'''public void setTemplateExceptionHandler(final TemplateExceptionHandler templateExceptionHandler)
'''
pass
def setLocale():
'''public void setLocale(final Locale locale)
'''
pass
def setTimeZone():
'''public void setTimeZone(final TimeZone timeZone)
'''
pass
def setSQLDateAndTimeTimeZone():
'''public void setSQLDateAndTimeTimeZone(final TimeZone timeZone)
'''
pass
def setURLEscapingCharset():
'''public void setURLEscapingCharset(final String urlEscapingCharset)
'''
pass
def setOutputEncoding():
'''public void setOutputEncoding(final String outputEncoding)
'''
pass
def applyEqualsOperator():
'''public boolean applyEqualsOperator(final TemplateModel leftValue, final TemplateModel rightValue)
'''
pass
def applyEqualsOperatorLenient():
'''public boolean applyEqualsOperatorLenient(final TemplateModel leftValue, final TemplateModel rightValue)
'''
pass
def applyLessThanOperator():
'''public boolean applyLessThanOperator(final TemplateModel leftValue, final TemplateModel rightValue)
'''
pass
def applyLessThanOrEqualsOperator():
'''public boolean applyLessThanOrEqualsOperator(final TemplateModel leftValue, final TemplateModel rightValue)
'''
pass
def applyGreaterThanOperator():
'''public boolean applyGreaterThanOperator(final TemplateModel leftValue, final TemplateModel rightValue)
'''
pass
def applyWithGreaterThanOrEqualsOperator():
'''public boolean applyWithGreaterThanOrEqualsOperator(final TemplateModel leftValue, final TemplateModel rightValue)
'''
pass
def setOut():
'''public void setOut(final Writer out)
'''
pass
def getOut():
'''public Writer getOut()
'''
pass
def setNumberFormat():
'''public void setNumberFormat(final String formatName)
'''
pass
def setTimeFormat():
'''public void setTimeFormat(final String timeFormat)
'''
pass
def setDateFormat():
'''public void setDateFormat(final String dateFormat)
'''
pass
def setDateTimeFormat():
'''public void setDateTimeFormat(final String dateTimeFormat)
'''
pass
def getConfiguration():
'''public Configuration getConfiguration()
'''
pass
def getCNumberFormat():
'''public NumberFormat getCNumberFormat()
'''
pass
def getVariable():
'''public TemplateModel getVariable(final String name)
'''
pass
def getGlobalVariable():
'''public TemplateModel getGlobalVariable(final String name)
'''
pass
def setGlobalVariable():
'''public void setGlobalVariable(final String name, final TemplateModel model)
'''
pass
def setVariable():
'''public void setVariable(final String name, final TemplateModel model)
'''
pass
def setLocalVariable():
'''public void setLocalVariable(final String name, final TemplateModel model)
'''
pass
def getKnownVariableNames():
'''public Set getKnownVariableNames()
'''
pass
def outputInstructionStack():
'''public void outputInstructionStack(final PrintWriter pw)
'''
pass
def getNamespace():
'''public Namespace getNamespace(String name)
'''
pass
def getMainNamespace():
'''public Namespace getMainNamespace()
'''
pass
def getCurrentNamespace():
'''public Namespace getCurrentNamespace()
'''
pass
def getGlobalNamespace():
'''public Namespace getGlobalNamespace()
'''
pass
def getDataModel():
'''public TemplateHashModel getDataModel()
'''
pass
def isEmpty():
'''public boolean isEmpty()
public boolean isEmpty()
public boolean isEmpty()
'''
pass
def get():
'''public TemplateModel get(final String key)
public TemplateModel get(final String key)
public TemplateModel get(final String key)
'''
pass
def values():
'''public TemplateCollectionModel values()
'''
pass
def keys():
'''public TemplateCollectionModel keys()
'''
pass
def size():
'''public int size()
'''
pass
def getGlobalVariables():
'''public TemplateHashModel getGlobalVariables()
'''
pass
def getCurrentVisitorNode():
'''public TemplateNodeModel getCurrentVisitorNode()
'''
pass
def setCurrentVisitorNode():
'''public void setCurrentVisitorNode(final TemplateNodeModel node)
'''
pass
def include():
'''public void include(final String name, final String encoding, final boolean parse)
public void include(final Template includedTemplate)
'''
pass
def getTemplateForInclusion():
'''public Template getTemplateForInclusion(final String name, final String encoding, final boolean parse)
public Template getTemplateForInclusion(final String name, String encoding, final boolean parseAsFTL, final boolean ignoreMissing)
'''
pass
def importLib():
'''public Namespace importLib(final String name, final String namespace)
public Namespace importLib(final Template loadedTemplate, final String namespace)
'''
pass
def getTemplateForImporting():
'''public Template getTemplateForImporting(final String name)
'''
pass
def toFullTemplateName():
'''public String toFullTemplateName(final String baseName, final String targetName)
'''
pass
def getNamespaceForPrefix():
'''public String getNamespaceForPrefix(final String prefix)
'''
pass
def getPrefixForNamespace():
'''public String getPrefixForNamespace(final String nsURI)
'''
pass
def getDefaultNS():
'''public String getDefaultNS()
'''
pass
def __getitem__():
'''public Object __getitem__(final String key)
'''
pass
def __setitem__():
'''public void __setitem__(final String key, final Object o)
'''
pass
def write():
'''public void write(final char[] cbuf, final int off, final int len)
'''
pass
def flush():
'''public void flush()
'''
pass
def close():
'''public void close()
'''
pass
def render():
'''public void render(final Writer newOut)
'''
pass
def getElement():
'''public TemplateElement getElement()
'''
pass
def equals():
'''public boolean equals(final Object o)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
