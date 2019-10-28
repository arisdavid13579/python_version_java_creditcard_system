from abc import ABC, abstractmethod
from typing import Any
from transfer_objects.customer import Customer
from transfer_objects.transaction_list import TransactionList


class CustomersDaoI(ABC):
    """Defines abstractly the methods needed to handle the customer data.

    :Author: Aris Fernandez
    """

    @abstractmethod
    def get_customer_details(self, ssn: str, credit_card_no: str) -> Customer:  # Must raise  NoResultsFoundException
        """Queries the CDW_SAPP customer table to obtain the first name, last name, middle name, street name,
         social security number, phone number, city,country, e-mail address, state, credit card number, and time stamp
         of last update for a given customer with the given credit card number and social security number.

         Parameters
         ----------
         ssn: str
             The customer's social security number.
         credit_card_no : str
             The customer's credit card number.

         Returns
         -------
         Customer
             A Customer object containing all of the customer's information.

         Raises
         ------
         NoResultsFoundException
             If no customer is found for the given social security number and credit
             card number.
         """

    @abstractmethod
    def update_customer_details(self, ssn: str, credit_card_no: str, column_name: str, column_value: Any) -> bool:
        """
         For a given customer (Social security number and credit card), updates one
         field of information in the customer table.

         Parameters
         ----------

         ssn: str
             The customer's social security number.
         credit_card_no: str
             The customer's credit card number.
         column_name: str
             The column name of the field to be updated.
         column_value: Any
             The value with which the field will be updated.
         Returns
         --------
         bool
             True if the update was successful, otherwise it returns false.
        """

    @abstractmethod
    def get_customer_bill(self, ssn: str, credit_card_no: str,
                          month: int, year: int) -> TransactionList:  # Must raise  NoResultsFoundException
        """
        Generates a list of transactions for a given customer in a given month, in a
        given year.

        Parameters
        ----------
        ssn: str
            The customer's social security number.
        credit_card_no: str
            The customer's credit card number.
        month: int
            The month for which the customer bill will be generated.
        year: int
            The year during which the transactions occurred.

        Returns
        -------
        TransactionList
            A TransactionList object containing the list of transactions for the bill.

        Raises
        ------
         NoResultsFoundException
            If no transactions are found with the given information.
        """

    @abstractmethod
    def get_transaction_range(self, ssn: str, credit_card_no: str, from_day: int,
                              from_month: int, from_year: int, to_day: int, to_month: int,
                              to_year: int) -> TransactionList:  # Must raise  NoResultsFoundException
        """
        For a given customer, generates a list of transactions happening between two
        given dates.


        Parameters
        ----------
        ssn: str
            The customer's social security number.
        credit_card_no: str
            The customer's credit card number.
        from_day: int
            The day of initial date in the range.
        from_month: int
            The month of initial date in the range.
        from_year: int
            The year of initial date in the range.
        to_day: int
            The day of final date in the range.
        to_month: int
            The month of final date in the range.
        to_year:int
            The year of final date in the range.

        Returns
        -------
        TransactionList
            A TransactionList object with a list transactions happening in the given date range.

        Raises
        ------
        NoResultsFoundException
            If no transactions are found with the given information.
        """