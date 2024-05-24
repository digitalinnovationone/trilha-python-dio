from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import CardForm
from .models import Card


@login_required
def request_card(request):
    def generate_card_info() -> dict[str, str]:
        import random
        from datetime import UTC, datetime

        cc_month = str(random.randint(1, 12)).zfill(2)
        cc_year = str(datetime.now(UTC).year + 10)[2:]
        return {
            "name": "DIO Bank Platinum",
            "number": "".join([str(random.randint(0, 9)) for _ in range(16)]),
            "network": random.choice(["V", "M"]),
            "expiration_date": f"{cc_month}/{cc_year}",
            "cvv": "".join([str(random.randint(0, 9)) for _ in range(3)]),
        }

    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            card_info = generate_card_info()

            card_request = form.save(commit=False)
            card_request.user = request.user
            card_request.name = card_info["name"]
            card_request.number = card_info["number"]
            card_request.network = card_info["network"]
            card_request.expiration_date = card_info["expiration_date"]
            card_request.cvv = card_info["cvv"]
            card_request.save()

            return redirect(reverse("cards:view_requests"))
    else:
        form = CardForm()
    return render(request, "cards/request_card.html", {"form": form})


@login_required
def view_requests(request):
    user_requests = Card.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "cards/view_requests.html", {"user_requests": user_requests})


@login_required
def card_details(request, card_id):
    card = get_object_or_404(Card, id=card_id, user=request.user)
    return render(request, "cards/card_details.html", {"card": card})
