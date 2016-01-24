# from django.contrib.auth.models import User
# from django.contrib.auth.backends import ModelBackend
#
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