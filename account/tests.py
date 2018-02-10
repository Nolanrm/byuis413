from django.test import TestCase
from django.contrib.auth.models import Permission, Group, ContentType
from account import models as amod

class UserClassTest(TestCase):

    fixtures = ['data.yaml']

    def setUp(self):
        #Make unique user
        self.u1 = amod.User.objects.get(email='paige@maddy.com')
        
        #Make unique permission
        self.p1 = Permission.objects.get(id=1002)
        self.p1.save()
        #Make unique group
        self.g1 = Group.objects.get(id=1030)
        self.g1.save()
        #add permission to group
        self.g1.permissions.add(self.p1)
        self.g1.save()

    def test_change_user(self):
        '''change info in user database'''
        self.u1.first_name = 'Neal'
        self.u1.save()
        self.assertEqual(self.u1.first_name,'Neal')
      
    def test_load_save(self):
        '''Test creating, saving, and reloading a user'''

        u2 = amod.User.objects.create_user(email='test@test.com')
        u2.set_password('test')
        u2.save()
        self.assertEqual(u2.email, 'test@test.com')
        self.assertTrue(u2.check_password('test'))

    def test_user_functions(self):
        '''Test the functions in the User Class'''
        print(amod.User.get_purchases(self))

    def test_adding_permission(self):
        '''Test adding permissions to users'''

        self.u1.user_permissions.add(self.p1)
        self.u1.save() # bad idea, this gives all persmisons to 1 user

        print(self.u1.get_all_permissions())

    def test_add_groups(self):
        '''Test adding group to user'''
        #adds group to U1
        self.u1.groups.add(self.g1)
        self.u1.save()
        #checks to make sure that U1 has the permission from g1
        print(self.u1.get_all_permissions())
    

    def test_assign_group(self):
        '''assign group to user'''
        self.u1.groups.add(self.g1)
        self.assertTrue(self.u1.groups.filter(name='Customer Support').count() > 0)

    def test_create_permissions(self):
        '''Test creating and adding permissions'''
        self.p = Permission()
        self.p.codename = 'change_product_price'
        self.p.name = 'Change the price of a product'
        self.p.content_type = ContentType.objects.get(id=1)
        self.p.save()
        self.assertTrue(self.p.codename, 'change_product_price')

        self.u1.user_permissions.add(self.p)
        self.assertEquals(self.u1.has_perm('admin.change_product_price'),True)



    def test_check_password(self):
        '''testing user password'''
        self.assertTrue(self.u1.check_password('Nolan'))
