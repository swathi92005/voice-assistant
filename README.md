<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JARVIS - Your Smart Assistant</title>
</head>
<body>
    <h1>JARVIS - Your Smart Assistant</h1>
    <p>This Python script creates a virtual assistant named JARVIS that can perform various tasks using speech recognition and text-to-speech functionalities.</p>

    <h2>Features:</h2>
    <ul>
        <li>Play songs on YouTube</li>
        <li>Get the current time</li>
        <li>Get the current date</li>
        <li>Answer basic questions using Wikipedia</li>
        <li>Respond to greetings</li>
    </ul>

    <h2>Requirements:</h2>
    <ul>
        <li>Python 3</li>
        <li>SpeechRecognition library (<code>pip install speechrecognition</code>)</li>
        <li>pyttsx3 library (<code>pip install pyttsx3</code>)</li>
        <li>pywhatkit library (<code>pip install pywhatkit</code>)</li>
    </ul>

    <h2>Usage:</h2>
    <h3>Installation:</h3>
    <pre>bash
pip install speechrecognition pyttsx3 pywhatkit
</pre>

    <h3>Running the Script:</h3>
    <pre>bash
python jarvis.py
</pre>

    <h3>Using JARVIS:</h3>
    <p>Start your commands with "JARVIS" followed by your request (e.g., "JARVIS play music", "JARVIS what is the time").</p>

    <h2>Example Interaction:</h2>
    <p>You: JARVIS play music<br>
    JARVIS: Playing ... (your chosen song)</p>

    <p>You: JARVIS what is the time<br>
    JARVIS: Current time is ... (current time)</p>

    <p>You: JARVIS who is Albert Einstein?<br>
    JARVIS: (Fetches summary from Wikipedia and reads it aloud)</p>

    <h2>How it Works:</h2>
    <p>The script imports the necessary libraries for speech recognition, text-to-speech, YouTube playback, date and time, and Wikipedia access.</p>
    <p>It initializes a speech recognizer (listener) and a text-to-speech engine (engine).</p>
    <p>The <code>talk</code> function uses <code>engine.say</code> to convert text into speech and <code>engine.runAndWait</code> to play the spoken output.</p>
    <p>The <code>take_command</code> function listens for user input using the microphone, recognizes it with Google Speech Recognition, and returns the processed command (lowercase and without the wake word "JARVIS").</p>
    <p>The <code>run_jarvis</code> function continuously listens for commands and takes actions based on keywords:</p>
    <ul>
        <li>"play": Uses <code>pywhatkit.playonyt</code> to play the specified song on YouTube.</li>
        <li>"time": Gets the current time using <code>datetime</code> and speaks it.</li>
        <li>"date": Gets the current date using <code>datetime</code> and speaks it.</li>
        <li>"how are you": Responds politely.</li>
        <li>"what is your name": Introduces itself as JARVIS.</li>
        <li>"who is": Uses <code>wikipedia.summary</code> to get a brief summary from Wikipedia and speaks it.</li>
        <li>Other commands: Prompts the user to repeat for clarity.</li>
    </ul>
</body>
</html>
