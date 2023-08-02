from django.shortcuts import HttpResponse, get_object_or_404, redirect, render
from msgapp.models import Msg

# Create your views here.


def testing(request):
    return HttpResponse("Hello linked Successfully")


def create(request):
    if request.method == "GET":
        return render(request, "create.html")
    else:
        # fetch the data from form
        n = request.POST["uname"]
        mail = request.POST["umail"]
        mob = request.POST["mobile"]
        msg = request.POST["msg"]
        # print(n)
        # print(mail)
        # print(mob)
        # print(msg)
        m = Msg.objects.create(name=n, email=mail, mobile=mob, Message=msg)
        m.save()
        # return HttpResponse("data inserted succesfully")
        return redirect("/dashboard")


def dashboard(request):
    m = Msg.objects.all()
    # print(m)
    # return HttpResponse("data fetch succesfully from the database")
    context = {}
    context["data"] = m
    return render(request, "dashboard.html", context)


def delete(request, rid):
    # print("it to be deleted", rid)
    # return HttpResponse("id to be deleted:", +rid)
    m = Msg.objects.filter(id=rid)
    m.delete()
    return redirect("/dashboard")


def edit(request, rid):
    if request.method == "GET":
        m = get_object_or_404(Msg, id=rid)
        context = {"data": m}
        return render(request, "edit.html", context)
    else:
        n = request.POST["uname"]
        mail = request.POST["umail"]
        mob = request.POST["mobile"]
        msg = request.POST["msg"]
        k = Msg.objects.filter(id=rid).update(
            name=n, email=mail, mobile=mob, Message=msg
        )
        # k.save()
        return redirect("/dashboard")
