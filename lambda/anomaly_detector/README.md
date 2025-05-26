## CloudOps AI Monitoring 🚀

This project detects anomalies in AWS EC2 metrics using CloudWatch and a simple AI-based Lambda function. If a spike is detected, it can trigger auto-remediation actions.

 AI Used
Currently uses simple thresholding on CPU utilization.
Later: Isolation Forest anomaly detection model.

## 🛠️ Stack
- AWS Lambda
- Amazon CloudWatch
- Python 3.10
- boto3
- GitHub Actions (planned)

## 📦 Folder Structure
cloudops-ai-monitoring/
└── lambda/
└── anomaly_detector/
├── main.py
└── requirements.txt

## ✅ Next Steps
- Deploy to Lambda
- Add alerting/remediation logic
- Add CI/CD
