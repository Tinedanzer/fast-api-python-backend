import logging
import logging.config


logging.config.dictConfig({
    "version": 1,
    "formatters": {
        "json": {
            '()': 'logging_json.JSONFormatter',
            'fields': {
                "level": "levelname",
                "datetime": "asctime",
                "module": "module",
                "line": "lineno",
            }
        },
    },
    "handlers": {
        "standard_output": {
            "class": "logging.StreamHandler",
            "formatter": "json",
            "stream": "ext://sys.stderr",
        },
    },
    "loggers": {
        "app": {"level": "INFO"},
        "worker": {"level": "INFO"},
        "celery": {"level": "INFO"},
    },
    "root": {
        "level": "INFO",
        "handlers": ["standard_output"]
    }
})

logger = logging.getLogger(__name__)
