_Thanks for your interest in a position at Petro.ai! As part of the interview process, we use take-home technical
exercises as a way to assess your skills, background, and approach in certain technical problem-solving tasks. Our
expectation is that this exercise should require between 4-6 hours for someone familiar with the underlying concepts and
tools. If you find it taking longer, please feel free to submit partial solutions._

_In terms of allowed resources, we encourage the use of online resources like reference pages, StackOverflow, and the
like. However, please do not consult other people before submitting your solutions._

**Exercise 1: Linear regression analysis**

Build a linear regression model for the WHO life expectancy dataset that predicts the life expectancy for a country
based on other characteristics. Evaluate the performance of the model on the most recent data in the dataset.

For this exercise, deliver the following:

- [The WHO data file](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who)
- A python script for building the model
- A python script for evaluating the performance of the model
- A brief README explaining how to run your scripts and also providing an overview of your approach, any key design
  decisions that were made, and the ultimate performance of the model you found.

Worth noting: this problem is intentionally underspecified, leaving room for you to make decisions that you think best
achieve the desired outcome.

**Exercise 2: Logging Service**

Use Flask to implement the backend for a remote logging system.

[POST] /api/log

Body is a JSON with the structure:

{

"logEntries": [

"\<entry text 1\>",

"\<entry text 2\>",

…

]

}

Each line in the "logEntries" list is added, in order to the log.

[GET] /api/log[?num\_lines=10]

Returns the most recent lines in the log. By default, 10.

The RESTful controller should use a "log reader/writer" object to compartmentalize interactions with the permanent
storage of the log entries. While this specific implementation will read and write to exactly one file on the server
called "log.txt", you should employ inheritance in your design to allow for the future addition of other implementations
that could write to, for example, a database.

For this exercise, deliver a complete functioning python project with a short README to help the evaluator work with it.

**Exercise 3: Confidence intervals for a random forest classifier**

We use a random forest classifier (trained on existing well data) to predict the 12-month cumulative production expected
for a new well. Devise a technique for providing a confidence interval around this point prediction that would help a
non-data scientist use these predictions. For this exercise, you don't need to implement anything. Just provide a
paragraph explaining and justifying the approach.