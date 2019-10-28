from datetime import datetime


class Customer:
    """ Representation of a customer from the CDW_SAPP database.
        Author: Aris Fernandez"""

    def __init__(self):
        self.__ssn: int = None
        self.__cust_phone: int = None
        self.__apt_num: str = None
        self.__credit_card_num: str = None
        self.__city: str = None
        self.__country: str = None
        self.__email: str = None
        self.__state: str = None
        self.__zipcode: str = None
        self.__first_name: str = None
        self.__last_name: str = None
        self.__middle_name: str = None
        self.__street_name: str = None
        self.__last_updated: datetime = None

# *************************************************************************************************** #
#                                      GETTERS AND SETTERS                                            #
# *************************************************************************************************** #

    def get_ssn(self) -> int:
        return self.__ssn

    def set_ssn(self, ssn: int):
        self.__ssn = ssn

    def get_cust_phone(self) -> int:
        return self.__cust_phone

    def set_cust_phone(self, cust_phone: int):
        self.__cust_phone = cust_phone

    def get_apt_num(self) -> str:
        return self.__apt_num

    def set_apt_num(self, apt_num: str):
        self.__apt_num = apt_num

    def get_credit_card__num(self) -> str:
        return self.__credit_card_num

    def set_credit_card_num(self, credit_card_num: str):
        self.__credit_card_num = credit_card_num

    def get_city(self) -> str:
        return self.__city

    def set_city(self, city: str):
        self.__city = city

    def get_country(self) -> str:
        return self.__country

    def set_country(self, country: str):
        self.__country = country

    def get_email(self) -> str:
        return self.__email

    def set_email(self, email: str):
        self.__email = email

    def get_state(self) -> str:
        return self.__state

    def set_state(self, state: str):
        self.__state = state

    def get_zipcode(self) -> str:
        return self.__zipcode

    def set_zipcode(self, zipcode: str):
        self.__zipcode = zipcode

    def get_first_name(self) -> str:
        return self.__first_name

    def set_first_name(self, first_name: str):
        self.__first_name = first_name

    def get_last_name(self) -> str:
        return self.__last_name

    def set_last_name(self, last_name: str):
        self.__last_name = last_name

    def get_middle_name(self) -> str:
        return self.__middle_name

    def set_middle_name(self, middle_name: str):
        self.__middle_name = middle_name

    def get_street_name(self) -> str:
        return self.__street_name

    def set_street_name(self, street_name: str):
        self.__street_name = street_name

    def get_last_updated(self) -> datetime:
        return self.__last_updated

    def set_last_updated(self, last_updated: datetime):
        self.__last_updated = last_updated

# *************************************************************************************************** #
#                                             METHODS			                                      #
# *************************************************************************************************** #

    def __str__(self) -> str:
        output = "FULL NAME: " + str(self.__first_name) + " " + str(self.__middle_name) + " " + \
                 str(self.__last_name) + "\n\n"
        output += "ADDRESS: " + str(self.__apt_num) + " " + str(self.__street_name) + ". " + str(self.__city) + ", " + \
                  str(self.__state) + " " + str(self.__zipcode) + ". " + str(self.__country) + "\n\n"
        output += "E-MAIL: " + str(self.__email) + "\n\n"
        output += "PHONE NO.: " + str(self.__cust_phone) + "\n\n"
        output += "CREDIT CARD NO.: " + str(self.__credit_card_num) + "\n\n"
        output += "SOCIAL SECURITY: " + str(self.__ssn) + "\n\n"
        output += "LAST UPDATE: " + self.__last_updated.strftime("%Y-%m-%d %H:%M:%S")
        return output

    def csv_format(self) -> str:
        delimiter = ","
        f_name = str(self.__first_name)
        m_name = str(self.__middle_name)
        l_name = str(self.__last_name)
        apt_no = str(self.__apt_num)
        street = str(self.__street_name)
        city = str(self.__city)
        state = str(self.__state)
        zipcode = str(self.__zipcode)
        country = str(self.__country)
        email = str(self.__email)
        phone = str(self.__cust_phone)
        credit_card_no = str(self.__credit_card_num)
        ssn = str(self.__ssn)
        updated = str(self.__last_updated)
        return f_name + delimiter + m_name + delimiter + l_name + delimiter + ssn + delimiter + credit_card_no + \
               delimiter + apt_no + delimiter + street + delimiter + city + delimiter + state + delimiter + country + \
               delimiter + zipcode + delimiter + phone + delimiter + email + delimiter + updated + "\n"

    def info_as_table(self) -> str:
        delimiter = " "
        f_name = f"{str(self.__first_name):^12}"
        m_name = f"{str(self.__middle_name):^12}"
        l_name = f"{str(self.__last_name):^15}"
        apt_no = f"{str(self.__apt_num):^5}"
        street = f"{str(self.__street_name):^20}"
        city = f"{str(self.__city):^20}"
        state = f"{str(self.__state):^7}"
        zipcode = f"{str(self.__zipcode):^8}"
        country = f"{str(self.__country):^15}"
        email = f"{str(self.__email):^28}"
        phone = f"{str(self.__cust_phone):^13}"
        updated = f"{str(self.__last_updated):^20}"
        return f_name + delimiter + m_name + delimiter + l_name + delimiter + apt_no + delimiter + street + \
               delimiter + city + delimiter + state + delimiter + country + delimiter + zipcode + delimiter + \
               phone + delimiter + email + delimiter + updated + "\n"
