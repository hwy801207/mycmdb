from django import forms


'''
定义重置ldap账号密码的form,非常简单
'''

class LoginForm(forms.Form):
    username = forms.CharField(label = u"用户名", max_length=100)
    old_password = forms.CharField(label = u"旧密码", widget = forms.PasswordInput)
    new_password = forms.CharField(label = u"新密码", widget = forms.PasswordInput)
    



