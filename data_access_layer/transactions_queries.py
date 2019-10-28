# 1.1
TRANSACTIONS_BY_ZIPCODE_QUERY: str = \
    "SELECT cc.* " \
    "FROM cdw_sapp_customer cust " \
    "   INNER JOIN cdw_sapp_creditcard cc " \
    "   ON cc.credit_card_no = cust.credit_card_no " \
    "   AND cc.CUST_SSN = cust.SSN " \
    "WHERE cust.cust_zip = ? AND cc.MONTH = ? AND cc.YEAR = ? " \
    "ORDER BY 2 DESC"
# 1.2
TRANSACTIONS_BY_TYPE_QUERY: str = \
    "SELECT COUNT(TRANSACTION_VALUE) AS 'Transaction_Counts', SUM(TRANSACTION_VALUE) AS 'Sum_Values' " \
    "FROM cdw_sapp_creditcard " \
    "WHERE transaction_type = ?"
# 1.3
TRANSACTIONS_BY_STATE_QUERY: str = \
    "SELECT COUNT(TRANSACTION_VALUE) AS 'Transaction_Counts', SUM(TRANSACTION_VALUE) AS 'Sum_Values' " \
    "FROM cdw_sapp_creditcard " \
    "   INNER JOIN cdw_sapp_branch ON cdw_sapp_creditcard.branch_code = cdw_sapp_branch.BRANCH_CODE " \
    "WHERE BRANCH_STATE = ?"

# List of allowed transaction types
ALLOWED_TRANSACTION_TYPES_QUERY: str = \
    "SELECT DISTINCT transaction_type " \
    "FROM cdw_sapp_creditcard"
