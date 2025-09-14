from dotenv import load_dotenv
import os
from langchain_core.messages import BaseMessage,SystemMessage,HumanMessage,ToolMessage
from langgraph.graph import StateGraph ,END
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from typing import TypedDict,Annotated,Sequence
from operator import add as add_messages
from langchain_text_splitters import RecursiveCharacterTextSplitter
from q