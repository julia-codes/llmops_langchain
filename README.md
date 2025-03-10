# LLM Ops Project

## Overview
The **LLM Ops Project** provides a modular and scalable framework for managing large language models (LLMs) and their associated workflows. It integrates seamlessly with tools like LangChain, Pinecone, and Kubeflow, while leveraging best practices for infrastructure, monitoring, and CI/CD.

## Features
- **Prompt Engineering**: Predefined and dynamic prompt templates for LLM workflows.
- **LangChain Integration**: Customizable chains to manage LLM tasks.
- **Pinecone Vector Database**: Efficient storage and querying of embeddings.
- **Kubeflow Pipelines**: Automation and monitoring of machine learning workflows.
- **Monitoring and Observability**: Integration with LangSmith, AWS CloudWatch, and Prometheus.
- **Infrastructure as Code**: Terraform scripts for reproducible deployments.

---

## Project Structure
```plaintext
llm_ops_project/
├── README.md                           # Project documentation.
├── Dockerfile                          # Main Dockerfile for the project.
├── config/                             # Configuration files for various components.
│   ├── aws_secrets.yaml                # AWS secrets configuration.
│   ├── langchain_config.yaml           # LangChain configuration.
│   ├── logging_config.yaml             # Logging configuration.
│   └── model_config.yaml               # Model-specific parameters.
├── data/                               # Data directory.
│   ├── cache/                          # Cached intermediate files.
│   ├── embeddings/                     # Generated embeddings.
│   ├── outputs/                        # Final outputs.
│   └── prompts/                        # Prompt templates and examples.
├── examples/                           # Example scripts demonstrating functionality.
│   ├── kubeflow_pipeline.py            # Example of a Kubeflow pipeline.
│   ├── pinecone_index.py               # Pinecone setup and usage.
│   ├── simple_chain.py                 # Simple LangChain example.
│   └── step_function_handler_example.py # AWS Step Functions example.
├── infra/                              # Infrastructure-related scripts.
│   ├── docker/                         # Additional Docker configurations.
│   ├── kubeflow/                       # Kubeflow pipeline configurations.
│   ├── lambda/                         # AWS Lambda scripts.
│   └── terraform/                      # Terraform scripts for cloud infrastructure.
├── monitoring/                         # Monitoring and telemetry tools.
│   ├── aws_cloudwatch.py               # AWS CloudWatch integration.
│   ├── grafana_dashboards.json         # Grafana dashboard configurations.
│   ├── langsmith/                      # LangSmith monitoring tools.
│   ├── log_parser.py                   # Log parsing utilities.
│   └── prometheus_config.yaml          # Prometheus configuration.
├── notebooks/                          # Jupyter notebooks for prototyping.
│   ├── embeddings_analysis.ipynb       # Analysis and visualization of embeddings.
│   ├── langchain_testing.ipynb         # LangChain experimentation.
│   └── pipeline_experiments.ipynb      # Pipeline experiments.
├── requirements.txt                    # Python dependencies.
├── setup.py                            # Setup script for packaging.
├── src/                                # Core source code.
│   ├── base/                           # Base modules for integrations.
│   ├── handlers/                       # Error and Step Functions handlers.
│   ├── prompt_engineering/             # Prompt engineering utilities.
│   └── utils/                          # General utilities.
└── tests/                              # Unit and integration tests.
```

---

## Getting Started

### Prerequisites
- Python 3.8 or later
- Docker
- AWS CLI (configured)
- Terraform

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/llm_ops_project.git
   cd llm_ops_project
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables (e.g., AWS credentials).

### Run Examples
- Test LangChain workflows:
   ```bash
   python examples/simple_chain.py
   ```
- Create and query a Pinecone index:
   ```bash
   python examples/pinecone_index.py
   ```
- Run a Kubeflow pipeline:
   ```bash
   python examples/kubeflow_pipeline.py
   ```
- Test AWS Step Function integration:
   ```bash
   python examples/step_function_handler_example.py
   ```

---

## Development

### Directory Structure
- **`src/`**: Core modules for LLM integration, prompt engineering, and utilities.
- **`config/`**: YAML configuration files for models, logging, and AWS credentials.

### Testing
Run tests:
```bash
pytest tests/
```

---

## Infrastructure
- **Terraform**: Scripts for managing AWS infrastructure.
- **Docker**: Containerization for consistent environments.
- **Kubeflow**: Orchestration of machine learning workflows.

---

## Monitoring
- **LangSmith**: Observability for LangChain workflows.
- **AWS CloudWatch**: Log and metric monitoring.
- **Prometheus**: Metrics scraping and alerting.
- **Grafana**: Visualization for Prometheus metrics.

---

## Future Enhancements
- Add OpenTelemetry for distributed tracing.
- Enhance CI/CD workflows for deployment pipelines.

---

## Contributing
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/new_feature
   ```
3. Commit changes and open a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact
For questions or feedback, reach out to [David Stroud](mailto:david@davidstroud.me).

---

