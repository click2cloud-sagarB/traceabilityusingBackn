# FAQ - Agripilot Traceability Module

### Q1: What is the Beckn Protocol?
**A:** An open standard for enabling interoperable and decentralized digital transactions. It allows diverse systems to communicate using a common language.

### Q2: How is traceability implemented here?
**A:** The module uses endpoints (`/api/update`, `/api/search`, and `/api/track`) following a Beckn-like structure to record and retrieve product journey updates.

### Q3: How do I run the project?
**A:** Follow the steps in the README:
1. Clone the repository.
2. Set up a virtual environment.
3. Install dependencies.
4. Configure your environment variables.
5. Run the Flask server and then the client simulation script.

### Q4: Where do I set actual credentials?
**A:** Update the `.env` file with your real credentials. The provided `.env.example` shows the required variables.

### Q5: Can this be integrated with other systems?
**A:** Yes. By adhering to a standardized protocol (similar to Beckn), this module can interoperate with various platforms and stakeholders.
