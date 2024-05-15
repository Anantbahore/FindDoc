from django import forms
from hostal_grievance.models import StudentQuery 

from django import forms
SEM = (
    (1 , "I"),
    (2 , "II"),
    (3 , "III"),
    (4 , "IV"),
    (5 , "V"),
    (6 , "VI"),
    (7 , "VII"),
    (8 , "VIII"),
)
BRANCH = (
    (1 , "CSE"),
    (2 , "ME"),
    (3 , "CIVIL"),
    (4 , "EC"),
    (5 , "CSBS"),
    (6 , "IT"),
    (7 , "RPC"),
    (8 , "CE"),             
)

class StudentForm(forms.ModelForm):
    firstname = forms.CharField(label='Your Name',widget=forms.TextInput(attrs={
        'class':'form-control ',
        'placeholder':'First Name',
        'name':'firstname',
        'type':'text'
    }))
    lastname = forms.CharField(label='Last Name',widget=forms.TextInput(attrs={
        'class':'form-control ',
        'placeholder':'Last Name',
        'name':'lastname',
        'type':'text'
    }))
    roomno = forms.IntegerField(label='Room No' ,widget=forms.NumberInput(attrs={
        'class':'form-control ',
        'placeholder':'Room No',
        'type':'number',
        'name' :'roomno'
    }))
    # roomno = forms.ChoiceField(widget=forms.Select(attrs={
    #     'class':'form-control ',
    #     'type':'number',
    #     'name':'roomno'
    # }) ,choices=rmn)
    sem = forms.ChoiceField(widget=forms.Select(attrs={
        'class':'form-control ',
        'type':'number',
        'name':'sem'
    }),choices=SEM)

    email = forms.EmailField(label='Medi-Caps Email-Id' , widget=forms.EmailInput(attrs={
        'type':'email',
        'class':'form-control',
        'placeholder':'Enter email',
        'name':'email',
        'aria-describedy':'emailHelp',
    }))
    branch = forms.ChoiceField(label='Branch', widget=forms.Select(attrs={
        'class':'form-control ',
        'name':'Branch',
    }) ,choices = BRANCH ) 
    query = forms.CharField(label='Your Query' , widget=forms.Textarea(attrs={

        'class':'form-control ',
        'rows':'3',
        'name':'query'
    })) 

    
    class Meta:
        model = StudentQuery
        fields = '__all__' 
