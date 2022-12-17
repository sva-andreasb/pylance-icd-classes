def ():
    '''returns Environment\n\n
    (final Template template, final TemplateHashModel rootDataModel, final Writer out)\n
    '''
def getTemplate():
    '''returns Template\n\n
    getTemplate()\n
    getTemplate()\n
    '''
def getMainTemplate():
    '''returns Template\n\n
    getMainTemplate()\n
    '''
def getCurrentDirectiveCallPlace():
    '''returns DirectiveCallPlace\n\n
    getCurrentDirectiveCallPlace()\n
    '''
def process():
    '''returns None\n\n
    process()\n
    '''
def visit():
    '''returns None\n\n
    visit(final TemplateElement element, final TemplateDirectiveModel directiveModel, final Map args, final List bodyParameterNames)\n
    '''
def getLocalVariable():
    '''returns TemplateModel\n\n
    getLocalVariable(final String name)\n
    getLocalVariable(final String name)\n
    '''
def getLocalVariableNames():
    '''returns Collection\n\n
    getLocalVariableNames()\n
    '''
def isInAttemptBlock():
    '''returns boolean\n\n
    isInAttemptBlock()\n
    '''
def setTemplateExceptionHandler():
    '''returns None\n\n
    setTemplateExceptionHandler(final TemplateExceptionHandler templateExceptionHandler)\n
    '''
def setLocale():
    '''returns None\n\n
    setLocale(final Locale locale)\n
    '''
def setTimeZone():
    '''returns None\n\n
    setTimeZone(final TimeZone timeZone)\n
    '''
def setSQLDateAndTimeTimeZone():
    '''returns None\n\n
    setSQLDateAndTimeTimeZone(final TimeZone timeZone)\n
    '''
def setURLEscapingCharset():
    '''returns None\n\n
    setURLEscapingCharset(final String urlEscapingCharset)\n
    '''
def setOutputEncoding():
    '''returns None\n\n
    setOutputEncoding(final String outputEncoding)\n
    '''
def applyEqualsOperator():
    '''returns boolean\n\n
    applyEqualsOperator(final TemplateModel leftValue, final TemplateModel rightValue)\n
    '''
def applyEqualsOperatorLenient():
    '''returns boolean\n\n
    applyEqualsOperatorLenient(final TemplateModel leftValue, final TemplateModel rightValue)\n
    '''
def applyLessThanOperator():
    '''returns boolean\n\n
    applyLessThanOperator(final TemplateModel leftValue, final TemplateModel rightValue)\n
    '''
def applyLessThanOrEqualsOperator():
    '''returns boolean\n\n
    applyLessThanOrEqualsOperator(final TemplateModel leftValue, final TemplateModel rightValue)\n
    '''
def applyGreaterThanOperator():
    '''returns boolean\n\n
    applyGreaterThanOperator(final TemplateModel leftValue, final TemplateModel rightValue)\n
    '''
def applyWithGreaterThanOrEqualsOperator():
    '''returns boolean\n\n
    applyWithGreaterThanOrEqualsOperator(final TemplateModel leftValue, final TemplateModel rightValue)\n
    '''
def setOut():
    '''returns None\n\n
    setOut(final Writer out)\n
    '''
def getOut():
    '''returns Writer\n\n
    getOut()\n
    '''
def setNumberFormat():
    '''returns None\n\n
    setNumberFormat(final String formatName)\n
    '''
def setTimeFormat():
    '''returns None\n\n
    setTimeFormat(final String timeFormat)\n
    '''
def setDateFormat():
    '''returns None\n\n
    setDateFormat(final String dateFormat)\n
    '''
def setDateTimeFormat():
    '''returns None\n\n
    setDateTimeFormat(final String dateTimeFormat)\n
    '''
def getConfiguration():
    '''returns Configuration\n\n
    getConfiguration()\n
    '''
def getCNumberFormat():
    '''returns NumberFormat\n\n
    getCNumberFormat()\n
    '''
def getVariable():
    '''returns TemplateModel\n\n
    getVariable(final String name)\n
    '''
def getGlobalVariable():
    '''returns TemplateModel\n\n
    getGlobalVariable(final String name)\n
    '''
def setGlobalVariable():
    '''returns None\n\n
    setGlobalVariable(final String name, final TemplateModel model)\n
    '''
def setVariable():
    '''returns None\n\n
    setVariable(final String name, final TemplateModel model)\n
    '''
def setLocalVariable():
    '''returns None\n\n
    setLocalVariable(final String name, final TemplateModel model)\n
    '''
def getKnownVariableNames():
    '''returns Set\n\n
    getKnownVariableNames()\n
    '''
def outputInstructionStack():
    '''returns None\n\n
    outputInstructionStack(final PrintWriter pw)\n
    '''
def getNamespace():
    '''returns Namespace\n\n
    getNamespace(String name)\n
    '''
def getMainNamespace():
    '''returns Namespace\n\n
    getMainNamespace()\n
    '''
def getCurrentNamespace():
    '''returns Namespace\n\n
    getCurrentNamespace()\n
    '''
def getGlobalNamespace():
    '''returns Namespace\n\n
    getGlobalNamespace()\n
    '''
def getDataModel():
    '''returns TemplateHashModel\n\n
    getDataModel()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    isEmpty()\n
    isEmpty()\n
    '''
def get():
    '''returns TemplateModel\n\n
    get(final String key)\n
    get(final String key)\n
    get(final String key)\n
    '''
def values():
    '''returns TemplateCollectionModel\n\n
    values()\n
    '''
def keys():
    '''returns TemplateCollectionModel\n\n
    keys()\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def getGlobalVariables():
    '''returns TemplateHashModel\n\n
    getGlobalVariables()\n
    '''
def getCurrentVisitorNode():
    '''returns TemplateNodeModel\n\n
    getCurrentVisitorNode()\n
    '''
def setCurrentVisitorNode():
    '''returns None\n\n
    setCurrentVisitorNode(final TemplateNodeModel node)\n
    '''
def include():
    '''returns None\n\n
    include(final String name, final String encoding, final boolean parse)\n
    include(final Template includedTemplate)\n
    '''
def getTemplateForInclusion():
    '''returns Template\n\n
    getTemplateForInclusion(final String name, final String encoding, final boolean parse)\n
    getTemplateForInclusion(final String name, String encoding, final boolean parseAsFTL, final boolean ignoreMissing)\n
    '''
def importLib():
    '''returns Namespace\n\n
    importLib(final String name, final String namespace)\n
    importLib(final Template loadedTemplate, final String namespace)\n
    '''
def getTemplateForImporting():
    '''returns Template\n\n
    getTemplateForImporting(final String name)\n
    '''
def toFullTemplateName():
    '''returns String\n\n
    toFullTemplateName(final String baseName, final String targetName)\n
    '''
def getNamespaceForPrefix():
    '''returns String\n\n
    getNamespaceForPrefix(final String prefix)\n
    '''
def getPrefixForNamespace():
    '''returns String\n\n
    getPrefixForNamespace(final String nsURI)\n
    '''
def getDefaultNS():
    '''returns String\n\n
    getDefaultNS()\n
    '''
def __getitem__():
    '''returns Object\n\n
    __getitem__(final String key)\n
    '''
def __setitem__():
    '''returns None\n\n
    __setitem__(final String key, final Object o)\n
    '''
def write():
    '''returns None\n\n
    write(final char[] cbuf, final int off, final int len)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def render():
    '''returns None\n\n
    render(final Writer newOut)\n
    '''
def getElement():
    '''returns TemplateElement\n\n
    getElement()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
