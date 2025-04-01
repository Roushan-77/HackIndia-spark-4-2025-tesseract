questions = {
    "1. How often do you feel more irritable or frustrated than usual?": [
        "1) Rarely",
        "2) Sometimes",
        "3) Often",
        "4) Almost always"
    ],
    
    "2. Have you been experiencing physical pain, such as headaches, stomachaches, or muscle tension, without a clear cause?": [
        "1) No, not at all",
        "2) Occasionally",
        "3) Quite frequently",
        "4) Almost every day"
    ],

    "3. How often do you find yourself crying even when there is no clear reason for it?": [
        "1) Rarely or never",
        "2) Sometimes",
        "3) Frequently",
        "4) Almost every day"
    ],

    "4. How many hours do you sleep regularly?": [
        "1) More than 7 hours",
        "2) 5-7 hours",
        "3) 3-5 hours",
        "4) Less than 3 hours"
    ],

    "5. Has your sense of time changed? (e.g., days feeling too fast or too slow)": [
        "1) No, everything feels normal",
        "2) Sometimes I lose track of time",
        "3) Frequently, I struggle to keep track of time",
        "4) Almost always, time feels distorted"
    ],

    "6. Are you pushing people away, even though you might want to connect with them?": [
        "1) No, I feel connected",
        "2) Occasionally, I avoid people",
        "3) Often, I push people away",
        "4) Almost always, I isolate myself"
    ],

    "7. When you find yourself laughing or smiling, does it feel natural or forced?": [
        "1) Always natural",
        "2) Sometimes forced",
        "3) Mostly forced",
        "4) Almost always forced"
    ],

    "8. Have you ever looked for ways to escape your feelings, even if that meant risky behaviors or self-destructive habits?": [
        "1) No, I have healthy coping strategies",
        "2) Occasionally, I engage in unhealthy distractions",
        "3) Often, I turn to risky behaviors",
        "4) Almost always, I struggle with self-destructive habits"
    ]
}

suggestions = {
    (1.0, 1.5): [
        "You seem to be in a **really good place mentally**! 😊 Keep nurturing your well-being by doing things that bring you joy. **Stay connected with loved ones, keep practicing gratitude, and don’t hesitate to uplift others around you.** 💙",
        "You're **doing great!** It’s amazing that you are in a balanced state of mind. Keep up the self-care habits that make you feel good. If you ever feel down, remember to take a deep breath and remind yourself how far you’ve come. 🌟",
        "You have a **healthy mindset** and that’s wonderful! If you ever feel a little off, remember that small things like a walk in nature, a good conversation, or even just a warm cup of tea can do wonders. Keep spreading your positivity! 💖"
    ],
    
    (1.6, 2.5): [
        "You’re **doing okay**, but I can sense that there might be a few things weighing on your mind. That’s completely normal. Try to **take a step back, breathe, and prioritize self-care.** Maybe journaling, listening to music, or spending time with someone you trust can help. 💙",
        "Life has its **ups and downs**, and it’s okay if things don’t feel perfect. **You deserve kindness, especially from yourself.** If you’ve been feeling a bit off, make time for small joys—watch your favorite movie, take a break, and don’t be too hard on yourself. 💡",
        "You’re managing things well, but I sense that **some days might feel heavier than others.** If that’s the case, just know that **it’s okay to ask for help, to take a break, or to say no when you need to.** You’re doing your best, and that is enough. 🌿"
    ],
    
    (2.6, 3.2): [
        "I know it’s **not easy** to feel this way, but I want you to know that **you are not alone.** Your feelings are valid, and it’s okay to struggle sometimes. Maybe take some time for yourself today—listen to your favorite song, write down your thoughts, or even just sit in silence and breathe. 🌿",
        "You’ve been **going through a lot, haven’t you?** It’s okay to feel lost sometimes. But I promise you, **this moment won’t last forever.** Try to talk to someone, even if it’s just to say, ‘Hey, I’m feeling a bit off.’ You don’t have to go through this alone. 💜",
        "If things feel **a little overwhelming** right now, that’s okay. It doesn’t mean you’re weak—it just means you’re human. Take things one step at a time, and please, be gentle with yourself. You deserve love and care, even from yourself. 💙"
    ],
    
    (3.3, 4.0): [
        "I can tell that **you’re struggling right now, and that’s okay.** You don’t have to carry this burden alone. Please, if you can, reach out to someone you trust. **You deserve support, love, and care.** I promise you, you’re not as alone as you might feel. 💜",
        "**It sounds like things have been really tough for you.** I wish I could sit with you and just remind you that you matter. **You are important, and your feelings are valid.** If today feels too heavy, take it slow. Breathe. Even the smallest step forward is progress. 🌷",
        "Right now, it might feel like things will never get better, but I promise you, **there is hope.** Even if it’s just a tiny flicker, it’s there. **Please, don’t be afraid to reach out.** You don’t have to face this alone. 💙"
    ]
}

