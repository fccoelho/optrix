from wq.db import rest
from .models import Patient, Surgery, Postoperative, Financial, Hospital, Surgeon

# rest.router.add_page('index', {'url': ''})

rest.router.register_model(
    Patient,
    fields="__all__",
    can_delete=True,
)
rest.router.register_model(
    Surgery,
    fields="__all__",
    can_delete=True,
)
rest.router.register_model(
    Postoperative,
    fields="__all__",
    can_delete=True
)
rest.router.register_model(
    Financial,
    fields="__all__",
    can_delete=True
)
rest.router.register_model(
    Hospital,
    fields="__all__",
    can_delete=True
)
rest.router.register_model(
    Surgeon,
    fields="__all__",
    can_delete=True
)
