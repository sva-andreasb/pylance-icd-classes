VERSION = "String  \"2.0.3\""
CSI = "String  \"\u001b[\""
def ():
    '''returns MissingTypeConverterException\n\n
    (final Object command)\n
    (final int min, final int max, final boolean variable, final boolean unspecified, final String originalValue)\n
    (final Object command)\n
    (final Object command, final Ansi ansi)\n
    (final Object command, final ColorScheme colorScheme)\n
    (final String separator)\n
    (final ColorScheme colorScheme)\n
    (final ColorScheme colorScheme, final TextTable textTable)\n
    (final ColorScheme colorScheme, final TextTable textTable, final IOptionRenderer optionRenderer, final IParameterRenderer parameterRenderer)\n
    (final Ansi ansi)\n
    (final Ansi ansi, final int... columnWidths)\n
    (final Ansi ansi, final Column... columns)\n
    (final int column, final int row)\n
    (final int width, final int indent, final Overflow overflow)\n
    ()\n
    (final Ansi ansi)\n
    (final int maxLength)\n
    (final String input)\n
    (final String msg)\n
    (final String msg, final Exception ex)\n
    (final String msg)\n
    (final String msg, final Exception ex)\n
    (final CommandLine commandLine, final String msg)\n
    (final CommandLine commandLine, final String msg, final Exception ex)\n
    (final String msg)\n
    (final CommandLine commandLine, final String msg)\n
    (final CommandLine commandLine, final String msg, final Exception ex)\n
    (final CommandLine commandLine, final String msg)\n
    (final String msg)\n
    (final String msg)\n
    (final CommandLine commandLine, final String msg)\n
    (final CommandLine commandLine, final Stack<String> args)\n
    (final CommandLine commandLine, final List<String> args)\n
    (final CommandLine commandLine, final String msg)\n
    (final CommandLine commandLine, final String msg)\n
    (final CommandLine commandLine, final String msg)\n
    '''
def addSubcommand():
    '''returns Help\n\n
    addSubcommand(final String name, final Object command)\n
    addSubcommand(final String commandName, final Object command)\n
    '''
def getParent():
    '''returns CommandLine\n\n
    getParent()\n
    '''
def isUsageHelpRequested():
    '''returns boolean\n\n
    isUsageHelpRequested()\n
    '''
def isVersionHelpRequested():
    '''returns boolean\n\n
    isVersionHelpRequested()\n
    '''
def isOverwrittenOptionsAllowed():
    '''returns boolean\n\n
    isOverwrittenOptionsAllowed()\n
    '''
def setOverwrittenOptionsAllowed():
    '''returns CommandLine\n\n
    setOverwrittenOptionsAllowed(final boolean newValue)\n
    '''
def isUnmatchedArgumentsAllowed():
    '''returns boolean\n\n
    isUnmatchedArgumentsAllowed()\n
    '''
def setUnmatchedArgumentsAllowed():
    '''returns CommandLine\n\n
    setUnmatchedArgumentsAllowed(final boolean newValue)\n
    '''
def getUnmatchedArguments():
    '''returns List<String>\n\n
    getUnmatchedArguments()\n
    '''
def parse():
    '''returns List<CommandLine>\n\n
    parse(final String... args)\n
    '''
def parseWithHandler():
    '''returns List<Object>\n\n
    parseWithHandler(final IParseResultHandler handler, final PrintStream out, final String... args)\n
    '''
def parseWithHandlers():
    '''returns List<Object>\n\n
    parseWithHandlers(final IParseResultHandler handler, final PrintStream out, final Help.Ansi ansi, final IExceptionHandler exceptionHandler, final String... args)\n
    '''
def usage():
    '''returns None\n\n
    usage(final PrintStream out)\n
    usage(final PrintStream out, final Help.Ansi ansi)\n
    usage(final PrintStream out, final Help.ColorScheme colorScheme)\n
    '''
def printVersionHelp():
    '''returns None\n\n
    printVersionHelp(final PrintStream out)\n
    printVersionHelp(final PrintStream out, final Help.Ansi ansi)\n
    printVersionHelp(final PrintStream out, final Help.Ansi ansi, final Object... params)\n
    '''
