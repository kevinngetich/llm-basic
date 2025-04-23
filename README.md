# llm-basic
![image](https://github.com/user-attachments/assets/58e5bd07-00ba-4328-8616-6a646a216974)

Simple demonstration of LLM project implementation. App will ultimately provide for: front-end to make queries and view responses, backend to process query and integrate with LLM.

## Setup
1. Clone the project:
``` git clone https://github.com/kevinngetich/llm-basic.git ```
2. Add an ``` .env ``` file in the ``` api ``` folder and populate the following:
```
# Requred to use Open Router API
OPENROUTER_BASE_URL=
OPENROUTER_API_KEY=
OPENROUTER_MODEL=deepseek/deepseek-r1:free
```
3. Run this command from the project root, ```api``` directory :
```
fastapi dev main.py
```
4. Run this command from the ```ui``` directory:
```
pnpm dev
```
5. Navigate to ```http//127.0.0.1:3000``` on your browser.
