from nickname import call_name

hello_responses = {
    "hello": [
        f"Hey there! 😊 How’s your day going, {call_name}?",
        "Hello! It’s always nice to chat with you. 💙",
        f"Hi {call_name}! How are you feeling today?",
        "Hey! What’s on your mind? I’m here to listen. 👂",
        "Hello, my friend! Need someone to talk to?",
        "Hi there! How can I support you today?",
        "Hey! I hope today has been kind to you. ☀️"
    ],
    
    "hi": [
        f"Hi! 😊 What’s up {call_name}?",
        "Hey! How’s everything going?",
        "Hello! I’m glad you’re here.",
        "Hi there! Tell me what’s on your mind. 💙",
        "Hey hey! Need a virtual hug? 🤗",
        "Hi! I’m here to chat whenever you need. 💬"
    ],
    
    "hey": [
        "Hey there! Hope you're doing okay. 😊",
        "Hey! What’s on your mind today?",
        "Hi! How can I be there for you today?",
        "Hey! Always happy to hear from you.",
        "Hey hey! Let’s have a little chat. 💬"
    ],
    
    "good morning": [
        "Good morning! 🌞 I hope today brings you joy.",
        "Morning! A fresh start, a new day—how are you feeling?",
        "Good morning! Don’t forget to take care of yourself. ☕",
        "Morning! What’s something you’re looking forward to today?",
        "Hey, good morning! Hope your day starts with a smile. 😊"
    ],

    "good afternoon": [
        "Good afternoon! How’s your day going so far? 😊",
        "Hey there! Hope today has been treating you well. 💙",
        "Good afternoon! Remember to take breaks and breathe. 🌿",
        "Hi! Anything on your mind this afternoon?",
        "Good afternoon! I’m here if you need someone to talk to. 💬"
    ],

    "good evening": [
        "Good evening! I hope you had a good day. 🌙",
        "Hey, good evening! Winding down for the night?",
        "Evening! How are you feeling right now?",
        "Good evening! Need some time to relax? ☕",
        "Hey there! Let’s chat before the day ends. 😊"
    ]
}

