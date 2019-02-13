from django.test import TestCase
import re



# Create your tests here.
x = '^/userinfo/edit/(\\d+)/$'
z = re.match('^/order/edit/(\\d+)/$','/order/edit/1/')
print(z)
