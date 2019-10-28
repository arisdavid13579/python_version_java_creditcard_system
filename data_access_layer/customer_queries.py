# 2.1
CUSTOMER_DETAILS_QUERY: str = \
    "SELECT CDW_SAPP_CUSTOMER.* " \
    "FROM CDW_SAPP_CUSTOMER " \
    "WHERE SSN = ? AND CREDIT_CARD_NO = ?"

# 2.2
CUSTOMER_MODIFY_DETAILS_QUERY: str = \
    "UPDATE cdw_sapp_customer " \
    "SET REPLACE_COLUMN_NAME = ?, LAST_UPDATED = ?  " \
    "WHERE ((SSN = ? ) AND (CREDIT_CARD_NO = ? ))"

# 2.3
CUSTOMER_BILL_QUERY: str = \
    "SELECT cc.*, cust.CUST_ZIP " \
    "FROM CDW_SAPP_CREDITCARD  cc " \
    "   JOIN cdw_sapp_customer cust ON cc.CUST_SSN = cust.SSN " \
    "WHERE (CUST_SSN = ? AND cc.CREDIT_CARD_NO = ? ) AND (YEAR = ? AND MONTH = ? ) " \
    "ORDER BY DAY DESC"

# 2.4
CUSTOMER_TRANSACTIONS_QUERY: str = \
    "SELECT * " \
    "FROM CDW_SAPP_CREDITCARD " \
    "WHERE (CUST_SSN = ? AND CREDIT_CARD_NO = ?) " \
    "    AND (DATE_FORMAT(STR_TO_DATE(CONCAT(DAY,'/', MONTH , '/', YEAR) ,'%d/%m/%Y'),'%Y/%m/%d') " \
    "    BETWEEN DATE_FORMAT(STR_TO_DATE(CONCAT(?,'/', ? , '/', ?) ,'%d/%m/%Y'),'%Y/%m/%d') " \
    "    AND DATE_FORMAT(STR_TO_DATE(CONCAT(? ,'/', ? , '/', ?) ,'%d/%m/%Y'),'%Y/%m/%d')) " \
    "ORDER BY YEAR DESC, MONTH DESC, DAY DESC"
