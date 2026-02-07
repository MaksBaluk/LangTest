from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import MessagesState

from app.llm.providers.open_router import model


def agent(state: MessagesState):
    reply = model.invoke(state["messages"])
    return {"messages": [reply]}


def router(state: MessagesState):
    last = state["messages"][-1].content
    if last.startswith("FINAL"):
        return END
    return "agent"


graph = StateGraph(MessagesState)
graph.add_node("agent", agent)
graph.add_edge(START, "agent")
graph.add_conditional_edges("agent", router)

app = graph.compile()
