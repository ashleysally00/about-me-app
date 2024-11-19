# AI-Powered About Me Generator

This is a project currently under development and considered **work in progress**. ☀️ 🌈

## Overview
This is a Streamlit-based web application that helps users generate engaging and personalized "About Me" sections for platforms like LinkedIn, resumes, and personal websites. The app leverages the **Gemini Generative AI API** by Google to create professional, casual, or enthusiastic bios tailored to individual needs.

## Table of Contents
- [AI-Powered About Me Generator](#ai-powered-about-me-generator)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Installation and Setup](#installation-and-setup)
    - [Prerequisites](#prerequisites)
    - [Steps](#steps)
  - [Usage](#usage)
  - [Environment Variables](#environment-variables)
  - [Project Structure](#project-structure)
  - [Key API Information](#key-api-information)
  - [Example](#example)
    - [Input:](#input)
    - [Generated Bio:](#generated-bio)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Features
- **Customizable Bio Generation**
  - Generate bios in different tones (e.g., Casual, Professional, Enthusiastic, or Custom)
  - Specify details like name, profession, skills, and tone to create tailored outputs
- **Streamlit-Powered User Interface**
  - Interactive and intuitive interface for users to input their preferences
- **Real-Time AI-Generated Results**
  - Uses the **Gemini Generative AI API (Pro 1.5)** for high-quality text generation

## Technologies Used
- **Frontend**: Streamlit
- **Backend**: Python
- **AI Model**: Gemini Generative AI (Pro 1.5)
- **Authentication**: Google Generative AI API key

## Installation and Setup

### Prerequisites
- Python 3.8–3.12
- Google Generative AI API Key

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up API Key**:
   Create a `.env` file in the root directory and add your Google Generative AI API key:
   ```
   GOOGLE_API_KEY=your_google_api_key
   ```

5. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Open the app in your browser (Streamlit provides the local URL)
2. Enter details such as:
   - Name
   - Profession
   - Skills
   - Desired Tone (Casual, Professional, Enthusiastic, or Custom)
3. Click "Generate Bio" to get your personalized "About Me" section

## Environment Variables
Ensure your `.env` file includes the following:
```
GOOGLE_API_KEY=your_google_api_key
```

## Project Structure
```
.
├── app.py          # Main Streamlit app
├── server.py       # Backend logic for bio generation
├── requirements.txt # Python dependencies
├── .env            # API key (not included in the repository)
├── .gitignore      # Ignored files and folders
└── README.md       # Project documentation
```

## Key API Information
- **Model Used**: Gemini Pro 1.5
- **Endpoint**: `generate_text`
- **Features**:
  - Customizable Prompt Engineering: Tailored prompts for generating bios in various tones
  - Parameter Adjustments:
    - `temperature`: Controls creativity (e.g., 0.7 for balanced, 0.8 for casual tone)
    - `max_output_tokens`: Limits the length of the generated bio

## Example

### Input:
```
Name: Alice
Profession: Data Scientist
Skills: Machine Learning, Python, Data Visualization
Tone: Enthusiastic
```

### Generated Bio:
```
Meet Alice, an enthusiastic Data Scientist passionate about solving complex problems with Machine Learning. With expertise in Python and Data Visualization, she transforms raw data into actionable insights, bringing energy and creativity to every project!
```

## Contributing
1. Fork the repository
2. Create a new branch for your feature/bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to the branch:
   ```bash
   git commit -m "Add new feature"
   git push origin feature-name
   ```
4. Submit a pull request

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- Thanks to Google Generative AI (Gemini Pro 1.5) for powering the text generation
- Built with ❤️ using Streamlit