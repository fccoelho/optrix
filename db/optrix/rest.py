from wq.db import rest
from .models import Patient, Surgery, Postoperative, Financial

rest.router.register_model(
    Patient,
    fields="__all__",
)
rest.router.register_model(
    Surgery,
    fields="__all__",
)
rest.router.register_model(
    Postoperative,
    fields="__all__",
)
rest.router.register_model(
    Financial,
    fields="__all__",
)
