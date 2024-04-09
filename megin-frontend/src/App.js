/*
filename: App.js
author: Ananda Francis
description: main file for Megin, displaying all React components
*/

// import necessary libraries
import React from 'react';
import './App.css';
import ChatBot from './ChatBot';

// create app component with header & chatbot
function App() {
    return (
        <div className="App">
            <header className="App-header">
                <h1>Megin</h1>
                <h3>Your Idea Manager</h3>
                <br></br>
                <br></br>
                <ChatBot />
            </header>
        </div>
    );
}

export default App;
