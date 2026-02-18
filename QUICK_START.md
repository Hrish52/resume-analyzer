# 🚀 Quick Start Guide - AI Resume Analyzer

## ⚡ Get Running in 3 Minutes

### Step 1: Install Dependencies (1 minute)
```bash
pip install streamlit openai pypdf
```

### Step 2: Get Your API Key (1 minute)
1. Go to https://openrouter.ai/
2. Sign up (free)
3. Go to "Keys" section
4. Create a new API key
5. Copy it

### Step 3: Run the App (30 seconds)
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

---

## 📱 How to Use

### First Time Setup
1. **Paste API Key** in the sidebar (left side)
2. **Upload your resume** (PDF format)
3. **Copy & paste job description** from the job posting
4. **Click "Analyze Resume"**
5. Wait 30-60 seconds for AI analysis
6. **Review the report** and implement suggestions!

---

## 🎯 What You'll Get

### Match Score
- Overall score out of 100
- Breakdown by category (skills, tools, experience, keywords, formatting)

### Gap Analysis
- Missing hard skills
- Missing tools/platforms
- Underrepresented keywords
- Business terminology gaps

### Actionable Improvements
- Specific bullet point rewrites
- Skills section optimization
- Summary suggestions
- Final hiring recommendation

---

## 💡 Pro Tips

### For Best Results
1. ✅ Use PDF resumes (not DOCX or images)
2. ✅ Include COMPLETE job descriptions (copy everything)
3. ✅ Test with 3-5 similar job postings to find patterns
4. ✅ Apply suggestions incrementally and re-test
5. ✅ Download and save each report for reference

### Common Mistakes to Avoid
1. ❌ Don't use image-based PDFs (text must be selectable)
2. ❌ Don't include only job requirements - paste the full posting
3. ❌ Don't apply ALL suggestions blindly - use judgment
4. ❌ Don't forget to tailor for each job (generic resumes score lower)

---

## 🐛 Troubleshooting

### "API Error" Message
- Check your API key is correct
- Ensure you have credits on OpenRouter
- Try again (rate limits may apply)

### "Error Reading PDF"
- Ensure PDF contains selectable text (not just images)
- Try re-saving PDF or use a different PDF
- Check file isn't corrupted

### App Won't Start
```bash
# Reinstall dependencies
pip install --upgrade streamlit openai pypdf

# Check Python version (need 3.8+)
python --version

# Try running with full path
python -m streamlit run app.py
```

### Slow Analysis
- Normal! DeepSeek R1 thinks deeply (20K+ tokens)
- Wait 30-90 seconds depending on resume length
- Check internet connection

---

## 🌐 Deploy Online (Optional)

### Free Deployment on Streamlit Cloud

1. **Push to GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/resume-analyzer.git
git push -u origin main
```

2. **Deploy**
- Go to https://share.streamlit.io
- Click "New app"
- Connect your GitHub repo
- Select `app.py`
- Click "Deploy"

3. **Add API Key as Secret**
- In Streamlit Cloud dashboard
- Go to "Settings" → "Secrets"
- Add: `OPENROUTER_API_KEY = "your-key-here"`

**Your app is now live!** Share the URL with anyone.

---

## 📊 Understanding the Score

| Score | Meaning | Action |
|-------|---------|--------|
| 85-100 | Excellent Match | Apply confidently! |
| 70-84 | Good Match | Minor tweaks needed |
| 50-69 | Fair Match | Significant gaps to address |
| <50 | Poor Match | Consider if worth applying |

**Note:** Score isn't everything! A 65% match with strong experience might be better than an 80% keyword-stuffed resume.

---

## 🎓 Next Steps After Analysis

1. **Review Missing Skills**
   - Add skills you have but forgot to mention
   - Consider learning critical missing skills

2. **Rewrite Bullet Points**
   - Use suggested improvements as templates
   - Keep your authentic voice

3. **Optimize Keywords**
   - Naturally integrate missing keywords
   - Don't keyword stuff (ATS can detect this)

4. **Update Skills Section**
   - Match terminology from job description
   - Group similar tools together

5. **Tailor Summary/Objective**
   - Align with company's mission
   - Highlight relevant experience

6. **Re-analyze**
   - Test improved version
   - Aim for 10-15 point score increase

---

## 🆘 Need Help?

- **Issues**: Open a GitHub issue
- **Questions**: Check README.md
- **Updates**: Star the repo for notifications

---

**Ready to optimize your resume? Let's get started! 🚀**

Run: `streamlit run app.py`
