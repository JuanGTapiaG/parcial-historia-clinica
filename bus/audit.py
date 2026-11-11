from auditchain import AuditLog, SqliteBackend

async def get_audit_log():
    return AuditLog(SqliteBackend("audit.db"))

async def log_event(usuario: str, accion: str, recurso: str, metadata: dict = None):
    async with await get_audit_log() as log:
        await log.append(usuario, accion, recurso, metadata=metadata or {})

async def verify_audit():
    async with await get_audit_log() as log:
        report = await log.verify()
        return report
