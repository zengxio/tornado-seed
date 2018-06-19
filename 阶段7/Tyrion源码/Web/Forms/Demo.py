#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Tyrion.Forms import Form
from Tyrion.Fields import StringField
from Tyrion.Fields import EmailField
from Tyrion.Fields import IntegerField
from Tyrion.Fields import StringListField
from Tyrion.Fields import IntegerListField

from Tyrion.Widget import SingleSelect
from Tyrion.Widget import InputSingleCheckBox
from Tyrion.Widget import InputPassword
from Tyrion.Widget import InputRadio
from Tyrion.Widget import InputMultiCheckBox
from Tyrion.Widget import MultiSelect
from Tyrion.Widget import TextArea

from Tyrion.Forms import Form
from Tyrion.Fields import StringField
from Tyrion.Fields import EmailField


class LoginForm(Form):
    username = StringField(error={'required': '用户名不能为空'})
    password = StringField(error={'required': '密码不能为空'})
    email = EmailField(error={'required': '邮箱不能为空', 'invalid': '邮箱格式错误'})


class RegisterForm(Form):
    username = StringField(max_length=32,
                           min_length=6,
                           error={'required': '用户名不能为空',
                                  'min_length': '用户名不能少于6位',
                                  'max_length': '用户名不能超过32位'})

    password = StringField(max_length=32,
                           min_length=6,
                           error={'required': '密码不能为空'},
                           widget=InputPassword())

    gender = IntegerField(error={'required': '请选择性别',
                                 'invalid': '性别必须为数字'},
                          widget=InputRadio(text_value_list=[{'value': 1, 'text': '男', },
                                                             {'value': 2, 'text': '女', }],
                                            checked_value=2))

    age = IntegerField(max_value=500,
                       min_value=0,
                       error={'required': '年龄不能为空',
                              'invalid': '年龄必须为数字',
                              'min_value': '年龄不能小于0',
                              'max_value': '年龄不能大于500'})

    email = EmailField(error={'required': '邮箱不能为空',
                              'invalid': '邮箱格式错误'})

    city = IntegerField(error={'required': '城市选项不能为空', 'invalid': '城市选项必须为数字'},
                        widget=SingleSelect(text_value_list=[{'value': 1, 'text': '上海'},
                                                             {'value': 2, 'text': '北京'},
                                                             {'value': 3, 'text': '广州'}])
                        )
    protocol = IntegerField(error={'required': '请选择协议', 'invalid': '协议格式错误'},
                            widget=InputSingleCheckBox(attr={'value': 1}))

    memo = StringField(required=False,
                       max_length=150,
                       error={'invalid': '备注格式错误', 'max_length': '备注最大长度为150字'},
                       widget=TextArea())


class MultiCheckBoxForm(Form):
    favor_str_val = StringListField(error={'required': '请选择爱好', 'invalid': '选择爱好格式错误'},
                                    widget=InputMultiCheckBox(text_value_list=[{'value': '1', 'text': '篮球', },
                                                                               {'value': '2', 'text': '足球', },
                                                                               {'value': '3', 'text': '乒乓球', },
                                                                               {'value': '4', 'text': '羽毛球'}, ]))

    favor_str_val_default = StringListField(error={'required': '请选择爱好', 'invalid': '选择爱好格式错误'},
                                            widget=InputMultiCheckBox(text_value_list=[{'value': '1', 'text': '篮球', },
                                                                                       {'value': '2', 'text': '足球', },
                                                                                       {'value': '3', 'text': '乒乓球', },
                                                                                       {'value': '4', 'text': '羽毛球'}, ],
                                                                      checked_value_list=['1', '4']))

    favor_int_val = IntegerListField(error={'required': '请选择爱好', 'invalid': '选择爱好格式错误'},
                                     widget=InputMultiCheckBox(text_value_list=[{'value': 1, 'text': '篮球', },
                                                                                {'value': 2, 'text': '足球', },
                                                                                {'value': 3, 'text': '乒乓球', },
                                                                                {'value': 4, 'text': '羽毛球'}, ]))

    favor_int_val_default = IntegerListField(error={'required': '请选择爱好', 'invalid': '选择爱好格式错误'},
                                             widget=InputMultiCheckBox(text_value_list=[{'value': 1, 'text': '篮球', },
                                                                                        {'value': 2, 'text': '足球', },
                                                                                        {'value': 3, 'text': '乒乓球', },
                                                                                        {'value': 4, 'text': '羽毛球'}, ],
                                                                       checked_value_list=[2, ]))


