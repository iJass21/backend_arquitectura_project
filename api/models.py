from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, email, name, lastname, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            lastname=lastname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, lastname, password=None):
        user = self.create_user(
            email=email,
            name=name,
            lastname=lastname,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# Custom User Model
class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    role = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'lastname']

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

# Projects Model
class Project(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, related_name='owned_projects', on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    portrait = models.ImageField(upload_to='projects/images/', null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Comments Model
class Comment(models.Model):
    project = models.ForeignKey(Project, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Comment by {self.user.email} on {self.project.name}'

# Likes Model
class Like(models.Model):
    project = models.ForeignKey(Project, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Like by {self.user.email} on {self.project.name}'

# Project Members Model
class ProjectMember(models.Model):
    project = models.ForeignKey(Project, related_name='members', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='project_memberships', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.email} member of {self.project.name}'

# References Model
class Reference(models.Model):
    project = models.ForeignKey(Project, related_name='references', on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Reference for {self.project.name}'

# Files Model
class File(models.Model):
    route = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'File at {self.route}'

# Project Files Model
class ProjectFile(models.Model):
    project = models.ForeignKey(Project, related_name='project_files', on_delete=models.CASCADE)
    file = models.ForeignKey(File, related_name='file_projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'File {self.file.route} in project {self.project.name}'

# Tags Model
class Tag(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Project Tags Model
class ProjectTag(models.Model):
    project = models.ForeignKey(Project, related_name='project_tags', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='tag_projects', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Tag {self.tag.name} in project {self.project.name}'
