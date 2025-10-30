from langchain_core.prompts import PromptTemplate


# template
template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}
Explanation Length: {length_input}
1. Mathematical Details:
    - Include relevant equations and mathematical concepts if present in the paper.
    - Explain how these mathematical elements contribute to the overall findings.
2. Analogies:
    - Use relatable analogies to simplify complex concepts.
If certain information is not available in the paper, respond with "Information not available in the paper." insted of gussing.
Ensure the summary is clear, concise, and tailored to the specified style and length.
""",
input_variables=["paper_input", "style_input", "length_input"],
)

template.save("research_paper_summary_template.json")