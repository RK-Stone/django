from django.shortcuts import render, get_object_or_404
from product.models import Product
from .forms import ProductForm


def product(request):
  q = request.GET.get('q', None)
  products = ''
  if q is None or q is "":
    products = Product.objects.all()
  elif q is not None:
    products = Product.objects.filter(title__contains=q)
  return render(request, 'product/product.html', {'products': products})


def detail(request, slug=None):
  product = get_object_or_404(Product, slug=slug)
  return render(request, 'product/detail.html', locals())


def create(request):
  if request.method == 'POST':
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      #return HttpResponseRedirect('product/')
      return render(request, 'product/edit.html', {'form': ProductForm()})
  else:
    form = ProductForm()
  return render(request, 'product/edit.html', {'form': form})


def edit(request, pk=None):
  product = get_object_or_404(product, pk=pk)
  if request.method == "POST":
    form = ProductForm(request.POST, instance=product)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('product/')
  else:
    form = ProductForm(instance=product)
  return render(request, 'product/edit.html', {'form': form})


def delete(request, pk=None):
  product = get_object_or_404(Product, pk=pk)
  product.delete()

  return render(request, 'product/')
