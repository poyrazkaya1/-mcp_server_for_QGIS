# AI-Driven Attribute Analysis Plugin for QGIS

A QGIS plugin designed to streamline GIS data management and attribute analysis by integrating local Large Language Models (LLMs) via the Model Context Protocol (MCP).

## Overview
This project bridges the gap between traditional Geographic Information Systems and modern AI capabilities. As a City and Regional Planning student, I developed this tool to automate repetitive attribute analysis tasks, allowing planners and GIS professionals to focus on insights rather than manual data processing. 

Built with **PyQGIS** and powered by local LLMs, this plugin ensures privacy and efficiency by processing data locally, without the need for external API dependencies. (Cloud-based model support is planned for future versions to offer greater flexibility.)

## Key Features
* **Local LLM Integration:** Leverages local models (e.g., Qwen, Gemma) to perform intelligent analysis on attribute tables.
* **PyQGIS & MCP Implementation:** Utilizes the Model Context Protocol (MCP) to create an agentic workflow between the LLM and the QGIS environment.
* **Automated Data Insights:** Simplifies attribute table cleaning, summarization, and intelligent querying.
* **Privacy-First:** Since it runs locally, your sensitive GIS data never leaves your machine.
* **Linux Native:** Developed and optimized for Linux environments (Arch/Debian/Ubuntu).

## Tech Stack
* **Language:** Python
* **Frameworks:** PyQGIS (QGIS Python API)
* **AI/LLM:** Local LLM engines (Ollama, LM Studio)
* **Architecture:** Model Context Protocol (MCP)

## Current Status
This project is currently under active development. I am working on refining the agentic workflows and improving the reliability of the attribute analysis outputs. Contributions, feedback, and testing from the community are highly encouraged.

## Why Open Source?
I have been a part of the open-source community since my first days with Linux. This plugin is my contribution to the GIS ecosystem that has shaped my academic and professional journey. My goal is to build tools that empower urban planners and GIS users worldwide.

## Installation
*(Note: Installation instructions will be added as the project stabilizes.)*
1. Clone this repository to your QGIS plugins folder.
2. Ensure you have a local LLM server running (e.g., Ollama).
3. Configure the plugin settings with your model endpoint.

## Roadmap / To-Do List

I am actively working on improving the plugin. Here is the current development roadmap:

- [ ] **AI Gateway:** Add support for cloud-based AI models and implement a secure and intiutive UI for API key management and local mcp server setup.
- [ ] **Model Designer Integration:** Add support for `.model3` files to leverage existing workflows created in QGIS Model Designer.
- [ ] **Implement Multithreading:** Integrate `QgsTask` to execute LLM operations in the background, ensuring the QGIS interface remains responsive during heavy processing.
- [ ] **Integrated Chatbot Interface:** Develop a native, intuitive chatbot UI within the plugin for streamlined Model Context Protocol (MCP) integration. Currently, interactions require external interfaces (e.g., LM Studio/Ollama), and this feature aims to bring that experience directly into the QGIS environment.
- [ ] **Error Handling:** Implement robust validation for empty attribute tables and malformed geometry data.
- [ ] **Expanded PyQGIS Toolset:** Develop additional tools to broaden AI model capabilities within the QGIS environment.
- [ ] **QField Integration:** Explore workflows to bridge AI analysis results with QField projects.
- [ ] **Documentation:** Create a comprehensive Wiki and user guide.

*Contributions are welcome! If you'd like to tackle one of these tasks, please feel free to open a pull request.*

## Contact & Collaboration
I am passionate about Open Source, QGIS, and QField. I am actively looking to connect with like-minded developers and organizations interested in the intersection of AI and GIS.

* **Email:** poyraz@poyrazkaya.com
