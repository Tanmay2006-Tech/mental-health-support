import random

class ResponseGenerator:
    """
    Generates appropriate responses based on the detected mood and context.
    Includes motivational quotes and relaxation tips.
    """
    
    def __init__(self):
        
        self.mood_responses = {
            'happy': [
                "I'm glad to hear you're feeling happy! That's wonderful! 😊",
                "It's great that you're in a good mood today! 🌟",
                "Your happiness is contagious! Keep that positive energy flowing! ✨",
                "That's fantastic! What's something good that happened today? 🎉",
                "So happy to hear that! Positive emotions are worth celebrating. 🥳"
            ],
            'sad': [
                "I'm sorry to hear you're feeling sad. Remember that it's okay to feel this way sometimes. 💙",
                "I understand that feeling sad can be difficult. Is there anything specific on your mind? 🌧️",
                "When we feel sad, it can help to talk about it. I'm here to listen. 🫂",
                "Sadness is a natural emotion. Be gentle with yourself today. 🕊️",
                "I'm here for you during this difficult time. Sometimes expressing your feelings can help. 💭"
            ],
            'anxious': [
                "I understand feeling anxious. Remember to take deep breaths - in through the nose, out through the mouth. 🧘‍♂️",
                "Anxiety is challenging, but you're not alone in feeling this way. 🤝",
                "When anxiety strikes, try grounding yourself by naming 5 things you can see, 4 things you can touch, 3 things you can hear, 2 things you can smell, and 1 thing you can taste. 🌱",
                "It's okay to feel anxious sometimes. Your feelings are valid. 💗",
                "Anxiety can be overwhelming, but it will pass. Try to focus on the present moment. 🌈"
            ],
            'angry': [
                "I can understand feeling angry. It's a natural response to certain situations. 🧠",
                "When you're feeling angry, taking a moment to pause can be helpful. ⏸️",
                "Anger is telling you something important. Once you feel calmer, you might gain new insights. 💡",
                "It's okay to feel angry, but remember to be kind to yourself. 💖",
                "I hear that you're feeling angry. Would it help to talk about what triggered this feeling? 🗣️"
            ],
            'stressed': [
                "I can see you're feeling stressed. Remember that it's important to take breaks when needed. ☕",
                "Stress can be overwhelming. Have you tried any relaxation techniques? 🧘‍♀️",
                "When we're stressed, our bodies need extra care. Try to make time for activities you enjoy. 🎵",
                "Being stressed is a common response to pressure. Remember that you don't have to handle everything at once. 🐢",
                "I understand that stress can be difficult to manage. Small steps can help reduce overwhelming feelings. 🌱"
            ],
            'neutral': [
                "How are you feeling today? I'm here to chat if you need someone to talk to. 😊",
                "Is there anything specific on your mind today? 💭",
                "I'm here to support you. How can I help? 🤗",
                "Sometimes it helps to talk things through. What's on your mind? 🗨️",
                "I'm listening. Feel free to share what's going on with you. 👂"
            ]
        }
        
       
        self.context_responses = {
            'academic': [
                "Exams can be stressful. Have you tried breaking your study sessions into smaller chunks with breaks in between? ⏱️",
                "I understand academic pressure can be intense. Remember that one exam doesn't define your worth or intelligence. 🧠",
                "For upcoming tests, creating a study schedule might help make the workload feel more manageable. 📝",
                "School-related stress is common. Try to focus on what you can control, like your study environment and preparation. 🌱",
                "When preparing for exams, don't forget to get enough sleep - it's crucial for memory and concentration. 😴"
            ],
            'work': [
                "Work challenges can be demanding. Consider prioritizing tasks to tackle the most important ones first. 📋",
                "Work stress is normal, but remember to set boundaries between your professional and personal life. ⚖️",
                "For workplace issues, sometimes speaking with colleagues or supervisors can help find solutions. 🗣️",
                "When work gets overwhelming, taking short breaks can actually boost your productivity. ☕",
                "Remember that your value isn't determined by your productivity or job title. ✨"
            ],
            'health': [
                "Health concerns can be really worrying. Have you been able to speak with a healthcare provider? 🩺",
                "Taking care of your health is important. Remember that rest is also a productive activity. 💤",
                "Physical health and mental wellbeing are connected. Small self-care actions can make a difference. 🌿",
                "When dealing with health issues, it's okay to ask for help from friends, family, or professionals. 🤝",
                "Managing health challenges takes strength. Be patient and gentle with yourself. 💪"
            ],
            'relationship': [
                "Relationships can bring both joy and challenges. Communication is often key to working through difficult times. 💬",
                "When facing relationship issues, sometimes taking a moment to see things from the other person's perspective can help. 👀",
                "It's important to maintain healthy boundaries in any relationship. 🛡️",
                "Your feelings in relationships are valid. Trust your instincts about what feels right for you. 💖",
                "Remember that healthy relationships should bring more peace than stress to your life. ☮️"
            ]
        }
        
        
        self.motivational_quotes = [
            "✨ The only way to do great work is to love what you do. — Steve Jobs",
            "🌟 Believe you can and you're halfway there. — Theodore Roosevelt",
            "🚀 You are never too old to set another goal or to dream a new dream. — C.S. Lewis",
            "💫 The future belongs to those who believe in the beauty of their dreams. — Eleanor Roosevelt",
            "🐢 It does not matter how slowly you go as long as you do not stop. — Confucius",
            "💪 Success is not final, failure is not fatal: It is the courage to continue that counts. — Winston Churchill",
            "⭐ Hardships often prepare ordinary people for an extraordinary destiny. — C.S. Lewis",
            "⏱️ Your time is limited, don't waste it living someone else's life. — Steve Jobs",
            "😊 The purpose of our lives is to be happy. — Dalai Lama",
            "🏆 You miss 100% of the shots you don't take. — Wayne Gretzky",
            "🌅 The only limit to our realization of tomorrow will be our doubts of today. — Franklin D. Roosevelt",
            "🌱 What you get by achieving your goals is not as important as what you become by achieving your goals. — Zig Ziglar",
            "🧠 The mind is everything. What you think you become. — Buddha",
            "🌲 The best time to plant a tree was 20 years ago. The second best time is now. — Chinese Proverb",
            "🌠 It always seems impossible until it's done. — Nelson Mandela"
        ]
        
        
        self.academic_quotes = [
            "🎓 Education is the passport to the future, for tomorrow belongs to those who prepare for it today. — Malcolm X",
            "🔍 The expert in anything was once a beginner. — Helen Hayes",
            "📚 The beautiful thing about learning is that no one can take it away from you. — B.B. King",
            "💡 Don't let what you cannot do interfere with what you can do. — John Wooden",
            "📝 Success is the sum of small efforts, repeated day in and day out. — Robert Collier",
            "📖 The more that you read, the more things you will know. The more that you learn, the more places you'll go. — Dr. Seuss",
            "✨ Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. — Christian D. Larson",
            "🏆 The difference between try and triumph is just a little umph! — Marvin Phillips",
            "🌻 Your positive action combined with positive thinking results in success. — Shiv Khera",
            "🚀 You don't have to be great to start, but you have to start to be great. — Zig Ziglar"
        ]
        
    
        self.relaxation_tips = [
            "🧘‍♀️ Try the 4-7-8 breathing technique: Inhale for 4 seconds, hold for 7 seconds, exhale for 8 seconds. Repeat several times.",
            "💆‍♂️ Progressive muscle relaxation: Tense and then relax each muscle group in your body, starting from your toes and working upward.",
            "🌱 Practice mindfulness by focusing fully on what you're doing at the present moment, whether it's eating, walking, or just breathing.",
            "📵 Take a technology break. Step away from screens for at least 30 minutes and do something calming.",
            "🎵 Listen to soothing music or nature sounds to help calm your mind and reduce stress levels.",
            "🧠 Try a guided meditation. Even 5 minutes can help reduce stress and improve your mood.",
            "📓 Write down your thoughts in a journal. Getting them out of your head can provide relief and clarity.",
            "🌳 Take a short walk outside. Fresh air and gentle exercise can change your perspective and mood.",
            "🙏 Practice gratitude by listing three things you're thankful for today.",
            "👐 Try the 5-4-3-2-1 grounding technique: Acknowledge 5 things you see, 4 things you feel, 3 things you hear, 2 things you smell, and 1 thing you taste.",
            "🏡 Create a calming environment with soft lighting and minimal noise. Your surroundings affect your stress levels.",
            "🛁 Take a warm bath or shower to relieve physical tension in your body.",
            "🏝️ Visualize a peaceful scene like a beach or forest. Engage all your senses in the visualization.",
            "🎨 Practice a hobby that brings you joy and allows you to be in a flow state.",
            "👫 Connect with a supportive friend or family member. Social connection is a powerful stress reliever."
        ]
        
        
        self.study_tips = [
            "⏱️ Try the Pomodoro Technique: study for 25 minutes, then take a 5-minute break. After 4 cycles, take a longer 15-30 minute break.",
            "🪑 Create a dedicated study space that's comfortable, well-lit, and free from distractions.",
            "🧩 Break large tasks into smaller, manageable chunks to make studying less overwhelming.",
            "🔄 Use active study methods like practice tests, flashcards, or teaching concepts to someone else.",
            "💧 Take care of your physical needs: stay hydrated, eat nutritious snacks, and get enough sleep before your exam.",
            "🧠 Try visualization techniques: imagine yourself successfully taking the exam and knowing the answers.",
            "📅 Create a realistic study schedule that includes breaks and time for self-care.",
            "🔤 Use mnemonic devices or memory tricks to help remember complex information.",
            "🔄 Alternate between different subjects or topics to keep your mind engaged and prevent burnout.",
            "😌 Remember that some anxiety before an exam is normal and can actually help your performance – but extreme stress is counterproductive.",
            "💤 Review the most important concepts right before bedtime, as sleep helps consolidate memories.",
            "☕ Limit caffeine, especially close to bedtime, as it can interfere with quality sleep that's critical for memory.",
            "🫁 Practice deep breathing when you feel overwhelmed: breathe in for 4 counts, hold for 2, exhale for 6.",
            "🗺️ Focus on understanding concepts rather than memorizing. Creating mind maps can help connect ideas.",
            "💪 Give yourself positive self-talk and encouragement. Your mindset affects your performance."
        ]
    
    def get_mood_response(self, mood, context=None):
        """
        Returns a response appropriate for the detected mood and context
        
        Args:
            mood (str): The detected mood
            context (str, optional): The detected context
            
        Returns:
            str: A response appropriate for the mood and context
        """
        
        if context == 'academic' and (mood == 'stressed' or mood == 'anxious'):
            responses = [
                "Having an exam coming up can definitely be stressful. Remember to take breaks and practice self-care while studying. 📚✨",
                "Exam anxiety is common. Breaking your study time into smaller chunks with rewards can make it more manageable. 🍰📝",
                "I understand that upcoming exams can cause worry. Try to focus on what you already know rather than what you don't. 💪🧠",
                "Test preparation can be overwhelming. Consider making a study plan to organize your time effectively. 📅✏️",
                "Feeling nervous about exams is natural. Remember that proper sleep is just as important as studying. 😴📚"
            ]
            return random.choice(responses)
        
        
        if context and context in self.context_responses:
            return random.choice(self.context_responses[context])
        
        
        if mood in self.mood_responses:
            return random.choice(self.mood_responses[mood])
        
        
        return random.choice(self.mood_responses['neutral'])
    
    def get_motivational_quote(self, context=None):
        """
        Returns a motivational quote, potentially context-specific
        
        Args:
            context (str, optional): The detected context
            
        Returns:
            str: A motivational quote
        """
        if context == 'academic':
            return random.choice(self.academic_quotes)
        return random.choice(self.motivational_quotes)
    
    def get_relaxation_tip(self, context=None):
        """
        Returns a relaxation tip, potentially context-specific
        
        Args:
            context (str, optional): The detected context
            
        Returns:
            str: A relaxation tip
        """
        if context == 'academic':
            return random.choice(self.study_tips)
        return random.choice(self.relaxation_tips)
