# Coding Assistant
## Introduction
This project is an example using the CrewAI framework to automate the process of create code. CrewAI orchestrates autonomous AI agents, enabling them to collaborate and execute complex tasks efficiently.

#### Game Builder

- [CrewAI Framework](#crewai-framework)
- [Running the script](#running-the-script)
- [Details & Explanation](#details--explanation)
- [License](#license)

## CrewAI Framework
CrewAI is designed to facilitate the collaboration of role-playing AI agents. In this example, these agents work together to give a coding development assistance

## Running the Script
This example uses GPT-4o-mini.

- **Configure Environment**: set up the environment variable `.env`. OPENAI_API_KEY,SERPER_API_KEY
- **Install Dependencies**: Run `poetry install --no-root`.
- **Execute the Script**: Run `python main.py` and input your idea.

## Details & Explanation
- **Running the Script**: Execute `python main.py`` and input your idea when prompted. The script will leverage the CrewAI framework to process the idea and generate a landing page.
- **Key Components**:
  - `./main.py`: Main script file.
  - `./tasks.py`: Main file with the tasks prompts.
  - `./agents.py`: Main file with the agents creation.

## License
This project is released under the MIT License.
