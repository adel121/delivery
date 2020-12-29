from django import forms
from .models import Client, Delivery_In, Delivery_Out, Manager, EndClient
class EndClientForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(EndClientForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'
	Name=forms.CharField(label='Name', max_length=100)
	Location=forms.CharField(label='Location', max_length=100)
	Phone=forms.CharField(label='Phone', max_length=100)


class ManagerForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(ManagerForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'
	Name = forms.CharField(label='Name',max_length=100)
	Location = forms.CharField(label='Location',max_length=100)


class Delivery_OutForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(Delivery_OutForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'
	Name=forms.CharField(label='Name', max_length=100)
	Location=forms.CharField(label='Location', max_length=100)
	Phone=forms.CharField(label='Phone', max_length=100)

class ClientForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(ClientForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'
	Name=forms.CharField(label='Name', max_length=100)
	Location=forms.CharField(label='Location', max_length=100)
	Phone=forms.CharField(label='Phone', max_length=100)
	Company=forms.CharField(label='Company',max_length=100)

class Delivery_InForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(Delivery_InForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'
	Name=forms.CharField(label='Name', max_length=100)
	Location=forms.CharField(label='Location', max_length=100)
	Phone=forms.CharField(label='Phone', max_length=100)
	client=forms.ChoiceField(choices=[(x.pk,x.Company) for x in Client.objects.all()])

class BillForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(BillForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'
	Id = forms.CharField(label="Bill Id",max_length=20)
	#Date = forms.DateTimeField(label="Date")
	address = forms.CharField(label="Address",max_length=100000)
	delivery_in=forms.ChoiceField(choices=[(x.pk,x.Name) for x in Delivery_In.objects.all()])
	delivery_out=forms.ChoiceField(choices=[(x.pk,x.Name) for x in Delivery_Out.objects.all()])
	endclient=forms.ChoiceField(choices=[(x.pk,x.Name) for x in EndClient.objects.all()])
	manager=forms.ChoiceField(choices=[(x.pk,x.Name) for x in Manager.objects.all()])
	client=forms.ChoiceField(choices=[(x.pk,x.Company) for x in Client.objects.all()])
	Product_cost=forms.DecimalField(label="Product Cost in LBP", max_digits=30, decimal_places=5)
	Delivery_cost=forms.DecimalField(label="Delivery Cost in LBP", max_digits=30, decimal_places=5)