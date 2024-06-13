# RAG-based-AI-Agents
Retrieval Augmented Generation-based Agentic CrewAI

## Introduction
This repository contains agentic workflow with CrewAI with RAG framework. For the initial setup refer to the [CrewAI-Local-Agents-1](https://github.com/Maryam-Nasseri/CrewAI-Local-Agents-1) repository. This example assumes you have already installed CrewAI and its tools as per this link.

Run The Agents Using RAG
1. Set up a virtual environment and configure it in .venv file to point to the Ollama endpoints and specify the model
2. In your Model File set the model and parameters
3. In your script file create a new custom model with `Ollama create`, save and run the shell in terminal
5. Use the Python file in this repo, set the role and task descriptions
6. Using wget either download the CSV file from the terminal or integrate it via the `subprocess` and `Popen`. Specify the full path to the file in your Python file.
7. Run the py file.
