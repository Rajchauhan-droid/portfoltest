from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, label="Name")
    contact_email = forms.EmailField(required=True, label="Email")
    content = forms.CharField(required=True,widget=forms.Textarea,label="Message")
    

        
    def __init__(self,*args,**kwargs):
        super(ContactForm,self).__init__(*args,**kwargs)
        
        self.fields['contact_name'].widget.attrs['class'] = 'form-control'
        self.fields['contact_name'].widget.attrs['placeholder'] = 'Full Name' 
        self.fields['contact_name'].label = '' 
    
        self.fields['contact_email'].widget.attrs['class'] = 'form-control'
        self.fields['contact_email'].widget.attrs['placeholder'] = 'E-mail'
        self.fields['contact_email'].label = ''
       
        self.fields['content'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['placeholder'] = 'Message'
        self.fields['content'].label = '' 