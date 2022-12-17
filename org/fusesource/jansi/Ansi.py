def ():
    '''returns Ansi\n\n
    ()\n
    (final Ansi parent)\n
    (final int size)\n
    (final StringBuilder builder)\n
    '''
def fg():
    '''returns Ansi\n\n
    fg(final Color color)\n
    fg()\n
    fg(final Color color)\n
    '''
def fgBlack():
    '''returns Ansi\n\n
    fgBlack()\n
    '''
def fgBlue():
    '''returns Ansi\n\n
    fgBlue()\n
    '''
def fgCyan():
    '''returns Ansi\n\n
    fgCyan()\n
    '''
def fgDefault():
    '''returns Ansi\n\n
    fgDefault()\n
    '''
def fgGreen():
    '''returns Ansi\n\n
    fgGreen()\n
    '''
def fgMagenta():
    '''returns Ansi\n\n
    fgMagenta()\n
    '''
def fgRed():
    '''returns Ansi\n\n
    fgRed()\n
    '''
def fgYellow():
    '''returns Ansi\n\n
    fgYellow()\n
    '''
def bg():
    '''returns Ansi\n\n
    bg(final Color color)\n
    bg()\n
    bg(final Color color)\n
    '''
def bgCyan():
    '''returns Ansi\n\n
    bgCyan()\n
    '''
def bgDefault():
    '''returns Ansi\n\n
    bgDefault()\n
    '''
def bgGreen():
    '''returns Ansi\n\n
    bgGreen()\n
    '''
def bgMagenta():
    '''returns Ansi\n\n
    bgMagenta()\n
    '''
def bgRed():
    '''returns Ansi\n\n
    bgRed()\n
    '''
def bgYellow():
    '''returns Ansi\n\n
    bgYellow()\n
    '''
def fgBright():
    '''returns Ansi\n\n
    fgBright(final Color color)\n
    fgBright()\n
    fgBright(final Color color)\n
    '''
def fgBrightBlack():
    '''returns Ansi\n\n
    fgBrightBlack()\n
    '''
def fgBrightBlue():
    '''returns Ansi\n\n
    fgBrightBlue()\n
    '''
def fgBrightCyan():
    '''returns Ansi\n\n
    fgBrightCyan()\n
    '''
def fgBrightDefault():
    '''returns Ansi\n\n
    fgBrightDefault()\n
    '''
def fgBrightGreen():
    '''returns Ansi\n\n
    fgBrightGreen()\n
    '''
def fgBrightMagenta():
    '''returns Ansi\n\n
    fgBrightMagenta()\n
    '''
def fgBrightRed():
    '''returns Ansi\n\n
    fgBrightRed()\n
    '''
def fgBrightYellow():
    '''returns Ansi\n\n
    fgBrightYellow()\n
    '''
def bgBright():
    '''returns Ansi\n\n
    bgBright(final Color color)\n
    bgBright()\n
    bgBright(final Color color)\n
    '''
def bgBrightCyan():
    '''returns Ansi\n\n
    bgBrightCyan()\n
    '''
def bgBrightDefault():
    '''returns Ansi\n\n
    bgBrightDefault()\n
    '''
def bgBrightGreen():
    '''returns Ansi\n\n
    bgBrightGreen()\n
    '''
def bgBrightMagenta():
    '''returns Ansi\n\n
    bgBrightMagenta()\n
    '''
def bgBrightRed():
    '''returns Ansi\n\n
    bgBrightRed()\n
    '''
def bgBrightYellow():
    '''returns Ansi\n\n
    bgBrightYellow()\n
    '''
def a():
    '''returns Ansi\n\n
    a(final Attribute attribute)\n
    a(final String value)\n
    a(final boolean value)\n
    a(final char value)\n
    a(final char[] value, final int offset, final int len)\n
    a(final char[] value)\n
    a(final CharSequence value, final int start, final int end)\n
    a(final CharSequence value)\n
    a(final double value)\n
    a(final float value)\n
    a(final int value)\n
    a(final long value)\n
    a(final Object value)\n
    a(final StringBuffer value)\n
    a(final Attribute attribute)\n
    '''
def cursor():
    '''returns Ansi\n\n
    cursor(final int x, final int y)\n
    cursor(final int x, final int y)\n
    '''
def cursorToColumn():
    '''returns Ansi\n\n
    cursorToColumn(final int x)\n
    cursorToColumn(final int x)\n
    '''
def cursorUp():
    '''returns Ansi\n\n
    cursorUp(final int y)\n
    cursorUp(final int y)\n
    '''
def cursorDown():
    '''returns Ansi\n\n
    cursorDown(final int y)\n
    cursorDown(final int y)\n
    '''
def cursorRight():
    '''returns Ansi\n\n
    cursorRight(final int x)\n
    cursorRight(final int x)\n
    '''
def cursorLeft():
    '''returns Ansi\n\n
    cursorLeft(final int x)\n
    cursorLeft(final int x)\n
    '''
def cursorDownLine():
    '''returns Ansi\n\n
    cursorDownLine()\n
    cursorDownLine(final int n)\n
    cursorDownLine()\n
    cursorDownLine(final int n)\n
    '''
def cursorUpLine():
    '''returns Ansi\n\n
    cursorUpLine()\n
    cursorUpLine(final int n)\n
    cursorUpLine()\n
    cursorUpLine(final int n)\n
    '''
def eraseScreen():
    '''returns Ansi\n\n
    eraseScreen()\n
    eraseScreen(final Erase kind)\n
    eraseScreen()\n
    eraseScreen(final Erase kind)\n
    '''
def eraseLine():
    '''returns Ansi\n\n
    eraseLine()\n
    eraseLine(final Erase kind)\n
    eraseLine()\n
    eraseLine(final Erase kind)\n
    '''
def scrollUp():
    '''returns Ansi\n\n
    scrollUp(final int rows)\n
    scrollUp(final int rows)\n
    '''
def scrollDown():
    '''returns Ansi\n\n
    scrollDown(final int rows)\n
    scrollDown(final int rows)\n
    '''
def saveCursorPosition():
    '''returns Ansi\n\n
    saveCursorPosition()\n
    saveCursorPosition()\n
    '''
def restorCursorPosition():
    '''returns Ansi\n\n
    restorCursorPosition()\n
    restorCursorPosition()\n
    '''
def restoreCursorPosition():
    '''returns Ansi\n\n
    restoreCursorPosition()\n
    restoreCursorPosition()\n
    '''
def reset():
    '''returns Ansi\n\n
    reset()\n
    reset()\n
    '''
def bold():
    '''returns Ansi\n\n
    bold()\n
    '''
def boldOff():
    '''returns Ansi\n\n
    boldOff()\n
    '''
def newline():
    '''returns Ansi\n\n
    newline()\n
    '''
def format():
    '''returns Ansi\n\n
    format(final String pattern, final Object... args)\n
    '''
def render():
    '''returns Ansi\n\n
    render(final String text)\n
    render(final String text, final Object... args)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    '''
def call():
    '''returns Boolean\n\n
    call()\n
    '''
def value():
    '''returns int\n\n
    value()\n
    value()\n
    value()\n
    '''
