# RAG-based-AI-Agents
Retrieval Augmented Generation-based Agentic CrewAI

## Introduction
This repository contains agentic workflow with CrewAI with RAG framework. For the initial setup refer to the [CrewAI-Local-Agents-1](https://github.com/Maryam-Nasseri/CrewAI-Local-Agents-1) repository. This example assumes you have already installed CrewAI and its tools as per this link.

## Run The Agents Using RAG
1. Set up a virtual environment and configure it in .venv file to point to the Ollama endpoints and specify the model
2. In your Model File set the model and parameters
3. In your script file create a new custom model with `Ollama create`, save and run the shell in terminal
5. Use the Python file in this repo, set the role and task descriptions
6. Using wget either download the CSV file from the terminal or integrate it via the `subprocess` and `Popen`. Specify the full path to the file in your Python file.
7. Run the py file.

## Additional Explanation and the Main Features
This is a simple setup project that employs only two agents, each performing one task. You may set as many refiners as you need. You can also enhance the quality of the responses by setting allow delegation to True to allow agents to solve more complex problems using a chain of internal enquiries. This project uses a sequential task execution but you can set up a hierarchical one.

## Tutorial Video:
[![Watch the video about AI agents using RAG or Retrieval Aygmented Generation](https://img.youtube.com/vi/4G6MlUxh3q8/maxresdefault.jpg)](https://youtu.be/4G6MlUxh3q8) 
