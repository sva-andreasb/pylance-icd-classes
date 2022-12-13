GREGORIAN = "String  gregorian""
ISLAMIC = "String  islamic""
HEBREW = "String  hebrew""
DOJO_ISLAMIC = "String  dojox.date.islamic""
DOJO_HEBREW = "String  dojox.date.hebrew""
ICU_GREGORIAN = "String  gregorian""
ICU_ISLAMIC = "String  islamic-civil""
ICU_HEBREW = "String  hebrew""
def getDojoDatePackage():
'''public static String getDojoDatePackage(final String CalendarType)
'''
pass
def getICUDateClass():
'''public static String getICUDateClass(final String CalendarType)
'''
pass
def getICULocale():
'''public static ULocale getICULocale(final UserInfo user)
public static ULocale getICULocale(final Locale loc, final String CalendarType)
'''
pass
def getDefaultICULocale():
'''public static ULocale getDefaultICULocale()
public static ULocale getDefaultICULocale(final Locale loc)
'''
pass
def getICUCalendar():
'''public static Calendar getICUCalendar(final TimeZone zone, final Locale loc, final String CalendarType)
public static Calendar getICUCalendar(final Locale loc, final String CalendarType)
public static Calendar getICUCalendar(final UserInfo user)
public static Calendar getICUCalendar(final java.util.TimeZone zone, final Locale loc, final String CalendarType)
'''
pass
def getDefaultICUCalendar():
'''public static Calendar getDefaultICUCalendar()
public static Calendar getDefaultICUCalendar(final Locale loc)
public static Calendar getDefaultICUCalendar(final ULocale loc, final TimeZone tz)
public static Calendar getDefaultICUCalendar(final Locale loc, final java.util.TimeZone tz)
'''
pass
def stripUnicode():
'''public static String[] stripUnicode(final String[] list)
'''
pass
def getFullMonthNameForMonth():
'''public static String getFullMonthNameForMonth(final int num, final Locale loc)
'''
pass
