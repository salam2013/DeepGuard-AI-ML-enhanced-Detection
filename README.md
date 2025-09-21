# DeepGuard AI ML enhanced-Detection
## DeepGuard AI, a multi-modal deepfake detection tool!

---

## Overview

DeepGuard AI, Pro (with ML) is a Streamlit-powered application that helps verify the authenticity of digital content. It supports text, image, audio, and video analysis, making it versatile for multiple use cases. The tool allows users to upload files or paste text directly, automatically extracting and preparing content for evaluation. Results are displayed with clear likelihood scores and visual feedback, helping users understand whether material is AI-generated or authentic. With modular utilities in `utils.py`, developers can easily swap in real machine learning models for enhanced accuracy. DeepGuard AI is designed for simplicity, scalability, and practical demonstrations in cybersecurity and content authenticity verification.
Perfect
# DeepGuard AI Pro (with ML)


---
## Features
- **Multi-Modality Support**: Analyze text, images, videos, and audio files.
- **File Upload & Direct Input**:
  - Upload `.txt`, `.pdf`, `.docx`, `.rtf`, `.odt` files for text analysis.
  - Upload media files for image, audio, or video analysis.
- **Text Extraction**:
  - Extracts text from PDFs, Word docs, ODTs, and plain text.
- **Interactive UI**:
  - Built with [Streamlit](https://streamlit.io/) for a clean, interactive web app.
  - Sidebar controls for modality selection and detection threshold.
- **Session Management**:
  - Keeps track of results and detailed analysis across runs.
- **Customizable Analysis**:
  - Uses placeholder ML logic (via `utils.py`) that can be replaced with real pretrained models.

---


## Project Structure
DeepGuard-AI/
│
├── app.py              # Main Streamlit app
├── utils.py            # Utility functions (setup, analysis, session state)
├── requirements.txt    # Dependencies
└── README.md           # Project documentation

````

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/deepguard-ai.git
   cd deepguard-ai
````

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

##  Usage

Run the Streamlit app:


<img width="782" height="214" alt="image" src="https://github.com/user-attachments/assets/7dfbf129-9234-4b74-b3b9-3d95692cdc12" />



```bash
streamlit run app.py
```

This will open **DeepGuard AI** in your browser.




<img width="1887" height="782" alt="image" src="https://github.com/user-attachments/assets/0d456889-1420-4a5f-aa0e-04fc24517ebd" />





---

## Requirements

```
streamlit
pymupdf
python-docx
odfpy
```

*(Add ML frameworks such as `torch` and `transformers` later if you integrate real models.)*

---



<img width="478" height="342" alt="image" src="https://github.com/user-attachments/assets/a94188d8-473e-40b5-a698-da3060978611" />


<img width="1039" height="37" alt="image" src="https://github.com/user-attachments/assets/082157f7-6834-436a-928a-950ebb1b8969" />


---
**Output**
Example Analysis Result

Input: IMAGE


   <img width="1900" height="859" alt="Screenshot 2025-09-21 174012" src="https://github.com/user-attachments/assets/8afbbfd9-6ee0-44e4-93c8-4c5c480ae783" />


   
   ![photo_2025-09-01_22-05-49](https://github.com/user-attachments/assets/a626e4ac-96ff-4e35-83b2-68cefdb408c5)

Original
--

   
   <img width="1024" height="1536" alt="aab" src="https://github.com/user-attachments/assets/0cc3092b-9c67-4d6d-a63d-10014f5361d9" />
 
AI generated
--


   <img width="1798" height="856" alt="image" src="https://github.com/user-attachments/assets/9b0785f2-0b43-4d47-b2e5-1983340c13d6" />
   <img width="1888" height="820" alt="image" src="https://github.com/user-attachments/assets/a741baf2-db5e-47c4-8e81-597fcfe9b319" />

 result
--


Processing: Extracts image, runs placeholder ML logic

Output:

AI Likelihood Score: 86.6%


Verdict: Likely AI-generated (above 60% threshold)
--
  Repeat the process with Text, Audio, vedio 



## Future Enhancements

* Improve detection accuracy with multimodal deep learning.
* Add report export (PDF/CSV) for results.
* Cloud deployment with Docker support.
* Multi-user authentication and history tracking.

---

##  Disclaimer

This project currently uses **dummy analysis functions** for demonstration.
Replace with real ML models before using in production.

---

## Author

**Shuaib Salami A. cybersecurity consultant**

Developed as part of a **BNS Cyberlab exercise** on AI-driven content authenticity verification.

---

```

---


```

