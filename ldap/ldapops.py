from ldap3 import Server, Connection, LDAPBindError, LDAPChangesError
from cmdb.settings import LDAP_SERVER
class LdapAuth:
    
    def __init__(self):
        self.server = Server(LDAP_SERVER, use_ssl=False)
        self.conn = Connection(self.server, 'cn=admin,dc=9icaishi,dc=net', 'Bad$2Fish', auto_bind=True)
        self.messages = {}
        
    
    def ldap_auth(self, username, password):
        '''
                     修改密码前，验证用户是否存在，并且密码是否正确
        '''
        base = "uid={},ou=People,dc=9icaishi,dc=net".format(username)
        self.conn.search(base, search_filter="(uid={})".format(username))
        if len(self.conn.entries) == 0:
            self.messages['status'] = -1
            self.messages['error'] = "用户不存在"
        else:
            self.conn.rebind(base, password)
            if self.conn.bound:
                self.messages['status'] = 0
            else:
                self.messages['status'] = -1
                self.messages['error'] = "密码不正确"
        return self.messages
        
    def ldap_chpasswd(self, username, password):   
        dn="uid={},ou=People,dc=9icaishi,dc=net".format(username)
        changes = {'userpassword':(2, [password,])}
        try:
            self.conn.modify(dn, changes)
        except LDAPChangesError:
            print(u'修改密码失败')
       
