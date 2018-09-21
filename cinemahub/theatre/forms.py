from django import forms

class TheatreCreateForms(forms.Form):
	movie_name		= forms.CharField()
	genre			= forms.CharField(required=False)
	director		= forms.CharField(required=False)