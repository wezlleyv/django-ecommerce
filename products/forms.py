from django import forms

class ProductCreate(forms.Form):
    title = forms.CharField(label="Titulo", max_length=100)
    description = forms.CharField(label="Descrição", max_length=250)
    price = forms.FloatField(label="Price")
    quantity = forms.IntegerField(label="Quantidade")
    image = forms.FileField(label="Imagem")

    YEAR_IN_SCHOOL_CHOICES = [
        ('clothes', 'clothes'),
        ('tech', 'tech'),
        ('food', 'food'),
        ('shoes', 'shoes'),
        ('acessories', 'acessories'),
    ]
    tags = forms.ChoiceField(choices=YEAR_IN_SCHOOL_CHOICES)