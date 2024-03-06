from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self , email, password = None , **extra_fields):
        if not email:
            raise ValueError("Phone Number required")

        # extra_fields['email'] = self.normalize_email(extra_fields['email'])
        # Normalize is used because email is case sensitive

        user = self.model(phone_number = email, **extra_fields)
        user.set_password(password)
        user.save(using = self.db)

        return user
    
    def create_superuser(self , email, password = None , **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email , password , **extra_fields)