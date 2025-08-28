# Flask + PostgreSQL + DevOps Assignment

This project demonstrates a production-ready DevOps workflow for a simple Flask application backed by PostgreSQL.  
It includes containerization, infrastructure automation, monitoring, and CI/CD using GitHub Actions.

---

## 🚀 Features
- **Flask + PostgreSQL** application containerized using **Docker & Docker Compose**
- **Prometheus + Grafana** for application, system, and database monitoring
- **GitHub Actions CI/CD** for:
  - Build & Test
  - Security Scanning (Trivy)
  - Docker Image Build & Push
- **Container Security Best Practices**
  - Runs as non-root user
  - Minimal image size
  - Secrets management
  - Principle of least privilege

---

## 🛠️ Tech Stack
- **Languages**: Python (Flask)
- **Database**: PostgreSQL
- **DevOps Tools**: Docker, Docker Compose, GitHub Actions, Trivy
- **Monitoring**: Prometheus, Grafana
- **Cloud**: AWS EC2 (deployment tested)

---

## 📂 Project Structure
.
├── app/ # Flask application source code
│ ├── app.py
│ ├── requirements.txt
│ └── ...
├── docker-compose.yml # Docker Compose file (App + DB + Monitoring)
├── Dockerfile # Multi-stage build for Flask app
├── prometheus.yml # Prometheus configuration
├── .github/workflows/ # GitHub Actions workflows
│ └── ci.yml
└── README.md # Project documentation

yaml
Copy code

---

## ⚡ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
2. Run with Docker Compose
bash
Copy code
docker-compose up -d
3. Access the services
Flask App → http://localhost:8000

Prometheus → http://localhost:9090

Grafana → http://localhost:3000

🔍 Monitoring Dashboards
Node Exporter Dashboard → System metrics (CPU, Memory, Disk, Network)

PostgreSQL Dashboard → Database performance & query stats

Custom Flask Dashboard → Application-specific metrics

Import dashboards into Grafana using IDs from Grafana Dashboard Library.

🤖 CI/CD Workflow
Located at .github/workflows/ci.yml:

Lint & test Python code

Scan images with Trivy

Build & push Docker image to GitHub Container Registry / Docker Hub

Deploy via Docker Compose on server (optional)

📦 Dockerfile Highlights
Multi-stage build (reduces image size)

OS Hardening (only if using EC2):

sudo ufw allow 22
sudo ufw allow 8000
sudo ufw allow 3000
sudo ufw allow 9090
sudo ufw enable

Runs as non-root user

Includes healthcheck for container

🧪 Security
Container scans using Trivy

Secrets stored securely (not hardcoded in code)

Least privilege principle in Docker setup

🏗️ Future Improvements
Automate deployment on EC2 using Ansible/Terraform

Extend CI/CD with staging & production environments

Add alerting rules in Prometheus

👨‍💻 Author
Rushikesh Borekar
DevOps Engineer | Pune, India | LinkedIn
