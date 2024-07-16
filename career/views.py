from django.shortcuts import render

from .forms import careermodelform


# Create your views here.


def jobapply(request):
    print('ji')
    if request.method == 'POST':
        print('jiii')
        form=careermodelform(request.POST,request.FILES)

        if form.is_valid():
            print('jisafda')
            form.save()

    else:
        form=careermodelform()

    return render(request,'career.html',{'form':form})

    