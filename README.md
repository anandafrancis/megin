# Megin Description

## Short Version

Megin: Your personal idea whisperer: Megin is a platform that communicates with you via text to routinely remind you about different ideas you have recorded onto the platform, to get to “later”. Megin takes into consideration how strong, urgent, important and prevalent all your ideas are and will nudge some more than others as well as provide suggestions on how to actualize them


## Long Version

In a fast-paced and overstimulating world, many of us struggle with memory retention issues, a lack of motivation, unclear execution plans, and inadequate support. This overwhelm causes many valuable ideas to get lost in what I call the "mental Bermuda triangle."  Missing out on so many personal ideas contribute to the staggering depression, dissatisfaction and apathy many individuals feel in their day-to-day lives. Existing productivity tools, like Google Tasks Board or Notion, though effective for some, often require a steep learning curve and a high level of organizational skills.

Megin, your personal idea whisperer, introduces a more intuitive and dynamic approach to idea management. Unlike traditional tools that feel corporate and impersonal, Megin's conversational interface adapts to users' preferences, offering a natural and accessible interaction. Megin categorizes ideas based on factors like strength, urgency, importance, and prevalence. Users also have the flexibility to customize these factors to suit their individual needs. Megin not only sends routine reminders and nudges but also provides actionable steps, from idea conception to execution, empowering users to bring their creative thoughts to fruition at their own pace. By the end of the semester I believe that we could produce a fully functional prototype able to have a user input ideas, have those ideas stored and tagged and then a schedule created that communicates the ideas back to the user as dates and times determined by the algorithm that runs the scheduling feature.



# Megin Setup Instructions
Welcome to Megin, your personal idea manager!

## Prerequisites

Before you begin, ensure you have the following installed:

* Flask: Python framework required to run the backend server.
    * Run pip install flask in your terminal to install Flask
* Node.js and npm: JavaScript framework required to run the frontend application
    * Download and install them from https://nodejs.org/en/download/ based on your operating system
* OpenAI API: API used to power Megin-chatbot
    * Run export OPENAI_API_KEY='your_api_key_here'
    * If you do not have an OpenAI API key generate one at https://platform.openai.com/api-keys 

# Installation and Running Megin

## Extract the Project:

1. Open the downloaded zip folder and uncompress its contents.
2. You will find a directory named Megin containing two subdirectories: megin-backend and megin-frontend.

## Run the Backend Server:

1. Open your terminal or command prompt.
2. Navigate to the backend directory by running cd megin-backend.
3. Start the Flask server with the command flask run.
4. Once the server is running, you will see a message indicating it's live on http://127.0.0.1:5000


## Run the Frontend Application:

1. Open a new terminal window or tab.
2. Navigate to the frontend directory by running cd megin-frontend.
3. Start the frontend application with npm start.
4. Navigate to http://localhost:3000 where you can interact with Megin

Congratulations! You've successfully set up and started Megin.


# Reflection:

## Design Choices
The color of the UI was inspired my nation’s flags Green, Yellow and Black. I like how the colors complement each other and I came up with the idea will back home in Jamaica so it felt fitting. I wanted the platform to require minimal user navigation with the backend doing a lot of the work to help users seamless just spit out ideas and not need to worry about managing, organizing and making sense of those ideas themselves.


## Helpful Resources
Between the documentation and experience I gained from a chatbot I created in the past for several projects: AI4Impact AI-EP Project @ Burnes Center for Social Change, Legal-eaze @ TreeHacks Hosted by Stanford and other personal projects with chatbots, this was a rather simple assignment for me to complete.  The React tutorial in class as well as using ChatGPT 4 to debug CORS middleware issues were helpful resources.

## API Integration Process

The API I integrated into Megin was OpenAI's text generation model, GPT 3.5 Turbo. In the initial "Hello World" assignment, the Python Flask backend app.py file used an automated response in the chatbot_message() function to return to the user what they sent to the chatbot as “Received message: {message}”. Exploring the OpenAI chat completion documentation I was able to integrate the GPT 3.5 Turbo model to track the input of the user and the previous outputs by the model in a conversation_history global variable. Every time the user input a new message this function and chat history was called and created a chat completion object that was used to generate Megin's next message to the user.

## Challenges I Faced
Limitations of the current code include how I am storing conversation history. I am interested in potentially leveraging a database into of the local Python environment to store chat history and build queries and prompt engineering that can easily access important information from pervious conversation. While this is more a long term goal, in the next interation more fine tuning will be done on the model to better fulfill my goals of what Megin is to be as a product: a personalized AI idea management system.

## What I learned
I have a lot of experience with chatbots powered by GPT so this wasn’t much of a new experience for me, more so good practice. Something I do want to explore is how the fine tuning of this will be a lot different because Megin won’t be just a chatbot but an AI accethat interacts with users via text, that will prompt and “talk” to the user even if the user does not initiate conversation. For example, if the user mentions to Megin an idea that needs to be executed by April 24, Megin may periodically check in and remind the user of that idea as well as aid in strategy development to make the task easier to execute. Right now as a chatbot, Megin only helps the user execute ideas in the here and now and doesn’t help with short term or long term idea management outside of the immediate use case which will take a lot of creative brainstorming to create these features. 
