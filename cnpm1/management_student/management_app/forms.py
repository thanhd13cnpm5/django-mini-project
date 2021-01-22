from django import forms
from .models import FeedBackStudent, FeedBackStaff, NotificationStudent, NotificationStaff


class FeedbackStudentForm(forms.ModelForm):
    class Meta:
        model = FeedBackStudent
        exclude = []


class FeedbackStaffForm(forms.ModelForm):
    class Meta:
        model = FeedBackStaff
        exclude = []


class NotificationStaffForm(forms.ModelForm):
    class Meta:
        model = NotificationStaff
        exclude = []


class NotificationStudentForm(forms.ModelForm):
    class Meta:
        model = NotificationStudent
        exclude = []