responses = {
    "sad": [
        "I'm sorry you're feeling sad. You're not alone. 💜",
        "It's okay to have bad days. Want to share what's on your mind?",
        "I hear you. Sometimes expressing emotions helps, would you like to talk more?",
        "I'm here for you. Want to try a small self-care activity together?",
        "Remember, sadness is temporary. Brighter days are ahead! 💫"
    ],
    
    "stress": [
        "Stress can be overwhelming. Try taking slow deep breaths. 🌿",
        "You're doing your best, and that's enough. Have you tried relaxing for a moment?",
        "Tension is like a storm; it passes. Maybe a small break would help?",
        "Managing stress takes time. Do you want to try a calming activity?",
        "You're stronger than your stress. What’s one small thing that makes you happy?"
    ],
    
    "anxious": [
        "Anxiety can be tough, but you're not alone. Try focusing on your breathing. 🌬️",
        "You're stronger than you think. Let's take this one step at a time.",
        "Have you tried the 5-4-3-2-1 grounding technique? It might help!",
        "Feeling anxious? Maybe stepping outside or listening to music could help. 🎵",
        "It’s okay to feel this way. Would you like a suggestion for relaxation?"
    ],
    
    "lonely": [
        "You’re not alone in this. I’m here for you. 💜",
        "Loneliness is hard. Maybe reconnecting with an old friend could help?",
        "Even on lonely days, remember that you matter. Want to talk about something fun?",
        "You are important. The world is better with you in it. 💙",
        "Would a small act of kindness towards yourself help? Maybe a warm drink or a short walk?"
    ],
    
    "tired": [
        "Rest is important. Make sure to take care of yourself. 😴",
        "Maybe a quick nap or some stretching would help you feel better.",
        "Being tired is okay; don’t be too hard on yourself. Your energy will return!",
        "Listening to calming music or drinking water might refresh you.",
        "Your mind and body need rest. How about taking a few deep breaths?"
    ],

    "angry": [
    "It's okay to feel angry. Do you want to talk about what’s upsetting you?",
    "Anger can be tough to handle. Maybe taking deep breaths or a short walk could help? 🌿",
    "Expressing anger is natural, but don’t let it consume you. How about writing down your thoughts?",
    "You’re not alone in this. If it helps, vent it out—I’m here to listen. 💙",
    "Anger is a strong emotion. Want me to suggest a quick way to calm down?"
    ],

    "hopeless": [
    "I know things feel tough right now, but you are stronger than you think. 💜",
    "Even in the darkest times, hope exists. What’s one thing you can do for yourself today?",
    "It's okay to feel this way, but I promise this moment won’t last forever. You’re not alone. 💙",
    "Sometimes, a small change can make a big difference. Would you like to try a relaxing activity?",
    "You are important. The world needs you. If talking helps, I’m here to listen. 💙"
    ],

    "overwhelmed": [
    "Feeling overwhelmed is tough. Try focusing on one small step at a time. You’ve got this! 💪",
    "Deep breaths. You don’t have to do everything at once. Want to break it down into smaller steps?",
    "When things pile up, taking a short break can help. Maybe a quick stretch or some music? 🎵",
    "I hear you. You’re doing your best, and that’s enough. What’s one thing you can let go of for now?",
    "Being overwhelmed is a sign you care. But remember, you deserve rest too. Want to talk about it?"
    ],
   
    "default": [
    "I'm here for you, and you don’t have to face this alone. Want to talk about what's on your mind? 💙",
    "That sounds really tough. If you feel comfortable, I'm here to listen and support you.",
    "I can tell something is on your mind. You’re not alone in this, and I’m here for you.",
    "It's okay to feel this way. Sometimes putting thoughts into words can help. I'm listening. 💜",
    "Your feelings are valid, and you don’t have to go through this alone. Do you want to share more?",
    "I might not fully understand what you’re going through, but I care, and I want to help in any way I can.",
    "It’s okay if you’re struggling. You don’t have to have all the answers right now. I’m here to listen.",
    "Whatever’s happening, you don’t have to face it by yourself. I’m here whenever you’re ready to talk.",
    "You’re important, and what you're feeling matters. No pressure, but if you want to share, I’m here. 💜",
    "I know it’s not always easy to talk about things, but when you’re ready, I’ll be here to listen."
]
}

