import pandas as pd

from app.utils import get_questions_df
from inputs import question_file, unanswered_question_file

q_and_as_df = get_questions_df(question_file, unanswered_question_file)
