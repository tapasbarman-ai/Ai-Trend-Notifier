from langgraph.graph import StateGraph, END
from typing import TypedDict, List

from src.langgraph.nodes.ingestion_node import ingestion_node
from src.langgraph.nodes.sentiment_node import sentiment_node
from src.langgraph.nodes.enrichment_node import enrichment_node
from src.langgraph.nodes.summarizer_node import summarizer_node
from src.langgraph.nodes.notifier_node import notifier_node


class AgentState(TypedDict):
    trends: List[dict]


def create_workflow():
    workflow = StateGraph(AgentState)

    workflow.add_node("ingest", ingestion_node)
    workflow.add_node("sentiment", sentiment_node)
    workflow.add_node("enrich", enrichment_node)
    workflow.add_node("summarize", summarizer_node)
    workflow.add_node("notify", notifier_node)

    workflow.set_entry_point("ingest")
    workflow.add_edge("ingest", "sentiment")
    workflow.add_edge("sentiment", "enrich")
    workflow.add_edge("enrich", "summarize")
    workflow.add_edge("summarize", "notify")
    workflow.add_edge("notify", END)

    return workflow.compile()


def run_pipeline():
    app = create_workflow()
    result = app.invoke({"trends": []})
    return result