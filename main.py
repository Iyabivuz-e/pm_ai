from src.pm.crew import ProjectManagementCrew

def main():
    pm_crew = ProjectManagementCrew()
    print("Hey PM!!")    
    results = pm_crew.crew().kickoff(inputs={"topic": "Rejection analysis for a job application management platform"})
    
    print(results.raw)

if __name__ == "__main__":
    main()
