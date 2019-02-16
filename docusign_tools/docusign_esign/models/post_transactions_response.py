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


class PostTransactionsResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, document_data=None, transaction_sid=None):
        """
        PostTransactionsResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'document_data': 'str',
            'transaction_sid': 'str'
        }

        self.attribute_map = {
            'document_data': 'documentData',
            'transaction_sid': 'transactionSid'
        }

        self._document_data = document_data
        self._transaction_sid = transaction_sid

    @property
    def document_data(self):
        """
        Gets the document_data of this PostTransactionsResponse.
        

        :return: The document_data of this PostTransactionsResponse.
        :rtype: str
        """
        return self._document_data

    @document_data.setter
    def document_data(self, document_data):
        """
        Sets the document_data of this PostTransactionsResponse.
        

        :param document_data: The document_data of this PostTransactionsResponse.
        :type: str
        """

        self._document_data = document_data

    @property
    def transaction_sid(self):
        """
        Gets the transaction_sid of this PostTransactionsResponse.
        

        :return: The transaction_sid of this PostTransactionsResponse.
        :rtype: str
        """
        return self._transaction_sid

    @transaction_sid.setter
    def transaction_sid(self, transaction_sid):
        """
        Sets the transaction_sid of this PostTransactionsResponse.
        

        :param transaction_sid: The transaction_sid of this PostTransactionsResponse.
        :type: str
        """

        self._transaction_sid = transaction_sid

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
