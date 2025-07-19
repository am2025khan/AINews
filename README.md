# F&O OI Alert Bot (Streamlit App)

A simple Streamlit dashboard that displays real-time (or simulated) Open Interest (OI) building and shedding signals for Indian F&O stocks.

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🌐 How to Deploy on Render (Free)

1. Push this folder to your GitHub (e.g. github.com/AINews/fno-oi-alert)
2. Go to [https://render.com](https://render.com) > New > Web Service
3. Connect your GitHub repo
4. Use these settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port=8000`

Enjoy your free live dashboard!
