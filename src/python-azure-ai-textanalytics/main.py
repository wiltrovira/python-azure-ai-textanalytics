from dotenv import load_dotenv
import os
from pathlib import Path

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


def main():
    global cog_endpoint
    global cog_key

    try:
        # Obtiene configuraciones del archivo .env
        ENV_PATH = Path(__file__).resolve().parent / ".env"
        load_dotenv(dotenv_path=ENV_PATH)

        cog_endpoint = os.getenv("COG_SERVICE_ENDPOINT")
        cog_key = os.getenv("COG_SERVICE_KEY")

        # Get user input (until they enter "quit")
        userText = ""
        while userText.lower() != "salir":
            userText = input(
                '\nEscribe un texto ("salir" para detener la ejecución del programa:)\n'
            )
            if userText.lower() != "salir":
                language = GetLanguage(userText)
                print("Idioma:", language)

    except Exception as ex:
        print(ex)


def GetLanguage(text):

    # Create client using endpoint and key
    credential = AzureKeyCredential(cog_key)
    client = TextAnalyticsClient(endpoint=cog_endpoint, credential=credential)

    # Call the service to get the detected language
    detectedLanguage = client.detect_language(documents=[text])[0]
    return detectedLanguage.primary_language.name


if __name__ == "__main__":
    main()