class MultiSelectForm(Form):
    select_str_val = StringListField(error={'required': '请选择爱好', 'invalid': '选择爱好格式错误'},
                                     widget=MultiSelect(text_value_list=[{'value': '1', 'text': '篮球', },
                                                                         {'value': '2', 'text': '足球', },
                                                                         {'value': '3', 'text': '乒乓球', },
                                                                         {'value': '4', 'text': '羽毛球'}, ]))

    select_str_val_default = StringListField(error={'required': '请选择爱好', 'invalid': '选择爱好格式错误'},
                                             widget=MultiSelect(text_value_list=[{'value': '1', 'text': '篮球', },
                                                                                 {'value': '2', 'text': '足球', },
                                                                                 {'value': '3', 'text': '乒乓球', },
                                                                                 {'value': '4', 'text': '羽毛球'}, ],
                                                                selected_value_list=['1', '3']))

    select_int_val = IntegerListField(error={'required': '请选择爱好', 'invalid': '选择爱好格式错误'},
                                      widget=MultiSelect(text_value_list=[{'value': 1, 'text': '篮球', },
                                                                          {'value': 2, 'text': '足球', },
                                                                          {'value': 3, 'text': '乒乓球', },
                                                                          {'value': 4, 'text': '羽毛球'}, ]))

    select_int_val_default = IntegerListField(error={'required': '请选择爱好', 'invalid': '选择爱好格式错误'},
                                              widget=MultiSelect(text_value_list=[{'value': 1, 'text': '篮球', },
                                                                                  {'value': 2, 'text': '足球', },
                                                                                  {'value': 3, 'text': '乒乓球', },
                                                                                  {'value': 4, 'text': '羽毛球'}, ],
                                                                 selected_value_list=[2]))


class DynamicSelectForm(Form):
    city = IntegerField(error={'required': '年龄不能为空', 'invalid': '年龄必须为数字'},
                        widget=SingleSelect(text_value_list=[{'value': 1, 'text': '上海'},
                                                             {'value': 2, 'text': '北京'},
                                                             {'value': 3, 'text': '广州'}])
                        )

    multi_favor = IntegerListField(error={'required': '请选择爱好', 'invalid': '选择爱好格式错误'},
                                   widget=MultiSelect(text_value_list=[{'value': 1, 'text': '篮球', },
                                                                       {'value': 2, 'text': '足球', },
                                                                       {'value': 3, 'text': '乒乓球', },
                                                                       {'value': 4, 'text': '羽毛球'}, ]))

    def __init__(self, *args, **kwargs):
        super(DynamicSelectForm, self).__init__(*args, **kwargs)

        # 获取数据库中的最新数据并显示在页面上（每次创建对象都执行一次数据库操作来获取最新数据）
        self.city.widget.text_value_list = [{'value': 1, 'text': '上海'},
                                            {'value': 2, 'text': '北京'},
                                            {'value': 3, 'text': '南京'},
                                            {'value': 4, 'text': '广州'}]

        self.multi_favor.widget.text_value_list = [{'value': 1, 'text': '篮球'},
                                                   {'value': 2, 'text': '足球'},
                                                   {'value': 3, 'text': '乒乓球'},
                                                   {'value': 4, 'text': '羽毛球'},
                                                   {'value': 5, 'text': '玻璃球'}]


class InitValueForm(Form):
    username = StringField(error={'required': '用户名不能为空'})
    age = IntegerField(max_value=500,
                       min_value=0,
                       error={'required': '年龄不能为空',
                              'invalid': '年龄必须为数字',
                              'min_value': '年龄不能小于0',
                              'max_value': '年龄不能大于500'})

    city = IntegerField(error={'required': '年龄不能为空', 'invalid': '年龄必须为数字'},
                        widget=SingleSelect(text_value_list=[{'value': 1, 'text': '上海'},
                                                             {'value': 2, 'text': '北京'},
                                                             {'value': 3, 'text': '广州'}])
                        )

    gender = IntegerField(error={'required': '请选择性别',
                                 'invalid': '性别必须为数字'},
                          widget=InputRadio(text_value_list=[{'value': 1, 'text': '男', },
                                                             {'value': 2, 'text': '女', }],
                                            checked_value=2))

    protocol = IntegerField(error={'required': '请选择协议', 'invalid': '协议格式错误'},
                            widget=InputSingleCheckBox(attr={'value': 1}))

    favor_int_val = IntegerListField(error={'required': '请选择爱好', 'invalid': '选择爱好格式错误'},
                                     widget=InputMultiCheckBox(text_value_list=[{'value': 1, 'text': '篮球', },
                                                                                {'value': 2, 'text': '足球', },
                                                                                {'value': 3, 'text': '乒乓球', },
                                                                                {'value': 4, 'text': '羽毛球'}, ]))

    favor_str_val = StringListField(error={'required': '请选择爱好', 'invalid': '选择爱好格式错误'},
                                    widget=InputMultiCheckBox(text_value_list=[{'value': '1', 'text': '篮球', },
                                                                               {'value': '2', 'text': '足球', },
                                                                               {'value': '3', 'text': '乒乓球', },
                                                                               {'value': '4', 'text': '羽毛球'}, ]))

    select_str_val = StringListField(error={'required': '请选择爱好', 'invalid': '选择爱好格式错误'},
                                     widget=MultiSelect(text_value_list=[{'value': '1', 'text': '篮球', },
                                                                         {'value': '2', 'text': '足球', },
                                                                         {'value': '3', 'text': '乒乓球', },
                                                                         {'value': '4', 'text': '羽毛球'}, ]))

    select_int_val = IntegerListField(error={'required': '请选择爱好', 'invalid': '选择爱好格式错误'},
                                      widget=MultiSelect(text_value_list=[{'value': 1, 'text': '篮球', },
                                                                          {'value': 2, 'text': '足球', },
                                                                          {'value': 3, 'text': '乒乓球', },
                                                                          {'value': 4, 'text': '羽毛球'}, ]))
