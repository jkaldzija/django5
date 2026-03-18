from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.users.tasks import log_total_users, long_count_users_sleep_and_recount


@api_view(["GET"])
@permission_classes([AllowAny])
def ping(request):
    log_task_ids = [log_total_users.delay().id for _ in range(5)]
    long_task_ids = [long_count_users_sleep_and_recount.delay().id for _ in range(5)]
    return Response(
        {
            "message": "pong",
            "enqueued": {
                "log_total_users": log_task_ids,
                "long_count_users_sleep_and_recount": long_task_ids,
            },
        }
    )


