from django.db import models

class Student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    lop=models.CharField(max_length=80)
    khoa=models.CharField(max_length=80)
    ngaysinh=models.CharField(max_length=30)
    email=models.CharField(max_length=255)
    address=models.TextField()
    gender=models.CharField(max_length=255)
    quequan=models.CharField(max_length=30)
    sdt=models.CharField(max_length=255)
    objects = models.Manager()
    def __str__(self):
        return self.name


class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    bomon = models.CharField(max_length=80)
    khoa_gd = models.CharField(max_length=80)
    ngaysinh = models.CharField(max_length=30)
    email = models.CharField(max_length=255)
    address = models.TextField()
    gender = models.CharField(max_length=255)
    quequan = models.CharField(max_length=30)
    sdt = models.CharField(max_length=255)
    objects = models.Manager()
    def __str__(self):
        return self.name

class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    sdt=models.CharField(max_length=255)
    objects=models.Manager()


class FeedBackStudent(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    feedback=models.TextField()
    feedback_reply=models.TextField()
    objects=models.Manager()


class FeedBackStaff(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
    feedback=models.TextField()
    feedback_reply=models.TextField()
    objects=models.Manager()

class NotificationStaff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id= models.ForeignKey(Staff, on_delete=models.CASCADE)
    message = models.TextField()
    objects = models.Manager()


class NotificationStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id= models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    objects = models.Manager()