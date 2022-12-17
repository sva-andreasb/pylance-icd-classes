STATUS_OPT = "String  \"t\""
LA_PATH_OPT = "String  \"l\""
MASTER_PATH_OPT = "String  \"m\""
STATUS_PATH_OPT = "String  \"s\""
REVALIDATE_OPT = "String  \"revalidate\""
NO_PRINT_OPT = "String  \"no_print\""
NO_EXPORT_OPT = "String  \"no_export\""
WIN_STYLE_OPT = "String  \"win_style\""
WIN_COLOR_OPT = "String  \"win_color\""
DIALOG_BACKCOLOR_OPT = "String  \"dialog_backcolor\""
DIALOG_SIZE_OPT = "String  \"dialog_size\""
FONT_NAME_OPT = "String  \"font_name\""
FONT_STYLE_OPT = "String  \"font_style\""
FONT_SIZE_OPT = "String  \"font_size\""
ASKVERSION = "String  \"version\""
SETLANG = "String  \"setlang\""
LANGSET = "String  \"langset\""
TEXT_ONLY_OPT = "String  \"text_only\""
REG_OPT = "String  \"register\""
UNIQUE_ID_OPT = "String  \"uid\""
REG_DESC_OPT = "String  \"desc\""
SHOW_EXIT_CODE_OPT = "String  \"show_exit_code\""
def ():
    '''returns LAP\n\n
    ()\n
    (final String[] array)\n
    (final String[] array, final boolean b)\n
    '''
def breakText():
    '''returns String[]\n\n
    breakText(final int n, final int n2, final String[] array, final Locale locale)\n
    '''
def doLAP():
    '''returns None\n\n
    doLAP()\n
    doLAP(final boolean b)\n
    '''
def doLapCommandLine():
    '''returns int\n\n
    doLapCommandLine()\n
    '''
def statusChanged():
    '''returns None\n\n
    statusChanged(final int n)\n
    '''
def getLAPTitle():
    '''returns String\n\n
    getLAPTitle()\n
    '''
def getLicenseAcceptanceProcess():
    '''returns LicenseAcceptanceProcess\n\n
    getLicenseAcceptanceProcess()\n
    '''
def getLicenseAgreement():
    '''returns String[]\n\n
    getLicenseAgreement(final Locale locale)\n
    '''
def getStatus():
    '''returns int\n\n
    getStatus()\n
    '''
def getSupportedLanguages():
    '''returns SupportedLanguages\n\n
    getSupportedLanguages()\n
    '''
def licenseIsValid():
    '''returns boolean\n\n
    licenseIsValid()\n
    '''
def setExportLA():
    '''returns None\n\n
    setExportLA(final boolean b)\n
    '''
def setStatus():
    '''returns None\n\n
    setStatus(final int status)\n
    '''
def getmPath():
    '''returns String\n\n
    getmPath()\n
    '''
def getnoPrint():
    '''returns boolean\n\n
    getnoPrint()\n
    '''
def getnoExport():
    '''returns boolean\n\n
    getnoExport()\n
    '''
def getwinStyle():
    '''returns String\n\n
    getwinStyle()\n
    '''
def getwinColorString():
    '''returns String\n\n
    getwinColorString()\n
    '''
def getdialogBackcolorString():
    '''returns String\n\n
    getdialogBackcolorString()\n
    '''
def getdialogSizeString():
    '''returns String\n\n
    getdialogSizeString()\n
    '''
def getfontName():
    '''returns String\n\n
    getfontName()\n
    '''
def getfontStyleString():
    '''returns String\n\n
    getfontStyleString()\n
    '''
def getfontSizeString():
    '''returns String\n\n
    getfontSizeString()\n
    '''
def getbShowExitCode():
    '''returns boolean\n\n
    getbShowExitCode()\n
    '''
