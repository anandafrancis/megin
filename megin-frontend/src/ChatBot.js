// Import React features, useState, useEffect, and CSS styling file
import React, { useState, useEffect } from 'react';
import './ChatBot.css';

const ChatBot = () => {
  
  const [messages, setMessages] = useState([]);
  const [idea, setIdea] = useState({ title: '', description: '', urgency: 'Medium', importance: 'Medium' });

  // Fetch the initial message and reminders when the component mounts
  useEffect(() => {
      fetchInitialMessage();
      fetchReminders();
  }, []);

  const fetchInitialMessage = async () => {
      const response = await fetch('http://127.0.0.1:5000/chatbot');
      if (response.ok) {
          const result = await response.json();
          setMessages([{ role: 'bot', content: result.message }]);
      } else {
          console.error('Failed to fetch initial message');
      }
  };

  // New function to fetch reminders from the backend
  const fetchReminders = async () => {
    const response = await fetch('http://127.0.0.1:5000/reminders');
    if (response.ok) {
      const reminders = await response.json();
      reminders.reminders.forEach(reminder => { // Notice the change here
          setMessages(prevMessages => [
              ...prevMessages,
              { role: 'bot', content: `Reminder: ${reminder.title} - ${reminder.description}` }
          ]);
      });      
    } else {
        console.error('Failed to fetch reminders');
    }
};


    // Handle user message input
    const handleUserMessage = (userMessage) => {
        if (!idea.title) {
            setIdea({ ...idea, title: userMessage });
            setMessages((prevMessages) => [
                ...prevMessages,
                { role: 'user', content: userMessage },
                { role: 'bot', content: 'What is the description of your idea?' },
            ]);
        } else if (!idea.description) {
            setIdea({ ...idea, description: userMessage });
            setMessages((prevMessages) => [
                ...prevMessages,
                { role: 'user', content: userMessage },
                { role: 'bot', content: 'How urgent is your idea? (Low/Medium/High)' },
            ]);
        } else {
            // If urgency and importance are already set, handle other inputs or complete the flow
            handleCategorySelection(userMessage);
        }
    };

    // Handle category selection for the idea
    const handleCategorySelection = (userInput) => {
        if (['Low', 'Medium', 'High'].includes(userInput)) {
            if (!idea.urgencySet) {
                setIdea({ ...idea, urgency: userInput, urgencySet: true });
                setMessages((prevMessages) => [
                    ...prevMessages,
                    { role: 'user', content: userInput },
                    { role: 'bot', content: 'How important is your idea? (Low/Medium/High)' },
                ]);
            } else if (!idea.importanceSet) {
                setIdea({ ...idea, importance: userInput, importanceSet: true });
                setMessages((prevMessages) => [
                    ...prevMessages,
                    { role: 'user', content: userInput },
                ]);
                // Submit the idea to the backend or proceed to the next step
                submitIdea();
            }
        } else {
            setMessages((prevMessages) => [
                ...prevMessages,
                { role: 'user', content: userInput },
                { role: 'bot', content: 'Please select a valid option (Low/Medium/High).' },
            ]);
        }
    };

    // Submit the idea to the backend
    const submitIdea = async () => {
        try {
            const response = await fetch('http://127.0.0.1:5000/ideas', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(idea),
            });

            if (response.ok) {
                setMessages((prevMessages) => [
                    ...prevMessages,
                    { role: 'bot', content: 'Your idea has been saved successfully!' },
                ]);
                // Reset the idea state
                setIdea({ title: '', description: '', urgency: 'Medium', importance: 'Medium', urgencySet: false, importanceSet: false });
            } else {
                console.error('Error submitting idea');
            }
        } catch (error) {
            console.error('Error during fetch:', error.message);
        }
    };

    // Design UI of the chatbot displaying the entire conversation
    return (
      <div className="chat-container">
          <div className="messages">
              {messages.map((message, index) => (
                  <div key={index} className={`message ${message.role}`}>
                      <span className="message-content">{message.content}</span>
                  </div>
              ))}
          </div>
          <div className="user-input">
              <input
                  type="text"
                  placeholder="Type your message..."
                  onKeyDown={(e) => {
                      if (e.key === 'Enter' && e.target.value.trim() !== '') {
                          handleUserMessage(e.target.value.trim());
                          e.target.value = '';
                      }
                  }}
              />
          </div>
      </div>
  );
};

export default ChatBot;



