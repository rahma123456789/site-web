"""MySQL ER Constants

These constants are error codes for the bulk of the error conditions
that may occur.
"""

if __name__ == "__main__":
    """
    Usage: python ER.py [/path/to/mysql/mysqld_error.h ...] >> ER.py
    """
    import fileinput
    import re

    data = {}
    error_last = None
    for line in fileinput.input():
        line = re.sub(r"/\*.*?\*/", "", line)
        m = re.match(r"^\s*#define\s+((ER|WARN)_[A-Z0-9_]+)\s+(\d+)\s*", line)
        if m:
            name = m.group(1)
            if name.startswith("ER_"):
                name = name[3:]
            value = int(m.group(3))
            if name == "ERROR_LAST":
                if error_last is None or error_last < value:
                    error_last = value
                continue
            if value not in data:
                data[value] = set()
            data[value].add(name)
    for value, names in sorted(data.items()):
        for name in sorted(names):
            print("{} = {}".format(name, value))
    if error_last is not None:
        print("ERROR_LAST = %s" % error_last)


ERROR_FIRST = 1000
NO = 1002
YES = 1003
CANT_CREATE_FILE = 1004
CANT_CREATE_TABLE = 1005
CANT_CREATE_DB = 1006
DB_CREATE_EXISTS = 1007
DB_DROP_EXISTS = 1008
DB_DROP_RMDIR = 1010
CANT_FIND_SYSTEM_REC = 1012
CANT_GET_STAT = 1013
CANT_LOCK = 1015
CANT_OPEN_FILE = 1016
FILE_NOT_FOUND = 1017
CANT_READ_DIR = 1018
CHECKREAD = 1020
DUP_KEY = 1022
ERROR_ON_READ = 1024
ERROR_ON_RENAME = 1025
ERROR_ON_WRITE = 1026
FILE_USED = 1027
FILSORT_ABORT = 1028
GET_ERRNO = 1030
ILLEGAL_HA = 1031
KEY_NOT_FOUND = 1032
NOT_FORM_FILE = 1033
NOT_KEYFILE = 1034
OLD_KEYFILE = 1035
OPEN_AS_READONLY = 1036
OUTOFMEMORY = 1037
OUT_OF_SORTMEMORY = 1038
CON_COUNT_ERROR = 1040
OUT_OF_RESOURCES = 1041
BAD_HOST_ERROR = 1042
HANDSHAKE_ERROR = 1043
DBACCESS_DENIED_ERROR = 1044
ACCESS_DENIED_ERROR = 1045
NO_DB_ERROR = 1046
UNKNOWN_COM_ERROR = 1047
BAD_NULL_ERROR = 1048
BAD_DB_ERROR = 1049
TABLE_EXISTS_ERROR = 1050
BAD_TABLE_ERROR = 1051
NON_UNIQ_ERROR = 1052
SERVER_SHUTDOWN = 1053
BAD_FIELD_ERROR = 1054
WRONG_FIELD_WITH_GROUP = 1055
WRONG_GROUP_FIELD = 1056
WRONG_SUM_SELECT = 1057
WRONG_VALUE_COUNT = 1058
TOO_LONG_IDENT = 1059
DUP_FIELDNAME = 1060
DUP_KEYNAME = 1061
DUP_ENTRY = 1062
WRONG_FIELD_SPEC = 1063
PARSE_ERROR = 1064
EMPTY_QUERY = 1065
NONUNIQ_TABLE = 1066
INVALID_DEFAULT = 1067
MULTIPLE_PRI_KEY = 1068
TOO_MANY_KEYS = 1069
TOO_MANY_KEY_PARTS = 1070
TOO_LONG_KEY = 1071
KEY_COLUMN_DOES_NOT_EXITS = 1072
BLOB_USED_AS_KEY = 1073
TOO_BIG_FIELDLENGTH = 1074
WRONG_AUTO_KEY = 1075
READY = 1076
SHUTDOWN_COMPLETE = 1079
FORCING_CLOSE = 1080
IPSOCK_ERROR = 1081
NO_SUCH_INDEX = 1082
WRONG_FIELD_TERMINATORS = 1083
BLOBS_AND_NO_TERMINATED = 1084
TEXTFILE_NOT_READABLE = 1085
FILE_EXISTS_ERROR = 1086
LOAD_INFO = 1087
ALTER_INFO = 1088
WRONG_SUB_KEY = 1089
CANT_REMOVE_ALL_FIELDS = 1090
CANT_DROP_FIELD_OR_KEY = 1091
INSERT_INFO = 1092
UPDATE_TABLE_USED = 1093
NO_SUCH_THREAD = 1094
KILL_DENIED_ERROR = 1095
NO_TABLES_USED = 1096
TOO_BIG_SET = 1097
NO_UNIQUE_LOGFILE = 1098
TABLE_NOT_LOCKED_FOR_WRITE = 1099
TABLE_NOT_LOCKED = 1100
BLOB_CANT_HAVE_DEFAULT = 1101
WRONG_DB_NAME = 1102
WRONG_TABLE_NAME = 1103
TOO_BIG_SELECT = 1104
UNKNOWN_ERROR = 1105
UNKNOWN_PROCEDURE = 1106
WRONG_PARAMCOUNT_TO_PROCEDURE = 1107
WRONG_PARAMETERS_TO_PROCEDURE = 1108
UNKNOWN_TABLE = 1109
FIELD_SPECIFIED_TWICE = 1110
INVALID_GROUP_FUNC_USE = 1111
UNSUPPORTED_EXTENSION = 1112
TABLE_MUST_HAVE_COLUMNS = 1113
RECORD_FILE_FULL = 1114
UNKNOWN_CHARACTER_SET = 1115
TOO_MANY_TABLES = 1116
TOO_MANY_FIELDS = 1117
TOO_BIG_ROWSIZE = 1118
STACK_OVERRUN = 1119
WRONG_OUTER_JOIN_UNUSED = 1120
NULL_COLUMN_IN_INDEX = 1121
CANT_FIND_UDF = 1122
CANT_INITIALIZE_UDF = 1123
UDF_NO_PATHS = 1124
UDF_EXISTS = 1125
CANT_OPEN_LIBRARY = 1126
CANT_FIND_DL_ENTRY = 1127
FUNCTION_NOT_DEFINED = 1128
HOST_IS_BLOCKED = 1129
HOST_NOT_PRIVILEGED = 1130
PASSWORD_ANONYMOUS_USER = 1131
PASSWORD_NOT_ALLOWED = 1132
PASSWORD_NO_MATCH = 1133
UPDATE_INFO = 1134
CANT_CREATE_THREAD = 1135
WRONG_VALUE_COUNT_ON_ROW = 1136
CANT_REOPEN_TABLE = 1137
INVALID_USE_OF_NULL = 1138
REGEXP_ERROR = 1139
MIX_OF_GROUP_FUNC_AND_FIELDS = 1140
NONEXISTING_GRANT = 1141
TABLEACCESS_DENIED_ERROR = 1142
COLUMNACCESS_DENIED_ERROR = 1143
ILLEGAL_GRANT_FOR_TABLE = 1144
GRANT_WRONG_HOST_OR_USER = 1145
NO_SUCH_TABLE = 1146
NONEXISTING_TABLE_GRANT = 1147
NOT_ALLOWED_COMMAND = 1148
SYNTAX_ERROR = 1149
ABORTING_CONNECTION = 1152
NET_PACKET_TOO_LARGE = 1153
NET_READ_ERROR_FROM_PIPE = 1154
NET_FCNTL_ERROR = 1155
NET_PACKETS_OUT_OF_ORDER = 1156
NET_UNCOMPRESS_ERROR = 1157
NET_READ_ERROR = 1158
NET_READ_INTERRUPTED = 1159
NET_ERROR_ON_WRITE = 1160
NET_WRITE_INTERRUPTED = 1161
TOO_LONG_STRING = 1162
TABLE_CANT_HANDLE_BLOB = 1163
TABLE_CANT_HANDLE_AUTO_INCREMENT = 1164
WRONG_COLUMN_NAME = 1166
WRONG_KEY_COLUMN = 1167
WRONG_MRG_TABLE = 1168
DUP_UNIQUE = 1169
BLOB_KEY_WITHOUT_LENGTH = 1170
PRIMARY_CANT_HAVE_NULL = 1171
TOO_MANY_ROWS = 1172
REQUIRES_PRIMARY_KEY = 1173
UPDATE_WITHOUT_KEY_IN_SAFE_MODE = 1175
KEY_DOES_NOT_EXITS = 1176
CHECK_NO_SUCH_TABLE = 1177
CHECK_NOT_IMPLEMENTED = 1178
CANT_DO_THIS_DURING_AN_TRANSACTION = 1179
ERROR_DURING_COMMIT = 1180
ERROR_DURING_ROLLBACK = 1181
ERROR_DURING_FLUSH_LOGS = 1182
NEW_ABORTING_CONNECTION = 1184
MASTER = 1188
MASTER_NET_READ = 1189
MASTER_NET_WRITE = 1190
FT_MATCHING_KEY_NOT_FOUND = 1191
LOCK_OR_ACTIVE_TRANSACTION = 1192
UNKNOWN_SYSTEM_VARIABLE = 1193
CRASHED_ON_USAGE = 1194
CRASHED_ON_REPAIR = 1195
WARNING_NOT_COMPLETE_ROLLBACK = 1196
TRANS_CACHE_FULL = 1197
SLAVE_NOT_RUNNING = 1199
BAD_SLAVE = 1200
MASTER_INFO = 1201
SLAVE_THREAD = 1202
TOO_MANY_USER_CONNECTIONS = 1203
SET_CONSTANTS_ONLY = 1204
LOCK_WAIT_TIMEOUT = 1205
LOCK_TABLE_FULL = 1206
READ_ONLY_TRANSACTION = 1207
WRONG_ARGUMENTS = 1210
NO_PERMISSION_TO_CREATE_USER = 1211
LOCK_DEADLOCK = 1213
TABLE_CANT_HANDLE_FT = 1214
CANNOT_ADD_FOREIGN = 1215
NO_REFERENCED_ROW = 1216
ROW_IS_REFERENCED = 1217
CONNECT_TO_MASTER = 1218
ERROR_WHEN_EXECUTING_COMMAND = 1220
WRONG_USAGE = 1221
WRONG_NUMBER_OF_COLUMNS_IN_SELECT = 1222
CANT_UPDATE_WITH_READLOCK = 1223
MIXING_NOT_ALLOWED = 1224
DUP_ARGUMENT = 1225
USER_LIMIT_REACHED = 1226
SPECIFIC_ACCESS_DENIED_ERROR = 1227
LOCAL_VARIABLE = 1228
GLOBAL_VARIABLE = 1229
NO_DEFAULT = 1230
WRONG_VALUE_FOR_VAR = 1231
WRONG_TYPE_FOR_VAR = 1232
VAR_CANT_BE_READ = 1233
CANT_USE_OPTION_HERE = 1234
NOT_SUPPORTED_YET = 1235
MASTER_FATAL_ERROR_READING_BINLOG = 1236
SLAVE_IGNORED_TABLE = 1237
INCORRECT_GLOBAL_LOCAL_VAR = 1238
WRONG_FK_DEF = 1239
KEY_REF_DO_NOT_MATCH_TABLE_REF = 1240
OPERAND_COLUMNS = 1241
SUBQUERY_NO_1_ROW = 1242
UNKNOWN_STMT_HANDLER = 1243
CORRUPT_HELP_DB = 1244
AUTO_CONVERT = 1246
ILLEGAL_REFERENCE = 1247
DERIVED_MUST_HAVE_ALIAS = 1248
SELECT_REDUCED = 1249
TABLENAME_NOT_ALLOWED_HERE = 1250
NOT_SUPPORTED_AUTH_MODE = 1251
SPATIAL_CANT_HAVE_NULL = 1252
COLLATION_CHARSET_MISMATCH = 1253
TOO_BIG_FOR_UNCOMPRESS = 1256
ZLIB_Z_MEM_ERROR = 1257
ZLIB_Z_BUF_ERROR = 1258
ZLIB_Z_DATA_ERROR = 1259
CUT_VALUE_GROUP_CONCAT = 1260
WARN_TOO_FEW_RECORDS = 1261
WARN_TOO_MANY_RECORDS = 1262
WARN_NULL_TO_NOTNULL = 1263
WARN_DATA_OUT_OF_RANGE = 1264
WARN_DATA_TRUNCATED = 1265
WARN_USING_OTHER_HANDLER = 1266
CANT_AGGREGATE_2COLLATIONS = 1267
REVOKE_GRANTS = 1269
CANT_AGGREGATE_3COLLATIONS = 1270
CANT_AGGREGATE_NCOLLATIONS = 1271
VARIABLE_IS_NOT_STRUCT = 1272
UNKNOWN_COLLATION = 1273
SLAVE_IGNORED_SSL_PARAMS = 1274
SERVER_IS_IN_SECURE_AUTH_MODE = 1275
WARN_FIELD_RESOLVED = 1276
BAD_SLAVE_UNTIL_COND = 1277
MISSING_SKIP_SLAVE = 1278
UNTIL_COND_IGNORED = 1279
WRONG_NAME_FOR_INDEX = 1280
WRONG_NAME_FOR_CATALOG = 1281
BAD_FT_COLUMN = 1283
UNKNOWN_KEY_CACHE = 1284
WARN_HOSTNAME_WONT_WORK = 1285
UNKNOWN_STORAGE_ENGINE = 1286
WARN_DEPRECATED_SYNTAX = 1287
NON_UPDATABLE_TABLE = 1288
FEATURE_DISABLED = 1289
OPTION_PREVENTS_STATEMENT = 1290
DUPLICATED_VALUE_IN_TYPE = 1291
TRUNCATED_WRONG_VALUE = 1292
INVALID_ON_UPDATE = 1294
UNSUPPORTED_PS = 1295
GET_ERRMSG = 1296
GET_TEMPORARY_ERRMSG = 1297
UNKNOWN_TIME_ZONE = 1298
WARN_INVALID_TIMESTAMP = 1299
INVALID_CHARACTER_STRING = 1300
WARN_ALLOWED_PACKET_OVERFLOWED = 1301
CONFLICTING_DECLARATIONS = 1302
SP_NO_RECURSIVE_CREATE = 1303
SP_ALREADY_EXISTS = 1304
SP_DOES_NOT_EXIST = 1305
SP_DROP_FAILED = 1306
SP_STORE_FAILED = 1307
SP_LILABEL_MISMATCH = 1308
SP_LABEL_REDEFINE = 1309
SP_LABEL_MISMATCH = 1310
SP_UNINIT_VAR = 1311
SP_BADSELECT = 1312
SP_BADRETURN = 1313
SP_BADSTATEMENT = 1314
UPDATE_LOG_DEPRECATED_IGNORED = 1315
UPDATE_LOG_DEPRECATED_TRANSLATED = 1316
QUERY_INTERRUPTED = 1317
SP_WRONG_NO_OF_ARGS = 1318
SP_COND_MISMATCH = 1319
SP_NORETURN = 1320
SP_NORETURNEND = 1321
SP_BAD_CURSOR_QUERY = 1322
SP_BAD_CURSOR_SELECT = 1323
SP_CURSOR_MISMATCH = 1324
SP_CURSOR_ALREADY_OPEN = 1325
SP_CURSOR_NOT_OPEN = 1326
SP_UNDECLARED_VAR = 1327
SP_WRONG_NO_OF_FETCH_ARGS = 1328
SP_FETCH_NO_DATA = 1329
SP_DUP_PARAM = 1330
SP_DUP_VAR = 1331
SP_DUP_COND = 1332
SP_DUP_CURS = 1333
SP_CANT_ALTER = 1334
SP_SUBSELECT_NYI = 1335
STMT_NOT_ALLOWED_IN_SF_OR_TRG = 1336
SP_VARCOND_AFTER_CURSHNDLR = 1337
SP_CURSOR_AFTER_HANDLER = 1338
SP_CASE_NOT_FOUND = 1339
FPARSER_TOO_BIG_FILE = 1340
FPARSER_BAD_HEADER = 1341
FPARSER_EOF_IN_COMMENT = 1342
FPARSER_ERROR_IN_PARAMETER = 1343
FPARSER_EOF_IN_UNKNOWN_PARAMETER = 1344
VIEW_NO_EXPLAIN = 1345
WRONG_OBJECT = 1347
NONUPDATEABLE_COLUMN = 1348
VIEW_SELECT_CLAUSE = 1350
VIEW_SELECT_VARIABLE = 1351
VIEW_SELECT_TMPTABLE = 1352
VIEW_WRONG_LIST = 1353
WARN_VIEW_MERGE = 1354
WARN_VIEW_WITHOUT_KEY = 1355
VIEW_INVALID = 1356
SP_NO_DROP_SP = 1357
TRG_ALREADY_EXISTS = 1359
TRG_DOES_NOT_EXIST = 1360
TRG_ON_VIEW_OR_TEMP_TABLE = 1361
TRG_CANT_CHANGE_ROW = 1362
TRG_NO_SUCH_ROW_IN_TRG = 1363
NO_DEFAULT_FOR_FIELD = 1364
DIVISION_BY_ZERO = 1365
TRUNCATED_WRONG_VALUE_FOR_FIELD = 1366
ILLEGAL_VALUE_FOR_TYPE = 1367
VIEW_NONUPD_CHECK = 1368
VIEW_CHECK_FAILED = 1369
PROCACCESS_DENIED_ERROR = 1370
RELAY_LOG_FAIL = 1371
UNKNOWN_TARGET_BINLOG = 1373
IO_ERR_LOG_INDEX_READ = 1374
BINLOG_PURGE_PROHIBITED = 1375
FSEEK_FAIL = 1376
BINLOG_PURGE_FATAL_ERR = 1377
LOG_IN_USE = 1378
LOG_PURGE_UNKNOWN_ERR = 1379
RELAY_LOG_INIT = 1380
NO_BINARY_LOGGING = 1381
RESERVED_SYNTAX = 1382
PS_MANY_PARAM = 1390
KEY_PART_0 = 1391
VIEW_CHECKSUM = 1392
VIEW_MULTIUPDATE = 1393
VIEW_NO_INSERT_FIELD_LIST = 1394
VIEW_DELETE_MERGE_VIEW = 1395
CANNOT_USER = 1396
XAER_NOTA = 1397
XAER_INVAL = 1398
XAER_RMFAIL = 1399
XAER_OUTSIDE = 1400
XAER_RMERR = 1401
XA_RBROLLBACK = 1402
NONEXISTING_PROC_GRANT = 1403
PROC_AUTO_GRANT_FAIL = 1404
PROC_AUTO_REVOKE_FAIL = 1405
DATA_TOO_LONG = 1406
SP_BAD_SQLSTATE = 1407
STARTUP = 1408
LOAD_FROM_FIXED_SIZE_ROWS_TO_VAR = 1409
CANT_CREATE_USER_WITH_GRANT = 1410
WRONG_VALUE_FOR_TYPE = 1411
TABLE_DEF_CHANGED = 1412
SP_DUP_HANDLER = 1413
SP_NOT_VAR_ARG = 1414
SP_NO_RETSET = 1415
CANT_CREATE_GEOMETRY_OBJECT = 1416
BINLOG_UNSAFE_ROUTINE = 1418
BINLOG_CREATE_ROUTINE_NEED_SUPER = 1419
STMT_HAS_NO_OPEN_CURSOR = 1421
COMMIT_NOT_ALLOWED_IN_SF_OR_TRG = 1422
NO_DEFAULT_FOR_VIEW_FIELD = 1423
SP_NO_RECURSION = 1424
TOO_BIG_SCALE = 1425
TOO_BIG_PRECISION = 1426
M_BIGGER_THAN_D = 1427
WRONG_LOCK_OF_SYSTEM_TABLE = 1428
CONNECT_TO_FOREIGN_DATA_SOURCE = 1429
QUERY_ON_FOREIGN_DATA_SOURCE = 1430
FOREIGN_DATA_SOURCE_DOESNT_EXIST = 1431
FOREIGN_DATA_STRING_INVALID_CANT_CREATE = 1432
FOREIGN_DATA_STRING_INVALID = 1433
TRG_IN_WRONG_SCHEMA = 1435
STACK_OVERRUN_NEED_MORE = 1436
TOO_LONG_BODY = 1437
WARN_CANT_DROP_DEFAULT_KEYCACHE = 1438
TOO_BIG_DISPLAYWIDTH = 1439
XAER_DUPID = 1440
DATETIME_FUNCTION_OVERFLOW = 1441
CANT_UPDATE_USED_TABLE_IN_SF_OR_TRG = 1442
VIEW_PREVENT_UPDATE = 1443
PS_NO_RECURSION = 1444
SP_CANT_SET_AUTOCOMMIT = 1445
VIEW_FRM_NO_USER = 1447
VIEW_OTHER_USER = 1448
NO_SUCH_USER = 1449
FORBID_SCHEMA_CHANGE = 1450
ROW_IS_REFERENCED_2 = 1451
NO_REFERENCED_ROW_2 = 1452
SP_BAD_VAR_SHADOW = 1453
TRG_NO_DEFINER = 1454
OLD_FILE_FORMAT = 1455
SP_RECURSION_LIMIT = 1456
SP_WRONG_NAME = 1458
TABLE_NEEDS_UPGRADE = 1459
SP_NO_AGGREGATE = 1460
MAX_PREPARED_STMT_COUNT_REACHED = 1461
VIEW_RECURSIVE = 1462
NON_GROUPING_FIELD_USED = 1463
TABLE_CANT_HANDLE_SPKEYS = 1464
NO_TRIGGERS_ON_SYSTEM_SCHEMA = 1465
REMOVED_SPACES = 1466
AUTOINC_READ_FAILED = 1467
USERNAME = 1468
HOSTNAME = 1469
WRONG_STRING_LENGTH = 1470
NON_INSERTABLE_TABLE = 1471
ADMIN_WRONG_MRG_TABLE = 1472
TOO_HIGH_LEVEL_OF_NESTING_FOR_SELECT = 1473
NAME_BECOMES_EMPTY = 1474
AMBIGUOUS_FIELD_TERM = 1475
FOREIGN_SERVER_EXISTS = 1476
FOREIGN_SERVER_DOESNT_EXIST = 1477
ILLEGAL_HA_CREATE_OPTION = 1478
PARTITION_REQUIRES_VALUES_ERROR = 1479
PARTITION_WRONG_VALUES_ERROR = 1480
PARTITION_MAXVALUE_ERROR = 1481
PARTITION_WRONG_NO_PART_ERROR = 1484
PARTITION_WRONG_NO_SUBPART_ERROR = 1485
WRONG_EXPR_IN_PARTITION_FUNC_ERROR = 1486
FIELD_NOT_FOUND_PART_ERROR = 1488
INCONSISTENT_PARTITION_INFO_ERROR = 1490
PARTITION_FUNC_NOT_ALLOWED_ERROR = 1491
PARTITIONS_MUST_BE_DEFINED_ERROR = 1492
RANGE_NOT_INCREASING_ERROR = 1493
INCONSISTENT_TYPE_OF_FUNCTIONS_ERROR = 1494
MULTIPLE_DEF_CONST_IN_LIST_PART_ERROR = 1495
PARTITION_ENTRY_ERROR = 1496
MIX_HANDLER_ERROR = 1497
PARTITION_NOT_DEFINED_ERROR = 1498
TOO_MANY_PARTITIONS_ERROR = 1499
SUBPARTITION_ERROR = 1500
CANT_CREATE_HANDLER_FILE = 1501
BLOB_FIELD_IN_PART_FUNC_ERROR = 1502
UNIQUE_KEY_NEED_ALL_FIELDS_IN_PF = 1503
NO_PARTS_ERROR = 1504
PARTITION_MGMT_ON_NONPARTITIONED = 1505
FOREIGN_KEY_ON_PARTITIONED = 1506
DROP_PARTITION_NON_EXISTENT = 1507
DROP_LAST_PARTITION = 1508
COALESCE_ONLY_ON_HASH_PARTITION = 1509
REORG_HASH_ONLY_ON_SAME_NO = 1510
REORG_NO_PARAM_ERROR = 1511
ONLY_ON_RANGE_LIST_PARTITION = 1512
ADD_PARTITION_SUBPART_ERROR = 1513
ADD_PARTITION_NO_NEW_PARTITION = 1514
COALESCE_PARTITION_NO_PARTITION = 1515
REORG_PARTITION_NOT_EXIST = 1516
SAME_NAME_PARTITION = 1517
NO_BINLOG_ERROR = 1518
CONSECUTIVE_REORG_PARTITIONS = 1519
REORG_OUTSIDE_RANGE = 1520
PARTITION_FUNCTION_FAILURE = 1521
LIMITED_PART_RANGE = 1523
PLUGIN_IS_NOT_LOADED = 1524
WRONG_VALUE = 1525
NO_PARTITION_FOR_GIVEN_VALUE = 1526
FILEGROUP_OPTION_ONLY_ONCE = 1527
CREATE_FILEGROUP_FAILED = 1528
DROP_FILEGROUP_FAILED = 1529
TABLESPACE_AUTO_EXTEND_ERROR = 1530
WRONG_SIZE_NUMBER = 1531
SIZE_OVERFLOW_ERROR = 1532
ALTER_FILEGROUP_FAILED = 1533
BINLOG_ROW_LOGGING_FAILED = 1534
EVENT_ALREADY_EXISTS = 1537
EVENT_DOES_NOT_EXIST = 1539
EVENT_INTERVAL_NOT_POSITIVE_OR_TOO_BIG = 1542
EVENT_ENDS_BEFORE_STARTS = 1543
EVENT_EXEC_TIME_IN_THE_PAST = 1544
EVENT_SAME_NAME = 1551
DROP_INDEX_FK = 1553
WARN_DEPRECATED_SYNTAX_WITH_VER = 1554
CANT_LOCK_LOG_TABLE = 1556
FOREIGN_DUPLICATE_KEY_OLD_UNUSED = 1557
COL_COUNT_DOESNT_MATCH_PLEASE_UPDATE = 1558
TEMP_TABLE_PREVENTS_SWITCH_OUT_OF_RBR = 1559
STORED_FUNCTION_PREVENTS_SWITCH_BINLOG_FORMAT = 1560
PARTITION_NO_TEMPORARY = 1562
PARTITION_CONST_DOMAIN_ERROR = 1563
PARTITION_FUNCTION_IS_NOT_ALLOWED = 1564
NULL_IN_VALUES_LESS_THAN = 1566
WRONG_PARTITION_NAME = 1567
CANT_CHANGE_TX_CHARACTERISTICS = 1568
DUP_ENTRY_AUTOINCREMENT_CASE = 1569
EVENT_SET_VAR_ERROR = 1571
PARTITION_MERGE_ERROR = 1572
BASE64_DECODE_ERROR = 1575
EVENT_RECURSION_FORBIDDEN = 1576
ONLY_INTEGERS_ALLOWED = 1578
UNSUPORTED_LOG_ENGINE = 1579
BAD_LOG_STATEMENT = 1580
CANT_RENAME_LOG_TABLE = 1581
WRONG_PARAMCOUNT_TO_NATIVE_FCT = 1582
WRONG_PARAMETERS_TO_NATIVE_FCT = 1583
WRONG_PARAMETERS_TO_STORED_FCT = 1584
NATIVE_FCT_NAME_COLLISION = 1585
DUP_ENTRY_WITH_KEY_NAME = 1586
BINLOG_PURGE_EMFILE = 1587
EVENT_CANNOT_CREATE_IN_THE_PAST = 1588
EVENT_CANNOT_ALTER_IN_THE_PAST = 1589
NO_PARTITION_FOR_GIVEN_VALUE_SILENT = 1591
BINLOG_UNSAFE_STATEMENT = 1592
BINLOG_FATAL_ERROR = 1593
BINLOG_LOGGING_IMPOSSIBLE = 1598
VIEW_NO_CREATION_CTX = 1599
VIEW_INVALID_CREATION_CTX = 1600
TRG_CORRUPTED_FILE = 1602
TRG_NO_CREATION_CTX = 1603
TRG_INVALID_CREATION_CTX = 1604
EVENT_INVALID_CREATION_CTX = 1605
TRG_CANT_OPEN_TABLE = 1606
NO_FORMAT_DESCRIPTION_EVENT_BEFORE_BINLOG_STATEMENT = 1609
SLAVE_CORRUPT_EVENT = 1610
LOG_PURGE_NO_FILE = 1612
XA_RBTIMEOUT = 1613
XA_RBDEADLOCK = 1614
NEED_REPREPARE = 1615
WARN_NO_MASTER_INFO = 1617
WARN_OPTION_IGNORED = 1618
PLUGIN_DELETE_BUILTIN = 1619
WARN_PLUGIN_BUSY = 1620
VARIABLE_IS_READONLY = 1621
WARN_ENGINE_TRANSACTION_ROLLBACK = 1622
SLAVE_HEARTBEAT_VALUE_OUT_OF_RANGE = 1624
NDB_REPLICATION_SCHEMA_ERROR = 1625
CONFLICT_FN_PARSE_ERROR = 1626
EXCEPTIONS_WRITE_ERROR = 1627
TOO_LONG_TABLE_COMMENT = 1628
TOO_LONG_FIELD_COMMENT = 1629
FUNC_INEXISTENT_NAME_COLLISION = 1630
DATABASE_NAME = 1631
TABLE_NAME = 1632
PARTITION_NAME = 1633
SUBPARTITION_NAME = 1634
TEMPORARY_NAME = 1635
RENAMED_NAME = 1636
TOO_MANY_CONCURRENT_TRXS = 1637
WARN_NON_ASCII_SEPARATOR_NOT_IMPLEMENTED = 1638
DEBUG_SYNC_TIMEOUT = 1639
DEBUG_SYNC_HIT_LIMIT = 1640
DUP_SIGNAL_SET = 1641
SIGNAL_WARN = 1642
SIGNAL_NOT_FOUND = 1643
SIGNAL_EXCEPTION = 1644
RESIGNAL_WITHOUT_ACTIVE_HANDLER = 1645
SIGNAL_BAD_CONDITION_TYPE = 1646
WARN_COND_ITEM_TRUNCATED = 1647
COND_ITEM_TOO_LONG = 1648
UNKNOWN_LOCALE = 1649
SLAVE_IGNORE_SERVER_IDS = 1650
SAME_NAME_PARTITION_FIELD = 1652
PARTITION_COLUMN_LIST_ERROR = 1653
WRONG_TYPE_COLUMN_VALUE_ERROR = 1654
TOO_MANY_PARTITION_FUNC_FIELDS_ERROR = 1655
MAXVALUE_IN_VALUES_IN = 1656
TOO_MANY_VALUES_ERROR = 1657
ROW_SINGLE_PARTITION_FIELD_ERROR = 1658
FIELD_TYPE_NOT_ALLOWED_AS_PARTITION_FIELD = 1659
PARTITION_FIELDS_TOO_LONG = 1660
BINLOG_ROW_ENGINE_AND_STMT_ENGINE = 1661
BINLOG_ROW_MODE_AND_STMT_ENGINE = 1662
BINLOG_UNSAFE_AND_STMT_ENGINE = 1663
BINLOG_ROW_INJECTION_AND_STMT_ENGINE = 1664
BINLOG_STMT_MODE_AND_ROW_ENGINE = 1665
BINLOG_ROW_INJECTION_AND_STMT_MODE = 1666
BINLOG_MULTIPLE_ENGINES_AND_SELF_LOGGING_ENGINE = 1667
BINLOG_UNSAFE_LIMIT = 1668
BINLOG_UNSAFE_SYSTEM_TABLE = 1670
BINLOG_UNSAFE_AUTOINC_COLUMNS = 1671
BINLOG_UNSAFE_UDF = 1672
BINLOG_UNSAFE_SYSTEM_VARIABLE = 1673
BINLOG_UNSAFE_SYSTEM_FUNCTION = 1674
BINLOG_UNSAFE_NONTRANS_AFTER_TRANS = 1675
MESSAGE_AND_STATEMENT = 1676
SLAVE_CANT_CREATE_CONVERSION = 1678
INSIDE_TRANSACTION_PREVENTS_SWITCH_BINLOG_FORMAT = 1679
PATH_LENGTH = 1680
WARN_DEPRECATED_SYNTAX_NO_REPLACEMENT = 1681
WRONG_NATIVE_TABLE_STRUCTURE = 1682
WRONG_PERFSCHEMA_USAGE = 1683
WARN_I_S_SKIPPED_TABLE = 1684
INSIDE_TRANSACTION_PREVENTS_SWITCH_BINLOG_DIRECT = 1685
STORED_FUNCTION_PREVENTS_SWITCH_BINLOG_DIRECT = 1686
SPATIAL_MUST_HAVE_GEOM_COL = 1687
TOO_LONG_INDEX_COMMENT = 1688
LOCK_ABORTED = 1689
DATA_OUT_OF_RANGE = 1690
WRONG_SPVAR_TYPE_IN_LIMIT = 1691
BINLOG_UNSAFE_MULTIPLE_ENGINES_AND_SELF_LOGGING_ENGINE = 1692
BINLOG_UNSAFE_MIXED_STATEMENT = 1693
INSIDE_TRANSACTION_PREVENTS_SWITCH_SQL_LOG_BIN = 1694
STORED_FUNCTION_PREVENTS_SWITCH_SQL_LOG_BIN = 1695
FAILED_READ_FROM_PAR_FILE = 1696
VALUES_IS_NOT_INT_TYPE_ERROR = 1697
ACCESS_DENIED_NO_PASSWORD_ERROR = 1698
SET_PASSWORD_AUTH_PLUGIN = 1699
TRUNCATE_ILLEGAL_FK = 1701
PLUGIN_IS_PERMANENT = 1702
SLAVE_HEARTBEAT_VALUE_OUT_OF_RANGE_MIN = 1703
SLAVE_HEARTBEAT_VALUE_OUT_OF_RANGE_MAX = 1704
STMT_CACHE_FULL = 1705
MULTI_UPDATE_KEY_CONFLICT = 1706
TABLE_NEEDS_REBUILD = 1707
WARN_OPTION_BELOW_LIMIT = 1708
INDEX_COLUMN_TOO_LONG = 1709
ERROR_IN_TRIGGER_BODY = 1710
ERROR_IN_UNKNOWN_TRIGGER_BODY = 1711
INDEX_CORRUPT = 1712
UNDO_RECORD_TOO_BIG = 1713
BINLOG_UNSAFE_INSERT_IGNORE_SELECT = 1714
BINLOG_UNSAFE_INSERT_SELECT_UPDATE = 1715
BINLOG_UNSAFE_REPLACE_SELECT = 1716
BINLOG_UNSAFE_CREATE_IGNORE_SELECT = 1717
BINLOG_UNSAFE_CREATE_REPLACE_SELECT = 1718
BINLOG_UNSAFE_UPDATE_IGNORE = 1719
PLUGIN_NO_UNINSTALL = 1720
PLUGIN_NO_INSTALL = 1721
BINLOG_UNSAFE_WRITE_AUTOINC_SELECT = 1722
BINLOG_UNSAFE_CREATE_SELECT_AUTOINC = 1723
BINLOG_UNSAFE_INSERT_TWO_KEYS = 1724
TABLE_IN_FK_CHECK = 1725
UNSUPPORTED_ENGINE = 1726
BINLOG_UNSAFE_AUTOINC_NOT_FIRST = 1727
CANNOT_LOAD_FROM_TABLE_V2 = 1728
MASTER_DELAY_VALUE_OUT_OF_RANGE = 1729
ONLY_FD_AND_RBR_EVENTS_ALLOWED_IN_BINLOG_STATEMENT = 1730
PARTITION_EXCHANGE_DIFFERENT_OPTION = 1731
PARTITION_EXCHANGE_PART_TABLE = 1732
PARTITION_EXCHANGE_TEMP_TABLE = 1733
PARTITION_INSTEAD_OF_SUBPARTITION = 1734
UNKNOWN_PARTITION = 1735
TABLES_DIFFERENT_METADATA = 1736
ROW_DOES_NOT_MATCH_PARTITION = 1737
BINLOG_CACHE_SIZE_GREATER_THAN_MAX = 1738
WARN_INDEX_NOT_APPLICABLE = 1739
PARTITION_EXCHANGE_FOREIGN_KEY = 1740
RPL_INFO_DATA_TOO_LONG = 1742
BINLOG_STMT_CACHE_SIZE_GREATER_THAN_MAX = 1745
CANT_UPDATE_TABLE_IN_CREATE_TABLE_SELECT = 1746
PARTITION_CLAUSE_ON_NONPARTITIONED = 1747
ROW_DOES_NOT_MATCH_GIVEN_PARTITION_SET = 1748
CHANGE_RPL_INFO_REPOSITORY_FAILURE = 1750
WARNING_NOT_COMPLETE_ROLLBACK_WITH_CREATED_TEMP_TABLE = 1751
WARNING_NOT_COMPLETE_ROLLBACK_WITH_DROPPED_TEMP_TABLE = 1752
MTS_FEATURE_IS_NOT_SUPPORTED = 1753
MTS_UPDATED_DBS_GREATER_MAX = 1754
MTS_CANT_PARALLEL = 1755
MTS_INCONSISTENT_DATA = 1756
FULLTEXT_NOT_SUPPORTED_WITH_PARTITIONING = 1757
DA_INVALID_CONDITION_NUMBER = 1758
INSECURE_PLAIN_TEXT = 1759
INSECURE_CHANGE_MASTER = 1760
FOREIGN_DUPLICATE_KEY_WITH_CHILD_INFO = 1761
FOREIGN_DUPLICATE_KEY_WITHOUT_CHILD_INFO = 1762
SQLTHREAD_WITH_SECURE_SLAVE = 1763
TABLE_HAS_NO_FT = 1764
VARIABLE_NOT_SETTABLE_IN_SF_OR_TRIGGER = 1765
VARIABLE_NOT_SETTABLE_IN_TRANSACTION = 1766
SET_STATEMENT_CANNOT_INVOKE_FUNCTION = 1769
GTID_NEXT_CANT_BE_AUTOMATIC_IF_GTID_NEXT_LIST_IS_NON_NULL = 1770
MALFORMED_GTID_SET_SPECIFICATION = 1772
MALFORMED_GTID_SET_ENCODING = 1773
MALFORMED_GTID_SPECIFICATION = 1774
GNO_EXHAUSTED = 1775
BAD_SLAVE_AUTO_POSITION = 1776
AUTO_POSITION_REQUIRES_GTID_MODE_NOT_OFF = 1777
CANT_DO_IMPLICIT_COMMIT_IN_TRX_WHEN_GTID_NEXT_IS_SET = 1778
GTID_MODE_ON_REQUIRES_ENFORCE_GTID_CONSISTENCY_ON = 1779
CANT_SET_GTID_NEXT_TO_GTID_WHEN_GTID_MODE_IS_OFF = 1781
CANT_SET_GTID_NEXT_TO_ANONYMOUS_WHEN_GTID_MODE_IS_ON = 1782
CANT_SET_GTID_NEXT_LIST_TO_NON_NULL_WHEN_GTID_MODE_IS_OFF = 1783
GTID_UNSAFE_NON_TRANSACTIONAL_TABLE = 1785
GTID_UNSAFE_CREATE_SELECT = 1786
GTID_UNSAFE_CREATE_DROP_TEMPORARY_TABLE_IN_TRANSACTION = 1787
GTID_MODE_CAN_ONLY_CHANGE_ONE_STEP_AT_A_TIME = 1788
MASTER_HAS_PURGED_REQUIRED_GTIDS = 1789
CANT_SET_GTID_NEXT_WHEN_OWNING_GTID = 1790
UNKNOWN_EXPLAIN_FORMAT = 1791
CANT_EXECUTE_IN_READ_ONLY_TRANSACTION = 1792
TOO_LONG_TABLE_PARTITION_COMMENT = 1793
SLAVE_CONFIGURATION = 1794
INNODB_FT_LIMIT = 1795
INNODB_NO_FT_TEMP_TABLE = 1796
INNODB_FT_WRONG_DOCID_COLUMN = 1797
INNODB_FT_WRONG_DOCID_INDEX = 1798
INNODB_ONLINE_LOG_TOO_BIG = 1799
UNKNOWN_ALTER_ALGORITHM = 1800
UNKNOWN_ALTER_LOCK = 1801
MTS_CHANGE_MASTER_CANT_RUN_WITH_GAPS = 1802
MTS_RECOVERY_FAILURE = 1803
MTS_RESET_WORKERS = 1804
COL_COUNT_DOESNT_MATCH_CORRUPTED_V2 = 1805
SLAVE_SILENT_RETRY_TRANSACTION = 1806
DISCARD_FK_CHECKS_RUNNING = 1807
TABLE_SCHEMA_MISMATCH = 1808
TABLE_IN_SYSTEM_TABLESPACE = 1809
IO_READ_ERROR = 1810
IO_WRITE_ERROR = 1811
TABLESPACE_MISSING = 1812
TABLESPACE_EXISTS = 1813
TABLESPACE_DISCARDED = 1814
INTERNAL_ERROR = 1815
INNODB_IMPORT_ERROR = 1816
INNODB_INDEX_CORRUPT = 1817
INVALID_YEAR_COLUMN_LENGTH = 1818
NOT_VALID_PASSWORD = 1819
MUST_CHANGE_PASSWORD = 1820
FK_NO_INDEX_CHILD = 1821
FK_NO_INDEX_PARENT = 1822
FK_FAIL_ADD_SYSTEM = 1823
FK_CANNOT_OPEN_PARENT = 1824
FK_INCORRECT_OPTION = 1825
FK_DUP_NAME = 1826
PASSWORD_FORMAT = 1827
FK_COLUMN_CANNOT_DROP = 1828
FK_COLUMN_CANNOT_DROP_CHILD = 1829
FK_COLUMN_NOT_NULL = 1830
DUP_INDEX = 1831
FK_COLUMN_CANNOT_CHANGE = 1832
FK_COLUMN_CANNOT_CHANGE_CHILD = 1833
MALFORMED_PACKET = 1835
READ_ONLY_MODE = 1836
GTID_NEXT_TYPE_UNDEFINED_GTID = 1837
VARIABLE_NOT_SETTABLE_IN_SP = 1838
CANT_SET_GTID_PURGED_WHEN_GTID_EXECUTED_IS_NOT_EMPTY = 1840
CANT_SET_GTID_PURGED_WHEN_OWNED_GTIDS_IS_NOT_EMPTY = 1841
GTID_PURGED_WAS_CHANGED = 1842
GTID_EXECUTED_WAS_CHANGED = 1843
BINLOG_STMT_MODE_AND_NO_REPL_TABLES = 1844
ALTER_OPERATION_NOT_SUPPORTED = 1845
ALTER_OPERATION_NOT_SUPPORTED_REASON = 1846
ALTER_OPERATION_NOT_SUPPORTED_REASON_COPY = 1847
ALTER_OPERATION_NOT_SUPPORTED_REASON_PARTITION = 1848
ALTER_OPERATION_NOT_SUPPORTED_REASON_FK_RENAME = 1849
ALTER_OPERATION_NOT_SUPPORTED_REASON_COLUMN_TYPE = 1850
ALTER_OPERATION_NOT_SUPPORTED_REASON_FK_CHECK = 1851
ALTER_OPERATION_NOT_SUPPORTED_REASON_NOPK = 1853
ALTER_OPERATION_NOT_SUPPORTED_REASON_AUTOINC = 1854
ALTER_OPERATION_NOT_SUPPORTED_REASON_HIDDEN_FTS = 1855
ALTER_OPERATION_NOT_SUPPORTED_REASON_CHANGE_FTS = 1856
ALTER_OPERATION_NOT_SUPPORTED_REASON_FTS = 1857
SQL_SLAVE_SKIP_COUNTER_NOT_SETTABLE_IN_GTID_MODE = 1858
DUP_UNKNOWN_IN_INDEX = 1859
IDENT_CAUSES_TOO_LONG_PATH = 1860
ALTER_OPERATION_NOT_SUPPORTED_REASON_NOT_NULL = 1861
MUST_CHANGE_PASSWORD_LOGIN = 1862
ROW_IN_WRONG_PARTITION = 1863
MTS_EVENT_BIGGER_PENDING_JOBS_SIZE_MAX = 1864
BINLOG_LOGICAL_CORRUPTION = 1866
WARN_PURGE_LOG_IN_USE = 1867
WARN_PURGE_LOG_IS_ACTIVE = 1868
AUTO_INCREMENT_CONFLICT = 1869
WARN_ON_BLOCKHOLE_IN_RBR = 1870
SLAVE_MI_INIT_REPOSITORY = 1871
SLAVE_RLI_INIT_REPOSITORY = 1872
ACCESS_DENIED_CHANGE_USER_ERROR = 1873
INNODB_READ_ONLY = 1874
STOP_SLAVE_SQL_THREAD_TIMEOUT = 1875
STOP_SLAVE_IO_THREAD_TIMEOUT = 1876
TABLE_CORRUPT = 1877
TEMP_FILE_WRITE_FAILURE = 1878
INNODB_FT_AUX_NOT_HEX_ID = 1879
OLD_TEMPORALS_UPGRADED = 1880
INNODB_FORCED_RECOVERY = 1881
AES_INVALID_IV = 1882
PLUGIN_CANNOT_BE_UNINSTALLED = 1883
GTID_UNSAFE_BINLOG_SPLITTABLE_STATEMENT_AND_ASSIGNED_GTID = 1884
SLAVE_HAS_MORE_GTIDS_THAN_MASTER = 1885
MISSING_KEY = 1886
ERROR_LAST = 1973