def getSeparator():
    '''returns String\n\n
    getSeparator()\n
    '''
def setSeparator():
    '''returns CommandLine\n\n
    setSeparator(final String separator)\n
    '''
def getCommandName():
    '''returns String\n\n
    getCommandName()\n
    '''
def setCommandName():
    '''returns CommandLine\n\n
    setCommandName(final String commandName)\n
    '''
def handleException():
    '''returns List<Object>\n\n
    handleException(final ParameterException ex, final PrintStream out, final Help.Ansi ansi, final String... args)\n
    '''
def handleParseResult():
    '''returns List<Object>\n\n
    handleParseResult(final List<CommandLine> parsedCommands, final PrintStream out, final Help.Ansi ansi)\n
    handleParseResult(final List<CommandLine> parsedCommands, final PrintStream out, final Help.Ansi ansi)\n
    handleParseResult(final List<CommandLine> parsedCommands, final PrintStream out, final Help.Ansi ansi)\n
    '''
def min():
    '''returns Range\n\n
    min(final int newMin)\n
    '''
def max():
    '''returns Range\n\n
    max(final int newMax)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final int value)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object object)\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    toString(final StringBuilder text)\n
    toString()\n
    toString()\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Range other)\n
    '''
def convert():
    '''returns UUID\n\n
    convert(final String value)\n
    convert(final String value)\n
    convert(final String value)\n
    convert(final String value)\n
    convert(final String value)\n
    convert(final String value)\n
    convert(final String value)\n
    convert(final String value)\n
    convert(final String value)\n
    convert(final String value)\n
    convert(final String value)\n
    convert(final String value)\n
    convert(final String value)\n
    convert(final String value)\n
    convert(final String value)\n
    convert(final String value)\n
    convert(final String value)\n
    convert(final String value)\n
    convert(final String value)\n
    convert(final String value)\n
    convert(final String s)\n
    convert(final String s)\n
    convert(final String s)\n
    convert(final String s)\n
    '''
def compare():
    '''returns int\n\n
    compare(final Field o1, final Field o2)\n
    compare(final String o1, final String o2)\n
    compare(final Field f1, final Field f2)\n
    compare(final Field f1, final Field f2)\n
    '''
def addAllSubcommands():
    '''returns Help\n\n
    addAllSubcommands(final Map<String, CommandLine> commands)\n
    '''
def synopsis():
    '''returns String\n\n
    synopsis()\n
    synopsis(final int synopsisHeadingLength)\n
    '''
def abbreviatedSynopsis():
    '''returns String\n\n
    abbreviatedSynopsis()\n
    '''
def detailedSynopsis():
    '''returns String\n\n
    detailedSynopsis(final Comparator<Field> optionSort, final boolean clusterBooleanOptions)\n
    detailedSynopsis(final int synopsisHeadingLength, final Comparator<Field> optionSort, final boolean clusterBooleanOptions)\n
    '''
def synopsisHeadingLength():
    '''returns int\n\n
    synopsisHeadingLength()\n
    '''
def optionList():
    '''returns String\n\n
    optionList()\n
    optionList(final Layout layout, final Comparator<Field> optionSort, final IParamLabelRenderer valueLabelRenderer)\n
    '''
def parameterList():
    '''returns String\n\n
    parameterList()\n
    parameterList(final Layout layout, final IParamLabelRenderer paramLabelRenderer)\n
    '''
def customSynopsis():
    '''returns String\n\n
    customSynopsis(final Object... params)\n
    '''
def description():
    '''returns String\n\n
    description(final Object... params)\n
    '''
def header():
    '''returns String\n\n
    header(final Object... params)\n
    '''
def footer():
    '''returns String\n\n
    footer(final Object... params)\n
    '''
def headerHeading():
    '''returns String\n\n
    headerHeading(final Object... params)\n
    '''
def synopsisHeading():
    '''returns String\n\n
    synopsisHeading(final Object... params)\n
    '''
def descriptionHeading():
    '''returns String\n\n
    descriptionHeading(final Object... params)\n
    '''
