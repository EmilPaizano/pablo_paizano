from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

db = []

def index(request):

    if request.method =="POST":
        monto = float(request.POST.get("monto"))
        tasa = float(request.POST.get("tasa"))
        plazo = int(request.POST.get("plazo"))

        tasa = tasa/100/12
        plazo = plazo*12
        cuota = (monto*tasa)/(1-(1+tasa)**-plazo)
        total = plazo*cuota

        db.append({
            "monto":round(monto,2),
            "tasa":tasa*12*100,
            "plazo":plazo,
            "cuota":round(cuota,2),
            "total":round(total,2),
        })
        
        ctx={
            "datos":db
        }
        return render(request,'html/index.html',ctx)
    else:
        ctx={
            "datos":db
        }
        return render(request,'html/index.html',ctx)



