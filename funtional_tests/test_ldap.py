from django.test import TestCase
from django.http import HttpRequest
from ldap.views import ldap_auth

#生成基类，完成startUp跟tearDown的一些清理工作
class LdapChpasswdTest(TestCase):
    def setUp(self):
        print("start----")

    def tearDown(self):
        print("end------")

    def test_change_ldap_passwd(self):
        request = HttpRequest()
        request.POST['username'] = "test1"
        request.POST['password'] = "123456"
        response = ldap_auth(request)
        self.assertContains(response, "123456")

        #1 post 提交新老密码与用户名

        #2 验证用户名是否存在

        #3 如果提交了老密码，验证是否可以通过bind

        #4 通过验证后才可以自己重置密码


    def test_reset_ldap_passwd(self):
        #1 post 提交新老密码与用户名

        #2 验证用户名是否存在

        #3 直接强制重置密码
        pass

