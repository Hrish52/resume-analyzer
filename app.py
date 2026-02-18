import streamlit as st
from openai import OpenAI
from pypdf import PdfReader
import io
import time

# Page configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stAlert {
        margin-top: 1rem;
    }
    .reportview-container .markdown-text-container {
        font-family: monospace;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">🎯 AI Resume Analyzer</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Powered by DeepSeek R1 - Get ATS insights and optimize your resume</p>', unsafe_allow_html=True)

# Sidebar for API key and settings
with st.sidebar:
    st.header("⚙️ Configuration")
    
    api_key = st.text_input(
        "OpenRouter API Key",
        type="password",
        help="Enter your OpenRouter API key. Get one at https://openrouter.ai/"
    )
    
    st.divider()
    
    st.header("📊 About")
    st.info("""
    This tool analyzes your resume against job descriptions using:
    - **ATS keyword matching**
    - **Hiring manager evaluation**
    - **Skill gap analysis**
    - **Improvement suggestions**
    """)
    
    st.divider()
    
    st.header("🚀 Features")
    st.markdown("""
    - ✅ Detailed match scoring
    - ✅ Missing skills identification
    - ✅ Bullet point improvements
    - ✅ ATS optimization tips
    - ✅ Professional formatting
    """)
    
    st.divider()
    
    with st.expander("💡 Tips for Best Results"):
        st.markdown("""
        1. Upload a **PDF** resume
        2. Paste the **complete** job description
        3. Review all suggestions carefully
        4. Apply improvements incrementally
        5. Test with multiple job postings
        """)


# Function to extract PDF content
def extract_content(pdf_file):
    """Extract text content from uploaded PDF file"""
    try:
        pdf_reader = PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {str(e)}")
        return None


# Function to analyze resume
def analyze_resume(resume_content, job_description, api_key):
    """Analyze resume against job description using DeepSeek API"""
    
    prompt = f"""
You are an ATS system + senior hiring manager for Data Analyst roles.

Your job is to analyze the resume against the job description using both:
1. ATS keyword matching logic
2. Human recruiter 7-second scan evaluation

Resume:
{resume_content}

Job Description:
{job_description}

Evaluation Instructions:

1. Extract all required hard skills from the Job Description.
2. Extract all preferred skills.
3. Extract soft skills and business skills.
4. Compare them to the resume content.
5. Calculate a weighted match score:
  - 40% Hard Skills Match
  - 20% Tools/Technologies Match
  - 15% Experience Alignment
  - 15% Keyword Density
  - 10% Formatting & Clarity

6. Identify:
  - Missing hard skills
  - Missing tools/platforms
  - Missing business/analytical phrases
  - Underrepresented keywords
  - Title misalignment (if any)

7. Evaluate resume quality:
  - Bullet clarity (strong/weak)
  - Quantified metrics presence
  - Action verbs usage
  - ATS formatting risks
  - Keyword stuffing risks

8. Suggest:
  - Exact bullet rewrites (max 5)
  - Skills section rewrite
  - Summary rewrite aligned to JD
  - Title adjustments if needed

Return output in this structured format:

=============================
ATS MATCH REPORT
=============================

Overall Match Score: XX/100

Hard Skills Match: XX%
Tools & Platforms Match: XX%
Experience Alignment: XX%
Keyword Density Score: XX%
Formatting Score: XX%

Missing Hard Skills:
- ...

Missing Tools/Platforms:
- ...

Missing Business Keywords:
- ...

Underrepresented Keywords:
- ...

Title Alignment Issues:
- ...

Bullet Improvements:
1. Original: ...
  Improved: ...

2. Original: ...
  Improved: ...

Skills Section Optimization:
- ...

Summary Optimization:
- ...

Final Recommendation:
(Should candidate apply? Yes/No + reasoning)
"""
    
    try:
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key
        )
        
        response = client.chat.completions.create(
            model="deepseek/deepseek-r1-0528:free",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=4000,
            temperature=0.7
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        st.error(f"API Error: {str(e)}")
        return None


# Main app layout
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📄 Upload Your Resume")
    uploaded_file = st.file_uploader(
        "Choose your resume PDF",
        type=['pdf'],
        help="Upload your resume in PDF format"
    )
    
    if uploaded_file:
        st.success(f"✅ Uploaded: {uploaded_file.name}")
        
        # Show file details
        with st.expander("📋 File Details"):
            file_details = {
                "Filename": uploaded_file.name,
                "File Size": f"{uploaded_file.size / 1024:.2f} KB",
                "File Type": uploaded_file.type
            }
            for key, value in file_details.items():
                st.text(f"{key}: {value}")

with col2:
    st.header("💼 Job Description")
    job_description = st.text_area(
    "Paste the complete job description here",
    height=300,
    placeholder="Paste the job description then press Ctrl+Enter...",
    help="Include all details for accurate analysis"
)
    
    if job_description:
        word_count = len(job_description.split())
        st.caption(f"📊 Word count: {word_count} words")

# Analyze button
st.divider()

col_analyze, col_space = st.columns([1, 3])

with col_analyze:
    analyze_button = st.button(
        "🔍 Analyze Resume",
        type="primary",
        use_container_width=True,
        disabled=not (uploaded_file and job_description and api_key)
    )

# Validation messages
if analyze_button:
    if not api_key:
        st.error("⚠️ Please enter your OpenRouter API key in the sidebar")
    elif not uploaded_file:
        st.error("⚠️ Please upload your resume PDF")
    elif not job_description:
        st.error("⚠️ Please paste the job description")

# Analysis section
if analyze_button and uploaded_file and job_description and api_key:
    
    with st.spinner("🔄 Extracting resume content..."):
        resume_content = extract_content(uploaded_file)
    
    if resume_content:
        st.success("✅ Resume content extracted successfully!")
        
        with st.expander("👀 Preview Resume Content"):
            st.text_area("Extracted Text", resume_content[:1000] + "...", height=200)
        
        with st.spinner("🤖 Analyzing with AI... This may take 2-3 minutes..."):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.3)  # Simulated progress
                progress_bar.progress(i + 1)
            
            result = analyze_resume(resume_content, job_description, api_key)
        
        if result:
            st.balloons()
            st.success("✅ Analysis Complete!")
            
            st.divider()
            
            # Display results
            st.header("📊 Analysis Results")
            
            # Create tabs for different views
            tab1, tab2 = st.tabs(["📋 Full Report", "💾 Download"])
            
            with tab1:
                st.markdown(result)
            
            with tab2:
                st.subheader("Download Your Report")
                
                col_dl1, col_dl2 = st.columns(2)
                
                with col_dl1:
                    # Download as text
                    st.download_button(
                        label="📄 Download as TXT",
                        data=result,
                        file_name="resume_analysis_report.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                
                with col_dl2:
                    # Download as markdown
                    st.download_button(
                        label="📝 Download as MD",
                        data=result,
                        file_name="resume_analysis_report.md",
                        mime="text/markdown",
                        use_container_width=True
                    )
                
                st.info("💡 **Tip:** Save this report and implement the suggestions before applying!")

# Footer
st.divider()
st.markdown("""
    <div style='text-align: center; color: #666; padding: 2rem;'>
        <p>Built with ❤️ using Streamlit and DeepSeek R1</p>
        <p style='font-size: 0.9rem;'>© 2025 AI Resume Analyzer | 
        <a href='https://github.com/yourusername/resume-analyzer' target='_blank'>GitHub</a> | 
        <a href='https://openrouter.ai/' target='_blank'>Get API Key</a></p>
    </div>
    """, unsafe_allow_html=True)
