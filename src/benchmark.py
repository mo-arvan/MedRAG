from src.medrag import MedRAG

question = "A lesion causing compression of the facial nerve at the stylomastoid foramen will cause ipsilateral"
options = {
    "A": "paralysis of the facial muscles.",
    "B": "paralysis of the facial muscles and loss of taste.",
    "C": "paralysis of the facial muscles, loss of taste and lacrimation.",
    "D": "paralysis of the facial muscles, loss of taste, lacrimation and decreased salivation."
}

medrag = MedRAG(llm_name="OpenAI/gpt-4o-mini-2024-07-18",
                rag=True,
                retriever_name="RRF-4",
                corpus_name="MedCorp",
                corpus_cache=True)
answer, snippets, scores = medrag.answer(question=question,
                                         options=options,
                                         k=32)  # scores are given by the retrieval system
print(f"Final answer in json with rationale: {answer}")
# {
#   "step_by_step_thinking": "A lesion causing compression of the facial nerve at the stylomastoid foramen will result in paralysis of the facial muscles. Loss of taste, lacrimation, and decreased salivation are not specifically mentioned in relation to a lesion at the stylomastoid foramen.",
#   "answer_choice": "A"
# }


