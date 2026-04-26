# 🚀 AI Server Platform v6.4

> Multi-tenant AI-powered DevOps platform with billing, automation, and infrastructure intelligence.

---

## 🧠 Overview

AI Server Platform v6.4 is a production-ready SaaS backend designed for:

- 🏢 Multi-tenant organizations
- 💳 Subscription billing (Stripe)
- 📊 Usage-based limits
- 🤖 AI-driven infrastructure decisions
- ⚙️ DevOps automation

This system acts as a control plane for managing servers, deployments, and AI-assisted operations.

---

## 🧱 Architecture

txt backend/ │ ├── auth/              # Authentication (JWT) ├── organizations/     # Multi-tenant org system ├── billing/           # Stripe integration + pricing ├── usage/             # Usage tracking ├── api_keys/          # API key management ├── rbac/              # Role-based access control ├── realtime/          # WebSocket (live updates) ├── database/          # PostgreSQL models ├── core/              # Security + config │ └── main.py            # FastAPI entrypoint 

---

## 🔑 Key Features

### 🏢 Organizations (Multi-Tenant)
- Create and manage teams
- Role system: owner, admin, member
- Isolation per organization

---

### 💳 Billing (Stripe)
- Customer creation
- Subscription management
- Monthly / yearly plans
- Usage-based enforcement

---

### 📊 Usage Tracking
- Tracks API usage per organization
- Enforces plan limits
- Ready for scaling (Redis / analytics DB)

---

### 🔐 Authentication & Security
- JWT-based authentication
- Role-based access control (RBAC)
- API key system (per organization)

---

### 🤖 AI Integration (Foundation Ready)
- AI decision endpoints
- Automation hooks
- Extendable for anomaly detection & self-healing

---

## 💰 Pricing Model

Defined in:

txt backend/billing/pricing.py 

Example:

python PLANS = {     "free": {"limit": 1000, "price": 0},     "pro": {"limit": 10000, "price": 29},     "enterprise": {"limit": None, "price": 99}, } 

---

## 🔌 API Structure

### Organizations
/api/orgs/*

### Billing
/api/billing/*

### Auth
/register /login

---

## 🐳 Running Locally (Docker)

bash docker-compose up --build 

Backend:
http://localhost:8000

---

## ⚙️ Environment Variables

Create a .env file:

env SECRET_KEY=supersecret DATABASE_URL=postgresql://user:pass@db:5432/app REDIS_URL=redis://redis:6379 STRIPE_SECRET=sk_test_xxx 

---

## 🧪 Example Flow

1. Register user
2. Create organization
3. Create Stripe customer
4. Subscribe to plan
5. Send requests with:
   - Authorization header
   - X-ORG-ID
6. Usage is tracked automatically

---

## 🔐 Security Notes (IMPORTANT)

Before production:

- ❗ Use bcrypt for password hashing
- ❗ Add Stripe webhooks
- ❗ Store API keys hashed
- ❗ Use HTTPS (NGINX / reverse proxy)
- ❗ Add rate limiting

---

## 📈 Scaling Path

### v6.5 (Enterprise)
- SSO (Google / Azure AD)
- Advanced RBAC (ABAC)
- Audit dashboards
- SOC2 readiness

### v6.6 (AI Automation)
- Auto-healing infrastructure
- AI-run playbooks
- Predictive scaling

---

## 🧠 Vision

This platform evolves toward:

> “An AI-driven infrastructure control plane for modern cloud systems.”

---

## 🧑‍💻 Author

Built as part of a high-scale AI infrastructure project.

---

## 📄 License