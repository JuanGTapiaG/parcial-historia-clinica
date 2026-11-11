from fastapi_idempotency import IdempotencyMiddleware, MemoryStore

def setup_idempotency(app):
    app.add_middleware(
        IdempotencyMiddleware,
        store=MemoryStore(),
        header_name="Idempotency-Key",
        methods=("POST",),
        path_prefix="/ingest",
    )
