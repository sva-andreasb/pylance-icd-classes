def serialize():
'''public static void serialize(final Document document, final Writer output)
public static void serialize(final Document document, final PrintStream output)
'''
pass
def transform():
'''public static void transform(final Document document, final Result output)
'''
pass
def getColumn():
'''public static Element getColumn(final Element objectElement, final String columnName)
public static XMLColumn getColumn(final XMLObject objectElement, final String columnName)
'''
pass
def getColumnValue():
'''public static String getColumnValue(final Element columnElement)
public static String getColumnValue(final XMLColumn columnElement)
'''
pass
def setColumnValue():
'''public static void setColumnValue(final Element columnElement, final String newValue)
public static void setColumnValue(final XMLColumn columnElement, final String newValue)
'''
pass
def getNotNullColumnValue():
'''public static String getNotNullColumnValue(final Element element, final String columnName)
public static String getNotNullColumnValue(final XMLObject element, final String columnName)
'''
pass