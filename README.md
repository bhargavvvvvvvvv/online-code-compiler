Online Code Compiler



A lightweight web-based code compiler that allows users to write, run, and test code in multiple programming languages directly from the browser.

Built using FastAPI, Docker, and AWS Lambda to provide secure and isolated code execution environments.



Features



Execute code in multiple languages (Python, Java, C++) through a REST API



Containerized execution using Docker for sandboxed and secure environments



FastAPI backend for high-performance API routing



Optional AWS Lambda deployment for scalable, low-latency execution



Modular design for adding more languages and execution modes



Comprehensive error handling for runtime and syntax errors



Technology Stack

Layer	Technology

Backend	FastAPI, Python

Containerization	Docker

Cloud	AWS Lambda, API Gateway

Languages Supported	Python, C++, Java

Other	REST API, JSON, Logging

Project Structure

online-code-compiler/

│

├── app/

│   ├── main.py              # FastAPI entry point

│   ├── routes/

│   │   └── compile.py       # API routes for code submission

│   ├── services/

│   │   └── executor.py      # Docker sandbox and execution logic

│   ├── utils/

│   │   └── error\_handler.py # Common error handling

│

├── Dockerfile

├── requirements.txt

├── README.md

└── tests/

&nbsp;   └── test\_compile.py



How It Works



The client sends code and language details via a POST request to /compile.



The backend launches a temporary Docker container to execute the code safely.



The container returns the output, execution time, or any error message.



The container is destroyed immediately after execution.



API Example



POST /compile



Request



{

&nbsp; "language": "python",

&nbsp; "code": "print('Hello, World!')"

}





Response



{

&nbsp; "output": "Hello, World!\\n",

&nbsp; "execution\_time": "0.38s",

&nbsp; "status": "success"

}



Local Setup



Clone the repository:



git clone https://github.com/bhargavvvvvvvvv/online-code-compiler.git

cd online-code-compiler





Create a virtual environment and install dependencies:



python -m venv .venv

.\\.venv\\Scripts\\Activate.ps1   # On Windows

pip install -r requirements.txt





Run the FastAPI application:



uvicorn app.main:app --reload





Open http://127.0.0.1:8000

&nbsp;in your browser to test.



Docker Setup (Optional)



Build and run the service inside a Docker container:



docker build -t online-code-compiler .

docker run -p 8000:8000 online-code-compiler



Deployment (Optional)



To deploy on AWS Lambda:



Package the FastAPI app using Zappa or AWS SAM



Configure API Gateway for HTTPS requests



Test via the deployed endpoint



Future Improvements



Add support for additional languages (JavaScript, Go)



Implement authentication and usage limits



Integrate a simple React frontend



Store user execution history for analysis



License



This project is licensed under the MIT License.



Author



Bhargav Patel

Master’s Student, Computer Science — University of Texas at Arlington

Email: bhargavpatel9071@gmail.com

