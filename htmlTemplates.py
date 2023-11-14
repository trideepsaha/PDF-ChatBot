css = '''
<style>
body {
    background-color: #ffffff; /* Light background color */
    color: #333333; /* Dark text color */
    font-family: 'Roboto', sans-serif;
}

.container {
    max-width: 900px;
    margin: auto;
}

.header {
    background-color: #55a8b2; /* Light blue-green */
    color: #fff;
    padding: 1.5rem;
    text-align: center;
    border-radius: 0.8rem;
    margin-bottom: 1.5rem;
}

.sidebar {
    background-color: #ffffff; /* White background */
    padding: 1.5rem;
    border-radius: 0.8rem;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
}

.content {
    background-color: #ffffff; /* White background */
    padding: 1.5rem;
    border-radius: 0.8rem;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
}

.chat-message {
    padding: 2rem;
    border-radius: 0.8rem;
    margin-bottom: 1.5rem;
    display: flex;
}

.chat-message.user {
    background-color: #66b3ff; /* Light blue */
    color: #fff;
}

.chat-message.bot {
    background-color: #f2f2f2; /* Light gray */
    color: #333;
}

.chat-message .avatar {
    width: 18%;
}

.chat-message .avatar img {
    max-width: 70px;
    max-height: 70px;
    border-radius: 50%;
    object-fit: cover;
}

.chat-message .message {
    width: 82%;
    padding: 0 2rem;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://github.com/PixMusicaX/PDF-ChatBot/blob/main/chatbot.png?raw=true" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://previews.123rf.com/images/stockgiu/stockgiu1802/stockgiu180211004/96105655-a-doodle-user-man-with-elegant-shirt-design-vector-illustration.jpg style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
