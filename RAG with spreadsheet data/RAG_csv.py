#Ma.Nasseri_RAG_csv.py


from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
from crewai_tools import CSVSearchTool
import os
#from langchain_community.output_parsers.rail_parser import GuardrailsOutputParser

os.environ["OPENAI_API_KEY"] = "NA"

llm = ChatOpenAI(

    model = "llama3",

    base_url = "http://localhost:11434/v1")


# 1. wget the link from terminal:
#wget 'https://github.com/aiplanethub/Datasets/blob/master/IT_Salary_Survey_EU_18-20/Survey_2020.csv' -O './IT_salaries.csv'

# OR #2. integrate as a subprocess:

# import subprocess

# def runcmd(cmd, verbose = False, *args, **kwargs):

#     process = subprocess.Popen(
#         cmd,
#         stdout = subprocess.PIPE,
#         stderr = subprocess.PIPE,
#         text = True,
#         shell = True
#     )
#     std_out, std_err = process.communicate()
#     if verbose:
#         print(std_out.strip(), std_err)
#     pass

# runcmd("wget https://github.com/aiplanethub/Datasets/blob/master/IT_Salary_Survey_EU_18-20/Survey_2020.csv", verbose = True)

# OR #3. Local file:
# By default, the tool uses OpenAI for both embeddings and summarization
tool = CSVSearchTool(csv='FULL_PATH/IT_salaries.csv')


#agent1 researcher
researcher = Agent(role = "Expert Data Analyst",

                      goal = """Extract relevant data from the csv file and structure them as instructed""",

                      backstory = """You are an expert data analyst for extracting information from csv files as instructed in the task description""",

                      allow_delegation = False,

                      verbose = True,
                      
                      tool = tool,

                      llm = llm)

#agent2 writer
writer = Agent(role = "Technical Report Writer",

                      goal = """Summarise the researcher's responses in relevant and precise steps and then write technical report on the summarised data using your knowledge""",

                      backstory = """You are an expert in writing AI-related technical report for individual tech enthusiasts; produce a detailed report in simple language""",

                      allow_delegation = False,

                      verbose = True,

                      llm = llm)

# Create tasks
task1 = Task(
  description="""Using the csv file named 'IT_salaries.csv extract the top 10 rows with the highest salaries in the entire csv file based on the column 'Yearly brutto salary (without bonus and stocks) in EUR
' and rank them based on the column 'Position' and column 'Your main technology / programming language'. DO NOT deviate from the actual content of the csv file; then present them in a structured format.""",
  expected_output="top 10 rows based on salaries in a structured format",
  agent=researcher
)

task2 = Task(
  description="""Using the structured data and insights provided by the Expert Data Analyst agent, develop a precise technical report that highlights the most important skills, technologies, and programming languages needed to obtain highest salaries in the IT sector, then from your knowledge explain a brief overview of the path and timeline required to obtain that skills, technology, or programming language.""",
  expected_output="Technical report and explanation of at least 1000 words",
  agent=writer
)


# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  verbose=2, 
)


result = crew.kickoff()

