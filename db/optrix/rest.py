from wq.db import rest
from .models import Patient, Surgery

rest.router.register_model(
    Patient,
    fields="__all__",
)
rest.router.register_model(
    Surgery,
    fields="__all__",
)
