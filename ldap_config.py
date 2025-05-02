"""
LDAP configuration for Django integration with Active Directory.

This setup enables secure user authentication and group-based access control via LDAPS.

Key settings:
- LDAP Server: ldaps://ad.example.com:389
- Service Account: CN=NETBOXSA,OU=Service Accounts,DC=example,DC=com
- Certificates:
    - Ignore certificate errors: False (recommended for production)
    - CA Directory: /etc/ssl/certs
    - CA File: /path/to/your-ca.crt
- User search scope: limited to OU=Users
- Attribute mapping:
    - username ← sAMAccountName
    - email ← mail
    - first_name ← givenName
    - last_name ← sn
- Group membership required: NETBOX_ADMINSTRATOR or NETBOX_VIEW_ONLY
- Behavior:
    - User profile is updated on every login
    - LDAP data is cached for 1 hour

Note: Make sure the CA file is valid and trusted, and avoid disabling certificate validation in production environments.
"""

# Importação dos módulos necessários para autenticação LDAP no Django
import ldap
from django_auth_ldap.config import LDAPSearch, NestedGroupOfNamesType, LDAPGroupQuery

# Configurações do servidor LDAP
AUTH_LDAP_SERVER_URI = "ldaps://ad.example.com:389"  # Usando LDAPS para comunicação segura

# Opções de conexão LDAP
AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_REFERRALS: 0  # Desativa referrals (importante para AD)
}

# Conta de serviço para consultas no AD
AUTH_LDAP_BIND_DN = "CN=NETBOXSA,OU=Service Accounts,DC=example,DC=com"
AUTH_LDAP_BIND_PASSWORD = "demo"

# Configurações de certificados SSL/TLS
LDAP_IGNORE_CERT_ERRORS = False
LDAP_CA_CERT_DIR = "/etc/ssl/certs"
LDAP_CA_CERT_FILE = "/path/to/your-ca.crt"

# Pesquisa de usuários no AD
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "ou=Users,dc=example,dc=com",
    ldap.SCOPE_SUBTREE,
    "(&(objectClass=user)(|(userPrincipalName=%(user)s)(sAMAccountName=%(user)s)(cn=%(user)s)))"
)

# Sem montagem direta do DN do usuário
AUTH_LDAP_USER_DN_TEMPLATE = None

# Mapeamento de atributos LDAP para campos do Django
AUTH_LDAP_USER_ATTR_MAP = {
    "username": "sAMAccountName",
    "email": "mail",
    "first_name": "givenName",
    "last_name": "sn",
}

# Campo usado para consultas de usuários
AUTH_LDAP_USER_QUERY_FIELD = "username"

# Pesquisa de grupos no LDAP
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    "dc=example,dc=com",
    ldap.SCOPE_SUBTREE,
    "(objectClass=group)"
)

# Definição de tipo de grupo (aninhado)
AUTH_LDAP_GROUP_TYPE = NestedGroupOfNamesType()

# Controle de espelhamento de grupos
AUTH_LDAP_MIRROR_GROUPS = False

# Permissões de grupo
AUTH_LDAP_FIND_GROUP_PERMS = True

# Tempo de cache do LDAP (1 hora)
AUTH_LDAP_CACHE_TIMEOUT = 3600

# Atualizar dados do usuário a cada login
AUTH_LDAP_ALWAYS_UPDATE_USER = True

# Função para definir atributos padrão do usuário
def ldap_user_defaults(profile):
    profile.is_active = True

AUTH_LDAP_PROFILE_FLAGS = ldap_user_defaults

# Requer pertencimento a pelo menos um dos grupos para login
AUTH_LDAP_REQUIRE_GROUP = (
    LDAPGroupQuery("CN=NETBOX_ADMINSTRATOR,ou=Users,dc=example,dc=com") |
    LDAPGroupQuery("CN=NETBOX_VIEW_ONLY,ou=Users,dc=example,dc=com")
)
