from datetime import timedelta

broker_url = "redis://localhost:6379/0"
result_backend = "redis://localhost:6379/1"
timezone = "UTC"
accept_content = ["json"]
task_serializer = "json"
result_serializer = "json"
