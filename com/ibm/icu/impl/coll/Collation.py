SENTINEL_CP = "int -1"
LESS = "int -1"
EQUAL = "int 0"
GREATER = "int 1"
TERMINATOR_BYTE = "int 0"
LEVEL_SEPARATOR_BYTE = "int 1"
MERGE_SEPARATOR_BYTE = "int 2"
MERGE_SEPARATOR_PRIMARY = "long 33554432L"
PRIMARY_COMPRESSION_LOW_BYTE = "int 3"
PRIMARY_COMPRESSION_HIGH_BYTE = "int 255"
COMMON_WEIGHT16 = "int 1280"
COMMON_SEC_AND_TER_CE = "int 83887360"
CASE_MASK = "int 49152"
ONLY_TERTIARY_MASK = "int 16191"
QUATERNARY_MASK = "int 192"
CASE_AND_QUATERNARY_MASK = "int 49344"
MAX_PRIMARY = "long 4294901760L"
FFFD_PRIMARY = "long 4294770688L"
NO_CE = "long 4311744768L"
NO_LEVEL = "int 0"
PRIMARY_LEVEL = "int 1"
SECONDARY_LEVEL = "int 2"
CASE_LEVEL = "int 3"
TERTIARY_LEVEL = "int 4"
QUATERNARY_LEVEL = "int 5"
IDENTICAL_LEVEL = "int 6"
ZERO_LEVEL = "int 7"
def makeCE():
'''public static long makeCE(final long p)
'''
pass
def incTwoBytePrimaryByOffset():
'''public static long incTwoBytePrimaryByOffset(final long basePrimary, final boolean isCompressible, int offset)
'''
pass
def incThreeBytePrimaryByOffset():
'''public static long incThreeBytePrimaryByOffset(final long basePrimary, final boolean isCompressible, int offset)
'''
pass
