# LangServe Example - Translator API

This is a simple example of LangServe. It serves a bunch of endpoints act as a smart translator agent.

## Get started

1. Installation

    ```shell
    pip install -r requirements.txt
    ```

2. Set up your OpenAI API key

    Create a `.env` file in the project root folder and add the following content:

    ```shell
    OPENAI_API_KEY=<your valid openai api key>
    ```

3. Launch the server

    ```shell
    python app.py
    ```

4. Visit the API docs

    [http://localhost:8888/docs](http://localhost:8888/docs)