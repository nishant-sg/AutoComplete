# Use a pipeline as a high-level helper
from transformers import pipeline
import time

access_token='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'

pipe = pipeline("text-generation", model="gpt2-large", max_new_tokens = 5,token=access_token)


start = time.time()
print(pipe("hi, I am writing this email regarding the"))
print(time.time()-start)