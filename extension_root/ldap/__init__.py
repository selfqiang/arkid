from runtime import Runtime
from common.extension import InMemExtension
from .provider import LDAPAppTypeProvider
from .serializers import LDAPAppSerializer


class LDAPExtension(InMemExtension):    

    def start(self, runtime: Runtime, *args, **kwargs):
        runtime.register_app_type(
            key='LDAP', 
            name='LDAP',
            provider=LDAPAppTypeProvider,
            serializer=LDAPAppSerializer,
        )

        super().start(runtime=runtime, *args, **kwargs)


extension = LDAPExtension(
    name='ldap',
    description='',
    version='1.0',
    homepage='https://www.longguikeji.com',
    logo='',
    maintainer='rock@longguikeji.com',
)
