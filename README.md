# 🏥 Plataforma Distribuida de Interoperabilidad Clínica

Sistema distribuido de historia clínica electrónica basado en **HL7 FHIR R4**, con un **Bus de Servicios de Salud (HSB)**, **Keycloak** para seguridad por roles, **auditoría encadenada por hash** y **cuatro vistas por rol**. Todo el sistema se levanta con un solo comando usando Docker Compose.

## 📋 Requisitos previos

- Docker y Docker Compose instalados.
- Python 3.11+ (solo si se ejecuta el bus fuera de Docker).
- Minikube y kubectl (opcional, para el despliegue en Kubernetes).

## 🚀 Instalación y despliegue

1. Clona el repositorio:
   ```bash
   git clone https://github.com/JuanGTapiaG/proyecto_historia_clinica_distribuida
   cd proyecto_historia_clinica_distribuida
```bash

2. Levanta todos los servicios:
