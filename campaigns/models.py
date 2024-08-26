from django.db import models
from users.models import User
from rest_framework.response import Response
# Create your models here.
STATUS_CHOICES1 = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]



class CreatorRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.CharField(max_length=200, blank=True, null=True)
    experience_years = models.PositiveIntegerField(default=0)
    service_areas = models.TextField(blank=True, null=True)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES1, default='pending')

    def __str__(self):
        return f"Request by {self.user.username}"

    def approve(self):
        if not Creator.objects.filter(user=self.user).exists():  
            Creator.objects.create(
                user=self.user,
                organization=self.organization,
                experience_years=self.experience_years,
                service_areas=self.service_areas,
            )
        else:
            return Response("You are already a creator")
        self.status = 'approved'
        self.save()

    def reject(self):
        creator = Creator.objects.filter(user=self.user).first()
        if creator:
            creator.delete()
        self.delete()
        

        
        
class Creator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.CharField(max_length=200, blank=True, null=True)
    experience_years = models.PositiveIntegerField(default=0)
    service_areas = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username




TYPE_CHOICES = [
    ('flood', 'Flood Relief'),
    ('education', 'Education Support'),
    ('health', 'Health Services'),
    ('food', 'Food Distribution'),
    ('shelter', 'Shelter Provision'),
    ('other', 'Other'),
]
    
STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
class Campaigns(models.Model):
    creator=models.ForeignKey(Creator,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='campaigns/',default='dummyimage.jpg')
    description=models.TextField(blank=True,null=True)
    goal_amount=models.DecimalField(max_digits=12,decimal_places=2)
    fund_raised=models.DecimalField(max_digits=12,decimal_places=2,default=0)
    location=models.CharField(max_length=200)
    deadline=models.DateField()
    type=models.CharField(choices=TYPE_CHOICES,max_length=20)
    status=models.CharField(choices=STATUS_CHOICES,max_length=20,default='active')
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]
    
class Review(models.Model):
    reviewer=models.ForeignKey(User,on_delete=models.CASCADE)
    comments=models.TextField(max_length=200)
    created=models.DateField(auto_now_add=True)
    rating=models.CharField(choices=STAR_CHOICES,max_length=20)
    
    
    def __str__(self):
        return f"Review by {self.reviewer.username}"
    
    
    