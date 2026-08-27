# ResumeLens — AI Resume Screening & Job Matching

ResumeLens is an AI-powered resume screening system that analyzes a job description, parses multiple candidate resumes, compares candidates against job requirements, and ranks them based on an AI-generated match score.

The project uses Groq's API with `openai/gpt-oss-120b` for LLM-based extraction and matching, Pydantic for structured data validation, and PyPDF / python-docx for extracting text from resumes.

## Features

- Read job descriptions from a `.txt` file
- Support PDF and DOCX resumes
- Extract structured job requirements using an LLM
- Parse resumes using an LLM
- Extract candidate:
  - Name
  - Email
  - Phone
  - Total experience
  - Skills
  - Work experience
  - Education
  - Projects
  - Certifications
- Compare resumes against job requirements
- Generate an overall match score from 0–100
- Identify matching skills
- Identify missing important skills
- Check whether experience requirements are met
- Rank candidates by score
- Display top 2 candidates
- Display lowest 2 candidates
- Validate LLM-generated JSON using Pydantic

## Project Structure

```text
ResumeLens/
│
├── resume_parser.py
│
├── Resumes/
│   └── job_description.txt
│
├── resumes/
│   ├── candidate_1.pdf
│   ├── candidate_2.pdf
│   ├── candidate_3.docx
│   └── ...
│
├── .env
├── .gitignore
└── README.md
