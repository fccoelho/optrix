from wq.db import rest
from .models import Patient

rest.router.register_model(
    Patient,
    fields="__all__",
)