option_specific_suggestions = {
    1: {  # Irritability/Frustration
        1: [
            "It’s wonderful that frustration rarely affects you! That’s a sign of emotional strength and balance. Keep embracing moments of joy and peace, and continue doing what makes you feel fulfilled. 😊",
            "You seem to have a healthy relationship with your emotions, and that’s truly admirable. Keep nurturing this stability by surrounding yourself with positivity and self-care practices.",
            "Handling emotions well is a great strength. But if frustration ever sneaks in, remember it’s okay to pause, breathe, and take a moment for yourself."
        ],
        2: [
            "It’s okay to feel irritated sometimes—your emotions are valid. Life can be overwhelming, and you don’t have to suppress how you feel. Taking deep breaths, listening to calming music, or just stepping outside for a bit might help you feel a little lighter. 💙",
            "Frustration doesn’t mean you’re weak; it means you’re human. If something is bothering you, it’s worth taking a moment to reflect on it. Maybe talking to a trusted friend or writing down your thoughts can bring clarity.",
            "You’re carrying emotions, and that’s completely okay. It might help to take a deep breath and remind yourself that tough moments don’t define you."
        ],
        3: [
            "If frustration is becoming a frequent visitor, it might be time to check in with yourself. What’s been weighing on you? You deserve kindness—even from yourself. Give yourself permission to take breaks and prioritize your well-being. 🌿",
            "You don’t have to push through every difficult moment alone. It’s okay to step back, rest, and recharge. Small acts of self-care—like drinking water, stretching, or simply sitting in silence—can make a difference.",
            "Frequent frustration might be your mind’s way of asking for relief. Be gentle with yourself. A little patience and kindness can go a long way."
        ],
        4: [
            "Constant frustration can be exhausting, and I’m really sorry you’re feeling this way. You don’t have to carry it all alone. If things feel overwhelming, please reach out—whether to a friend, a loved one, or a professional. You matter. 💜",
            "Feeling this way all the time must be incredibly draining. Please know that your emotions are valid, but they don’t have to define you. There are people who care about you and want to support you.",
            "If frustration feels like a constant weight, it’s not something you have to battle alone. You deserve peace, and help is out there. Even taking a small step—like talking to someone or writing about your feelings—can bring a little relief."
        ]
    },

    2: {  # Physical Pain
        1: [
            "It’s great that your body is feeling well! Keep listening to what it needs—rest, hydration, and movement. Your well-being matters. 😊",
            "A body free from pain is something to cherish. Keep up with your self-care habits and continue taking care of yourself.",
            "It’s wonderful that you’re not experiencing discomfort. Keep prioritizing your health and well-being!"
        ],
        2: [
            "Mild discomfort can be frustrating, but your body is just asking for a little extra care. Maybe try some stretching, a warm drink, or a short break. 🌿",
            "Even small aches and pains deserve attention. Be gentle with yourself today, and don’t ignore your body’s signals.",
            "If you’re feeling a little off, a few deep breaths or a moment of rest might help. Take care of yourself!"
        ],
        3: [
            "Your body might be holding onto stress. Have you tried a warm bath, light exercise, or simply lying down for a bit? You deserve to feel at ease. 💙",
            "If your body is aching, please don’t ignore it. A little self-care—hydration, good sleep, and relaxation—can go a long way.",
            "Pain is your body’s way of communicating. Listen to it, be kind to yourself, and allow yourself the rest you need."
        ],
        4: [
            "Ongoing pain can be really tough. Please know that you don’t have to push through it alone. Seeking support is okay. You deserve relief. 💜",
            "I’m sorry that you’re feeling this way. If this continues, please reach out for help—your well-being is important.",
            "Pain can be overwhelming, but you are not alone. Whether it’s a friend, doctor, or someone who cares, please don’t hesitate to talk about it."
        ]
    },

    3: {  # Crying for No Reason
        1: [
            "It’s great that you feel emotionally stable. Remember, it’s okay to cry when you need to, too. 😊",
            "Having emotional balance is wonderful! Continue embracing moments of peace and joy in your life.",
            "You seem to have a solid emotional foundation, which is great! Keep surrounding yourself with things that bring you comfort and happiness."
        ],
        2: [
            "Crying sometimes is natural. If something is weighing on your heart, allow yourself to feel it without judgment. 💙",
            "Your emotions are valid, and you don’t need a reason to feel them. If you’re feeling overwhelmed, taking a moment for yourself might help.",
            "Letting emotions out is not a weakness—it’s a sign of strength. You deserve kindness, especially from yourself."
        ],
        3: [
            "Crying frequently might mean you have a lot on your heart. You don’t have to hold it all in. Letting it out and reaching out for support might bring relief. 🌿",
            "Tears are your body’s way of expressing what words sometimes can’t. You deserve to be heard and understood.",
            "If you’re feeling overwhelmed, please know that you don’t have to go through this alone. Even sharing your feelings with someone can lighten the weight."
        ],
        4: [
            "Crying every day must feel exhausting. You deserve comfort and understanding. Please don’t hesitate to seek support—someone out there truly cares about you. 💜",
            "Your pain is real, and it matters. You don’t have to battle these feelings alone. There is help, and you deserve it.",
            "If tears feel endless, please know that you’re not alone. There are people who want to support you. You deserve peace, and you are worthy of kindness."
        ]
    },


    4: {  # Sleep
        1: [
            "Getting enough sleep is one of the best gifts you can give yourself! Keep prioritizing your rest, and your body and mind will thank you. 😊",
            "A well-rested mind is a strong mind. It’s wonderful that you’re taking care of your sleep—keep it up!",
            "Sleep is essential for your well-being, and it’s great that you’re getting enough. Keep cherishing those peaceful nights!"
        ],
        2: [
            "Your sleep is decent, but your body might appreciate a little extra rest. Maybe try winding down with a book or soft music before bed. 🌙",
            "A few more hours of sleep could do wonders for your energy and mood. Try creating a calming bedtime routine to help you relax.",
            "Your sleep pattern is okay, but if you ever feel drained, consider adjusting your routine for deeper, more restful sleep."
        ],
        3: [
            "Lack of sleep can make everything feel harder. You deserve rest—please try to give yourself the time to recharge. 🌿",
            "Your body is calling out for rest. Even short naps or relaxing before bed can help restore your energy and improve your mood.",
            "When sleep is scarce, everything feels heavier. Be kind to yourself, and try to prioritize even small moments of rest."
        ],
        4: [
            "Sleep deprivation is tough, and I’m really sorry you’re going through this. Your body and mind need rest to heal—please try to seek support if needed. 💜",
            "Consistently missing sleep can take a toll on your well-being. If this is becoming a pattern, consider speaking to someone about it—you deserve to feel rested.",
            "If sleepless nights are overwhelming you, please know that you don’t have to go through this alone. Seeking help is a sign of strength."
        ]
    },

    5: {  # Sense of Time
        1: [
            "It’s great that your sense of time feels normal! Having structure and balance in your days can bring a sense of peace and stability. 😊",
            "Feeling in sync with time can be grounding. Keep engaging in activities that bring you joy and structure to your days.",
            "A balanced perception of time often means you’re mentally at ease—keep nurturing that well-being!"
        ],
        2: [
            "Losing track of time occasionally is normal. If it ever feels too disorienting, small routines like journaling or setting reminders might help. ⏳",
            "It’s okay if time feels a little blurry sometimes. Try grounding yourself with a daily routine or a few minutes of mindfulness.",
            "If time slips away sometimes, don’t worry—you’re not alone. Taking small moments to pause and reflect might help."
        ],
        3: [
            "Time feeling distorted can be unsettling. If you’re feeling lost in your days, maybe try setting gentle goals or connecting with a friend for a sense of structure. 🌿",
            "When time feels like it’s moving too fast or too slow, it might be a sign of stress. Take a deep breath, and know that you’re doing the best you can.",
            "It’s okay to feel disconnected from time sometimes. If this is bothering you, try to introduce small routines to regain a sense of normalcy."
        ],
        4: [
            "Feeling disconnected from time can be overwhelming. Please know that you don’t have to navigate this alone—someone out there wants to help. 💜",
            "If time constantly feels out of control, it may be a sign of deeper emotional exhaustion. Please consider reaching out for support—you deserve it.",
            "You’re not alone in feeling this way. If time feels like it’s slipping away, grounding exercises or speaking with someone might help."
        ]
    },

    6: {  # Social Withdrawal
        1: [
            "It’s wonderful that you feel connected to the people around you! Keep nurturing those relationships, as they bring warmth and support to your life. 😊",
            "Having people in your life who you feel connected to is a beautiful thing. Keep cherishing those moments of companionship.",
            "Social bonds are important for well-being, and it’s great that you maintain them. Keep surrounding yourself with positivity!"
        ],
        2: [
            "Wanting space sometimes is natural, but don’t forget that you are worthy of love and connection. Reach out when you feel ready. 💙",
            "Even if you take a step back now and then, remember that people care about you and want to be there for you.",
            "Needing some solitude is okay, but don’t let self-doubt stop you from seeking warmth when you need it."
        ],
        3: [
            "Pushing people away might feel like the only option sometimes, but you deserve connection just as much as anyone else. Be gentle with yourself. 🌿",
            "It’s okay if opening up feels hard. But please remember, you are never a burden. The right people will always want to be there for you.",
            "You are worthy of care and friendship, no matter what your mind tells you. Take your time, but don’t shut yourself away completely."
        ],
        4: [
            "Isolating yourself can feel safe, but you don’t have to go through everything alone. There are people who truly care about you—please don’t hesitate to reach out. 💜",
            "Even when it feels like no one understands, there are people who want to be there for you. You are not alone in this.",
            "If you’re struggling with loneliness, please consider talking to someone. You deserve support, and you don’t have to carry this weight by yourself."
        ]
    },

    7: {  # Forced Laughter
        1: [
            "Genuine laughter is a beautiful thing! Keep embracing those moments of joy and sharing them with those around you. 😊",
            "It’s great that your happiness comes naturally! Keep surrounding yourself with things and people that make you smile.",
            "Authentic happiness is wonderful—keep cherishing those little joyful moments!"
        ],
        2: [
            "If laughter feels forced sometimes, that’s okay. Be patient with yourself—joy doesn’t always come easily, but it will find its way back to you. 💙",
            "Smiling when you don’t feel like it is exhausting. Give yourself permission to feel your emotions without pressure.",
            "You don’t have to fake happiness for anyone. Your feelings are valid, and you deserve to experience joy in your own time."
        ],
        3: [
            "If happiness feels distant, please be kind to yourself. It’s okay to not be okay, and you’re not alone. 🌿",
            "Forced laughter can be exhausting. You don’t have to pretend—your feelings matter, and you deserve to be supported.",
            "You are allowed to feel however you truly feel. If laughter doesn’t come naturally right now, that’s okay."
        ],
        4: [
            "If laughter feels like a mask, please know that you don’t have to wear it forever. You deserve to feel joy in a way that’s real and true. 💜",
            "Pretending to be happy can be isolating. You don’t have to put on a brave face all the time—let yourself be seen as you truly are.",
            "If everything feels forced, please reach out. You deserve real, deep, genuine happiness."
        ]
    },

    8: {  # Escapism & Risky Behavior
        1: [
            "It’s wonderful that you have healthy ways of coping! Keep prioritizing your well-being and embracing things that bring you peace. 😊",
            "You seem to have a good relationship with your emotions—keep nurturing that self-awareness and strength.",
            "Having positive coping mechanisms is a great strength! Keep taking care of yourself."
        ],
        2: [
            "If you sometimes turn to distractions, that’s okay. Just make sure they’re serving you in a positive way. 💙",
            "Distractions can be helpful in moderation, but don’t forget to check in with yourself too. You deserve healing, not just avoidance.",
            "Coping looks different for everyone. Just be kind to yourself and make sure you’re taking care of your emotional needs."
        ],
        3: [
            "Risky behaviors may feel like an escape, but you deserve safety and comfort. Please be kind to yourself. 🌿",
            "If you find yourself engaging in self-destructive habits, please know that there are better ways to cope, and you are not alone in this.",
            "You deserve to heal, not to hurt. Please take a moment to consider healthier outlets."
        ],
        4: [
            "If you’re struggling with self-destructive habits, please reach out. You are worthy of love, care, and support. 💜",
            "You don’t have to face this alone. Please talk to someone who can help—you deserve peace.",
            "Your pain is real, but it does not define you. There is hope, and you are not alone."
        ]
    }
}