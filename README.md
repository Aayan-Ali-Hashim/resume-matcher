# Resume vs Job Description Matcher

This web application allows users to upload their resumes and job descriptions to calculate a match percentage based on text similarity. It helps recruiters find the best candidates for a job by matching the skills and content from resumes with job descriptions.

## Features

- Upload PDF resume files and paste job descriptions.
- Preprocesses resume and job description texts to extract relevant information.
- Compares resumes with job descriptions using cosine similarity.
- Extracts and compares skills mentioned in both the resume and the job description.

## Tech Stack

- **Backend:** Python
- **Libraries:** 
  - `spacy` for Natural Language Processing (NLP)
  - `PyMuPDF` for extracting text from PDF resumes
  - `sklearn` for calculating text similarity
- **Frontend:** Streamlit for the user interface

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- [Anaconda](https://www.anaconda.com/products/individual) (recommended)
- Internet connection to download necessary models and dependencies

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/resume-matcher.git
   cd resume-matcher

   ```

2. Create a virtual environment and install dependencies:
   ```bash
   conda create -n resume-matcher python=3.8
   conda activate resume-matcher
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

## How to Use

### 1. Upload your Resume (PDF): 

 `Click on the "Upload your resume" button and select your resume in PDF format.`

### 2. Paste the Job Description:

`Copy and paste the job description into the text area provided.`

### 3. View Results:

`The app will display the match score between your resume and the job description, along with a skill comparison.`

## Skills Matching
 You can modify the skills list in the app to match your desired job roles. The app will compare the skills mentioned in your resume with the job description.

## Contributing
Feel free to fork this repository, make improvements, and open pull requests. Contributions are always welcome!

## License
This project is licensed under the MIT License - see the [License](LICENSE) file for details.

