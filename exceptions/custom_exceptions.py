class IncorrectDateOrderException(Exception):
    def __init__(self, message: str = None):
        if message is None:
            Exception.__init__(self)
        else:
            Exception.__init__(self, message)


class InvalidDayValue(Exception):
    def __init__(self, message: str = None):
        if message is None:
            Exception.__init__(self)
        else:
            Exception.__init__(self, message)


class InvalidEmailException(Exception):
    def __init__(self, message: str = None):
        if message is None:
            Exception.__init__(self)
        else:
            Exception.__init__(self, message)


class InvalidMonthInputException(Exception):
    def __init__(self, message: str = None):
        if message is None:
            Exception.__init__(self)
        else:
            Exception.__init__(self, message)


class InvalidPhoneNumberException(Exception):
    def __init__(self, message: str = None):
        if message is None:
            Exception.__init__(self)
        else:
            Exception.__init__(self, message)


class InvalidStateException(Exception):
    def __init__(self, message: str = None):
        if message is None:
            Exception.__init__(self)
        else:
            Exception.__init__(self, message)


class InvalidTransactionType(Exception):
    def __init__(self, message: str = None):
        if message is None:
            Exception.__init__(self)
        else:
            Exception.__init__(self, message)


class InvalidYearException(Exception):
    def __init__(self, message: str = None):
        if message is None:
            Exception.__init__(self)
        else:
            Exception.__init__(self, message)


class InvalidZipcodeException(Exception):
    def __init__(self, message: str = None):
        if message is None:
            Exception.__init__(self)
        else:
            Exception.__init__(self, message)


class NoResultsFoundException(Exception):
    def __init__(self, message: str = None):
        if message is None:
            Exception.__init__(self)
        else:
            Exception.__init__(self, message)


class WrongCreditCardFormat(Exception):
    def __init__(self, message: str = None):
        if message is None:
            Exception.__init__(self)
        else:
            Exception.__init__(self, message)


class WrongSsnFormatException(Exception):
    def __init__(self, message: str = None):
        if message is None:
            Exception.__init__(self)
        else:
            Exception.__init__(self, message)
