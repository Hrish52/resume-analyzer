# 🎯 AI Resume Analyzer

An intelligent resume analysis tool powered by DeepSeek R1 that provides ATS insights, skill gap analysis, and actionable improvement suggestions.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.31+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🌟 Features

- **ATS Keyword Matching** - Analyze how well your resume matches job descriptions
- **Skill Gap Analysis** - Identify missing skills and technologies
- **Bullet Point Optimization** - Get specific suggestions to improve your resume bullets
- **Match Scoring** - Receive detailed scoring across multiple dimensions
- **Professional Reports** - Download formatted analysis reports
- **Easy-to-Use Interface** - Clean, intuitive web interface

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenRouter API key ([Get one here](https://openrouter.ai/))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/resume-analyzer.git
cd resume-analyzer
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the app**
```bash
streamlit run app.py
```

4. **Open your browser**
The app will automatically open at `http://localhost:8501`

## 📖 How to Use

1. **Enter API Key** - Add your OpenRouter API key in the sidebar
2. **Upload Resume** - Upload your resume in PDF format
3. **Paste Job Description** - Copy and paste the complete job description
4. **Analyze** - Click the "Analyze Resume" button
5. **Review Results** - Get detailed insights and suggestions
6. **Download Report** - Save the analysis for future reference

## 🎨 Features Breakdown

### Scoring Metrics

- **Hard Skills Match (40%)** - Technical skills alignment
- **Tools & Technologies (20%)** - Platform and tool proficiency
- **Experience Alignment (15%)** - Role and responsibility match
- **Keyword Density (15%)** - ATS optimization score
- **Formatting & Clarity (10%)** - Resume structure quality

### Analysis Components

- ✅ Missing skills identification
- ✅ Tool/platform gaps
- ✅ Business keyword analysis
- ✅ Bullet point improvements
- ✅ Skills section optimization
- ✅ Summary rewrite suggestions
- ✅ Final hiring recommendation

## 🌐 Deployment

### Deploy on Streamlit Cloud (Recommended)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Deploy!

### Deploy on Heroku

```bash
# Create Procfile
echo "web: streamlit run app.py --server.port=$PORT" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
```

### Deploy on Railway

1. Connect your GitHub repo to Railway
2. Add environment variables
3. Deploy automatically on push

## 🔧 Configuration

### API Key Setup

You can provide the API key in three ways:

1. **Through the UI** (Recommended for local use)
   - Enter in the sidebar

2. **Environment Variable**
   ```bash
   export OPENROUTER_API_KEY="your-key-here"
   ```

3. **Streamlit Secrets** (For deployment)
   Create `.streamlit/secrets.toml`:
   ```toml
   OPENROUTER_API_KEY = "your-key-here"
   ```

## 📊 Tech Stack

- **Frontend**: Streamlit
- **AI Model**: DeepSeek R1 (via OpenRouter)
- **PDF Processing**: pypdf
- **API Client**: OpenAI Python SDK

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Future Enhancements

- [ ] Batch resume processing
- [ ] Resume rewriter with one-click optimization
- [ ] Skill gap visualizations (charts/graphs)
- [ ] Cover letter generator
- [ ] LinkedIn profile analyzer
- [ ] Multi-role support (SWE, PM, Marketing, etc.)
- [ ] Export to PDF/DOCX formats
- [ ] Resume version comparison

## 🐛 Known Issues

- Large PDF files (>5MB) may take longer to process
- API rate limits may apply on free tier
- Some complex PDF formats may not extract perfectly

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [DeepSeek](https://www.deepseek.com/) for the powerful R1 model
- [OpenRouter](https://openrouter.ai/) for API access
- [Streamlit](https://streamlit.io/) for the amazing framework

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/resume-analyzer](https://github.com/yourusername/resume-analyzer)

---

⭐ **Star this repo if you find it helpful!**
