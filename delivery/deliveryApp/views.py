from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Manager, Bill,EndClient,Client,Delivery_In,Delivery_Out
from django.db import models
from django.utils import timezone
import datetime
from .forms import EndClientForm, ManagerForm,Delivery_OutForm, ClientForm, Delivery_InForm, BillForm
from datetime import date as DATE
# Create your views here.

def index(request, category='None', year=0, month=0, day=0):
	print(request.POST)
	if request.method=='POST':
		datelist=request.POST['requested_date'].split('-')
		if datelist[0]!="Today":
			year=int(datelist[0])
			month=int(datelist[1])
			day=int(datelist[2])
	if category=="paid":
		lst = Bill.objects.all().filter(Status="paid")
	elif category=="pending":
		lst = Bill.objects.all().filter(Status="pending")
	elif category=="sent":
		lst = Bill.objects.all().filter(Status="sent")
	else:
		lst = Bill.objects.all()
	if year!=0:
		date=datetime.date(int(year),int(month),int(day))
	else:
		date='0-0-0'
		#date=date.today()
	return render(request, 'index.html', {'bills':lst, 'date':date, 'category':category})

def bill_details(request, bill_id, status):
	bill = Bill.objects.get(Id=bill_id)
	if bill.Status == status:
		return render(request, 'bill_details.html', {'bill':bill})
	bill.Status=status
	bill.save()
	lst = Bill.objects.all()
	return render(request, 'index.html', {'bills':lst,'date':'0-0-0','category':'all'})

		

def add_endclient(request):
	if request.method=='POST':
		form=EndClientForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			endclient = EndClient()
			endclient.Name=data['Name']
			endclient.Location=data['Location']
			endclient.Phone=data['Phone']
			endclient.save()
			return render(request,'thanks.html',{'Message': "End Client Added Successfully"})
	else:
		form=EndClientForm()
	return render(request,'add_endclient.html', {'form':form})

def add_manager(request):
	if request.method=='POST':
		form=ManagerForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			manager=Manager()
			manager.Name=data['Name']
			manager.Location=data['Location']
			manager.save()
			return render(request,'thanks.html',{'Message': "Manager Added Successfully"})
	else:
		form=ManagerForm()
	return render(request,'add_manager.html',{'form':form})

def add_deliveryout(request):
	if request.method=='POST':
		form = Delivery_OutForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			delivery_out=Delivery_Out()
			delivery_out.Name=data['Name']
			delivery_out.Location=data['Location']
			delivery_out.Phone=data['Phone']
			delivery_out.save()
			return render(request,'thanks.html',{'Message': "Delivery Out Added Successfully"})
	else:
		form=Delivery_OutForm()
	return render(request,'add_deliveryout.html',{'form':form})

def add_client(request):
	if request.method=='POST':
		form = ClientForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			client=Client()
			client.Name=data['Name']
			client.Location=data['Location']
			client.Phone=data['Phone']
			client.Company=data['Company']
			client.save()
			return render(request,'thanks.html',{'Message': "Client Added Successfully"})
	else:
		form=ClientForm()
	return render(request,'add_client.html',{'form':form})

def add_deliveryin(request):
	if request.method=='POST':
		form=Delivery_InForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			deliveryin=Delivery_In()
			deliveryin.Name=data['Name']
			deliveryin.Location=data['Location']
			deliveryin.Phone=data['Phone']
			deliveryin.client=Client.objects.get(pk=data['client'])
			deliveryin.save()
			return render(request,'thanks.html',{'Message': "Delivery In Added Successfully"})
	else:
		form=Delivery_InForm()
	return render(request,'add_deliveryin.html',{'form':form})


def add_bill(request):
	if request.method=='POST':
		form=BillForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			print(data)
			bill=Bill()
			bill.Id=data['Id']
			bill.Date=datetime.datetime.now()
			bill.address=data['address']
			bill.delivery_in=Delivery_In.objects.get(pk=data['delivery_in'])
			bill.delivery_out=Delivery_Out.objects.get(pk=data['delivery_out'])
			bill.end_client=EndClient.objects.get(pk=data['endclient'])
			bill.manager=Manager.objects.get(pk=data['manager'])
			bill.client=Client.objects.get(pk=data['client'])
			bill.Product_cost=data['Product_cost']
			bill.Delivery_cost=data['Delivery_cost']
			bill.status="pending"
			bill.save()
			return render(request,'thanks.html',{'Message': "Bill Added Successfully"})
	else:
		form = BillForm()
	return render(request,'add_bill.html',{'form':form})