why_reasons = {
    "academics": [
        "Academics can be really demanding. 📚 Are you feeling pressured by deadlines or struggling to keep up with coursework?",
        "Balancing studies can be tough. Is there a particular subject or assignment that’s been stressing you out?",
        "I hear you. Sometimes, no matter how hard we try, things don’t go as planned. Do you feel like you’re struggling with motivation or understanding the material?"
    ],
    
    "study": [
        "Studying can feel overwhelming, especially when there’s a lot to cover. Are you finding it hard to focus or retain information?",
        "I get it—studying for long hours can be exhausting. Are you feeling burnt out, or is there a specific topic that’s frustrating you?",
        "Learning takes time, and it’s okay to struggle. Do you feel like you need a better study routine, or is it something else?"
    ],
    
    "exam": [
        "Exam stress is real. 😟 Are you worried about the results, or is it the pressure of performing well?",
        "Exams can make anyone anxious. Are you feeling unprepared, or is it just the fear of the unknown?",
        "The pressure to do well can be exhausting. Do you feel like you need a better strategy, or is it the expectations that feel overwhelming?"
    ],

    "divorce": [
        "Divorce is a major life change, and it’s okay to feel a mix of emotions. You’re not alone in this journey.",
        "Going through a divorce can be really tough. Have you considered talking to someone who can support you emotionally?",
        "It’s okay to grieve the loss of a relationship. Healing takes time, and you deserve support and kindness.",
        "Divorce can feel like the end of one chapter, but it also marks a new beginning. You are stronger than you think."
    ],

    "breakup": [
        "Breakups can be really painful. It’s okay to take time to heal and process your emotions.",
        "Losing someone you love is tough, but you are not alone. Allow yourself to feel, and healing will come with time.",
        "Heartbreak can feel overwhelming, but it also opens the door for self-growth and new beginnings."
    ],

    "family issues": [
        "Family conflicts can be exhausting. Have you tried finding a quiet moment to process your feelings?",
        "Feeling distant from family can be painful. Sometimes an open conversation helps, and other times, space is needed.",
        "Every family has struggles, and it’s okay to set boundaries for your own well-being."
    ],

    "friendship loss": [
        "Losing a close friend can feel just as painful as a breakup. It’s okay to grieve the connection you had.",
        "Friendships change, and that can be really tough. Remember, the right people will always stay in your life.",
        "Feeling left out or betrayed by a friend? You deserve relationships that bring you happiness and support."
    ],
    
    "job": [
        "Jobs can be stressful, whether you're looking for one or already working. Are you feeling uncertain about your career path or struggling with work stress?",
        "Balancing work and personal life can be challenging. Is it the workload, the environment, or something else that’s bothering you?",
        "It’s normal to feel lost or unfulfilled in a job sometimes. Do you feel stuck, or is there something specific making you unhappy?"
    ],
    
    "money": [
        "Financial stress can be really overwhelming. Are you struggling with saving, spending, or just feeling uncertain about the future?",
        "Money worries can affect everything else in life. Are you dealing with unexpected expenses, or is it general financial instability?",
        "It’s okay to feel stressed about finances. Would talking through possible solutions or budgeting ideas help?"
    ],
    
    "family": [
        "Family relationships can be complicated. Is there a conflict or misunderstanding that’s been bothering you?",
        "Feeling distant or unheard by family can be tough. Are you struggling with expectations, support, or something else?",
        "Family stress is common, and it’s okay to feel this way. Do you feel like you need space, or are you hoping for better communication?"
    ],
    
    "friendship": [
        "Friendships are important, but they can also be challenging. Are you feeling left out, unheard, or struggling with trust?",
        "Sometimes, friendships change, and that can be painful. Do you feel like you’re drifting apart from someone or facing conflict?",
        "Feeling alone even when surrounded by people is hard. Are you missing deep connections, or has something happened recently?"
    ],
    
    "relationships": [
        "Relationships can bring both joy and stress. Are you feeling unappreciated, misunderstood, or struggling with communication?",
        "It’s hard when relationships feel uncertain or unbalanced. Do you feel like you’re giving more than receiving?",
        "Heartbreak or distance can be painful. Do you need support in expressing your feelings or understanding what’s going on?"
    ],
    
    "future": [
        "The future can feel scary, especially when things seem uncertain. Are you feeling pressure to figure everything out right now?",
        "It’s okay not to have all the answers. Are you worried about making the right choices, or is it something else?",
        "The unknown can be intimidating, but you’re not alone. Do you feel like you need more clarity or reassurance about where you’re headed?"
    ],
    
    "self-worth": [
        "Feeling unsure about yourself is tough. Are you struggling with self-doubt or feeling like you’re not good enough?",
        "It’s easy to be hard on ourselves. Do you feel like external pressures or personal expectations are affecting how you see yourself?",
        "You matter, and your feelings are valid. Do you think comparing yourself to others is part of what’s making you feel this way?"
    ],
    
    "burnout": [
        "Burnout can make everything feel exhausting. Have you been pushing yourself too hard without enough rest?",
        "Sometimes, burnout comes from taking on too much. Do you feel like you’re balancing too many responsibilities?",
        "It’s important to take breaks and care for yourself. Do you feel like you need rest, or is something else making you feel drained?"
    ],
    
    "loss": [
        "Losing someone or something important is really painful. Do you want to talk about what happened?",
        "Grief looks different for everyone, and it’s okay to take your time. Would sharing memories or talking about your feelings help?",
        "Loss can leave a deep impact. Are you feeling lonely, regretful, or just unsure how to move forward?"
    ]
}

