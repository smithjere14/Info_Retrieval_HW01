README
AUTHOR: Jeremiah D Smith

HOW TO SETUP AND RUN TOKENIZER.PY:
* Used Python 3.8.1 Might be ok with lesser Python 3.x version
01. Create a virtual environment and activate it
        Follow the directions in the link if you need help creating and activating a virtual environment
        https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
02. Install Git
03. Issue the following command at your terminal in your virtual environment
        git clone https://github.com/smithjere14/Info_Retrieval_HW01.git
04. After the repository is installed issue the following command to install any necessary libraries
        pip install -r requirements.txt
05. Type tokenizer.py and hit Enter (You'll have to wait a minute or two depending on your computer but it works)

QUESTIONS:
1. What is the total number of words in the collection?
        582710
2. What is the vocabulary size? (i.e., number of unique terms).
        including stopwords 10812
        filter out stopwords 10491
3. What are the top 20 words in the ranking? (i.e., the words with the highest frequencies).
        stopwords included      stopwords filtered
        the 25734               system 3771
        of 18722                agent 3259
        and 14210               base 2765
        a 13445                 data 2764
        to 11654                inform 2438
        in 10114                model 2356
        for 7387                paper 2251
        is 6583                 queri 1944
        we 5153                 user 1884
        that 4824               learn 1826
        thi 4451                algorithm 1599
        on 3788                 problem 1578
        system 3771             web 1561
        use 3750                comput 1556
        are 3740                applic 1552
        an 3285                 approach 1547
        agent 3259              present 1508
        with 3205               databas 1442
        as 3078                 method 1225
        by 2792                 object 1220

4. From these top 20 words, which ones are stop-words?
        the
        of
        and
        a
        to
        in
        for
        is
        we
        that
        thi
        on
        use
        are
        an
        with
        as
        by
5. What is the minimum number of unique words accounting for 15% of the total number of words in the collection?
        stopwords included 6
        stopwords filtered 79



