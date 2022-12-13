def getCurrentEnvironment():
    '''    public static Environment getCurrentEnvironment()
    '''
def Environment():
    '''    public Environment(final Template template, final TemplateHashModel rootDataModel, final Writer out)
    '''
def getTemplate():
    '''    public Template getTemplate()
    public Template getTemplate()
    '''
def getMainTemplate():
    '''    public Template getMainTemplate()
    '''
def getCurrentDirectiveCallPlace():
    '''    public DirectiveCallPlace getCurrentDirectiveCallPlace()
    '''
def process():
    '''    public void process()
    '''
def visit():
    '''    public void visit(final TemplateElement element, final TemplateDirectiveModel directiveModel, final Map args, final List bodyParameterNames)
    '''
def getLocalVariable():
    '''    public TemplateModel getLocalVariable(final String name)
    public TemplateModel getLocalVariable(final String name)
    '''
def getLocalVariableNames():
    '''    public Collection getLocalVariableNames()
    '''
def isInAttemptBlock():
    '''    public boolean isInAttemptBlock()
    '''
def setTemplateExceptionHandler():
    '''    public void setTemplateExceptionHandler(final TemplateExceptionHandler templateExceptionHandler)
    '''
def setLocale():
    '''    public void setLocale(final Locale locale)
    '''
def setTimeZone():
    '''    public void setTimeZone(final TimeZone timeZone)
    '''
def setSQLDateAndTimeTimeZone():
    '''    public void setSQLDateAndTimeTimeZone(final TimeZone timeZone)
    '''
def setURLEscapingCharset():
    '''    public void setURLEscapingCharset(final String urlEscapingCharset)
    '''
def setOutputEncoding():
    '''    public void setOutputEncoding(final String outputEncoding)
    '''
def applyEqualsOperator():
    '''    public boolean applyEqualsOperator(final TemplateModel leftValue, final TemplateModel rightValue)
    '''
def applyEqualsOperatorLenient():
    '''    public boolean applyEqualsOperatorLenient(final TemplateModel leftValue, final TemplateModel rightValue)
    '''
def applyLessThanOperator():
    '''    public boolean applyLessThanOperator(final TemplateModel leftValue, final TemplateModel rightValue)
    '''
def applyLessThanOrEqualsOperator():
    '''    public boolean applyLessThanOrEqualsOperator(final TemplateModel leftValue, final TemplateModel rightValue)
    '''
def applyGreaterThanOperator():
    '''    public boolean applyGreaterThanOperator(final TemplateModel leftValue, final TemplateModel rightValue)
    '''
def applyWithGreaterThanOrEqualsOperator():
    '''    public boolean applyWithGreaterThanOrEqualsOperator(final TemplateModel leftValue, final TemplateModel rightValue)
    '''
def setOut():
    '''    public void setOut(final Writer out)
    '''
def getOut():
    '''    public Writer getOut()
    '''
def setNumberFormat():
    '''    public void setNumberFormat(final String formatName)
    '''
def setTimeFormat():
    '''    public void setTimeFormat(final String timeFormat)
    '''
def setDateFormat():
    '''    public void setDateFormat(final String dateFormat)
    '''
def setDateTimeFormat():
    '''    public void setDateTimeFormat(final String dateTimeFormat)
    '''
def getConfiguration():
    '''    public Configuration getConfiguration()
    '''
def getCNumberFormat():
    '''    public NumberFormat getCNumberFormat()
    '''
def getVariable():
    '''    public TemplateModel getVariable(final String name)
    '''
def getGlobalVariable():
    '''    public TemplateModel getGlobalVariable(final String name)
    '''
def setGlobalVariable():
    '''    public void setGlobalVariable(final String name, final TemplateModel model)
    '''
def setVariable():
    '''    public void setVariable(final String name, final TemplateModel model)
    '''
def setLocalVariable():
    '''    public void setLocalVariable(final String name, final TemplateModel model)
    '''
def getKnownVariableNames():
    '''    public Set getKnownVariableNames()
    '''
def outputInstructionStack():
    '''    public void outputInstructionStack(final PrintWriter pw)
    '''
def getNamespace():
    '''    public Namespace getNamespace(String name)
    '''
def getMainNamespace():
    '''    public Namespace getMainNamespace()
    '''
def getCurrentNamespace():
    '''    public Namespace getCurrentNamespace()
    '''
def getGlobalNamespace():
    '''    public Namespace getGlobalNamespace()
    '''
def getDataModel():
    '''    public TemplateHashModel getDataModel()
    '''
def isEmpty():
    '''    public boolean isEmpty()
    public boolean isEmpty()
    public boolean isEmpty()
    '''
def get():
    '''    public TemplateModel get(final String key)
    public TemplateModel get(final String key)
    public TemplateModel get(final String key)
    '''
def values():
    '''    public TemplateCollectionModel values()
    '''
def keys():
    '''    public TemplateCollectionModel keys()
    '''
def size():
    '''    public int size()
    '''
def getGlobalVariables():
    '''    public TemplateHashModel getGlobalVariables()
    '''
def getCurrentVisitorNode():
    '''    public TemplateNodeModel getCurrentVisitorNode()
    '''
def setCurrentVisitorNode():
    '''    public void setCurrentVisitorNode(final TemplateNodeModel node)
    '''
def include():
    '''    public void include(final String name, final String encoding, final boolean parse)
    public void include(final Template includedTemplate)
    '''
def getTemplateForInclusion():
    '''    public Template getTemplateForInclusion(final String name, final String encoding, final boolean parse)
    public Template getTemplateForInclusion(final String name, String encoding, final boolean parseAsFTL, final boolean ignoreMissing)
    '''
def importLib():
    '''    public Namespace importLib(final String name, final String namespace)
    public Namespace importLib(final Template loadedTemplate, final String namespace)
    '''
def getTemplateForImporting():
    '''    public Template getTemplateForImporting(final String name)
    '''
def toFullTemplateName():
    '''    public String toFullTemplateName(final String baseName, final String targetName)
    '''
def getNamespaceForPrefix():
    '''    public String getNamespaceForPrefix(final String prefix)
    '''
def getPrefixForNamespace():
    '''    public String getPrefixForNamespace(final String nsURI)
    '''
def getDefaultNS():
    '''    public String getDefaultNS()
    '''
def __getitem__():
    '''    public Object __getitem__(final String key)
    '''
def __setitem__():
    '''    public void __setitem__(final String key, final Object o)
    '''
def write():
    '''    public void write(final char[] cbuf, final int off, final int len)
    '''
def flush():
    '''    public void flush()
    '''
def close():
    '''    public void close()
    '''
def render():
    '''    public void render(final Writer newOut)
    '''
def getElement():
    '''    public TemplateElement getElement()
    '''
def equals():
    '''    public boolean equals(final Object o)
    '''
def hashCode():
    '''    public int hashCode()
    '''
