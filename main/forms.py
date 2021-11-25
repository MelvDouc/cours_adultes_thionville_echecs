from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["sender_name", "sender_email", "subject", "body"]
        labels = {
            "sender_name": "Nom",
            "sender_email": "Adresse email",
            "subject": "Sujet",
            "body": "Message"
        }