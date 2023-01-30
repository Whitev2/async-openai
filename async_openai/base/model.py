from typing import List


class Model:
    def __init__(
            self,
            model: str = 'text-davinci-003',
            prompt: str = None,
            temperature: float = None,
            max_tokens: int = None,
            top_p: float = None,
            frequency_penalty: float = None,
            presence_penalty: float = None,
            stop: List = None
    ):

        self.model: str = model
        self.prompt: str = prompt
        self.temperature: float = temperature
        self.max_tokens: int = max_tokens
        self.top_p: float = top_p
        self.frequency_penalty: float = frequency_penalty
        self.presence_penalty: float = presence_penalty
        self.stop: List = stop

    def qa(self):
        self.model = "text-davinci-003"
        self.temperature = 0
        self.max_tokens = 100
        self.top_p = 1
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        self.stop = ["\n"]
        return self

    def grammar_correction(self):
        self.model = "text-davinci-003"
        self.temperature = 0
        self.max_tokens = 60
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0

    def summarize_for_a_2nd_grader(self):
        self.model = "text-davinci-003"
        self.temperature = 0.7
        self.max_tokens = 64
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0

    def natural_language_to_openai(self):
        self.model = "code-davinci-002"
        self.temperature = 0
        self.max_tokens = 64
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        self.stop = ["\"\"\""]

    def text_to_command(self):
        self.model = "text-davinci-003"
        self.temperature = 0
        self.max_tokens = 100
        self.top_p = 1.0
        self.frequency_penalty = 0.2
        self.presence_penalty = 0.0
        self.stop = ["\n"]
        return self

    def english_to_other_languages(self):
        self.model = "text-davinci-003"
        self.temperature = 0.3
        self.max_tokens = 100
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        return self

    def natural_language_to_stripe_api(self):
        self.model = "code-davinci-002"
        self.temperature = 0
        self.max_tokens = 100
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        self.stop = ["\"\"\""]
        return self

    def sql_translate(self):
        self.model = "code-davinci-002"
        self.temperature = 0
        self.max_tokens = 150
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        self.stop = ["#", ";"]
        return self

    def parse_unstructured_data(self):
        self.model = "text-davinci-003"
        self.temperature = 0
        self.max_tokens = 100
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        return self

    def classification(self):
        self.model = "text-davinci-003"
        self.temperature = 0
        self.max_tokens = 64
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        return self

    def python_to_natural_language(self):
        self.model = "code-davinci-002"
        self.temperature = 0
        self.max_tokens = 64
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        return self

    def movie_to_emoji(self):
        self.model = "text-davinci-003"
        self.temperature = 0.8
        self.max_tokens = 60
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        self.stop = ["\n"]
        return self

    def calculate_time_complexity(self):
        self.model = "text-davinci-003"
        self.temperature = 0
        self.max_tokens = 64
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        self.stop = ["\n"]
        return self

    def translate_programming_languages(self):
        self.model = "code-davinci-002"
        self.temperature = 0
        self.max_tokens = 54
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        self.stop = ["###"]
        return self

    def advanced_tweet_classifier(self):
        self.model = "text-davinci-003"
        self.temperature = 0
        self.max_tokens = 60
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        return self

    def explain_code(self):
        self.model = "code-davinci-002"
        self.temperature = 0
        self.max_tokens = 64
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        self.stop = ["\"\"\""]
        return self

    def keywords(self):
        self.model = "text-davinci-003"
        self.temperature = 0.5
        self.max_tokens = 60
        self.top_p = 1.0
        self.frequency_penalty = 0.8
        self.presence_penalty = 0.0
        return self

    def factual_answering(self):
        self.model = "text-davinci-003"
        self.temperature = 0
        self.max_tokens = 60
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        return self

    def ad_from_product_description(self):
        self.model = "text-davinci-003"
        self.temperature = 0.5
        self.max_tokens = 100
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        return self

    def product_name_generator(self):
        self.model = "text-davinci-003"
        self.temperature = 0.8
        self.max_tokens = 60
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        return self

    def tl_dr_summarization(self):
        self.model = "text-davinci-003"
        self.temperature = 0.7
        self.max_tokens = 60
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 1
        return self

    def python_bug_fixer(self):
        self.model = "code-davinci-002"
        self.temperature = 0
        self.max_tokens = 182
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        self.stop = ["###"]
        return self

    def spreadsheet_creator(self):
        self.model = "text-davinci-003"
        self.temperature = 0.5
        self.max_tokens = 60
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        return self

    def javascript_helper_chatbot(self):
        self.model = "code-davinci-002"
        self.temperature = 0
        self.max_tokens = 60
        self.top_p = 1.0
        self.frequency_penalty = 0.5
        self.presence_penalty = 0.0
        self.stop = ["You:"]
        return self

    def ml_al_language_model_tutor(self):
        self.model = "text-davinci-003"
        self.temperature = 0.3
        self.max_tokens = 60
        self.top_p = 1.0
        self.frequency_penalty = 0.5
        self.presence_penalty = 0.0
        self.stop = ["You:"]
        return self

    def science_fiction_book_list_maker(self):
        self.model = "text-davinci-003"
        self.temperature = 0.5
        self.max_tokens = 200
        self.top_p = 1.0
        self.frequency_penalty = 0.52
        self.presence_penalty = 0.5
        self.stop = ["11."]
        return self

    def tweet_classifier(self):
        self.model = "text-davinci-003"
        self.temperature = 0
        self.max_tokens = 60
        self.top_p = 1.0
        self.frequency_penalty = 0.5
        self.presence_penalty = 0.0
        return self

    def airport_code_extractor(self):
        self.model = "text-davinci-003"
        self.temperature = 0
        self.max_tokens = 60
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        self.stop = ["\n"]
        return self

    def sql_request(self):
        self.model = "text-davinci-003"
        self.temperature = 0.3
        self.max_tokens = 60
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        return self

    def extract_contact_information(self):
        self.model = "text-davinci-003"
        self.temperature = 0
        self.max_tokens = 64
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        return self

    def javascript_to_python(self):
        self.model = "code-davinci-002"
        self.temperature = 0
        self.max_tokens = 64
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        return self

    def friend_chat(self):
        self.model = "text-davinci-003"
        self.temperature = 0.5
        self.max_tokens = 60
        self.top_p = 1.0
        self.frequency_penalty = 0.5
        self.presence_penalty = 0.0
        self.stop = ["You:"]
        return self

    def mood_to_color(self):
        self.model = "text-davinci-003"
        self.temperature = 0
        self.max_tokens = 64
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        self.stop = [";"]
        return self

    def write_a_python_docstring(self):
        self.model = "code-davinci-002"
        self.temperature = 0
        self.max_tokens = 150
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        self.stop = ["#", "\"\"\""]
        return self

    def analogy_maker(self):
        self.model = "text-davinci-003"
        self.temperature = 0.5
        self.max_tokens = 60
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        return self

    def javascript_one_line_function(self):
        self.model = "code-davinci-002"
        self.temperature = 0
        self.max_tokens = 60
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        self.stop = [";"]
        return self

    def micro_horror_story_creator(self):
        self.model = "text-davinci-003"
        self.temperature = 0.8
        self.max_tokens = 60
        self.top_p = 1.0
        self.frequency_penalty = 0.5
        self.presence_penalty = 0.0
        return self

    def third_person_converter(self):
        self.model = "text-davinci-003"
        self.temperature = 0
        self.max_tokens = 60
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        return self

    def notes_to_summary(self):
        self.model = "text-davinci-003"
        self.temperature = 0
        self.max_tokens = 64
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        return self

    def vr_fitness_idea_generator(self):
        self.model = "text-davinci-003"
        self.temperature = 0.6
        self.max_tokens = 150
        self.top_p = 1.0
        self.frequency_penalty = 1
        self.presence_penalty = 1
        return self

    def essay_outline(self):
        self.model = "text-davinci-003"
        self.temperature = 0.3
        self.max_tokens = 150
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        return self

    def recipe_creator(self):
        self.model = "text-davinci-003"
        self.temperature = 0.3
        self.max_tokens = 120
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        return self

    def chat(self):
        self.model = "text-davinci-003"
        self.temperature = 0.9
        self.max_tokens = 150
        self.top_p = 1
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.6
        self.stop = [" Human:", " AI:"]
        return self

    def marv_the_sarcastic_chat_bot(self):
        self.model = "text-davinci-003"
        self.temperature = 0.5
        self.max_tokens = 60
        self.top_p = 0.3
        self.frequency_penalty = 0.5
        self.presence_penalty = 0.0
        return self

    def turn_by_turn_directions(self):
        self.model = "text-davinci-003"
        self.temperature = 0.3
        self.max_tokens = 64
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        return self

    def restaurant_review_creator(self):
        self.model = "text-davinci-003"
        self.temperature = 0.5
        self.max_tokens = 64
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        return self

    def create_study_notes(self):
        self.model = "text-davinci-003"
        self.temperature = 0.3
        self.max_tokens = 150
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        return self

    def interview_questions(self):
        self.model = "text-davinci-003"
        self.temperature = 0.5
        self.max_tokens = 150
        self.top_p = 1.0
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        return self
