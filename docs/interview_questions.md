# Interview Questions

1. What is MCP?

Model Context Protocol is a standardized protocol for exposing application context and capabilities to AI applications. An MCP server can expose tools, resources, and prompts.

2. Why use MCP here?

The resume analyzer functionality becomes discoverable and callable as structured tools by an MCP-compatible AI host.

3. How does skill extraction work?

A curated taxonomy maps canonical skill names to aliases. Text is normalized and known aliases are detected.

4. What is TF-IDF?

Term Frequency-Inverse Document Frequency represents term importance and is used here to vectorize resume and job-description text.

5. What is cosine similarity?

It measures the angle between vectors. Values closer to 1 indicate stronger directional similarity.

6. How is the score calculated?

This portfolio heuristic combines 70% job-skill coverage and 30% TF-IDF similarity. It is not a hiring decision.

7. How would you improve it?

Use embedding-based semantic matching, better entity/experience extraction, an evaluation dataset, authentication, background processing, persistence, observability, and production security controls.
