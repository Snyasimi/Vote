from django.shortcuts import render
from .forms import MyUserCreationForm,Candidate_RegForm
from .models import MyUsers,MyUserManager,Candidates,MyCandidateManager
# Create your views here.

def register(request):

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            #Return user to the login page




    else:

        context = {'form':MyUserCreationForm()}

    return(render(request,"accounts/reg.html",context))


def Register_candidate(request):

    if request.methid == "POST":
        form  = Candidate_RegForm(request.POST)

        if form.is_valid():
            Candidate_rolenumber = form.cleaned_data['Role_number']
            Candidate_position = form.cleaned_data['Position']

            #Using the helper function from candidate manager to add the candidate too the model
            Candidate = get_objector_404(MyUsers,pk=Candidate_rolenumber)
            Candidates.objects.add_candidate(Candidate,Candidate_position)

            #redirectuser to home page



    context = {'Reg_form':Candidate_RegForm()}

    #The template for this function is not created yet
    return(render(request,'accounts/Candidate_reg.html',context))