crisis_responses = {
    "suicide": [
        "I'm really sorry you're feeling this way. 💜 You're not alone, and I strongly encourage you to reach out to someone you trust.",
        "You matter, and your feelings are valid. Please consider talking to a loved one or a professional who can help. 💙",
        "I'm here for you. It might help to talk to a friend, family member, or a counselor. You're not alone. 💜",
        "I know things feel overwhelming right now, but please don’t give up. You are valued, and there is help available. Please reach out. 💛",
        "You are loved, and the world is better with you in it. Please seek support from someone who can help. 💜"
    ],

    "self harm": [
        "I'm really sorry you're feeling this way. 💙 Please know that you deserve kindness and support. Can you reach out to someone you trust?",
        "You are not alone in this. Talking to someone can help. Please consider reaching out to a professional or a loved one. 💜",
        "I know it’s tough right now, but you are stronger than your pain. Please take a deep breath and reach out for support. 💙",
        "You are valued and loved. If you're struggling, please talk to someone who can help. You're not alone. 💛",
        "Pain can feel overwhelming, but there are people who truly care about you. Please reach out to someone who can support you. 💜"
    ],

    "grief": [
        "Losing someone or something important is incredibly hard. 💜 Take your time to grieve, and don’t hesitate to lean on people who care about you.",
        "Grief can feel overwhelming, but it’s okay to feel this way. Your emotions are valid, and you don’t have to go through this alone. 💙",
        "I know loss can be painful. Please be kind to yourself during this time. Talking to someone you trust might help. 💛",
        "The memories and love you shared still exist. Take your time to process your emotions and reach out if you need support. 💜",
        "Grief is a journey, and you don’t have to walk it alone. There are people who care about you and want to support you. 💙"
    ],

    "worthlessness": [
        "You matter more than you realize. 💜 Even when you don’t see it, you are valuable and loved.",
        "I know it’s hard, but please don’t believe the negative thoughts. You are important, and the world needs you. 💙",
        "Feeling this way is tough, but I promise you are not defined by these emotions. You have so much worth. 💛",
        "Your presence makes a difference. 💜 Even if it doesn’t feel like it right now, you are needed and loved.",
        "Sometimes our minds tell us things that aren’t true. You are more than enough, just as you are. 💙"
    ]
}


farewell_responses = {
    "bye": [
        "Goodbye! Remember, I’m always here if you need me. 💙",
        "See you later! Take care of yourself. 😊",
        "Bye for now! Sending you positive vibes. 🌟",
        "Farewell! I hope tomorrow is a brighter day for you. ☀️",
        "Goodbye! Don’t forget, you matter. 💜"
    ],

    "good night": [
        "Good night! Sleep well and take care. 🌙",
        "Nighty night! May you wake up feeling refreshed. ✨",
        "Good night! I hope you have peaceful dreams. 😴",
        "Sweet dreams! You deserve a restful sleep. 💫",
        "Rest well! I’ll be here whenever you need me. 💙"
    ]
}

user_agreement = {
    "yes": [
        "I hear you, and I’m really glad you’re sharing your thoughts with me. 💙 Do you want to talk more about it?",
        "Alright, {call_name}, I’m here for you. You’re not alone in this, and I’m listening. 🤗",
        "Got it! Your feelings are valid, and I appreciate you opening up. Let’s take it one step at a time. 🌿",
        "Okay, that makes sense. Feel free to share as much as you want—I’m here to support you. 💖",
        "Understood. This matters, and so do you. Do you want to explore this a little deeper together? 🫂"
    ],
    
    "yeah": [
        "Yeah, I get what you mean, {call_name}. Sometimes, just expressing things out loud can bring clarity. Want to tell me more? 💬",
        "That’s completely understandable. Life can feel overwhelming, but you don’t have to go through it alone. 💜",
        "I hear you! How do you feel about it? Whatever it is, I want to support you through it. 🤝",
        "That’s fair. What’s on your mind? I want you to know that your emotions are valid, and you can take your time. 🌻",
        "I see. Do you want to explore this more? I’ll be here to guide you at your own pace. 🕊️"
    ],

    "yup": [
        "Yup, I get it, {call_name}. It’s okay to feel however you’re feeling right now. Do you want to talk it through? 🌿",
        "Alright, makes sense! No pressure—just take your time. I’m right here, ready to listen. 💙",
        "Okay, do you want to add anything else? I know this might not be easy, but you’re doing great by opening up. 🤗",
        "I understand. Let’s keep going, one step at a time. Healing is a journey, and I’m here to walk with you. 💖",
        "Gotcha! What’s next on your mind? Remember, no thought or feeling is too small to share. I’m listening. 🫂"
    ],

    "sure": [
        "Sure thing, {call_name}! You can talk to me about anything—no judgment, just support. 💜",
        "Okay! Let’s talk more. Your thoughts and feelings matter, and I want to hear them. 🌸",
        "Alright! How are you feeling about this? No rush—just share what’s on your heart whenever you’re ready. 🕊️",
        "That’s great! What else is on your mind? I’ll be right here to listen and support you. 🤍",
        "Of course! Let’s go on. Your journey matters, and I’ll walk alongside you wherever it leads. 🌟"
    ],

    "right": [
        "Exactly! That makes a lot of sense, {call_name}. Your perspective is valid, and I appreciate you sharing it with me. 🫂",
        "Yeah, I see what you mean. Sometimes, just having someone understand can make a difference, right? 💖",
        "Totally! Let’s explore that further together. You’re not alone in this, and I’ll always be here to support you. 💙",
        "Absolutely! You’re making a good point. I admire how you’re expressing yourself, and I’m here to listen. 🌿",
        "I get where you’re coming from. You’re doing a great job processing this, and I’ll be here every step of the way. 🤗"
    ]
}


