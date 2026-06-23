from backend.agents.graph_agent import graph


try:

    png_bytes = graph.get_graph().draw_mermaid_png()

    with open("docs/agent_graph.png", "wb") as f:
        f.write(png_bytes)

    print("Graph saved to docs/agent_graph.png")


except Exception as e:

    print("Mermaid PNG export failed")

    print(e)


    mermaid = graph.get_graph().draw_mermaid()

    print("\nMERMAID DIAGRAM\n")

    print(mermaid)