def parameterListHeading():
    '''returns String\n\n
    parameterListHeading(final Object... params)\n
    '''
def optionListHeading():
    '''returns String\n\n
    optionListHeading(final Object... params)\n
    '''
def commandListHeading():
    '''returns String\n\n
    commandListHeading(final Object... params)\n
    '''
def footerHeading():
    '''returns String\n\n
    footerHeading(final Object... params)\n
    '''
def commandList():
    '''returns String\n\n
    commandList()\n
    '''
def createDefaultLayout():
    '''returns Layout\n\n
    createDefaultLayout()\n
    '''
def createDefaultOptionRenderer():
    '''returns IOptionRenderer\n\n
    createDefaultOptionRenderer()\n
    '''
def createDefaultParameterRenderer():
    '''returns IParameterRenderer\n\n
    createDefaultParameterRenderer()\n
    '''
def separator():
    '''returns String\n\n
    separator()\n
    separator()\n
    '''
def createDefaultParamLabelRenderer():
    '''returns IParamLabelRenderer\n\n
    createDefaultParamLabelRenderer()\n
    '''
def ansi():
    '''returns Ansi\n\n
    ansi()\n
    ansi()\n
    '''
def layout():
    '''returns None\n\n
    layout(final Field field, final Ansi.Text[][] cellValues)\n
    '''
def addOptions():
    '''returns None\n\n
    addOptions(final List<Field> fields, final IParamLabelRenderer paramLabelRenderer)\n
    '''
def addOption():
    '''returns None\n\n
    addOption(final Field field, final IParamLabelRenderer paramLabelRenderer)\n
    '''
def addPositionalParameters():
    '''returns None\n\n
    addPositionalParameters(final List<Field> fields, final IParamLabelRenderer paramLabelRenderer)\n
    '''
def addPositionalParameter():
    '''returns None\n\n
    addPositionalParameter(final Field field, final IParamLabelRenderer paramLabelRenderer)\n
    '''
def rowCount():
    '''returns int\n\n
    rowCount()\n
    '''
def addEmptyRow():
    '''returns None\n\n
    addEmptyRow()\n
    '''
def addRowValues():
    '''returns None\n\n
    addRowValues(final String... values)\n
    addRowValues(final Ansi.Text... values)\n
    '''
def putValue():
    '''returns Cell\n\n
    putValue(int row, int col, Ansi.Text value)\n
    '''
def commands():
    '''returns ColorScheme\n\n
    commands(final Ansi.IStyle... styles)\n
    '''
def options():
    '''returns ColorScheme\n\n
    options(final Ansi.IStyle... styles)\n
    '''
def parameters():
    '''returns ColorScheme\n\n
    parameters(final Ansi.IStyle... styles)\n
    '''
def optionParams():
    '''returns ColorScheme\n\n
    optionParams(final Ansi.IStyle... styles)\n
    '''
def applySystemProperties():
    '''returns ColorScheme\n\n
    applySystemProperties()\n
    '''
def enabled():
    '''returns boolean\n\n
    enabled()\n
    '''
def apply():
    '''returns Text\n\n
    apply(final String plainText, final List<IStyle> styles)\n
    '''
def on():
    '''returns String\n\n
    on()\n
    on()\n
    '''
def off():
    '''returns String\n\n
    off()\n
    off()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def splitLines():
    '''returns Text[]\n\n
    splitLines()\n
    '''
def substring():
    '''returns Text\n\n
    substring(final int start)\n
    substring(final int start, final int end)\n
    '''
def append():
    '''returns Text\n\n
    append(final String string)\n
    append(final Text other)\n
    '''
def getStyledChars():
    '''returns None\n\n
    getStyledChars(final int from, final int length, final Text destination, final int offset)\n
    '''
def plainString():
    '''returns String\n\n
    plainString()\n
    '''
def isEnabled():
    '''returns boolean\n\n
    isEnabled(final TraceLevel other)\n
    '''
def getCommandLine():
    '''returns CommandLine\n\n
    getCommandLine()\n
    getCommandLine()\n
    '''
