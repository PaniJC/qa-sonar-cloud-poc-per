from ddtrace import tracer

# Network socket
tracer.configure(
    hostname='datadog-agent',
    port=8126,
)
