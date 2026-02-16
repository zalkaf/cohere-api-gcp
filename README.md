# cohere-api-gcp
API server powered by Cohere's language models, deployed on Google Cloud Platform with GPU support.

## Features

- **Cohere Integration**: integration with Cohere's latest API models (Command-R-Plus, Embeddings)
- **GPU-Enabled VM**: Ubuntu 22.04 instance with NVIDIA T4 GPU on GCP
- **RESTful API**: Flask-based API [still under work]

## Prerequisites

- Google Cloud Platform account with billing enabled
- `gcloud` CLI installed and configured
- Cohere API key (used the free tier)
- Your subnet should have the port 8080 tcp allowed 

## Installation

### 1. Create GCP GPU Instance

```bash
# Create Ubuntu instance with T4 GPU
gcloud compute instances create cohere-gpu-vm \
  --zone=us-central1-a \
  --machine-type=n1-standard-4 \
  --accelerator=type=nvidia-tesla-t4,count=1 \
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud \
  --boot-disk-size=100GB \
  --maintenance-policy=TERMINATE \
  --metadata="install-nvidia-driver=True"
```

### 2. SSH into Instance

```bash
gcloud compute ssh cohere-gpu-vm --zone=us-central1-a
```

### 3. Install NVIDIA Drivers (if not auto-installed)

```bash
sudo apt-get update
sudo apt-get install -y ubuntu-drivers-common
sudo ubuntu-drivers autoinstall
sudo reboot
```

After reboot, verify GPU:
```bash
nvidia-smi
```

### 4. Set Up Python Environment

```bash
# Create virtual environment (after ensuring python is installed)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
#cohere==5.11.4, python-dotenv==1.0.1, flask==3.0.3, flask-cors==4.0.1, requests==2.32.3
pip install -r requirements.txt

```

### 5. Configure Environment Variables

```bash

# Edit with your API key
nano .env

COHERE_API_KEY=add-your-cohere-api-key-here
PORT=8080
```

### 7. Test the Installation

```bash
python test_cohere.py
```

You should see successful API responses.



## Testing

### Run All Tests
```bash
python test_cohere.py
```



## Cost Estimation

This costed me about 3-4 dollars. I kept the VM running for 3 hours or so
Cohere API, I used the free tier 

## Project Structure

```
cohere-gcp-gpu/
├── README.md
├── requirements.txt
├── test_cohere.py         # Test script
```


