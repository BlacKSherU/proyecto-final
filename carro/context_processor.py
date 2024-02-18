def importe_total_carro(request):
    total = 0.0
    if request.user.is_authenticated and "carro" in request.session:
        for key, value in request.session["carro"].items():
            total += float(value["precio"])
    return {"importe_total_carro": round(total, 2)}
