# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# 헬퍼 클래스
class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):

        superuser = self.create_user(
            email=email,
            password=password,
        )
        
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        
        superuser.save(using=self._db)
        return superuser
        """
        주어진 이메일, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여
        """

# AbstractBaseUser를 상속해서 유저 커스텀
class User(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

	# 헬퍼 클래스 사용
    objects = UserManager()

	# 사용자의 username field는 email으로 설정 (이메일로 로그인)
    USERNAME_FIELD = 'email'
    
    
# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class Board(models.Model):
#     board_id = models.BigAutoField(primary_key=True)
#     postname = models.CharField(max_length=100, blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     createdate = models.DateTimeField()
#     updatedate = models.DateTimeField()
#     user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'board'


# class Chat(models.Model):
#     chat_id = models.BigAutoField(primary_key=True)
#     chat = models.CharField(max_length=100, blank=True, null=True)
#     sendtime = models.DateTimeField()
#     checker = models.IntegerField()
#     user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     chatroom = models.ForeignKey('Chatroom', models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'chat'


# class Chatpa(models.Model):
#     chatpa_id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     chatroom = models.ForeignKey('Chatroom', models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'chatpa'


# class Chatroom(models.Model):
#     chatroom_id = models.BigAutoField(primary_key=True)
#     chatname = models.CharField(max_length=100, blank=True, null=True)
#     chatstate = models.CharField(max_length=100)
#     entertime = models.DateTimeField()
#     user1 = models.ForeignKey('Users', models.DO_NOTHING)
#     user2 = models.ForeignKey('Users', models.DO_NOTHING, related_name='chatroom_user2_set')

#     class Meta:
#         managed = False
#         db_table = 'chatroom'


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'


# class Style(models.Model):
#     style_id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'style'


# class Users(models.Model):
#     user_id = models.BigAutoField(primary_key=True)
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     age = models.IntegerField()
#     name = models.CharField(max_length=100)
#     university = models.CharField(max_length=50)
#     major = models.CharField(max_length=100)
#     studentnumber = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'users'