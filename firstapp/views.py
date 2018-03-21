from django.shortcuts import render
from firstapp.models import *
from django.http import HttpResponse

# Create your views here.
def data_entry(request):
	if request.method=="GET":
		return render(request,"login.html")
	studentname=request.POST.get("student_name")
	studentid=request.POST.get("student_id")
	number=request.POST.get("student_number")
	email=request.POST.get("student_email")
	student_time=request.POST.get("student_time")
	obj= Student.objects.create(student_name=studentname,student_id=studentid,student_number=number,student_email=email,student_time=student_time)
	obj.save()
	message="your data entered succesfully"
	return HttpResponse(message)


	def data_filter_date(request):
	if request.method=='GET':
		return render(request,'login.html')
	frmdate=request.POST.get('fromdate')
	todate=request.POST.get('todate')
	obj=Student.objects.filter(student_time=frmdate,student_time=todate)
	message='frmdate to todate'
	return render_to_response(ahshs,'data':obj)


	{% for i in data %}
	{% if i.studentname==%}
	{{i}}

	{% end if %}
	{% end for %}





	


	
