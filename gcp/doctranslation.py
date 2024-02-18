# Imports the Google Cloud Translation library
from google.cloud import translate

# Initialize Translation client
def translate_document(
    project_id: str = "YOUR_PROJECT_ID", source_lang: str = "", target_lang: str = ""
) -> translate.TranslationServiceClient:
    """Translating Document."""

    client = translate.TranslationServiceClient()

    location = "global"

    parent = f"projects/{project_id}/locations/{location}"

    gcs_source = translate.GcsSource()
    gcs_source.input_uri = "gs://doctranslate/sample.pdf"

    gcs_destination = translate.GcsDestination()
    gcs_destination.output_uri_prefix = "gs://doctranslate/fr-translated/"

    docinputconfig = translate.DocumentInputConfig()
    docinputconfig.content=b'content_blob'
    docinputconfig.gcs_source=gcs_source

    docoutputconfig = translate.DocumentOutputConfig()
    docoutputconfig.gcs_destination=gcs_destination

    # Translate text from English to French
    # Detail on supported types can be found here:
    # https://cloud.google.com/translate/docs/supported-formats
    response = client.translate_document(
        request={
            "parent": parent,
            #"contents": [text],
            #"mime_type": "application/pdf",  # mime types: text/plain, text/html
            "source_language_code": source_lang,
            "target_language_code": target_lang,
            "document_input_config": docinputconfig,
            "document_output_config": docoutputconfig,
        }
    )

    # Display the translation for each input text provided
    print(f"Translated text: {response.document_translation}")
        
    return response
