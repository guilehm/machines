from django.shortcuts import render
from machines.product.models import Machine, Module, Variation


def index(request):
    machines = Machine.objects.all()
    modules = Module.objects.all()
    return render(request, 'web/index.html', {
        'machines': machines,
        'modules': modules,
    })


def machine_detail(request, machine_id):
    machine = Machine.objects.get(id=machine_id)
    return render(request, 'web/machine-detail.html', {
        'machine': machine,
    })


def module_detail(request, module_id):
    module = Module.objects.get(id=module_id)
    return render(request, 'web/module-detail.html', {
        'module': module,
    })


def variation_detail(request, variation_id):
    variation = Variation.objects.get(id=variation_id)
    return render(request, 'web/variation-detail.html', {
        'variation': variation,
    })
