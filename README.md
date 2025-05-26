# CloudOps AI Monitoring 🔍🚀

This project is a backend-focused cloud monitoring system that detects anomalies in AWS EC2 metrics using Amazon CloudWatch and AWS Lambda. It is designed to emulate core functionalities found in enterprise monitoring tools like Datadog or AWS CloudWatch Alarms — with AI-based anomaly detection logic built into a serverless function.

---

## ✅ Completed Features

- 🎯 **Real-time metric analysis** using AWS CloudWatch (`CPUUtilization`)
- 🧠 **Anomaly detection Lambda function** using Python and threshold logic
- 🛠️ **Lambda deployed via .zip package** — fully cloud-native
- 📊 **CloudWatch metrics integration** (with plans for automated remediation)

---

## 🔜 Planned Features

- [ ] Auto-remediation Lambda to restart EC2 instances on anomalies
- [ ] Trigger flow between detection and remediation via `boto3` or SNS
- [ ] Alerting via email/SNS/Slack
- [ ] Optional frontend dashboard (Streamlit or S3-hosted HTML)
- [ ] CI/CD via GitHub Actions for automated deployment

---

## 🧱 Architecture (Current Phase)

[EC2 Instance]
      ↓
[CloudWatch Metrics]
      ↓
[Anomaly Detection Lambda]
      ↓
Logs to Console (for now)

## 📁 Project Structure

cloudops-ai-monitoring/
├── lambda/
│ └── anomaly_detector/
│ ├── main.py
│ └── requirements.txt
├── README.md

## 🛠️ Technologies Used

| Technology         | Role                                |
|--------------------|-------------------------------------|
| **AWS EC2**        | Simulated infrastructure to monitor |
| **AWS CloudWatch** | Collects system metrics like CPU usage |
| **AWS Lambda**     | Runs anomaly detection logic serverlessly |
| **Python (boto3)** | AWS SDK to fetch metrics and handle logic |
| **GitHub**         | Version control and project hosting |

---

## 💡 How It Works

1. **EC2 instance** sends CPU metrics to **CloudWatch**
2. **Lambda function** is triggered manually or on schedule
3. It fetches the last 5–10 minutes of CPU usage
4. Uses logic (e.g., `CPU > 80%`) to flag anomalies
5. Logs results — ready to trigger remediation in next phase

---

## 🤝 Why This Project Matters

This is a real-world simulation of cloud infrastructure monitoring + smart automation. It demonstrates:
- 🔍 Observability
- 🧠 AI-driven backend logic
- ⚡ Serverless operations
- 🧑‍💻 DevOps + Cloud Engineering principles

---

## 📣 About the Author

This project is part of my cloud portfolio as an aspiring cloud/DevOps engineer. I built it using AWS Free Tier tools and Python, and I’m actively working on adding automated remediation and alerting features.

📬 [Connect with me on LinkedIn](https://www.linkedin.com/in/aditya-hede-1971211aa/)

---

## 🗺️ License

This project is open-source and available under the MIT License.
