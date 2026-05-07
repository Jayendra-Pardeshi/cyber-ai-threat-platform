from app.agents.collector_agent import collect_threats
from app.agents.retriever_agent import retrieval_agent
from app.agents.risk_agent import risk_analysis
from app.agents.report_agent import generate_report

def run_pipeline(query):

    threat = collect_threats(query)

    rag_context = retrieval_agent(threat)

    combined = threat + "\n" + rag_context

    risk = risk_analysis(combined)

    report = generate_report(risk)

    return {
        "threat": threat,
        "risk": risk,
        "report": report
    }