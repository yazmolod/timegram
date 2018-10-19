from django import forms

class ImageForm(forms.Form):

    image_caption = forms.CharField(label='Описание к фотографии', max_length=500)
    image_file = forms.ImageField()