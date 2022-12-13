FLAG_NEGATIVE = "int 1"
FLAG_PERCENT = "int 2"
FLAG_PERMILLE = "int 4"
FLAG_HAS_EXPONENT = "int 8"
FLAG_HAS_DECIMAL_SEPARATOR = "int 32"
FLAG_NAN = "int 64"
FLAG_INFINITY = "int 128"
FLAG_FAIL = "int 256"
def ParsedNumber():
'''public ParsedNumber()
'''
pass
def clear():
'''public void clear()
'''
pass
def copyFrom():
'''public void copyFrom(final ParsedNumber other)
'''
pass
def setCharsConsumed():
'''public void setCharsConsumed(final StringSegment segment)
'''
pass
def postProcess():
'''public void postProcess()
'''
pass
def success():
'''public boolean success()
'''
pass
def seenNumber():
'''public boolean seenNumber()
'''
pass
def getNumber():
'''public Number getNumber()
public Number getNumber(final int parseFlags)
'''
pass
def compare():
'''public int compare(final ParsedNumber o1, final ParsedNumber o2)
'''
pass
