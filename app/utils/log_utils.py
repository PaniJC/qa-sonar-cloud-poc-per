from ddtrace import tracer

# Network socket
tracer.configure(
  dogstatsd_url="udp://localhost:8125",
)