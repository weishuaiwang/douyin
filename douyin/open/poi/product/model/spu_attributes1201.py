# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
"""

import pprint
import re  # noqa: F401

import six


class SpuAttributes1201(object):
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
        'code': 'int',
        'name': 'str'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name'
    }

    def __init__(self, code=None, name=None):  # noqa: E501
        """SpuAttributes1201 - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._name = None
        self.discriminator = None
        self.code = code
        self.name = name

    @property
    def code(self):
        """Gets the code of this SpuAttributes1201.  # noqa: E501

        设施ID(目前没用，后期可能涉及到展示设施的icon) 1 - 空调; 2 - 电视; 3 - 阳台; 4 - 窗户; 5 - 独立卫浴; 6 - 浴缸; 7 - 吹风机; 8 - 衣架; 9 - 热水; 10 - 洗衣机; 11 - 基本厨具; 12 - 冰箱; 13 - 免费Wifi; 14 - 电热水壶; 15 - 暖气; 16 - 智能马桶; 17 - 微波炉; 18 - 门禁系统; 19 - 智能门锁; 20 - 私家花园; 21 - 私家泳池; 22 - 观景露台; 23 - 免费停车; 24 - 行李寄存   # noqa: E501

        :return: The code of this SpuAttributes1201.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this SpuAttributes1201.

        设施ID(目前没用，后期可能涉及到展示设施的icon) 1 - 空调; 2 - 电视; 3 - 阳台; 4 - 窗户; 5 - 独立卫浴; 6 - 浴缸; 7 - 吹风机; 8 - 衣架; 9 - 热水; 10 - 洗衣机; 11 - 基本厨具; 12 - 冰箱; 13 - 免费Wifi; 14 - 电热水壶; 15 - 暖气; 16 - 智能马桶; 17 - 微波炉; 18 - 门禁系统; 19 - 智能门锁; 20 - 私家花园; 21 - 私家泳池; 22 - 观景露台; 23 - 免费停车; 24 - 行李寄存   # noqa: E501

        :param code: The code of this SpuAttributes1201.  # noqa: E501
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        allowed_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, -1]  # noqa: E501
        if code not in allowed_values:
            raise ValueError(
                "Invalid value for `code` ({0}), must be one of {1}"  # noqa: E501
                .format(code, allowed_values)
            )

        self._code = code

    @property
    def name(self):
        """Gets the name of this SpuAttributes1201.  # noqa: E501

        设施名称，code ！= -1 时展示name,其他情况下展示code对应的名称  # noqa: E501

        :return: The name of this SpuAttributes1201.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SpuAttributes1201.

        设施名称，code ！= -1 时展示name,其他情况下展示code对应的名称  # noqa: E501

        :param name: The name of this SpuAttributes1201.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(SpuAttributes1201, dict):
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
        if not isinstance(other, SpuAttributes1201):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other