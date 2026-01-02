import re
from spellchecker import SpellChecker

class QueryPreprocessor:
    def __init__(self):
        self.spell = SpellChecker()
        self.block_patterns = [
            r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",
            r"\b(password|login|admin|root|secret)\b",
            r"\.(exe|bat|sh|bin)$"
        ]

    def correct_spelling(self, query):
        words = query.split()
        corrected = []
        for word in words:
            corr = self.spell.correction(word)
            corrected.append(corr if corr else word)
        return " ".join(corrected)

    def is_safe(self, query):
        query_lower = query.lower()
        for pattern in self.block_patterns:
            if re.search(pattern, query_lower):
                return False
        return True

    def clarify_intent(self, query):
        if len(query) < 2:
            return "Query too short."
        if not self.is_safe(query):
            return "Query blocked for safety."
        return None

    def process(self, query):
        clarification = self.clarify_intent(query)
        if clarification:
            return None, clarification
        final_query = self.correct_spelling(query)
        return final_query, None