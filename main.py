from crewai import Crew
from agents import GameAgents
from tasks import ExistingCodeTasks, NewCodeTasks
from read_knowledge_base_tool import read_pdf_tool


def read_code(file_path):
    """FUNCTION TO READ A FILE"""
    with open(file_path, 'r+', encoding='utf-8') as file:
        content = file.read()
    return content


new_code_tasks = NewCodeTasks()
existing_code_tasks = ExistingCodeTasks()
agents = GameAgents()

print("## Bienvenidos al Asistente de Programacion##")
print('------------------------------------------')

while True:
    print("1. Nueva Implementacion")
    print("2. Agregar cambios o solucionar problemas en una implementacion existente")
    print("3. Salir")

    choice = input("Por favor, Ingrese una opción (1-3): ")

    if choice == '1':

        requirement = input(
            "Cuentanos. Que es lo que deseas implementar o crear?\n")
        # Create Agents
        senior_engineer_agent = agents.senior_engineer_agent()
        technical_leader_agent = agents.technical_leader_agent()
        # Create Tasks
        project_structure = new_code_tasks.set_init_project_structure(
            senior_engineer_agent)
        create_code = new_code_tasks.implement_code_task(senior_engineer_agent)
        # create_readme = new_code_tasks.create_readme_file(
        #    senior_engineer_agent)
        # Create Crew responsible for New Project
        crew = Crew(
            agents=[senior_engineer_agent, technical_leader_agent],
            tasks=[
                project_structure,
                create_code
            ],
            verbose=True
        )
        result = crew.kickoff(inputs={
            'requirement': requirement,
            'coding_standards': 'code-standards.pdf'
        })

        # Print results
        print("\n\n########################")
        print("## Here is the result")
        print("########################\n")
        print("Type of result:", type(result))
        print("final result:")
        print(result)

    elif choice == '2':
        print("Implementacion existente")
        code_path = input(
            "Ingrese la ruta donde se encuentra el proyecto para analizar:")
        requirement = input(
            "Cuentanos. Cuales son los cambios o problemas que deseas realizar?\n")
        # Create Agents
        senior_engineer_agent = agents.senior_engineer_agent()
        technical_leader_agent = agents.technical_leader_agent()
        # Create Tasks
        readme_task = existing_code_tasks.get_project_context(
            senior_engineer_agent)
        analyze_files_task = existing_code_tasks.get_files_to_change_task(
            senior_engineer_agent)
        implement_changes_task = existing_code_tasks.implement_update_code_task(
            senior_engineer_agent)

        # Create Crew responsible for Existing Project
        crew = Crew(
            agents=[senior_engineer_agent, technical_leader_agent],
            tasks=[
                readme_task,
                analyze_files_task,
                implement_changes_task
            ],
            verbose=True
        )
        result = crew.kickoff(inputs={
            'requirement': requirement,
            'coding_standards': 'code-standards.pdf',
            'project_path': code_path
        })

        # Print results
        print("\n\n########################")
        print("## Here is the result")
        print("########################\n")
        print("final code:")
        print(result)

    elif choice == '3':
        print("Gracias por su preferencia. !!Hasta Pronto!!")
        break

    else:
        print("Opción inválida. Por favor, Ingrese una opción del 1 al 3.")


# code = read_code('code-summary.txt')
# text_knowledge_base = fetch_pdf_content(
#    'NRM-STI-601 Estándar de programación para el desarrollo de software con tecnología Java v1.2.pdf')


# display_modified_files_task = tasks.display_changes_task(
#    technical_leader_agent)

# load_project_task = tasks.load_project_task(senior_engineer_agent)
# implement_update_code_task = tasks.implement_update_code_task(
#    senior_engineer_agent)
# review_compliance_task = tasks.review_compliance_task(technical_leader_agent)
# deliver_solution_task = tasks.deliver_solution_task(technical_leader_agent)


# code_solution = tasks.code_task(senior_engineer_agent, game)
# review_solution = tasks.review_task(qa_engineer_agent, game)
# correct_solution = tasks.code_correct_task(senior_engineer_agent, game)
# approve_solution = tasks.evaluate_task(
#    technical_leader_agent, game)


# crew = Crew(
#    agents=[
#        senior_engineer_agent,
#        # qa_engineer_agent,
#        technical_leader_agent
#    ],
#    tasks=[
#        load_project_task,
#        # review_solution,
#        # correct_solution,
#        implement_update_code_task
#    ],
#    verbose=True
# )


# game = crew.kickoff(
#    inputs={'github_repo': 'HenryVB/Test-CrewAI'})
