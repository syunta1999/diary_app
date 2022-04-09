from django.contrib.auth.models import UserManager, AbstractUser

# Create your models here.

#  ユーザーモデルの作成　＝＞　 https://rightcode.co.jp/blog/become-engineer/django-diary-app-make-approval-function
#  マイグレート時のエラー　＝＞　 https://note.com/mihami383/n/nb58eec166df6 settings.pyのadminをコメントアウト、urls.pyのadminもコメントアウト
#  HTMLファイルの修正　＝＞　　https://itc.tokyo/django/update-allauth-template/
class CustomUserManager(UserManager):

    use_in_migrations = True

    # 流れ = ユーザーの emailと username password を作成して保存　＝＞　管理者なら件を与える　＝＞　True or False

    def _create_user(self, email, username, password, **extra_fields):

        # _create_user と create_superuser の共通処理
        # Eメールとユーザーネームを保存している また　**extra_fields　に is_staff, is_superuser が入っている。 

        if not email:

            raise ValueError('email は必須です')
        
        if not username:

            raise ValueError('username は必須です')
        
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    

    def create_user(self, username, email=None, password=None, **extra_fields):
        
        # スタッフ権限、スーパーユーザー権限を与えない処理
        # is_staff, is_superuser を False にして_create_user関数に値を返している

        if not email:

            raise ValueError('email は必須です')
        
        if not username:

            raise ValueError('username は必須です')
        
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, username, password, **extra_fields)
    

    def create_superuser(self, username, email=None, password=None, **extra_fields):

        # スタッフ権限、スーパーユーザー権限を与える処理
        # is_staff, is_superuser を True にして_create_user関数に値を返している

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('管理者は is_staff が True である必要があります')
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('管理者は is_superuser が True である必要があります')
        
        return self._create_user(email, username, password, **extra_fields)


class CustomUser(AbstractUser):

    objects = CustomUserManager()

    def __str__(self):

        return self.email

# setting.py に以下の1行を追加する　ユーザーモデルとして CustomUser クラスを利用することを settings.py に明記します。
# AUTH_USER_MODEL = 'accounts.CustomUser'