#!/usr/bin/env python
#encoding:utf-8
#定制form组件
#插件
import re
import copy
class TextInput(object):
    def __init__(self,attrs=None):
        self.attrs=attrs
        if attrs:
            self.attrs=attrs
        else:
            self.attrs={}

    def __str__(self):
        data_list=[]
        for k,v in self.attrs.items():
            tmp="{0}='{1}'".format(k,v)
            data_list.append(tmp)
        tpl="< input type='text' {0} />".format(" ".join(data_list))
        return tpl

class EmailInput(object):
    def __init__(self, attrs=None):
        self.attrs = attrs
        if attrs:
            self.attrs = attrs
        else:
            self.attrs = {}

    def __str__(self):
        data_list = []
        for k, v in self.attrs.items():
            tmp = "{0}='{1}'".format(k, v)
            data_list.append(tmp)
        tpl = "< input type='email' {0} />".format(" ".join(data_list))
        return tpl


#字段
class Field(object):
    def __str__(self):
        if self.value:
            self.widget.attrs['value']=self.value
        return str(self.widget)

class CharField(Field):
    default_widget = TextInput
    regex="\w+"
    def __init__(self,widget=None):
        self.value = None
        self.widget=widget if widget else self.default_widget()

    def valid_field(self,value):
        self.value = value
        if re.match(self.regex,value):
            return True
        else:
            return False

class EmailField(Field):
    default_widget = EmailInput
    regex="\w+@\w+"
    def __init__(self,widget=None):
        self.value=None
        self.widget = widget if widget else self.default_widget()

    def valid_field(self,value):
        self.value=value

        if re.match(self.regex,value):
            return True
        else:
            return False

#定制form
class BaseForm(object):
    def __init__(self,data):
        self.data=data
        self.fields={}

        for name,field in type(self).__dict__.items():
            if isinstance(field,Field):
                new_field=copy.deepcopy(field)
                setattr(self,name,new_field)
                self.fields[name]=new_field

    def is_valid(self):
        flag = True
        for name,field in self.fields.items():
            user_input_val=self.data.get(name)
            result=field.valid_field(user_input_val)
            if not result:
                flag=False
            return flag

#使用
class LoginForm(BaseForm):
    user=CharField()
    email=EmailField()

form=LoginForm({'username':'alex','email':'alex@3714.com'})
is_valid=form.is_valid()
print(is_valid)
