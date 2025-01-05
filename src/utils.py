from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from settings import settings


def initialize_telemetry():

    COLLECTOR_ENDPOINT = settings.COLLECTOR_ENDPOINT
    COLLECTOR_PORT = settings.COLLECTOR_PORT
    resource = Resource(attributes={
        "service.name": settings.SERVICE_NAME,
        "os-version": settings.OS_VERSION,
        "cluster": settings.CLUSTER,
        "datacentre": settings.DATACENTRE
    })
    provider = TracerProvider(resource=resource)
    processor = BatchSpanProcessor(OTLPSpanExporter(endpoint=f"http://{COLLECTOR_ENDPOINT}:{COLLECTOR_PORT}/v1/traces"))
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)
    tracer = trace.get_tracer(settings.SERVICE_NAME)
    return tracer