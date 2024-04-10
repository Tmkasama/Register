from django import forms
from .models import TaskListModel, AmountModel,DeliveryModel,PaymentModel


class TaskList(forms.ModelForm):
    class Meta:
        model = TaskListModel
        fields = "__all__"

class Delivery(forms.ModelForm):
    class Meta:
        model = DeliveryModel
        fields = "__all__"

class Payment(forms.ModelForm):
    class Meta:
        model = PaymentModel
        fields ="__all__"

class Amount(forms.ModelForm):
    class Meta:
        model = AmountModel
        fields = "__all__"
        

