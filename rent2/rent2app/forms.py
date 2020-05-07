from django import forms
from .models import Login,DeliveryModel

class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields='__all__'


class DeliveryForm(forms.ModelForm):
    d_address=forms.CharField(widget=forms.Textarea(attrs={"rows":6, "cols":23}),label='Delivery Addr')

    class Meta:
        model=DeliveryModel
        fields='__all__'
        exclude=['customer','item_image','item_name','item_price']
        labels = {'cus_name': 'Name', 'cus_contact': 'Contact', 'cus_adhar': 'Adhar No'}

    def clean_cus_contact(self):
        cno=str(self.cleaned_data['cus_contact'])
        if len(cno)==10 and (cno[0]=='9' or cno[0]=='8' or cno[0]=='7' or cno[0]=='6'):
            return cno
        else:
            raise forms.ValidationError('Invalid Contact')

    def clean_cus_adhar(self):
        adhar = str(self.cleaned_data['cus_adhar'])
        if len(adhar) == 12:
            return adhar
        else:
            raise forms.ValidationError('Invalid Adhar No')
