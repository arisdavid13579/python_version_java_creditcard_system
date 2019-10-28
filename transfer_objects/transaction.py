from datetime import datetime


class Transaction:
    """Representation of a transaction from the CDW_SAPP database.
    Author: Aris Fernandez"""

    def __init__(self):
        self.__branch_code: int = None
        self.__transaction_day: int = None
        self.__transaction_month: int = None
        self.__transaction_year: int = None
        self.__transaction_id: int = None
        self.__cust_ssn: int = None
        self.__aggregate_count: int = None
        self.__transaction_value: float = None
        self.__credit_card_num: str = None
        self.__transaction_type: str = None
        self.__last_updated: datetime = None

# *************************************************************************************************** #
#                                      GETTERS AND SETTERS                                            #
# *************************************************************************************************** #

    def get_branch_code(self) -> int:
        return self.__branch_code

    def set_branch_code(self, branch_code: int):
        self.__branch_code = branch_code

    def get_transaction_day(self) -> int:
        return self.__transaction_day

    def set_transaction_day(self, transaction_day: int):
        self.__transaction_day = transaction_day

    def get_transaction_month(self) -> int:
        return self.__transaction_month

    def set_transaction_month(self, transaction_month: int):
        self.__transaction_month = transaction_month

    def get_transaction_year(self) -> int:
        return self.__transaction_year

    def set_transaction_year(self, transaction_year: int):
        self.__transaction_year = transaction_year

    def get_transaction_id(self) -> int:
        return self.__transaction_id

    def set_transaction_id(self, transaction_id: int):
        self.__transaction_id = transaction_id

    def get_cust_ssn(self) -> int:
        return self.__cust_ssn

    def set_cust_ssn(self, cust_ssn: int):
        self.__cust_ssn = cust_ssn

    def get_aggregate_count(self) -> int:
        return self.__aggregate_count

    def set_aggregate_count(self, aggregate_count: int):
        self.__aggregate_count = aggregate_count

    def get_transaction_value(self) -> float:
        return self.__transaction_value

    def set_transaction_value(self, transaction_value: float):
        self.__transaction_value = transaction_value

    def get_credit_card_num(self) -> str:
        return self.__credit_card_num

    def set_credit_card_num(self, credit_card_num: str):
        self.__credit_card_num = credit_card_num

    def get_transaction_type(self) -> str:
        return self.__transaction_type

    def set_transaction_type(self, transaction_type: str):
        self.__transaction_type = transaction_type

    def get_last_updated(self) -> datetime:
        return self.__last_updated

    def set_last_updated(self, last_updated: datetime):
        self.__last_updated = last_updated

# *************************************************************************************************** #
#                                             METHODS			                                      #
# *************************************************************************************************** #

    def __str__(self) -> str:
        delimiter = "     "
        amount = f'{f"{self.__transaction_value:.2f}":^9}'
        branch = f"{self.__branch_code:^7}"
        day = f'{f"{self.__transaction_day:0>2d}":^2}'
        month = f'{f"{self.__transaction_month:0>2d}":^2}'
        year = f'{f"{self.__transaction_year:0>4d}":^4}'
        date = day + "-" + month + "-" + year
        id = f"{self.__transaction_id:^5}"
        card_no = f"{self.__credit_card_num:^16}"
        tran_type = f"{self.__transaction_type:^13}"
        updated = self.__last_updated.strftime("%Y-%m-%d %H:%M:%S")
        return id + delimiter + date + delimiter + card_no + delimiter + tran_type + delimiter + branch +\
            delimiter + amount + delimiter + updated

    def csv_format(self) -> str:
        delimiter = ","
        branch = f"{self.__branch_code}"
        day = f"{self.__transaction_day}"
        month = f"{self.__transaction_month}"
        year = f"{self.__transaction_year}"
        id = f"{self.__transaction_id}"
        value = f"{self.__transaction_value}"
        card_no = f"{self.__credit_card_num}"
        tran_type = f"{self.__transaction_type}"
        ssn = f"{self.__cust_ssn}"
        updated = self.__last_updated.strftime("%Y-%m-%d %H:%M:%S")

        return id + delimiter + day + delimiter + month + delimiter + year + delimiter + card_no + delimiter +\
            ssn + delimiter + branch + delimiter + tran_type + delimiter + value + delimiter + updated + "\n"