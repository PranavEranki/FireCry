# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CreditCardInformation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, address=None, card_number=None, card_type=None, expiration_month=None, expiration_year=None, name_on_card=None):
        """
        CreditCardInformation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'address': 'AddressInformation',
            'card_number': 'str',
            'card_type': 'str',
            'expiration_month': 'str',
            'expiration_year': 'str',
            'name_on_card': 'str'
        }

        self.attribute_map = {
            'address': 'address',
            'card_number': 'cardNumber',
            'card_type': 'cardType',
            'expiration_month': 'expirationMonth',
            'expiration_year': 'expirationYear',
            'name_on_card': 'nameOnCard'
        }

        self._address = address
        self._card_number = card_number
        self._card_type = card_type
        self._expiration_month = expiration_month
        self._expiration_year = expiration_year
        self._name_on_card = name_on_card

    @property
    def address(self):
        """
        Gets the address of this CreditCardInformation.

        :return: The address of this CreditCardInformation.
        :rtype: AddressInformation
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this CreditCardInformation.

        :param address: The address of this CreditCardInformation.
        :type: AddressInformation
        """

        self._address = address

    @property
    def card_number(self):
        """
        Gets the card_number of this CreditCardInformation.
        The number on the credit card.

        :return: The card_number of this CreditCardInformation.
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """
        Sets the card_number of this CreditCardInformation.
        The number on the credit card.

        :param card_number: The card_number of this CreditCardInformation.
        :type: str
        """

        self._card_number = card_number

    @property
    def card_type(self):
        """
        Gets the card_type of this CreditCardInformation.
        The credit card type. Valid values are: visa, mastercard, or amex.

        :return: The card_type of this CreditCardInformation.
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """
        Sets the card_type of this CreditCardInformation.
        The credit card type. Valid values are: visa, mastercard, or amex.

        :param card_type: The card_type of this CreditCardInformation.
        :type: str
        """

        self._card_type = card_type

    @property
    def expiration_month(self):
        """
        Gets the expiration_month of this CreditCardInformation.
        The month that the credit card expires (1-12).

        :return: The expiration_month of this CreditCardInformation.
        :rtype: str
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """
        Sets the expiration_month of this CreditCardInformation.
        The month that the credit card expires (1-12).

        :param expiration_month: The expiration_month of this CreditCardInformation.
        :type: str
        """

        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """
        Gets the expiration_year of this CreditCardInformation.
        The year 4 digit year in which the credit card expires.

        :return: The expiration_year of this CreditCardInformation.
        :rtype: str
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """
        Sets the expiration_year of this CreditCardInformation.
        The year 4 digit year in which the credit card expires.

        :param expiration_year: The expiration_year of this CreditCardInformation.
        :type: str
        """

        self._expiration_year = expiration_year

    @property
    def name_on_card(self):
        """
        Gets the name_on_card of this CreditCardInformation.
        The exact name printed on the credit card.

        :return: The name_on_card of this CreditCardInformation.
        :rtype: str
        """
        return self._name_on_card

    @name_on_card.setter
    def name_on_card(self, name_on_card):
        """
        Sets the name_on_card of this CreditCardInformation.
        The exact name printed on the credit card.

        :param name_on_card: The name_on_card of this CreditCardInformation.
        :type: str
        """

        self._name_on_card = name_on_card

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
