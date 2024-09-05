import os
from textwrap import dedent
from dotenv import load_dotenv
from crewai import Agent
from langchain_openai import ChatOpenAI
from crewai_tools import PDFSearchTool, FileReadTool, SerperDevTool
from read_knowledge_base_tool import read_pdf_tool
from TestSearchTool import SafeDirectorySearchTool

load_dotenv(".env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["SERPER_API_KEY"] = SERPER_API_KEY


llm = ChatOpenAI(model="gpt-4o-mini")
safe_dir_search_tool = SafeDirectorySearchTool()

searchInternetTool = SerperDevTool()
# gh_tool = GithubSearchTool(
#    gh_token= os.getenv("GITHUB_PERSONAL_TOKEN") ,
#    content_types=['code']
# )

# knowledge_base = fetch_pdf_content('Java-Standard-OSCE.pdf')
# web_search_tool = WebsiteSearchTool()
# seper_dev_tool = SerperDevTool()
# file_read_tool = FileReadTool(
#    file_path='Java-Standard.pdf',
#    description='A tool to read the java coding standards.'
# )
# pdf_tool = PDFSearchTool(
#    pdf='NRM-STI-601 Estándar de programación para el desarrollo de software con tecnología Java v1.2.pdf',
#    description='A tool to read the java coding standards knowledge base.',
#    config=dict(
#        llm=dict(
#            provider="openai",
#            config=dict(
#                model="gpt-4o-mini",
#                api_key=OPENAI_API_KEY
#                # temperature=0.5,
# top_p=1,
# stream=true,
#            ),
#        ),
#        embedder=dict(
#            provider="openai",  # or openai, ollama, ...
#            config=dict(
#                model="text-embedding-3-small",
#                api_key=OPENAI_API_KEY
#                # task_type="retrieval_document",
#                # title="Embeddings",
#            ),
#        ),
#    ))


class GameAgents():

    def senior_engineer_agent(self):
        return Agent(
            role='Senior Software Engineer',
            goal='Generate, fix or update code according to the requirements provided.',
            backstory=dedent("""\
				A seasoned engineer with years of experience in writing clean, efficient, and maintainable code."""),
            allow_delegation=False,
            memory=True,
            verbose=True,
            llm=llm,
            tools=[
                # To search for project files
                safe_dir_search_tool,
                FileReadTool(),  # To read specific project files
                searchInternetTool  # Find internet
            ]
            # tools=[gh_tool]
        )

#    def qa_engineer_agent(self):
#        return Agent(
#            role='Software Quality Assurance (QA) Engineer ',
#            goal='Analyze the provided code to identify errors and inconsistencies in its operation to ensure reliable delivery of the product.',
#            backstory=dedent("""\
# You are a Quality Assurance Engineer that specializes in checking code functionality.
#                You have an eye for detail and a knack for finding even the most hidden bugs.
#  			    You also check for security vulnerabilities,logic errors and performance problems"""),
#            allow_delegation=False,
#            verbose=True,
#            llm=llm
#        )

    def technical_leader_agent(self):
        return Agent(
            role='Technical Leader',
            goal='Ensure the code is functional and correct and adheres to coding standards.',
            backstory=dedent("""\
                An expert with a sharp eye for detail, responsible for maintaining code quality and ensuring all deliverables meet high standards."""),
            allow_delegation=True,
            verbose=True,
            llm=llm
            # tools=[read_pdf_tool]
            # To interact with coding standards in PDF format
            # tools=[PDFSearchTool()]
        )
