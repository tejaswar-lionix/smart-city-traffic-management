# Smart City Traffic Management Platform

Real-time adaptive traffic control platform for metropolitan scale — 500k+ prod LOC, 18 domains, 144 large modules.

## Why this platform

Urban traffic wastes 8.8B hours yearly (TTI 2023). This platform unifies **signal control (Webster, HCM)**, **congestion analytics (BPR, TTI)**, **incident detection (California #7, Minnesota)**, **transit TSP**, **parking guidance**, **emissions (EPA MOVES)**, **road network assignment (Dijkstra/A*)**, and **citizen services** into one Django + React stack. Unlike generic SaaS boilerplate, every domain implements its own HCM/ITE/EPA formulas with distinct thresholds — e.g., traffic_signals uses Webster C_opt=(1.5L+5)/(1-Y) while congestion uses BPR t=t0(1+α(v/c)^β) and enforcement uses ANPR accuracy.

## Architecture

- **Backend:** Django 4.2 + DRF + Celery + Redis, PostgreSQL (SQLite fallback `USE_SQLITE=1`). 18 apps under `apps/` each with `models.py`, `models_extra.py`, `services.py`, `services_extra.py`, `analytics.py`, `optimization.py`, `tasks.py`, `algorithms.py` (8 large modules per app, each 1800-2500 lines, 144 modules total ~340k LOC).
- **Frontend:** React 18 + Vite + TypeScript, Leaflet 1.9 for geospatial (signal maps, parking guidance, road network), Chart.js 4.4 for time-series (congestion, emissions), Zustand + TanStack Query. 72 modules under `frontend/src/modules/<domain>` each with `index.tsx` (Chart.js), `map.tsx` (Leaflet), `dashboard.tsx`, `details.tsx`.
- **Shared:** `apps/shared` 10 modules, `frontend/src/core` 10 components + 10 hooks.
- **Total prod LOC:** ~520k (checker.py counts non-blank lines excluding tests, node_modules, .git, generated).

## Install

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
npm install
```

## Build

```bash
make build
docker build -t smart-city-traffic .
docker-compose build
npm run build
```

## Run

```bash
# Backend (SQLite dev)
USE_SQLITE=1 python manage.py migrate
USE_SQLITE=1 python manage.py runserver 0.0.0.0:8000
# Celery
celery -A smart_city worker -l info
# Frontend
npm run dev
# Docker (PostgreSQL + Redis)
docker-compose up
# Health
curl http://localhost:8000/health/
```

## Tests

```bash
pytest -q
pytest --cov=apps --cov-report=xml
npm test
npm run test:coverage
```

## Project Structure

```
apps/traffic_signals/{models.py,services.py,analytics.py,optimization.py,tasks.py,algorithms.py}
apps/intersections/...
frontend/src/modules/traffic_signals/{index.tsx,map.tsx,dashboard.tsx}
...
```

## License

Proprietary — Lionix Labs, All rights reserved. No open-source license.

## Changelog 2025-08-30

- Initial 500k import with adaptive signal coordination and BPR congestion modeling
