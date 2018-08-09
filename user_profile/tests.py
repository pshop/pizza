from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserInfo, PostalAddress, UserType

def create_user_types():

    u_t_1 = UserType(label='admin').save()
    u_t_2 = UserType(label='client').save()


def create_full_user_no_address():

    user = User.objects.create_user('paulshop', 'pc@gmail.com', 'prout')
    user.first_name = 'paul'
    user.last_name = 'choppin'
    user.save()

    info = UserInfo(user=user)
    info.user.phone_number='0609120124'
    info.save()

    return user

def create_full_postal_address(user):

    postal_address = PostalAddress(
        address_line_1='7 rue des lamelles',
        address_line_2='1er etage',
        postal_code = '91234',
        town='boudumonde',
        label='maison',
        user= user,
    )
    postal_address.save()

    return postal_address

#####################################################


class UserInfoTests(TestCase):

    def test_full_user_no_address_create(self):

        user = create_full_user_no_address()

        self.assertEqual(user.username, 'paulshop')
        self.assertEqual(user.first_name, 'paul')
        self.assertEqual(user.last_name, 'choppin')
        self.assertEqual(user.email, 'pc@gmail.com')
        self.assertTrue(user.password)
        self.assertEqual(user.phone_number, '0609120124')

    def test_full_user_address_create(self):

        user = create_full_user_no_address()
        postal_address = create_full_postal_address(user)

        self.assertEqual(postal_address.user.username, 'paulshop')
        self.assertEqual(postal_address.address_line_1, '7 rue des lamelles')
        self.assertEqual(postal_address.address_line_2, '1er etage')
        self.assertEqual(postal_address.town, 'boudumonde')
        self.assertEqual(postal_address.postal_code, '91234')
        self.assertEqual(postal_address.label, 'maison')

    def test_user_type_create(self):
        create_user_types()

        user_type = UserType.objects.get(pk=1)

        self.assertEqual(user_type.label, 'admin')

    def test_user_type_assigment(self):

        create_full_user_no_address()
        create_user_types()
        # I take the first user
        user = User.objects.get(pk=1)
        # i take the firts user type
        user_type = UserType.objects.get(pk=1)
        # I give to the user, the type i just got
        user.user_type = user_type

        self.assertEqual(user.user_type.label, 'admin')