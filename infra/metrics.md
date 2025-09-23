Basic monitoring options:

- Health endpoint: GET /health returns status JSON
- Add Prometheus metrics via `prometheus_client` if desired:
  - Install `prometheus-client`
  - Expose `/metrics` using a custom ASGI app mount
  - Scrape with Cloud Monitoring or a Prometheus server


