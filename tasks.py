from textwrap import dedent
from crewai import Task


class NewCodeTasks():
    def set_init_project_structure(self, agent):
        structure_task = Task(
            description=dedent(
                """\ Initialize the project structure in order to implement the  requirement: {requirement}. 
                     Search on internet for similar solutions to the requirement to build or improve the initial project structure"""),
            expected_output='The initial project structure and files.',
            agent=agent
        )
        return structure_task

    def implement_code_task(self, agent):
        implement_changes_task = Task(
            description=dedent("""\ According to the structure, implement the requirement: {requirement}.  
                               For libraries or dependencies, look for the latest stable version on the internet.
                               To complement your final answer, search on internet for similar solutions that match the requirement and the version of the project's libraries and dependencies.
                               If you think the initial structure is not enough to implement the requirement do the neccesary changes adding or eliminating files"""),
            expected_output='Complete content of all modified files with the implemented feature.',
            agent=agent
        )
        return implement_changes_task


class ExistingCodeTasks():

    def get_project_context(self, agent):
        readme_task = Task(
            description=dedent(
                """\ Read the README.md file to understand the project context from the project path: {project_path}."""),
            expected_output='Context and overview of the project based on the README.md file.',
            agent=agent
        )
        return readme_task

    def get_files_to_change_task(self, agent):
        analyze_files_task = Task(
            description="Analyze all the project files to determine which files need to be modified in order to implementent the requirement: {requirement}. Find the project files in {project_path}",
            expected_output='List of files with complete path that need modification or fixes based on the requirement.',
            agent=agent
        )
        return analyze_files_task

    def implement_update_code_task(self, agent):
        implement_changes_task = Task(
            description=dedent("""\ Make the necessary changes to implement the requirement: {requirement}. 
                               If you need to implement updating or correcting libraries or dependencies, look for the latest stable version on the internet.
                               To complement your final answer, search on internet for similar solutions that match the requirement and the version of the project's libraries and dependencies."""),
            expected_output='Complete content of all modified files with the implemented feature.',
            agent=agent
        )
        return implement_changes_task

    def display_changes_task(self, agent):
        display_modified_files_task = Task(
            description="Display the entire content of all modified files.",
            expected_output='Complete content of all modified files.',
            agent=agent
        )
        return display_modified_files_task
