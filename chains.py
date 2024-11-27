import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key = os.getenv("GROQ_API_KEY"), model="llama-3.1-70b-versatile")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
                ### SCRAPED TEXT FROM WEBSITE.
                (page_data)
                ### INSTRUCTION
                The scraped text is from a career's page of a website.
                Your job is to extract the job posting and return them in JSON format containing
                the following keys:- role , experience, skills and description
                Only return the valid JSON
                ### VALID JSON(NO PREAMBLE)
            """
        )
        chain_extract = prompt_extract | self.llm  # Byte operation
        res = chain_extract.invoke(input={'page_data': cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Content too big. Unable to parse jobs")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            (job_description)

            ### INSTRUCTION:
            You are Mohan, a business development executive at AtliQ,AtLiQ is an AI & Software Company.
            Over our experience, we have empowered numerous enterprises with tailores solutions
            processm optimization, cost reduction and heightened overall efficiency.
            Your job is to write a cold email to the client regarding the job mmentioned above in fulfilling
            their needs.
            Also add the most relevant ones from the following links to showcase AtliQ's portfolio: (link_list)
            Remember you are Mohan, BDE at AtliQ.
            DO not provide a preamble
            ### EMAIL (NO PREAMBLE):

            """
        )

        chain_email = prompt_email | self.llm
        res = chain_email.invoke(
            {"job_description": str(job), "link_list": links}) # Parameters within parenthesis, are to be supplied
        return res.content