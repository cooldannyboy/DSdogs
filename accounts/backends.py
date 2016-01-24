# from django.contrib.auth.models import User
from accounts.models import CustomerUser
from django.contrib.auth.backends import ModelBackend

class EmailAuthBackend(ModelBackend):
# class EmailAuthBackend(object):

    def authenticate(self, email=None, password=None):

        print("email = {0}".format(str(email)))
        print("password = {0}".format(password))

        try:
            print("WWW email = {0}".format(str(email)))
            user = CustomerUser.objects.get(email=email)
            if user.check_password(password):
                return user
        except:
        # except User.DoseNotExist:
            print("QQQ")
            return None

    def get_user(self, user_id):
        try:
            user = CustomerUser.objects.get(pk=user_id)
            if user.is_active:
                return user
            else:
                return None
        except CustomerUser.DoesNotExist:
            return None

# class EmailAuthBackend(ModelBackend):
#
#     def authenticate(self, email=None, password=None, **kwargs):
#
#         print("Danny Here!!")
#
#         try:
#             user = User.objects.get(email=email)
#             print("Danny get user OK email = {0}!!".format(email))
#             return user
#         except:
#             print("Danny get user fail email = {0}!!".format(email))
#             return None
#
#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None