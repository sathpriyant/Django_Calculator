from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads


# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class AdditionView(View):
    def post(self,request):
        rb=request.body
        form_data= loads(rb)
        n1=form_data.get('num1')
        n2=form_data.get('num2')
        result=n1+n2
        print(rb)
        data={
            "sum":result
        }
        return JsonResponse(data)
    
@method_decorator(csrf_exempt,name='dispatch')
class SubtractionView(View):
    def post(self,request):
        data=request.body
        form_data=loads(data)
        n1=form_data.get('num1')
        n2=form_data.get('num2')
        diff=n1-n2
        result={
            "difference":diff
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name='dispatch')
class MultiplicationView(View):
    def post(self,request):
        data=request.body
        form_data=loads(data)
        n1=form_data.get('num1')
        n2=form_data.get('num2')
        mul=n1*n2
        result={
            'Multiplication':mul
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name='dispatch')
class DivisionView(View):
    def post(self,request):
        data=request.body
        form_data=loads(data)
        n1=form_data.get('num1')
        n2=form_data.get('num2')
        div=n1/n2
        result={
            'Division':div
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name='dispatch')
class ModView(View):
    def post(self,request):
        data=request.body
        form_data=loads(data)
        n1=form_data.get('num1')
        n2=form_data.get('num2')
        mod=n1%n2
        result={
            'Mod':mod
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name='dispatch')
class Percentageiew(View):
    def post(self,request):
        data=request.body
        form_data=loads(data)
        n1=form_data.get('obtained_marks')
        n2=form_data.get('total_marks')
        perc=(n1/n2)*100
        result={
            'Percentage':perc
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name='dispatch')
class BmiView(View):
    def post(self,request):
        data=request.body
        form_data=loads(data)
        n1=form_data.get('weight')
        n2=form_data.get('height')
        bmi=n1/(n2**2)
        result={
            'Bmi':bmi
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name='dispatch')
class RectAreaView(View):
    def post(self,request):
        data=request.body
        form_data=loads(data)
        n1=form_data.get('length')
        n2=form_data.get('width')
        area=n1*n2
        result={
            'Area':area
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name='dispatch')
class AgeView(View):
    def post(self,request):
        data=request.body
        form_data=loads(data)
        n1=form_data.get('birth_yr')
        n2=form_data.get('current_yr')
        age=n2-n1
        result={
            'Age':age
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name='dispatch')
class SinterestView(View):
    def post(self,request):
        data=request.body
        form_data=loads(data)
        n1=form_data.get('principal')
        n2=form_data.get('rate')
        n3=form_data.get('time')
        si=(n1*n2*n3)/100
        result={
            'Principal':n1,
            'Rate':n2,
            'Time':n3,
            "SimpleInterest":si
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name='dispatch')
class ElectricityView(View):
    def post(self,request):
        data=request.body
        form_data=loads(data)
        n1=form_data.get('rate')
        n2=form_data.get('unit')
        ele=n2*n1
        result={
            'Amount':ele
        }
        return JsonResponse(result)