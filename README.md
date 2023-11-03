# A web-based application based on Python, SQL, and AI: KAI I  research experience web
#### Video Demo:  <https://youtu.be/7sQbvPlj-Yw>
#### Description:

> [!NOTE]
> Additional Module Requirement in Python
* BeautifulSoup
* selenium
* sentence_transformers
* sklearn
* flask
* cs50

> [!NOTE]
> Main coding languages are used
* Python
* SQLite
* HTML

#### Motivation
I want to create a website that introduces my experience and allows users to query for some difficult professional glossaries.

#### Web Structure
> HTML files (in templates folder)
1. index.html:
   * Home page for the web, which can link to the other four html files.
   * The home page introduces the main topics and tools of my research, which are shown as text or table.
2. CloudSeeding.html:
   * The research results are shown on this web.
   * With the abstract and figure.
3. TerrainPrecipitation.html:
   * The research results are shown on this web.
   * With the abstract and figure
4. AI_Application.html:
   * The research results are shown on this web.
   * With the abstract and figure
5. apology.html:
   * When the user's input is empty, return to this web.
6. Glossary_Query.html:
   * Let users input the question.
7. Glossary_Query_answer.html:
   * Let users get the answer returned by SQL and AI.
8. layout.html:
   * The layout for all the HTML.
9. CSS file and JS file (in static folder)
   * To make the website more beautiful and have more interaction with users. 

> Python files
1. Web_Crawl.py:
   * BeautifulSoup and selenium are used to crawl data on the AMS glossary web.
   * Insert about 500 glossaries and answers into SQL.
2. query_vectorize.py:
   * Vectorize the questions in SQL by sentence_transformers module.
   * Input the vector string to the SQL corresponding to the question.
3. Sentence_Similarity.py:
   * Vectorize the input question (asked by users).
   * A function that compares the input question vector to all the vectors in the SQL.
4. app.py:
   * flask is used to combine Python with HTML files.
   * call Sentence_Similarity.Answer_AI() to get the response of AI.
   * find out the syntax LIKE in the SQL database to get the response of SQL.

> SQLite
1. Atmosphere_glossary.db:
   * Including Q_A and sentence_vector table
   * Inserted questions, answers, and the vector of questions.


#### Overall
The most difficult part of this project is the glossary_query part.
> In this part I went through
* To collect glossary data, beautiful Soup and Selenium are used for web crawl. (data from AMS glossary)
* After collecting about 500 pairs of questions and answers, I INSERT these data to the SQL table.
* To figure out the most similar question, that people ask, in my database, SQL and AI (Transformers) will be used.
* SQL finds out the syntax LIKE in the database.
* AI vectorize the database questions and people’s question and compare the similarity (cosine_similarity).
* Output the answer that is found by SQL and AI.

#### Why need AI affiliation
* Sometimes the different glossaries have the same meaning, e.g. radar reflectivity and radar echo.
* However, the database won’t include those different glossaries with the same definition.
* Thus, AI can help us solve this problem.

#### Future work
* Sometimes AI will be wrong. Maybe adding more data can improve its performance.

This is KAI I CS50 final project. Thank you!
