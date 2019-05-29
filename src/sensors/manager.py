from django.db import models

class UserManager(models.Manager):
    
    def _create_user(self, username, password, **extra_fields):
        """
        Create and save a user with the given username and password.
        """
        salt = "" # randomString()
        hash = "" # hashFunction(self.salt + password)
        authToken = "dsaiadsjiadsj" # createToken()

        user = self.model(username=username, salt=salt, hash=hash, authToken=authToken)

        user.save(using=self._db)
        return user

    def create_user(self, username=None, password=None, **extra_fields):
        return self._create_user(username, password, **extra_fields)