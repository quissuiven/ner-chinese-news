
import spacy

MODEL_PATH = "model/best-spancat-model"


class NamedEntityService(object):
    def __init__(self):
    	self.spancat_model = spacy.load(MODEL_PATH)

    def get_entities(self, text_input):
        """Given text input, apply model to return dictionary containing entity, entity type and confidence score."""

        doc = self.spancat_model(text_input)
        spans = doc.spans["sc"]
        return {"entities": [(span.text, span.label_, str(confidence)) for span, confidence in zip(spans, spans.attrs["scores"])]}


