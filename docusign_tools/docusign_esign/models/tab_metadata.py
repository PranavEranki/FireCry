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


class TabMetadata(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, anchor=None, anchor_case_sensitive=None, anchor_horizontal_alignment=None, anchor_ignore_if_not_present=None, anchor_match_whole_word=None, anchor_units=None, anchor_x_offset=None, anchor_y_offset=None, bold=None, conceal_value_on_document=None, created_by_display_name=None, created_by_user_id=None, custom_tab_id=None, disable_auto_size=None, editable=None, font=None, font_color=None, font_size=None, height=None, included_in_email=None, initial_value=None, italic=None, items=None, last_modified=None, last_modified_by_display_name=None, last_modified_by_user_id=None, locked=None, maximum_length=None, merge_field=None, name=None, required=None, scale_value=None, shared=None, stamp_type=None, stamp_type_metadata=None, tab_label=None, type=None, underline=None, validation_message=None, validation_pattern=None, width=None):
        """
        TabMetadata - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'anchor': 'str',
            'anchor_case_sensitive': 'str',
            'anchor_horizontal_alignment': 'str',
            'anchor_ignore_if_not_present': 'str',
            'anchor_match_whole_word': 'str',
            'anchor_units': 'str',
            'anchor_x_offset': 'str',
            'anchor_y_offset': 'str',
            'bold': 'str',
            'conceal_value_on_document': 'str',
            'created_by_display_name': 'str',
            'created_by_user_id': 'str',
            'custom_tab_id': 'str',
            'disable_auto_size': 'str',
            'editable': 'str',
            'font': 'str',
            'font_color': 'str',
            'font_size': 'str',
            'height': 'str',
            'included_in_email': 'str',
            'initial_value': 'str',
            'italic': 'str',
            'items': 'list[str]',
            'last_modified': 'str',
            'last_modified_by_display_name': 'str',
            'last_modified_by_user_id': 'str',
            'locked': 'str',
            'maximum_length': 'str',
            'merge_field': 'MergeField',
            'name': 'str',
            'required': 'str',
            'scale_value': 'str',
            'shared': 'str',
            'stamp_type': 'str',
            'stamp_type_metadata': 'PropertyMetadata',
            'tab_label': 'str',
            'type': 'str',
            'underline': 'str',
            'validation_message': 'str',
            'validation_pattern': 'str',
            'width': 'str'
        }

        self.attribute_map = {
            'anchor': 'anchor',
            'anchor_case_sensitive': 'anchorCaseSensitive',
            'anchor_horizontal_alignment': 'anchorHorizontalAlignment',
            'anchor_ignore_if_not_present': 'anchorIgnoreIfNotPresent',
            'anchor_match_whole_word': 'anchorMatchWholeWord',
            'anchor_units': 'anchorUnits',
            'anchor_x_offset': 'anchorXOffset',
            'anchor_y_offset': 'anchorYOffset',
            'bold': 'bold',
            'conceal_value_on_document': 'concealValueOnDocument',
            'created_by_display_name': 'createdByDisplayName',
            'created_by_user_id': 'createdByUserId',
            'custom_tab_id': 'customTabId',
            'disable_auto_size': 'disableAutoSize',
            'editable': 'editable',
            'font': 'font',
            'font_color': 'fontColor',
            'font_size': 'fontSize',
            'height': 'height',
            'included_in_email': 'includedInEmail',
            'initial_value': 'initialValue',
            'italic': 'italic',
            'items': 'items',
            'last_modified': 'lastModified',
            'last_modified_by_display_name': 'lastModifiedByDisplayName',
            'last_modified_by_user_id': 'lastModifiedByUserId',
            'locked': 'locked',
            'maximum_length': 'maximumLength',
            'merge_field': 'mergeField',
            'name': 'name',
            'required': 'required',
            'scale_value': 'scaleValue',
            'shared': 'shared',
            'stamp_type': 'stampType',
            'stamp_type_metadata': 'stampTypeMetadata',
            'tab_label': 'tabLabel',
            'type': 'type',
            'underline': 'underline',
            'validation_message': 'validationMessage',
            'validation_pattern': 'validationPattern',
            'width': 'width'
        }

        self._anchor = anchor
        self._anchor_case_sensitive = anchor_case_sensitive
        self._anchor_horizontal_alignment = anchor_horizontal_alignment
        self._anchor_ignore_if_not_present = anchor_ignore_if_not_present
        self._anchor_match_whole_word = anchor_match_whole_word
        self._anchor_units = anchor_units
        self._anchor_x_offset = anchor_x_offset
        self._anchor_y_offset = anchor_y_offset
        self._bold = bold
        self._conceal_value_on_document = conceal_value_on_document
        self._created_by_display_name = created_by_display_name
        self._created_by_user_id = created_by_user_id
        self._custom_tab_id = custom_tab_id
        self._disable_auto_size = disable_auto_size
        self._editable = editable
        self._font = font
        self._font_color = font_color
        self._font_size = font_size
        self._height = height
        self._included_in_email = included_in_email
        self._initial_value = initial_value
        self._italic = italic
        self._items = items
        self._last_modified = last_modified
        self._last_modified_by_display_name = last_modified_by_display_name
        self._last_modified_by_user_id = last_modified_by_user_id
        self._locked = locked
        self._maximum_length = maximum_length
        self._merge_field = merge_field
        self._name = name
        self._required = required
        self._scale_value = scale_value
        self._shared = shared
        self._stamp_type = stamp_type
        self._stamp_type_metadata = stamp_type_metadata
        self._tab_label = tab_label
        self._type = type
        self._underline = underline
        self._validation_message = validation_message
        self._validation_pattern = validation_pattern
        self._width = width

    @property
    def anchor(self):
        """
        Gets the anchor of this TabMetadata.
        An optional string that is used to auto-match tabs to strings located in the documents of an envelope.

        :return: The anchor of this TabMetadata.
        :rtype: str
        """
        return self._anchor

    @anchor.setter
    def anchor(self, anchor):
        """
        Sets the anchor of this TabMetadata.
        An optional string that is used to auto-match tabs to strings located in the documents of an envelope.

        :param anchor: The anchor of this TabMetadata.
        :type: str
        """

        self._anchor = anchor

    @property
    def anchor_case_sensitive(self):
        """
        Gets the anchor_case_sensitive of this TabMetadata.
        When set to **true**, the anchor string does not consider case when matching strings in the document. The default value is **true**.

        :return: The anchor_case_sensitive of this TabMetadata.
        :rtype: str
        """
        return self._anchor_case_sensitive

    @anchor_case_sensitive.setter
    def anchor_case_sensitive(self, anchor_case_sensitive):
        """
        Sets the anchor_case_sensitive of this TabMetadata.
        When set to **true**, the anchor string does not consider case when matching strings in the document. The default value is **true**.

        :param anchor_case_sensitive: The anchor_case_sensitive of this TabMetadata.
        :type: str
        """

        self._anchor_case_sensitive = anchor_case_sensitive

    @property
    def anchor_horizontal_alignment(self):
        """
        Gets the anchor_horizontal_alignment of this TabMetadata.
        Specifies the alignment of anchor tabs with anchor strings. Possible values are **left** or **right**. The default value is **left**.

        :return: The anchor_horizontal_alignment of this TabMetadata.
        :rtype: str
        """
        return self._anchor_horizontal_alignment

    @anchor_horizontal_alignment.setter
    def anchor_horizontal_alignment(self, anchor_horizontal_alignment):
        """
        Sets the anchor_horizontal_alignment of this TabMetadata.
        Specifies the alignment of anchor tabs with anchor strings. Possible values are **left** or **right**. The default value is **left**.

        :param anchor_horizontal_alignment: The anchor_horizontal_alignment of this TabMetadata.
        :type: str
        """

        self._anchor_horizontal_alignment = anchor_horizontal_alignment

    @property
    def anchor_ignore_if_not_present(self):
        """
        Gets the anchor_ignore_if_not_present of this TabMetadata.
        When set to **true**, this tab is ignored if anchorString is not found in the document.

        :return: The anchor_ignore_if_not_present of this TabMetadata.
        :rtype: str
        """
        return self._anchor_ignore_if_not_present

    @anchor_ignore_if_not_present.setter
    def anchor_ignore_if_not_present(self, anchor_ignore_if_not_present):
        """
        Sets the anchor_ignore_if_not_present of this TabMetadata.
        When set to **true**, this tab is ignored if anchorString is not found in the document.

        :param anchor_ignore_if_not_present: The anchor_ignore_if_not_present of this TabMetadata.
        :type: str
        """

        self._anchor_ignore_if_not_present = anchor_ignore_if_not_present

    @property
    def anchor_match_whole_word(self):
        """
        Gets the anchor_match_whole_word of this TabMetadata.
        When set to **true**, the anchor string in this tab matches whole words only (strings embedded in other strings are ignored.) The default value is **true**.

        :return: The anchor_match_whole_word of this TabMetadata.
        :rtype: str
        """
        return self._anchor_match_whole_word

    @anchor_match_whole_word.setter
    def anchor_match_whole_word(self, anchor_match_whole_word):
        """
        Sets the anchor_match_whole_word of this TabMetadata.
        When set to **true**, the anchor string in this tab matches whole words only (strings embedded in other strings are ignored.) The default value is **true**.

        :param anchor_match_whole_word: The anchor_match_whole_word of this TabMetadata.
        :type: str
        """

        self._anchor_match_whole_word = anchor_match_whole_word

    @property
    def anchor_units(self):
        """
        Gets the anchor_units of this TabMetadata.
        Specifies units of the X and Y offset. Units could be pixels, millimeters, centimeters, or inches.

        :return: The anchor_units of this TabMetadata.
        :rtype: str
        """
        return self._anchor_units

    @anchor_units.setter
    def anchor_units(self, anchor_units):
        """
        Sets the anchor_units of this TabMetadata.
        Specifies units of the X and Y offset. Units could be pixels, millimeters, centimeters, or inches.

        :param anchor_units: The anchor_units of this TabMetadata.
        :type: str
        """

        self._anchor_units = anchor_units

    @property
    def anchor_x_offset(self):
        """
        Gets the anchor_x_offset of this TabMetadata.
        Specifies the X axis location of the tab, in achorUnits, relative to the anchorString.

        :return: The anchor_x_offset of this TabMetadata.
        :rtype: str
        """
        return self._anchor_x_offset

    @anchor_x_offset.setter
    def anchor_x_offset(self, anchor_x_offset):
        """
        Sets the anchor_x_offset of this TabMetadata.
        Specifies the X axis location of the tab, in achorUnits, relative to the anchorString.

        :param anchor_x_offset: The anchor_x_offset of this TabMetadata.
        :type: str
        """

        self._anchor_x_offset = anchor_x_offset

    @property
    def anchor_y_offset(self):
        """
        Gets the anchor_y_offset of this TabMetadata.
        Specifies the Y axis location of the tab, in achorUnits, relative to the anchorString.

        :return: The anchor_y_offset of this TabMetadata.
        :rtype: str
        """
        return self._anchor_y_offset

    @anchor_y_offset.setter
    def anchor_y_offset(self, anchor_y_offset):
        """
        Sets the anchor_y_offset of this TabMetadata.
        Specifies the Y axis location of the tab, in achorUnits, relative to the anchorString.

        :param anchor_y_offset: The anchor_y_offset of this TabMetadata.
        :type: str
        """

        self._anchor_y_offset = anchor_y_offset

    @property
    def bold(self):
        """
        Gets the bold of this TabMetadata.
        When set to **true**, the information in the tab is bold.

        :return: The bold of this TabMetadata.
        :rtype: str
        """
        return self._bold

    @bold.setter
    def bold(self, bold):
        """
        Sets the bold of this TabMetadata.
        When set to **true**, the information in the tab is bold.

        :param bold: The bold of this TabMetadata.
        :type: str
        """

        self._bold = bold

    @property
    def conceal_value_on_document(self):
        """
        Gets the conceal_value_on_document of this TabMetadata.
        When set to **true**, the field appears normally while the recipient is adding or modifying the information in the field, but the data is not visible (the characters are hidden by asterisks) to any other signer or the sender.  When an envelope is completed the information is available to the sender through the Form Data link in the DocuSign Console.  This setting applies only to text boxes and does not affect list boxes, radio buttons, or check boxes.

        :return: The conceal_value_on_document of this TabMetadata.
        :rtype: str
        """
        return self._conceal_value_on_document

    @conceal_value_on_document.setter
    def conceal_value_on_document(self, conceal_value_on_document):
        """
        Sets the conceal_value_on_document of this TabMetadata.
        When set to **true**, the field appears normally while the recipient is adding or modifying the information in the field, but the data is not visible (the characters are hidden by asterisks) to any other signer or the sender.  When an envelope is completed the information is available to the sender through the Form Data link in the DocuSign Console.  This setting applies only to text boxes and does not affect list boxes, radio buttons, or check boxes.

        :param conceal_value_on_document: The conceal_value_on_document of this TabMetadata.
        :type: str
        """

        self._conceal_value_on_document = conceal_value_on_document

    @property
    def created_by_display_name(self):
        """
        Gets the created_by_display_name of this TabMetadata.
        The user name of the DocuSign user who created this object.

        :return: The created_by_display_name of this TabMetadata.
        :rtype: str
        """
        return self._created_by_display_name

    @created_by_display_name.setter
    def created_by_display_name(self, created_by_display_name):
        """
        Sets the created_by_display_name of this TabMetadata.
        The user name of the DocuSign user who created this object.

        :param created_by_display_name: The created_by_display_name of this TabMetadata.
        :type: str
        """

        self._created_by_display_name = created_by_display_name

    @property
    def created_by_user_id(self):
        """
        Gets the created_by_user_id of this TabMetadata.
        The userId of the DocuSign user who created this object.

        :return: The created_by_user_id of this TabMetadata.
        :rtype: str
        """
        return self._created_by_user_id

    @created_by_user_id.setter
    def created_by_user_id(self, created_by_user_id):
        """
        Sets the created_by_user_id of this TabMetadata.
        The userId of the DocuSign user who created this object.

        :param created_by_user_id: The created_by_user_id of this TabMetadata.
        :type: str
        """

        self._created_by_user_id = created_by_user_id

    @property
    def custom_tab_id(self):
        """
        Gets the custom_tab_id of this TabMetadata.
        The DocuSign generated custom tab ID for the custom tab to be applied. This can only be used when adding new tabs for a recipient. When used, the new tab inherits all the custom tab properties.

        :return: The custom_tab_id of this TabMetadata.
        :rtype: str
        """
        return self._custom_tab_id

    @custom_tab_id.setter
    def custom_tab_id(self, custom_tab_id):
        """
        Sets the custom_tab_id of this TabMetadata.
        The DocuSign generated custom tab ID for the custom tab to be applied. This can only be used when adding new tabs for a recipient. When used, the new tab inherits all the custom tab properties.

        :param custom_tab_id: The custom_tab_id of this TabMetadata.
        :type: str
        """

        self._custom_tab_id = custom_tab_id

    @property
    def disable_auto_size(self):
        """
        Gets the disable_auto_size of this TabMetadata.
        When set to **true**, disables the auto sizing of single line text boxes in the signing screen when the signer enters data. If disabled users will only be able enter as much data as the text box can hold. By default this is false. This property only affects single line text boxes.

        :return: The disable_auto_size of this TabMetadata.
        :rtype: str
        """
        return self._disable_auto_size

    @disable_auto_size.setter
    def disable_auto_size(self, disable_auto_size):
        """
        Sets the disable_auto_size of this TabMetadata.
        When set to **true**, disables the auto sizing of single line text boxes in the signing screen when the signer enters data. If disabled users will only be able enter as much data as the text box can hold. By default this is false. This property only affects single line text boxes.

        :param disable_auto_size: The disable_auto_size of this TabMetadata.
        :type: str
        """

        self._disable_auto_size = disable_auto_size

    @property
    def editable(self):
        """
        Gets the editable of this TabMetadata.
        When set to **true**, the custom tab is editable. Otherwise the custom tab cannot be modified.

        :return: The editable of this TabMetadata.
        :rtype: str
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """
        Sets the editable of this TabMetadata.
        When set to **true**, the custom tab is editable. Otherwise the custom tab cannot be modified.

        :param editable: The editable of this TabMetadata.
        :type: str
        """

        self._editable = editable

    @property
    def font(self):
        """
        Gets the font of this TabMetadata.
        The font to be used for the tab value. Supported Fonts: Arial, Arial, ArialNarrow, Calibri, CourierNew, Garamond, Georgia, Helvetica,   LucidaConsole, Tahoma, TimesNewRoman, Trebuchet, Verdana, MSGothic, MSMincho, Default.

        :return: The font of this TabMetadata.
        :rtype: str
        """
        return self._font

    @font.setter
    def font(self, font):
        """
        Sets the font of this TabMetadata.
        The font to be used for the tab value. Supported Fonts: Arial, Arial, ArialNarrow, Calibri, CourierNew, Garamond, Georgia, Helvetica,   LucidaConsole, Tahoma, TimesNewRoman, Trebuchet, Verdana, MSGothic, MSMincho, Default.

        :param font: The font of this TabMetadata.
        :type: str
        """

        self._font = font

    @property
    def font_color(self):
        """
        Gets the font_color of this TabMetadata.
        The font color used for the information in the tab.  Possible values are: Black, BrightBlue, BrightRed, DarkGreen, DarkRed, Gold, Green, NavyBlue, Purple, or White.

        :return: The font_color of this TabMetadata.
        :rtype: str
        """
        return self._font_color

    @font_color.setter
    def font_color(self, font_color):
        """
        Sets the font_color of this TabMetadata.
        The font color used for the information in the tab.  Possible values are: Black, BrightBlue, BrightRed, DarkGreen, DarkRed, Gold, Green, NavyBlue, Purple, or White.

        :param font_color: The font_color of this TabMetadata.
        :type: str
        """

        self._font_color = font_color

    @property
    def font_size(self):
        """
        Gets the font_size of this TabMetadata.
        The font size used for the information in the tab.  Possible values are: Size7, Size8, Size9, Size10, Size11, Size12, Size14, Size16, Size18, Size20, Size22, Size24, Size26, Size28, Size36, Size48, or Size72.

        :return: The font_size of this TabMetadata.
        :rtype: str
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """
        Sets the font_size of this TabMetadata.
        The font size used for the information in the tab.  Possible values are: Size7, Size8, Size9, Size10, Size11, Size12, Size14, Size16, Size18, Size20, Size22, Size24, Size26, Size28, Size36, Size48, or Size72.

        :param font_size: The font_size of this TabMetadata.
        :type: str
        """

        self._font_size = font_size

    @property
    def height(self):
        """
        Gets the height of this TabMetadata.
        Height of the tab in pixels.

        :return: The height of this TabMetadata.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this TabMetadata.
        Height of the tab in pixels.

        :param height: The height of this TabMetadata.
        :type: str
        """

        self._height = height

    @property
    def included_in_email(self):
        """
        Gets the included_in_email of this TabMetadata.
        When set to **true**, the tab is included in e-mails related to the envelope on which it exists. This applies to only specific tabs.

        :return: The included_in_email of this TabMetadata.
        :rtype: str
        """
        return self._included_in_email

    @included_in_email.setter
    def included_in_email(self, included_in_email):
        """
        Sets the included_in_email of this TabMetadata.
        When set to **true**, the tab is included in e-mails related to the envelope on which it exists. This applies to only specific tabs.

        :param included_in_email: The included_in_email of this TabMetadata.
        :type: str
        """

        self._included_in_email = included_in_email

    @property
    def initial_value(self):
        """
        Gets the initial_value of this TabMetadata.
        The original value of the tab.

        :return: The initial_value of this TabMetadata.
        :rtype: str
        """
        return self._initial_value

    @initial_value.setter
    def initial_value(self, initial_value):
        """
        Sets the initial_value of this TabMetadata.
        The original value of the tab.

        :param initial_value: The initial_value of this TabMetadata.
        :type: str
        """

        self._initial_value = initial_value

    @property
    def italic(self):
        """
        Gets the italic of this TabMetadata.
        When set to **true**, the information in the tab is italic.

        :return: The italic of this TabMetadata.
        :rtype: str
        """
        return self._italic

    @italic.setter
    def italic(self, italic):
        """
        Sets the italic of this TabMetadata.
        When set to **true**, the information in the tab is italic.

        :param italic: The italic of this TabMetadata.
        :type: str
        """

        self._italic = italic

    @property
    def items(self):
        """
        Gets the items of this TabMetadata.
        If the tab is a list, this represents the values that are possible for the tab.

        :return: The items of this TabMetadata.
        :rtype: list[str]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this TabMetadata.
        If the tab is a list, this represents the values that are possible for the tab.

        :param items: The items of this TabMetadata.
        :type: list[str]
        """

        self._items = items

    @property
    def last_modified(self):
        """
        Gets the last_modified of this TabMetadata.
        The UTC DateTime this object was last modified. This is in ISO8601 format.

        :return: The last_modified of this TabMetadata.
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """
        Sets the last_modified of this TabMetadata.
        The UTC DateTime this object was last modified. This is in ISO8601 format.

        :param last_modified: The last_modified of this TabMetadata.
        :type: str
        """

        self._last_modified = last_modified

    @property
    def last_modified_by_display_name(self):
        """
        Gets the last_modified_by_display_name of this TabMetadata.
        The User Name of the DocuSign user who last modified this object.

        :return: The last_modified_by_display_name of this TabMetadata.
        :rtype: str
        """
        return self._last_modified_by_display_name

    @last_modified_by_display_name.setter
    def last_modified_by_display_name(self, last_modified_by_display_name):
        """
        Sets the last_modified_by_display_name of this TabMetadata.
        The User Name of the DocuSign user who last modified this object.

        :param last_modified_by_display_name: The last_modified_by_display_name of this TabMetadata.
        :type: str
        """

        self._last_modified_by_display_name = last_modified_by_display_name

    @property
    def last_modified_by_user_id(self):
        """
        Gets the last_modified_by_user_id of this TabMetadata.
        The userId of the DocuSign user who last modified this object.

        :return: The last_modified_by_user_id of this TabMetadata.
        :rtype: str
        """
        return self._last_modified_by_user_id

    @last_modified_by_user_id.setter
    def last_modified_by_user_id(self, last_modified_by_user_id):
        """
        Sets the last_modified_by_user_id of this TabMetadata.
        The userId of the DocuSign user who last modified this object.

        :param last_modified_by_user_id: The last_modified_by_user_id of this TabMetadata.
        :type: str
        """

        self._last_modified_by_user_id = last_modified_by_user_id

    @property
    def locked(self):
        """
        Gets the locked of this TabMetadata.
        When set to **true**, the signer cannot change the data of the custom tab.

        :return: The locked of this TabMetadata.
        :rtype: str
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """
        Sets the locked of this TabMetadata.
        When set to **true**, the signer cannot change the data of the custom tab.

        :param locked: The locked of this TabMetadata.
        :type: str
        """

        self._locked = locked

    @property
    def maximum_length(self):
        """
        Gets the maximum_length of this TabMetadata.
        The maximum number of entry characters supported by the custom tab.

        :return: The maximum_length of this TabMetadata.
        :rtype: str
        """
        return self._maximum_length

    @maximum_length.setter
    def maximum_length(self, maximum_length):
        """
        Sets the maximum_length of this TabMetadata.
        The maximum number of entry characters supported by the custom tab.

        :param maximum_length: The maximum_length of this TabMetadata.
        :type: str
        """

        self._maximum_length = maximum_length

    @property
    def merge_field(self):
        """
        Gets the merge_field of this TabMetadata.

        :return: The merge_field of this TabMetadata.
        :rtype: MergeField
        """
        return self._merge_field

    @merge_field.setter
    def merge_field(self, merge_field):
        """
        Sets the merge_field of this TabMetadata.

        :param merge_field: The merge_field of this TabMetadata.
        :type: MergeField
        """

        self._merge_field = merge_field

    @property
    def name(self):
        """
        Gets the name of this TabMetadata.
        

        :return: The name of this TabMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TabMetadata.
        

        :param name: The name of this TabMetadata.
        :type: str
        """

        self._name = name

    @property
    def required(self):
        """
        Gets the required of this TabMetadata.
        When set to **true**, the signer is required to fill out this tab

        :return: The required of this TabMetadata.
        :rtype: str
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this TabMetadata.
        When set to **true**, the signer is required to fill out this tab

        :param required: The required of this TabMetadata.
        :type: str
        """

        self._required = required

    @property
    def scale_value(self):
        """
        Gets the scale_value of this TabMetadata.
        

        :return: The scale_value of this TabMetadata.
        :rtype: str
        """
        return self._scale_value

    @scale_value.setter
    def scale_value(self, scale_value):
        """
        Sets the scale_value of this TabMetadata.
        

        :param scale_value: The scale_value of this TabMetadata.
        :type: str
        """

        self._scale_value = scale_value

    @property
    def shared(self):
        """
        Gets the shared of this TabMetadata.
        When set to **true**, this custom tab is shared.

        :return: The shared of this TabMetadata.
        :rtype: str
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """
        Sets the shared of this TabMetadata.
        When set to **true**, this custom tab is shared.

        :param shared: The shared of this TabMetadata.
        :type: str
        """

        self._shared = shared

    @property
    def stamp_type(self):
        """
        Gets the stamp_type of this TabMetadata.
        

        :return: The stamp_type of this TabMetadata.
        :rtype: str
        """
        return self._stamp_type

    @stamp_type.setter
    def stamp_type(self, stamp_type):
        """
        Sets the stamp_type of this TabMetadata.
        

        :param stamp_type: The stamp_type of this TabMetadata.
        :type: str
        """

        self._stamp_type = stamp_type

    @property
    def stamp_type_metadata(self):
        """
        Gets the stamp_type_metadata of this TabMetadata.

        :return: The stamp_type_metadata of this TabMetadata.
        :rtype: PropertyMetadata
        """
        return self._stamp_type_metadata

    @stamp_type_metadata.setter
    def stamp_type_metadata(self, stamp_type_metadata):
        """
        Sets the stamp_type_metadata of this TabMetadata.

        :param stamp_type_metadata: The stamp_type_metadata of this TabMetadata.
        :type: PropertyMetadata
        """

        self._stamp_type_metadata = stamp_type_metadata

    @property
    def tab_label(self):
        """
        Gets the tab_label of this TabMetadata.
        The label string associated with the tab.

        :return: The tab_label of this TabMetadata.
        :rtype: str
        """
        return self._tab_label

    @tab_label.setter
    def tab_label(self, tab_label):
        """
        Sets the tab_label of this TabMetadata.
        The label string associated with the tab.

        :param tab_label: The tab_label of this TabMetadata.
        :type: str
        """

        self._tab_label = tab_label

    @property
    def type(self):
        """
        Gets the type of this TabMetadata.
        The type of this tab. Values are: Approve, CheckBox, Company, Date, DateSigned, Decline, Email, EmailAddress, EnvelopeId, FirstName, Formula, FullName, InitialHere, InitialHereOptional, LastName, List, Note, Number, Radio, SignerAttachment, SignHere, SignHereOptional, Ssn, Text, Title, Zip5, or Zip5Dash4.

        :return: The type of this TabMetadata.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TabMetadata.
        The type of this tab. Values are: Approve, CheckBox, Company, Date, DateSigned, Decline, Email, EmailAddress, EnvelopeId, FirstName, Formula, FullName, InitialHere, InitialHereOptional, LastName, List, Note, Number, Radio, SignerAttachment, SignHere, SignHereOptional, Ssn, Text, Title, Zip5, or Zip5Dash4.

        :param type: The type of this TabMetadata.
        :type: str
        """

        self._type = type

    @property
    def underline(self):
        """
        Gets the underline of this TabMetadata.
        When set to **true**, the information in the tab is underlined.

        :return: The underline of this TabMetadata.
        :rtype: str
        """
        return self._underline

    @underline.setter
    def underline(self, underline):
        """
        Sets the underline of this TabMetadata.
        When set to **true**, the information in the tab is underlined.

        :param underline: The underline of this TabMetadata.
        :type: str
        """

        self._underline = underline

    @property
    def validation_message(self):
        """
        Gets the validation_message of this TabMetadata.
        The message displayed if the custom tab fails input validation (either custom of embedded).

        :return: The validation_message of this TabMetadata.
        :rtype: str
        """
        return self._validation_message

    @validation_message.setter
    def validation_message(self, validation_message):
        """
        Sets the validation_message of this TabMetadata.
        The message displayed if the custom tab fails input validation (either custom of embedded).

        :param validation_message: The validation_message of this TabMetadata.
        :type: str
        """

        self._validation_message = validation_message

    @property
    def validation_pattern(self):
        """
        Gets the validation_pattern of this TabMetadata.
        A regular expressionn used to validate input for the tab.

        :return: The validation_pattern of this TabMetadata.
        :rtype: str
        """
        return self._validation_pattern

    @validation_pattern.setter
    def validation_pattern(self, validation_pattern):
        """
        Sets the validation_pattern of this TabMetadata.
        A regular expressionn used to validate input for the tab.

        :param validation_pattern: The validation_pattern of this TabMetadata.
        :type: str
        """

        self._validation_pattern = validation_pattern

    @property
    def width(self):
        """
        Gets the width of this TabMetadata.
        Width of the tab in pixels.

        :return: The width of this TabMetadata.
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this TabMetadata.
        Width of the tab in pixels.

        :param width: The width of this TabMetadata.
        :type: str
        """

        self._width = width

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
