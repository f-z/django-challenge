from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json

@require_POST
@csrf_exempt
def calculate(request):
    params = json.loads(request.body)
    savings_amount = params.get('savingsAmount', None)
    interest_rate = params.get('interestRate', None)
    monthly_contribution = params.get('monthlyContribution', None)

    if savings_amount is None or interest_rate is None or monthly_contribution is None:
        return HttpResponseBadRequest('Required parameters are not provided')

    # the requirements say 50 but you might want to let the users select that in a real app
    years_until_retirement = 50

    months_left = years_until_retirement / 12
    monthly_rate = interest_rate / 12

    savings_list = [0]
    month = 0

    while month < months_left:
        savings_amount += monthly_contribution
        savings_amount *= (1 + monthly_rate)
        savings_list.append(savings_amount)
        month += 1

    return JsonResponse({'result': savings_list})
