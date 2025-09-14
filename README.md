# BitChord

A Python framework for building and running complex workflows involving Large Language Models (LLMs), tools, and conditional logic.

## Installation

To install the library locally, clone the repository and run:

```bash
pip install .
```

**Dependencies:** Ensure you have Python 3.8+ installed. Specific LLM providers (e.g., Groq) may require additional client libraries, which will be installed with `pip install .`

## Features

BitChord is designed to facilitate the creation of sophisticated AI applications by providing:

*   **Flexible Workflow Definition:** Easily define complex sequences of operations involving LLMs, tools, and custom logic.
*   **LLM Integration:** Seamlessly integrate with various Large Language Models (LLMs) like Groq.
*   **Tool Utilization:** Incorporate external tools and APIs into your workflows to extend capabilities.
*   **Conditional Logic:** Implement dynamic decision-making within your workflows based on LLM outputs or other conditions.
*   **Modular Design:** Build reusable components for scalable and maintainable AI solutions.

## Usage

BitChord allows you to define and execute complex workflows involving Large Language Models (LLMs), external tools, and conditional logic. Here's a simple example demonstrating how to use an LLM to respond to a prompt:

```python
from bitchord.llms import LLM
from bitchord.workflow import Workflow

# Initialize your LLM (e.g., Groq)
# Ensure GROQ_API_KEY is set in your environment variables
llm = LLM(model_name="llama3-8b-8192")

# Define a simple workflow
def simple_llm_workflow(input_text: str):
    response = llm.generate(prompt=f"Respond to the following: {input_text}")
    return response.text

# Create a workflow instance
workflow = Workflow(simple_llm_workflow)

# Run the workflow
if __name__ == "__main__":
    user_input = "Hello, how are you today?"
    result = workflow.run(input_text=user_input)
    print(f"LLM Response: {result}")
```

This example demonstrates a basic workflow where an input string is passed to an LLM, and the LLM's response is returned. You can build much more complex graphs by chaining LLMs, tools, and custom functions together.

### Defining More Complex Workflows

BitChord's true power lies in its ability to chain multiple operations. While the above example is simple, you can extend it by:

*   **Chaining LLM calls:** Pass the output of one LLM as input to another.
*   **Integrating Tools:** Define functions that interact with external APIs or perform specific tasks, and include them in your workflow.
*   **Adding Conditional Branches:** Use the output of an LLM or a tool to determine the next step in your workflow.

(Further examples for complex workflows can be added here as the project evolves.)

## Configuration

To use the Groq LLM, you need to provide a Groq API key. You can do this by setting the `GROQ_API_KEY` environment variable:

```bash
export GROQ_API_KEY="your-groq-api-key"
```

## Note on Github Push Protection

This repository has Github Push Protection enabled. If you are contributing to this project, you might encounter a push rejection due to secrets being detected in your commits. To resolve this, you can either remove the secret from your commit history or, if you are sure that the secret is a false positive, you can allow the secret to be pushed by visiting the URL provided in the error message.

## Contributing

We welcome contributions to BitChord! If you'd like to contribute, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your features or bug fixes.
3.  Make your changes and ensure they adhere to the project's coding standards.
4.  Write appropriate tests for your changes.
5.  Submit a pull request.

For more details, please refer to our `CONTRIBUTING.md` (if available).
