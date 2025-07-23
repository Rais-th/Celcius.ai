# Celcius AI

## 🔥 Overview
A specialized thermal analysis application built for R&D teams to analyze glass toughening processes. The app provides comprehensive analysis of temperature data from multiple positions with AI-powered reporting capabilities.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Streamlit
- Required packages (see requirements.txt)

### Installation
```bash
pip install -r requirements.txt
```

### Running the Application
```bash
streamlit run app.py
```

## 📁 Project Structure
```
ANALYSIS/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (OpenAI API key)
├── cz_position6.dat   # Sample data file
└── README.md          # This documentation
```

## 🎯 Key Features

### 1. **Apple-Style UI Design**
- Dark theme with glassmorphism effects
- Responsive sidebar control panel
- Modern file upload interface
- Consistent styling throughout

### 2. **Multi-Format Data Support**
- `.dat` files (primary format)
- `.xlsx` Excel files
- `.csv` files
- `.txt` files

### 3. **Analysis Types**
1. **Temperature Curves Over Time** - Time-series visualization
2. **Individual Glass Shell Analysis** - Shell-specific analysis
3. **Peak Temperature Summary** - Temperature statistics
4. **Multi-Position Composite** - Cross-position comparison
5. **Interactive Plotly View** - Interactive visualizations
6. **Full Line Thermal Journey** - Complete process analysis
7. **AI Summary & Reports** - AI-powered insights

## 🔧 Technical Architecture

### Core Components

#### 1. **Data Processing Pipeline**
```python
# Key functions in app.py
- process_dat_file()      # Handles .dat file parsing
- process_excel_file()    # Handles Excel file processing
- detect_plateaus_for_ai() # AI plateau detection algorithm
```

#### 2. **Visualization Engine**
- **Plotly**: Interactive charts and 3D visualizations
- **Streamlit**: UI components and layout
- **Custom CSS**: Apple-style theming

#### 3. **AI Integration**
- **OpenAI GPT-4**: Report generation and analysis
- **Environment Variables**: API key management via `.env`
- **Prompt Engineering**: Specialized prompts for thermal analysis

#### 4. **PDF Generation**
- **ReportLab**: Professional PDF reports
- **Custom Templates**: SEDIVER branding
- **Watermark Support**: Internal use marking

### Data Flow
```
File Upload → Data Processing → Analysis Selection → Visualization/AI → Export
```

## 🔑 Critical Code Sections

### 1. **File Processing Logic** (Lines 590-750)
```python
# Handles multiple file formats and data validation
if uploaded_files:
    position_data = {}
    for uploaded_file in uploaded_files:
        # File processing logic
```

### 2. **Apple-Style CSS** (Lines 35-150)
```css
/* Critical styling for Apple UI */
.apple-control-panel {
    background: rgba(28, 28, 30, 0.95);
    backdrop-filter: blur(20px);
    /* ... */
}
```

### 3. **Analysis Sections** (Lines 800-2400)
Each analysis type has its own section with:
- Conditional rendering based on data availability
- Interactive controls
- Visualization components
- Export capabilities

### 4. **AI Integration** (Lines 1940-2200)
```python
# OpenAI API integration
openai_api_key = os.getenv("OPENAI_API_KEY")
# Plateau detection and analysis
plateaus = detect_plateaus_for_ai(df, sensor_column)
```

## 🛠️ Development Guidelines

### Code Organization
- **Single File Architecture**: All code in `app.py` for simplicity
- **Modular Functions**: Each analysis type is self-contained
- **State Management**: Uses Streamlit session state
- **Error Handling**: Comprehensive try-catch blocks

### Styling Conventions
- **Apple Design System**: Consistent with macOS aesthetics
- **Dark Theme**: Primary color scheme
- **Glassmorphism**: Backdrop blur effects
- **Responsive Design**: Works on different screen sizes

