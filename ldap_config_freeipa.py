"""
This config is based on `ldap_config.py` and LDAP configuration on Netbox
Documentation <https://netboxlabs.com/docs/netbox/installation/ldap/>.

LDAP configuration for Django integration with FreeIPA.

This setup enables secure user authentication and group-based access control via LDAPS.

Key settings:
- LDAP Server: ldaps://ipa.server.com
- Service Account: cn=users,cn=accounts,dc=ipa,dc=server,dc=com
- Certificates:
    - Ignore certificate errors: False (recommended for production)
    - CA Directory: /etc/ssl/certs
    - CA File: /path/to/your-ca.crt
- User search scope: limited to cn=users
- Attribute mapping:
    - username ← uid
    - email ← mail
    - first_name ← givenName
    - last_name ← sn
- Group membership required: netbox-viewers
- Behavior:
    - User profile is updated on every login
    - LDAP data cache is disabled, but you can enable inserting the time in seconds

Note: Make sure the CA file is valid and trusted, and avoid disabling certificate validation in production environments.
"""

import ldap
from django_auth_ldap.config import (GroupOfNamesType, LDAPGroupQuery,
                                     LDAPSearch)

# LDAP server URI (IP or FQDN)
# Usando LDAPS para comunicação segura
AUTH_LDAP_SERVER_URI = "ldaps://ipa.server.com"


# Account for consulting on LDAP server
AUTH_LDAP_BIND_DN = "uid=admin,cn=users,cn=accounts,dc=ipa,dc=server,dc=com"
AUTH_LDAP_BIND_PASSWORD = "admin-freeipa-password"

# SSL/TLS files
LDAP_IGNORE_CERT_ERRORS = False
LDAP_CA_CERT_DIR = "/etc/ssl/certs"
LDAP_CA_CERT_FILE = "/etc/ssl/certs/freeipa-ca.crt"

# This search matches users with the uid or email equal to the provided username.
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "cn=users,cn=accounts,dc=ipa,dc=server,dc=com",
    ldap.SCOPE_SUBTREE,
    "(|(uid=%(user)s)(mail=%(user)s))"
)

AUTH_LDAP_USER_DN_TEMPLATE = None

# You can map user attributes to Django attributes as so.
# You need to map `username` with `uid`. If not, logins with email or username
# will create two users for the same person. Ex: alan.turing and
# alan.turing@exemple.com will be to different users in the netbox.
AUTH_LDAP_USER_ATTR_MAP = {
    "username": "uid",
    "email": "mail",
    "first_name": "givenName",
    "last_name": "sn",
}

'''
This search ought to return all groups to which the user belongs.
django_auth_ldap uses this to determine group hierarchy. The string `netbox*` 
is only to mirror groups that have `netbox` in the name. If not, all LDAP 
groups associated to user will be created in unnecessarily.

On my environment I create the following structure:
 - netbox-viewers -> Can login with read-only
 - netbox-staff -> Receive Staff flag from Netbox
 - netbox-admins -> Receive Superuser flag and maps for group netbox-admins
'''
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    "cn=groups,cn=accounts,dc=ipa,dc=server,dc=com",
    ldap.SCOPE_SUBTREE,
    "(cn=netbox*)"
)

AUTH_LDAP_GROUP_TYPE = LDAPGroupQuery(query="(member=%(user_dn)s)")

AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn")

# Update user data every login.
AUTH_LDAP_ALWAYS_UPDATE_USER = True

# Mirror LDAP group assignments.
AUTH_LDAP_MIRROR_GROUPS = True

# For more granular permissions, we can map LDAP groups to Django groups.
AUTH_LDAP_FIND_GROUP_PERMS = True

# Cache groups for one hour to reduce LDAP traffic. I prefer not to cache.
AUTH_LDAP_CACHE_TIMEOUT = 0

# Função para definir atributos padrão do usuário
# Function to define the user default attributes


def ldap_user_defaults(profile):
    profile.is_active = True


AUTH_LDAP_PROFILE_FLAGS = ldap_user_defaults

# Define a group required to login.
AUTH_LDAP_REQUIRE_GROUP = "cn=netbox-viewers,cn=groups,cn=accounts,dc=ipa,dc=server,dc=com"

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "cn=netbox-viewers,cn=groups,cn=accounts,dc=ipa,dc=server,dc=com",
    "is_staff": "cn=netbox-staff,cn=groups,cn=accounts,dc=ipa,dc=server,dc=com",
    "is_superuser": "cn=netbox-admins,cn=groups,cn=accounts,dc=ipa,dc=server,dc=com",
}
