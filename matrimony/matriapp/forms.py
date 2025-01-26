# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, PartnerPreference, User, Message, Event

class SignupForm(UserCreationForm):  
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email',
            'style': 'background-color: rgba(255, 255, 255, 0.8); border: 1px solid #ddd; border-radius: 6px; padding: 10px;',
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Choose a username',
            'style': 'background-color: rgba(255, 255, 255, 0.8); border: 1px solid #ddd; border-radius: 6px; padding: 10px;',
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Create a password',
            'style': 'background-color: rgba(255, 255, 255, 0.8); border: 1px solid #ddd; border-radius: 6px; padding: 10px;',
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your password',
            'style': 'background-color: rgba(255, 255, 255, 0.8); border: 1px solid #ddd; border-radius: 6px; padding: 10px;',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date', 'gender', 
                  'religion', 'caste', 'height', 
                  'education', 'occupation', 
                  'income', 'profile_picture']
        
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control styled-bio',
                'placeholder': 'Write a short bio...',
                'rows': 3,
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control styled-location',
                'placeholder': 'Enter your location...',
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control styled-birth-date',
                'placeholder': 'Select your birth date...',
                'type': 'date',
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control styled-gender',
            }),
            'religion': forms.TextInput(attrs={
                'class': 'form-control styled-religion',
                'placeholder': 'Enter your religion...',
            }),
            'caste': forms.TextInput(attrs={
                'class': 'form-control styled-caste',
                'placeholder': 'Enter your caste...',
            }),
            'height': forms.NumberInput(attrs={
                'class': 'form-control styled-height',
                'placeholder': 'Enter your height in cm...',
            }),
            'education': forms.TextInput(attrs={
                'class': 'form-control styled-education',
                'placeholder': 'Enter your education...',
            }),
            'occupation': forms.TextInput(attrs={
                'class': 'form-control styled-occupation',
                'placeholder': 'Enter your occupation...',
            }),
            'income': forms.NumberInput(attrs={
                'class': 'form-control styled-income',
                'placeholder': 'Enter your income...',
            }),
            'profile_picture': forms.FileInput(attrs={
                'class': 'form-control styled-profile-picture',
            }),
        }

class PartnerPreferenceForm(forms.ModelForm):
    class Meta:
        model = PartnerPreference
        fields = ['min_age', 'max_age', 
                  'min_height', 'max_height',
                  'religion', 'caste',
                  'education', 'occupation',
                  'location']
        
        # widgets = {
        #     'min_age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter minimum age'}),
        #     'max_age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter maximum age'}),
        #     'min_height': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter minimum height (in cm)'}),
        #     'max_height': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter maximum height (in cm)'}),
        #     'religion': forms.Select(attrs={'class': 'form-control'}),
        #     'caste': forms.Select(attrs={'class': 'form-control'}),
        #     'education': forms.Select(attrs={'class': 'form-control'}),
        #     'occupation': forms.Select(attrs={'class': 'form-control'}),
        #     'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter preferred location'}),
        # }


    def __init__(self, *args, **kwargs):
        super(PartnerPreferenceForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        
class MessageForm(forms.ModelForm):
    sender = forms.ModelChoiceField(
        queryset=User.objects.none(),  # Initially empty; will populate in __init__
        required=True,
        label="Sender"
    )
    
    receiver = forms.ModelChoiceField(
        queryset=User.objects.none(),  # Initially empty; will populate in __init__
        required=True,
        label="Receiver"
    )

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'content']  # Include sender and receiver in the fields

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # Get the current user from kwargs
        super(MessageForm, self).__init__(*args, **kwargs)

        # Populate sender dropdown with current user (optional)
        self.fields['sender'].queryset = User.objects.filter(id=user.id)

        # Populate receiver dropdown with users of the opposite gender
        if user.profile.gender == 'Male':
            self.fields['receiver'].queryset = User.objects.filter(profile__gender='Female')
        else:
            self.fields['receiver'].queryset = User.objects.filter(profile__gender='Male')



class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'event_datetime']  # Use event_datetime instead of separate date and time
        # admin.py



