# utils.py (or inside your finance app)
from audit.models import Audit

def log_audit(action: str, obj, user):
    Audit.objects.create(
        action=action,
        group=obj.membership.group,
        performed_by=user,
        meta_json={
            f"{obj.__class__.__name__.lower()}_id": obj.id,
            "amount": str(getattr(obj, 'amount', '')),
        }
    )
