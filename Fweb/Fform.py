# -*- coding:utf-8 -*-
__author__ = 'dodo'
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms import validators
class loginfor_form(FlaskForm):
    name = StringField('姓名', validators= \
            [validators.DataRequired(),validators.length(4,20)], \
            render_kw={"placeholder":"请输入姓名", \
                       "style":"text-indent: 10px ;font-size:1.5em", \
                       "class":"form-username form-control", \
                       "id":"form-username", \
                       "onclick":"cleantips()"})
    pwd = PasswordField('密码',validators= \
            [validators.DataRequired(),validators.length(4,20)], \
            render_kw={"placeholder":"请输入密码", \
                       "style":"text-indent: 10px ; font-size:1.5em", \
                       "class":"form-password form-control", \
                       "id":"form-password", \
                       "onclick":"cleantips()"})
    submit = SubmitField('登录', \
                         render_kw={"class":"btn btn-primary btn-block" , \
                                    "style":"font-size:1.5em "})

if __name__ == '__main__':
    pass