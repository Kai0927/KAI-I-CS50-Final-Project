# A web-based application based on Python, SQL and AI: KAI I  research experience web
#### Video Demo:  <https://youtu.be/7sQbvPlj-Yw>
#### Description:

> [!NOTE]
> Additional Module Requirment in python
*BeautifulSoup
*selenium
*sentence_transformers
*sklearn

> [!NOTE]
> Main coding languages are used
*Python
*SQLite
*HTML

#### Motivation
I would like to create a website that introduces my experience and also make users able to query for some difficult professional glossaries.

#### Web Structure
> HTML files (in templates folder)
1. index.html
    _ Home page for the web, which can link to the other four .html files.
    _ In the home page, it introduces the main topics and tools of my researches, which is shown as text or table.
2. CloudSeeding.html
    _ Show the research results in this web.
    _ With the abstract and figure.
3. TerrainPrecipitation.html
    _ Show the research results in this web.
    _ With the abstract and figure.
4. AI_Application.html
    _ Show the research results in this web.
    _ With the abstract and figure.
5. apology.html
    _ When the user's input is empty, return to this web.
6. Glossary_Query.html
    _  let users input the question.
7. Glossary_Query_answer.html
    _  let users get the answer return by SQL and AI.
8. layout.html
    _ the layout for all the html.
9. CSS file and JS file (in static folder)
    _ to make the website beautiful and have more interation with users. 

> Python files
1. Web_Crawl.py
    _ BeautifulSoup and selenium are used to crawl data on AMS glossary web.
    _ Insert about 500 glossaries and answers into SQL.
2. query_vectorize.py
    _ vectorize the questions in SQL by sentence_transformers module.
    _ input the vector string to the SQL corresponding to question.
3. Sentence_Similarity.py
    _ vectorize the input question (ask by users).
    _ A function that compare the input question vector to all of the vector in the SQL.
4. app.py
    _ flask is used to combine python with HTML files.
    _ call Sentence_Similarity.Answer_AI() to get the respnse of AI.
    _ find out the syntax LIKE in the SQL database to get the response of SQL.

> SQLite
1. Atmosphere_glossary.db
    _ including Q_A and sentence_vector table
    _ inserted questions, answers and the vector of qestions.


#### Overall
The most difficault part in this project is the glossary_query part.
> in this part I went through
*To collect glossary data, beautiful Soup and selenium are used for web crawl. (data from: AMS glossary)
*After collecting about 500 pairs of questions and answers, I INSERT these data to the SQL table.
*To figure out the most similar question, that people ask, in my database, SQL and AI (Transformers) will be used.
*SQL just find out the syntax LIKE in the database.
*AI vectorize the database questions and people’s question and compare the similarity (cosine_similarity).
*Output the answer that is found by SQL and AI.

#### Why need AI affiliation
*Sometimes the different glossaries have the same meaning, e.g. radar reflectivity and radar echo.
*However, the database won’t include those different glossary with the same definition.
*Thus, AI can help us solve this problem.

#### Future work
*Sometimes AI will wrong. Maybe adding more data can improve its’ performance.

#### This is KAI I CS50 final project. Thank you!