### Data Handling
- **Multiple File Support**: Handles various formats
- **Memory Efficient**: Processes files individually
- **Error Resilient**: Graceful handling of malformed data

## 🔐 Security Considerations

### Environment Variables
```bash
# .env file (not in version control)
OPENAI_API_KEY=your_api_key_here
```

### Data Privacy
- No data persistence beyond session
- Local processing only
- Secure API key handling

## 📊 Data Formats

### Expected Data Structure
```
Time | Sensor1 | Sensor2 | ... | SensorN
-----|---------|---------|-----|--------
0    | 25.5    | 26.1    | ... | 24.8
1    | 26.2    | 27.0    | ... | 25.5
```

### File Naming Conventions
- Position files: `cz_position{N}.dat`
- Excel files: `{ID}_recap_temperature.xlsx`
- Generic: Any descriptive name with supported extension

## 🚨 Common Issues & Solutions

### 1. **File Upload Issues**
- **Problem**: Files not processing
- **Solution**: Check file format and data structure
- **Debug**: Check browser console for errors

### 2. **AI Analysis Failures**
- **Problem**: OpenAI API errors
- **Solution**: Verify API key in `.env` file
- **Debug**: Check API quota and network connectivity

### 3. **Visualization Errors**
- **Problem**: Charts not rendering
- **Solution**: Ensure data has required columns
- **Debug**: Check data types and null values

### 4. **Performance Issues**
- **Problem**: Slow loading with large files
- **Solution**: Implement data sampling for preview
- **Optimization**: Consider chunked processing

## 🔄 Deployment

### Local Development
```bash
streamlit run app.py --server.port 8501
```

### Production Deployment
1. **Streamlit Cloud**: Direct GitHub integration
2. **Docker**: Containerized deployment
3. **Heroku**: Cloud platform deployment

### Environment Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
echo "OPENAI_API_KEY=your_key" > .env
```

## 📈 Future Enhancements

### Planned Features
1. **Database Integration**: Persistent data storage
2. **User Authentication**: Multi-user support
3. **Real-time Processing**: Live data feeds
4. **Advanced AI Models**: Custom thermal analysis models
5. **Mobile Optimization**: Responsive mobile interface

### Technical Debt
1. **Code Splitting**: Break down large `app.py` file
2. **Testing Suite**: Unit and integration tests
3. **Documentation**: Inline code documentation
4. **Performance**: Optimize large file handling

## 🤝 Developer Handover Checklist

### Immediate Tasks
- [ ] Review all analysis sections functionality
- [ ] Test file upload with various formats
- [ ] Verify AI integration works
- [ ] Check PDF export functionality
- [ ] Test responsive design

### Knowledge Transfer
- [ ] Understand data processing pipeline
- [ ] Review Apple UI styling system
- [ ] Learn Plotly visualization patterns
- [ ] Understand AI prompt engineering
- [ ] Review error handling strategies

### Setup Requirements
- [ ] Python environment setup
- [ ] OpenAI API key configuration
- [ ] Streamlit familiarity
- [ ] CSS/styling knowledge
- [ ] Data analysis understanding

## 📞 Support & Maintenance

### Key Dependencies
- **Streamlit**: UI framework
- **Plotly**: Visualization library
- **Pandas**: Data manipulation
- **OpenAI**: AI integration
- **ReportLab**: PDF generation

### Monitoring Points
- File upload success rates
- AI API response times
- User session durations
- Error frequencies
- Performance metrics

## 📝 Notes for Developers

### Code Quality
- Follow PEP 8 style guidelines
- Add docstrings to new functions
- Implement proper error handling
- Test with various data formats

### UI/UX Principles
- Maintain Apple design consistency
- Ensure accessibility compliance
- Optimize for user workflow
- Provide clear feedback messages

### Performance Optimization
- Lazy load large datasets
- Implement caching where appropriate
- Optimize Plotly chart rendering
- Monitor memory usage

---

Dev: Rais Thelemuka | rthelemuka@gmail.com
