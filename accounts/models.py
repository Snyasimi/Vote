from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
#  models here



class DepartmentManager(models.Manager):

    def add_dept(self,Dept_id,DEPT_NAME):
        if not Dept_id and DEPT_NAME:
            raise ValueError("Please Provide dept details")
        dept = self.model(
                Dept_id = Dept_id,
                DEPT_NAME = DEPT_NAME

                )
        dept.save(using=self._db)

        return dept




class Departments(models.Model):

    Dept_id = models.CharField(primary_key=True,max_length=255)
    DEPT_NAME = models.CharField(max_length=255)
    objects = DepartmentManager()






class MyUserManager(models.Manager):

    def __str__(self):
        return Name



    def create_user(self,Role_number,Name,Email,Dept_id,password=None):
        if not Role_number and Name:
            raise ValueError("Credentials not provided!")

        user = self.model(
                Name=Name,
                Role_number=Role_number,
                Dept_id = Dept_id,
                Email = Email,
                Vote_status=False,
                is_candidate = False

                )
        
        user.is_staff = False
        user.is_superuser = False
        user.set_password(password)
        user.save(using=self._db)

        return user
        

    def create_superuser(self,Name,Role_number,Email,password=None):

        if not Role_number and Email:
            raise ValueError("Credentials not provided!")

        user = self.model(
     
                Name=Name,
                Role_number=Role_number,
                Email = self.normalize_email(Email)
                
                )

        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)

        return user






class MyUsers(AbstractBaseUser,PermissionsMixin):

    Name = models.CharField(max_length=255)

    #role number can be adimission or the staff id(super user)
    Role_number = models.CharField(max_length=255,unique=True,primary_key=True)
    #DEPT ID TO BE RELATED WITH DEPT TABLE

    Dept_id = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255,unique=True)
    Vote_status = models.BooleanField(default=False)
    is_candidate = models.BooleanField(default=False)


    
    USERNAME_FIELD = 'Role_number'
    EMAIL_FIELD= 'Email'
    REQUIRED_FIELDS = ['Name','Email',]
    objects = MyUserManager()


    def get_username(self):
        return f"{self.Name} {self.Role_number}"

    
    def __str__(self):
        return f"{self.Name} {self.Role_number} "

    def is_staff(self):

        return self.is_superuser

    def has_perm(self,perm,obj=None):

        return True





    
class MyCandidateManager(models.Manager):



    def add_candidate(self,Role_number,Position):
        if not Role_number  and Name:
            raise ValueError("Missing credantials")

        candidate = self.model(
                Role_number = Role_number,
                Position = Position,
                Votes = 0
                )

        candidate.save(using=self._db)
        
        return candidate

    


class Candidates(models.Model):

    Role_number = models.OneToOneField(MyUsers,on_delete=models.PROTECT,primary_key=True)
    Position = models.CharField(max_length=255)
    Votes = models.IntegerField(default=0)

    objects = MyCandidateManager()

    def __str__(self):

        return f"ID = {self.Role_number} Votes = {self.Votes} "












