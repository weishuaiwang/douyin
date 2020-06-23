# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
"""

import pprint
import re  # noqa: F401

import six


class PoiExtHotelOrderCancelBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'supplier_ext_id': 'str',
        'order_id': 'str',
        'order_ext_id': 'str'
    }

    attribute_map = {
        'supplier_ext_id': 'supplier_ext_id',
        'order_id': 'order_id',
        'order_ext_id': 'order_ext_id'
    }

    def __init__(self, supplier_ext_id=None, order_id=None, order_ext_id=None):  # noqa: E501
        """PoiExtHotelOrderCancelBody - a model defined in Swagger"""  # noqa: E501
        self._supplier_ext_id = None
        self._order_id = None
        self._order_ext_id = None
        self.discriminator = None
        self.supplier_ext_id = supplier_ext_id
        self.order_id = order_id
        self.order_ext_id = order_ext_id

    @property
    def supplier_ext_id(self):
        """Gets the supplier_ext_id of this PoiExtHotelOrderCancelBody.  # noqa: E501

        接入方商铺ID  # noqa: E501

        :return: The supplier_ext_id of this PoiExtHotelOrderCancelBody.  # noqa: E501
        :rtype: str
        """
        return self._supplier_ext_id

    @supplier_ext_id.setter
    def supplier_ext_id(self, supplier_ext_id):
        """Sets the supplier_ext_id of this PoiExtHotelOrderCancelBody.

        接入方商铺ID  # noqa: E501

        :param supplier_ext_id: The supplier_ext_id of this PoiExtHotelOrderCancelBody.  # noqa: E501
        :type: str
        """
        if supplier_ext_id is None:
            raise ValueError("Invalid value for `supplier_ext_id`, must not be `None`")  # noqa: E501

        self._supplier_ext_id = supplier_ext_id

    @property
    def order_id(self):
        """Gets the order_id of this PoiExtHotelOrderCancelBody.  # noqa: E501

        抖音订单号  # noqa: E501

        :return: The order_id of this PoiExtHotelOrderCancelBody.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this PoiExtHotelOrderCancelBody.

        抖音订单号  # noqa: E501

        :param order_id: The order_id of this PoiExtHotelOrderCancelBody.  # noqa: E501
        :type: str
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def order_ext_id(self):
        """Gets the order_ext_id of this PoiExtHotelOrderCancelBody.  # noqa: E501

        接入方订单号  # noqa: E501

        :return: The order_ext_id of this PoiExtHotelOrderCancelBody.  # noqa: E501
        :rtype: str
        """
        return self._order_ext_id

    @order_ext_id.setter
    def order_ext_id(self, order_ext_id):
        """Sets the order_ext_id of this PoiExtHotelOrderCancelBody.

        接入方订单号  # noqa: E501

        :param order_ext_id: The order_ext_id of this PoiExtHotelOrderCancelBody.  # noqa: E501
        :type: str
        """
        if order_ext_id is None:
            raise ValueError("Invalid value for `order_ext_id`, must not be `None`")  # noqa: E501

        self._order_ext_id = order_ext_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(PoiExtHotelOrderCancelBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PoiExtHotelOrderCancelBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other