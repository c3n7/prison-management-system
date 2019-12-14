from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, first_name,
                    last_name, id_no, password=None, commit=True):
        if not email:
            raise ValueError('All users must have an email address')
        if not first_name:
            raise ValueError('All users must have a first name')
        if not last_name:
            raise ValueError('All users must have a last name')
        
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            id_no=id_no,
        )
        
        user.set_password(password)
        if commit:
            user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name,
                         last_name, id_no, password):
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            id_no=id_no,
            password=password,
            commit=False,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
