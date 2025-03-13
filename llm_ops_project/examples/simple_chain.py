# pip install -U langchain-openai

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
#from langchain.llms import OpenAI
# Changed because of error below
from langchain_community.llms import OpenAI
# /Users/julialayne/code/src/llmops_langchain/vllm/lib/python3.13/site-packages/langchain/llms/__init__.py:549: LangChainDeprecationWarning: Importing LLMs from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

# `from langchain_community.llms import OpenAI`.

# To install langchain-community run `pip install -U langchain-community`.
#   warnings.warn(
# /Users/julialayne/code/src/llmops_langchain/llm_ops_project/examples/simple_chain.py:16: LangChainDeprecationWarning: The class `OpenAI` was deprecated in LangChain 0.0.10 and will be removed in 1.0. An updated version of the class exists in the :class:`~langchain-openai package and should be used instead. To use it run `pip install -U :class:`~langchain-openai` and import as `from :class:`~langchain_openai import OpenAI``.
#   llm = OpenAI(model_name="davinci-002", api_key=OPEN_AI_KEY)

#Change2 because of Error below
from langchain_openai import OpenAI
# /Users/julialayne/code/src/llmops_langchain/llm_ops_project/examples/simple_chain.py:17: LangChainDeprecationWarning: The class `OpenAI` was deprecated in LangChain 0.0.10 and will be removed in 1.0. An updated version of the class exists in the :class:`~langchain-openai package and should be used instead. 
# #To use it run `pip install -U :class:`~langchain-openai` and import as `from :class:`~langchain_openai import OpenAI``.
#   llm = OpenAI(model_name="davinci-002", api_key=OPEN_AI_KEY)




import os
import sys

# Initialize LLM
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY", None)
# NOT RECOMMENDED: DONT ACCIDENTALLY UPLOAD YOUR OPEN AI KEY TO GIT
# OPEN_AI_KEY = "your-api-key"
if OPEN_AI_KEY is None:
    print("\r\n$OPEN_AI_KEY environment variable not set\r\n")
    sys.exit(1)

# Modified `model_name` to one found in currently available models
#openai.NotFoundError: Error code: 404 - {'error': {'message': 'The model `text-davinci-003` has been deprecated, 
# #learn more here: https://platform.openai.com/docs/deprecations', 'type': 'invalid_request_error', 'param': None, 
# 'code': 'model_not_found'}}
llm = OpenAI(model_name="davinci-002", api_key=OPEN_AI_KEY)




# Define a prompt template
prompt_template = PromptTemplate(
    input_variables=["topic"],
    template="Write a short essay about {topic}."
)

# Create a chain modified to updated runnable sequence library
# chain = LLMChain(llm=llm, prompt=prompt_template)
# /Users/julialayne/code/src/llmops_langchain/llm_ops_project/examples/simple_chain.py:26: LangChainDeprecationWarning: The class `LLMChain` was deprecated in LangChain 0.1.17 and will be removed in 1.0. Use :meth:`~RunnableSequence, e.g., `prompt | llm`` instead.
#   chain = LLMChain(llm=llm, prompt=prompt_template)
from langchain.schema.runnable import RunnableSequence


# Error of type
# TypeError: Expected a Runnable, callable or dict.Instead got an unsupported type: <class 'list'>
# chain = RunnableSequence([prompt_template, llm])
chain = prompt_template | llm

# Run the chain
# output = chain.run({"topic": "machine learning operations"})
# /Users/julialayne/code/src/llmops_langchain/llm_ops_project/examples/simple_chain.py:29: LangChainDeprecationWarning: 
# # The method `Chain.run` was deprecated in langchain 0.1.0 and will be removed in 1.0. Use :meth:`~invoke` instead.

output = chain.invoke({"topic": "machine learning operations"})
print(output)
