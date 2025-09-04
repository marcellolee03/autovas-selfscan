# AutoVAS

**Complete vulnerability assessment and automated patching solution**

AutoVAS provides end-to-end automation for vulnerability management, from vulnerability recognition through OpenVAS scanning to AI-powered patch script generation using Large Language Models.

## Features

- **Automated Vulnerability Discovery**: Automatically identifies localhost IP and creates OpenVAS scanning tasks
- **Comprehensive Scanning**: Executes vulnerability scans using OpenVAS engine
- **Intelligent Report Processing**: Formats scan reports to CSV and processes vulnerability data
- **AI-Powered Patch Generation**: Generates customized remediation scripts using Google Gemini or DeepSeek APIs
- **Environment-Aware**: Incorporates computational environment information for context-aware patching
- **Complete Automation**: Streamlines the entire process from scan to solution

### Generated Patch Examples

The repository includes real examples of AI-generated remediation scripts in the `/Generated Scripts` directory. These samples demonstrate the quality and variety of patches produced by different LLMs when processing actual vulnerability scan results.

**For research evaluators**: Please refer to the `/Generated Scripts` folder to examine the AI-generated code samples that showcase the system's capabilities in producing contextually appropriate security patches.

## Prerequisites

- Docker Compose

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/AutoVAS.git
cd AutoVAS
```

2. Run the setup script:
```bash
./setup-autovas.sh
```

## Usage

### Configuration

1. **API Key Setup**: Edit `src/main.py` to include your API key:
   - For Google Gemini: Add your Google API key
   - For DeepSeek: Add your DeepSeek API key

2. **LLM Selection**: Modify line 46 in `src/main.py` based on your chosen LLM:
   
   **For Google Gemini:**
   ```python
   response = ask_LLM.ask_gemini(API_KEY, prompt)
   ```
   
   **For DeepSeek:**
   ```python
   response = ask_LLM.ask_deepseek(API_KEY, API_URL, prompt)
   ```

### Running AutoVAS

Execute the main application:
```bash
python src/main.py
```

## How It Works

1. **Network Discovery**: Automatically identifies localhost IP address
2. **Task Creation**: Creates and configures vulnerability scanning tasks in OpenVAS
3. **Vulnerability Scanning**: Executes comprehensive security scans
4. **Report Processing**: Converts scan results to structured CSV format
5. **Data Analysis**: Processes vulnerability data alongside system environment information
6. **AI Patch Generation**: Creates customized remediation scripts using LLM APIs
