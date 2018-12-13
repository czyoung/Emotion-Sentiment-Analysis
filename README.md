# Emotion-Sentiment-Analysis
This was developed as a short project to demonstrate automatic detection of emotion based on text.

This project uses Tone Analyzer by Watson (version 2016-05-19).  Details may be found here:
https://gateway.watsonplatform.net/tone-analyzer

This project uses Emofani by steffenwittig.  Source for download and details may be found here:
https://github.com/steffenwittig/emofani

This project was developed using Python 3.6.  Python can be downloaded either as a package (such as through the Anaconda environment) or at the link here:
https://www.python.org/downloads/

For use of Tone Analyzer, an account must be made with access to Tone Analyzer.  The username and password for API purposes is used in toneAnalyzer.py.

Additional features were added to Emofani to create a textual display of results/responses using the variable "message".

The assumption made in this project is that the python code and emofani are both running on the same device using port 11000.  This can be changed in the sendMessage() function of manager.py.
