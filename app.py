body {
    font-family: Arial, sans-serif;
    background: #f4f4f4;
    display: flex;
    justify-content: center;
    padding: 20px;
}

.chat-container {
    width: 600px;
    background: white;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0,0,0,0.2);
}

#chat-box {
    max-height: 400px;
    overflow-y: auto;
    padding: 10px;
    border: 1px solid #ccc;
    margin-bottom: 10px;
    border-radius: 8px;
    background: #fafafa;
}

.bubble {
    padding: 10px 15px;
    margin: 5px;
    border-radius: 15px;
    max-width: 80%;
    word-wrap: break-word;
}

.user {
    background: #4CAF50;
    color: white;
    text-align: right;
    margin-left: auto;
}

.bot {
    background: #e0e0e0;
    color: black;
    text-align: left;
    margin-right: auto;
}

.input-container {
    display: flex;
}

input {
    flex: 1;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
}

button {
    background: #4CAF50;
    color: white;
    border: none;
    padding: 10px 15px;
    margin-left: 5px;
    border-radius: 5px;
    cursor: pointer;
}
