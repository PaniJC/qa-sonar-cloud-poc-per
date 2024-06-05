from ddtrace import tracer

tracer.configure(
    hostname="datadog-agent",
    port=8126,
)
