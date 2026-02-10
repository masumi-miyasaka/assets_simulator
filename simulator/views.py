from django.shortcuts import render
from .forms import AssetForm
from .logic import calculate_future_assets

# Create your views here.
def index(request):
    results = None
    form = AssetForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        results = calculate_future_assets(
            data['initial_asset'],
            data['interest_rate'],
            data['inflation_rate'],
            data['years']
        )
    return render(request, 'simulator/index.html', {
        'form': form,
        'results': results
    })