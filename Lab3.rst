Welcome to CST 236 Lab 2
------------------------

Requirements for a Dream
************************

In these weeks lab you will be presented with a series of requirements in which you will
implement requirements based tests for. Prior to getting to that point we will nose2 plugins
(required in order to complete this lab).

.. note:: 

    Remember from lecture, no matter how correct the code might look, the requirement 
    is always the definitive answer. If you find bugs you do not need to worry about fixing
    them instead during the writup you will be asked to submit a "bug report"
    
The code which you will be testing is located in my CST236 repo (https://github.com/kimballj/cst236) 
on the Lab3_Code branch
    
Grading
*******

+---------------------------------------+---------+
| Proper testing of requirements        | 30 pts  |
+---------------------------------------+---------+
| Coding Style / Readability            | 10 pts  |
+---------------------------------------+---------+
| No excessive duplicated code between  | 10 pts  |
| tests                                 |         |
+---------------------------------------+---------+
| Analysis Questions                    | 30 pts  |
+---------------------------------------+---------+
| Correct execution of trace plugin     | 20 pts  |
+---------------------------------------+---------+
| **Total**                             | 100 pts |
+---------------------------------------+---------+

.. note::

    For this lab assignment it sphinx is not required. Also because there is a high probability that some of your
    tests will be failing at the end of this lab you are no required to submit a functioning drone I/O.


Nose2 Plugins
*************

This week during lecture we covered how to create a nose2 plugin. Using this information and the link provided
below you will need to create your own traceability plugin

For more information about writing nose2 plugins please see
http://nose2.readthedocs.org/en/latest/dev/writing_plugins.html

Traceability
************

Remember what was covered in lecture this week. DO IT. You will find that each of the requirements
in this lab is uniquely identified. I highly recommend if you want to complete this lab correctly
that you tag each of these unique ids in the test case(s) which cover the requirement using ReqTracer.

.. note:: 

    Remember to check coverage to ensure you covered the requirements. If the requirements do no fully
    cover the requirements then you will add a bug report during the writeup.


Testing Requirements
********************

Only the numbered rows below are requirements. The rest is just context

**Acceptable Answers**

#0001 The system shall accept questions in the form of strings and attempt to answer them

#0002 The system shall answer questions that begin with one of the following valid question keywords: "How", "What", "Where", "Why" and "Who"

#0003 If the system does not detect a valid question keyword it shall return "Was that a question?"

#0004 If the system does not detect a question mark at end of the string it shall return "Was that a question?"

A question mark is defined as ascii value 0x3E

**Determining Answers**

#0005 The system shall break a question down into words separated by space

#0006 The system shall determine an answer to a question as a correct if the keywords provide a 90% match and return the answer

#0007 The system shall exclude any number value from match code and provide the values to generator function (if one exists)

#0008 When a valid match is determined the system shall return the answer

#0009 When no valid match is determined the system shall return "I don't know, please provide the answer"

**Providing Answers**

#0010 The system shall provide a means of providing an answer to the previously asked question.

#0011 The system shall accept and store answers to previous questions in the form of a string or a function pointer and store it as the generator function.

#0012 If no previous question has been asked the system shall respond with "Please ask a question first"

#0013 If an attempt is made to provide an answer to an already answered question the system shall respond with "I don\'t know about that. I was taught differently" and not update the question

**Correcting Answers**

#0014 The system shall provide a means of updating an answer to the previously asked question.

#0015 The system shall accept and store answers to previous questions in the form of a string or a function pointer and store it as the generator function.

#0016 If no previous question has been asked the system shall respond with "Please ask a question first"

**Initial Answers Provided**

#0017 The system shall respond to the question "What is <float> feet in miles" with the the float value divided by 5280 and append "miles" to the end of  the return.

#0018 The system shall respond to the question "How many seconds since <date time>" with the number of seconds from that point of day till now.

#0019 The system shall respond to the question "Who invented Python" with "Guido Rossum(BFDL)"

#0020 The system shall respond to the question "Why don't you understand me" with "Because you do not speak 1s and 0s"

#0021 The system shall respond to the question "Why don't you shutdown" with "I'm afraid I can't do that <username>"

Username shall be determined by the name of the currently logged in user.

.. note::

    Hint: To get full credit on #0017 The test must pass on any computer

Now add a nose2 plugin
**********************

Create a plugin that will output the contents of ReqTracer.requirements to a file 

**Make sure you fully tested/tagged the requirements**


Write Up
********

#. What are five examples of other testing(nose2) plugins that might be useful?
The doctests could be handy.  There is a third party one, nose2-cov, which helps generate the coverage reporting.  Profiling could be helpful.  There is an attribute plugin that will help with organizing tests and only running certain ones(I think).  Then there is one that layers your tests, which could be helpful.

#. Do you plan to create any of these plugins for your term project?
No.  I will be using the generic TESTCASE class and will call it good from that.  Other things that may be required, but I don't know if they fall under plugins, is the coverage reporting we implemented before and the doctests and html documentation.

#. What is the hardest part of this lab?
The hardest part was apparently remembering to do this section!  But really, the hardest part here was wrapping my head around using globals.  It's something that I have actually never done before.  So accessing the Requirements variable was a little strange to me.

#. Did the code fully and completely implement the requirements? Explain

No, there were a few tests that failed due to the code not doing what they were supposed to.  

#. Was the requirements complete? Explain
I would argue that no, they weren't complete because they didn't cover many negative testcases, as well as not covering certain parts, such as having too many arguments in your question, thus raising the exception "too many arguments".  

#. For each bug you found in the source code enter a "Bug Request" in your write up following this template.
   You should consider bugs to be not following the requirements, inaccurate requirements, or code that has
   no reason for existing (not covered by the requirements):
    
**ISSUE Number:**

**BREIF:**

**Steps to reproduce:**:

**Comments:**

**Time Spent:**

#. Why are requirements tracing so important?
Well, it allows you to target trouble areas with a feature.  If many of the requirements for a specific feature are failing their tests, perhaps the coder should re-evaluate how to implement the feature.

#. How long did it take to complete this lab?
I think it was about 6 hours in total.
Please submit your repo url