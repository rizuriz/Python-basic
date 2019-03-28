from django import forms

class contactform(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
                            attrs={
                                "class":"form-control","id":"form_id"
                                }
                             )
                           )
    email = forms.CharField(widget=forms.EmailInput(
                                attrs={
                                    "class":"form-control","id":"form_id"
                                        }
                            )
                           )
    password = forms.CharField(widget=forms.PasswordInput(
                                attrs={
                                    "class":"form-control","id":"form_id"
                                }
                            )
                                )
    detail = forms.CharField(widget=forms.Textarea(
                attrs={
                    "class":"form-control","name":"textarea_name"
                }))