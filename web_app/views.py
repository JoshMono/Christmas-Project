from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from pprint import pprint as print
from .models import Person, Company
from .forms import CreatePersonForm, CreateCompanyForm, LinkPersonToCompanyForm
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request):
    context = {}
    return render(request, "web_app/index.html", context=context)

def view_people(request):
    context = {}
    people = Person.objects.all()
    context["people"] = people
    
        
    return render(request, "web_app/view_people.html", context=context)
    
def create_person(request):
    
    if request.method == "GET": 
        form = CreatePersonForm()
        context = {"form": form}
            
        return render(request, "web_app/create_person.html", context=context)
    
    elif request.method == "POST":
        form = CreatePersonForm(data=request.POST)
        context = {"form": form}
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/view_people")
        else:
            print('not valid')
        return render(request, "web_app/create_person.html", context=context)

def edit_person(request, person_id):

    person = Person.objects.get(id=person_id)
    if request.method == "POST":
        form = CreatePersonForm(data=request.POST, instance=person)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/view_people")
           
    else: 
        form = CreatePersonForm(instance=person)
            
    return render(request, "web_app/create_person.html", context={"form": form})

def delete_person(request, person_id):
    try:
        person = Person.objects.get(id=person_id)
        if request.method == "GET":    
                person.delete()
    except ObjectDoesNotExist:
        pass
            
    return HttpResponseRedirect("/view_people")


def view_companies(request):
    context = {}
    companies = Company.objects.all()
    company_list = []
    for i in companies:
        people = i.person_set.all()
        number_of_people = len(people)
        company_list.append([i, number_of_people])

    context["companies"] = company_list
    return render(request, "web_app/view_companies.html", context=context)


def view_company(request, company_id):
    company = Company.objects.get(id=company_id)
    people = company.person_set.all()
    all_people = Person.objects.exclude(company=company)
    context = {}
    context["company"] = company
    context["people"] = people
    

    context["link_person_to_company_form"] = LinkPersonToCompanyForm(people=all_people)   

    if request.method == "POST":
        form = LinkPersonToCompanyForm(data=request.POST, people=all_people)
        if form.is_valid():
            person = form.cleaned_data.get("people")
            person.company = company
            person.save()
        
    return render(request, "web_app/view_company.html", context=context)

def create_company(request):
    
    if request.method == "GET": 
        form = CreateCompanyForm()
        context = {"form": form}
            
        return render(request, "web_app/create_company.html", context=context)
    elif request.method == "POST":
        form = CreateCompanyForm(data=request.POST)
        context = {"form": form}
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/view_companies")
        else:
            print('not valid')
        return render(request, "web_app/create_company.html", context=context)

def edit_company(request, company_id):

    company = Company.objects.get(id=company_id)
    if request.method == "POST":
        form = CreateCompanyForm(data=request.POST, instance=company)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/view_companies")
           
    else: 
        form = CreateCompanyForm(instance=company)
            
    return render(request, "web_app/create_company.html", context={"form": form})

def delete_company(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
        if request.method == "GET":    
                company.delete()
    except ObjectDoesNotExist:
        pass
            
    return HttpResponseRedirect("/view_companies")