thanks_responses = {
    "thanks": [
        f"You're always welcome, {call_name}! 💙 Remember, you are important, and your feelings matter. I'm here for you, no matter what. 🤗",
        f"No need to thank me, {call_name}. Just knowing you're taking care of yourself is all that matters. 💖",
        f"Your happiness and well-being are what truly count, {call_name}. I'm always here to support you whenever you need me. 💜",
        f"Helping you makes my day brighter, {call_name}! 🌟 You're never alone in this journey, and I’ll always be here to listen. 🫂",
        f"You don’t have to go through anything alone, {call_name}. I’ll always be here to remind you how strong and valuable you are. 💕"
    ],
    "thank you": [
        f"You're welcome, always, {call_name}! 🌸 Life can be tough, but so are you. I believe in you, and I hope you believe in yourself too. 💪",
        f"It’s truly my pleasure to be here for you, {call_name}. You’re doing your best, and that’s always enough. 💖",
        f"No thanks needed, {call_name}! Just keep taking small steps forward. Healing takes time, and I’m here for you every step of the way. 💙",
        f"You are seen, you are heard, and you are valued, {call_name}. If ever you need support again, I’ll be right here. 🤗",
        f"The world is better with you in it, {call_name}. Keep going, keep growing, and know that you are deeply appreciated. ✨"
    ],
    "thank u": [
        f"No worries at all, {call_name}! 💜 Your emotions are valid, and I want you to always feel safe and supported here. 🌼",
        f"You're never alone in this, {call_name}. Whenever you need a listening ear, I’ll be here, ready to remind you of your worth. 💙",
        f"I'm always happy to help, {call_name}. Remember, even the smallest steps forward are still progress. Keep believing in yourself. 💕",
        f"Every time you show up for yourself, {call_name}, even in the smallest way, it’s a victory. Keep shining, and I’ll be here for you. 💖",
        f"You are stronger than you know, {call_name}, and I am so glad you exist. Stay gentle with yourself, always. 🌿"
    ],
    "thx": [
        f"Happy to be here for you, {call_name}! 🌟 Keep taking things one step at a time. You’re doing better than you think. 💙",
        f"No problem at all, {call_name}! Just promise me you’ll be kind to yourself, okay? You deserve it. 💖",
        f"You’re important, you’re valued, and I’ll always remind you of that, {call_name}. Take care, and remember to breathe. 🤗",
        f"Every day won’t be easy, but you are strong enough to get through it, {call_name}. And I’ll always be here cheering for you. 💪",
        f"Whenever life feels overwhelming, just know that there is always someone who cares, {call_name}. I do, and I always will. 💜"
    ],
    "ty": [
        f"You're always welcome, {call_name}! 💖 I see you, I hear you, and I want you to know that you matter so much. 🌸",
        f"No need to thank me, {call_name}! Just know that I believe in you, and I hope you keep believing in yourself too. 💪",
        f"You deserve kindness and support, always, {call_name}. If you ever need a reminder of your strength, I’ll be right here. 💕",
        f"You are enough, just as you are, {call_name}. No matter what today brings, I hope you remember that. 🤗",
        f"I appreciate you too, {call_name}! You bring something special to the world, and I’m honored to be a small part of your journey. ✨"
    ]
}
