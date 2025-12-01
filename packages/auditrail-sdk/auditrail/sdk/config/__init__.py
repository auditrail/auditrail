import os


def is_tracing_enabled() -> bool:
    return (os.getenv("AUDITRAIL_TRACING_ENABLED") or "true").lower() == "true"


def is_content_tracing_enabled() -> bool:
    return (os.getenv("AUDITRAIL_TRACE_CONTENT") or "true").lower() == "true"


def is_metrics_enabled() -> bool:
    return (os.getenv("AUDITRAIL_METRICS_ENABLED") or "true").lower() == "true"


def is_logging_enabled() -> bool:
    return (os.getenv("AUDITRAIL_LOGGING_ENABLED") or "false").lower() == "true"
